package tourgolang

import "testing"

func TestUrlCounterCrawl(t *testing.T) {
	c := UrlCounter{seen: make(map[string]int)}
	c.Crawl("https://golang.org/", 4, fetcher)
	if len(c.seen) != 5 {
		t.Errorf("Expected crawler to fetch a total of 6 URLs")
	}
}
