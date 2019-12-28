package tourgolang

import (
	"fmt"
	"sync"
)

type Fetcher interface {
	// Fetch returns the body of URL and
	// a slice of URLs found on that page.
	Fetch(url string) (body string, urls []string, err error)
}

type UrlCounter struct {
	seen map[string]int
	mux  sync.Mutex
}

// Crawl uses fetcher to recursively crawl
// pages starting with url, to a maximum of depth.
func (c *UrlCounter) Crawl(url string, depth int, fetcher Fetcher) {
	if depth <= 0 {
		fmt.Printf("Done with %s, depth = %d\n", url, depth)
		return
	}
	c.mux.Lock()
	if _, uSeen := c.seen[url]; uSeen {
		c.mux.Unlock()
		fmt.Printf("Done with %s, already crawled\n", url)
		return
	} else {
		c.seen[url] += 1
		c.mux.Unlock()
		_, urls, err := fetcher.Fetch(url)

		if err != nil {
			fmt.Printf("Error fetching %s - %v\n", url, err)
			return
		}

		childUrlCrawled := make(chan bool)
		for _, u := range urls {
			go func(url string) {
				c.Crawl(url, depth-1, fetcher)
				childUrlCrawled <- true
			}(u)
		}
		for i, u := range urls {
			fmt.Printf("Waiting for child url #%d/%d: %s\n", i, len(urls), u)
			<-childUrlCrawled
		}
		fmt.Printf("Done with %s\n", url)
	}
}

// fakeFetcher is Fetcher that returns canned results.
type fakeFetcher map[string]*fakeResult

type fakeResult struct {
	body string
	urls []string
}

func (f fakeFetcher) Fetch(url string) (string, []string, error) {
	if res, ok := f[url]; ok {
		return res.body, res.urls, nil
	}
	return "", nil, fmt.Errorf("not found: %s", url)
}

// fetcher is a populated fakeFetcher.
var fetcher = fakeFetcher{
	"https://golang.org/": &fakeResult{
		"The Go Programming Language",
		[]string{
			"https://golang.org/pkg/",
			"https://golang.org/cmd/",
		},
	},
	"https://golang.org/pkg/": &fakeResult{
		"Packages",
		[]string{
			"https://golang.org/",
			"https://golang.org/cmd/",
			"https://golang.org/pkg/fmt/",
			"https://golang.org/pkg/os/",
		},
	},
	"https://golang.org/pkg/fmt/": &fakeResult{
		"Package fmt",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
	"https://golang.org/pkg/os/": &fakeResult{
		"Package os",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
}
