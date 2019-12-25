package interviews

import "fmt"

// Question
// You are given:
// 1) a string (str)
// 2) list of word parts (word_parts) that are all of the same length.
// Find all starting indices of substrings in str that are a concatenation of all parts in word_parts.
// Note: a concatenation has each of the parts from word_parts exactly once and without any intervening characters.
// Example 1:
// str: "blabarfoothefoobarman"
// word_parts: ["foo", "bar"]
// You should return the indices: [3, 12].
// (order does not matter).
// Example 2:
// str: "aaaa"
// word_parts: ["a", "a"]
// You should return the indices: [0, 1, 2].
// (order does not matter).
// str: "bbarfoo"
// word_parts: ["bar", "foo"]
// You should return the indices: [1].
//
// ["bar", "foo", "al"]
// "barfooal", "baralfoo", "foobaral", "fooalbar", "albarfoo", "alfoobar"
// n! time complexity of building all possible concatenations

type WordPartsToSeeAndPartsLength struct {
	wordPartsToSee map[string]int
	subStrLength   int
}

func buildToSeeMap(wordParts []string) (WordPartsToSeeAndPartsLength, error) {
	wordPartsToSee := make(map[string]int)
	substrLength := -1
	for _, w := range wordParts {
		wordPartsToSee[w] += 1
		if substrLength < 0 {
			substrLength = len(w)
		} else if len(w) != substrLength {
			return WordPartsToSeeAndPartsLength{}, fmt.Errorf("all substrings are expected to have the same length, found "+
				"at least 2 different lengths: %d and %d", substrLength, len(w))
		}
	}
	return WordPartsToSeeAndPartsLength{wordPartsToSee: wordPartsToSee, subStrLength: substrLength}, nil
}

// Part 1: Verify all parts have same length and build map of count of parts that need to be seen in string
// Part 2: walk through string to see if all parts are concatenated one after the other
// Part 3: if all parts have been seen, add index and recreate map, else recreate map
func startingIndices(s string, wordParts []string) []int {
	wMapAndLengthStruct, err := buildToSeeMap(wordParts)
	var indices []int
	if err != nil {
		return indices
	} else {
		wordPartsToSee := wMapAndLengthStruct.wordPartsToSee
		substrLength := wMapAndLengthStruct.subStrLength
		startIndex := 0
		for startIndex < len(s)-len(wordParts)*substrLength {
			for i := startIndex; i < len(s)-substrLength; i += substrLength {
				wordPart := s[i : i+substrLength]
				if _, exists := wordPartsToSee[wordPart]; exists {
					if wordPartsToSee[wordPart] == 1 {
						delete(wordPartsToSee, wordPart)
					} else {
						wordPartsToSee[wordPart] -= 1
					}
					if len(wordPartsToSee) == 0 {
						indices = append(indices, startIndex)
						startIndex += substrLength
						wMapAndLengthStruct, _ = buildToSeeMap(wordParts)
						break
					}
				} else {
					startIndex += substrLength
					wMapAndLengthStruct, _ = buildToSeeMap(wordParts)
					break
				}
			}
		}
		return indices
	}
}
