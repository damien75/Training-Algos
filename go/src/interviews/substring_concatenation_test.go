package interviews

import (
	"reflect"
	"testing"
)

func TestStartingIndicesExample1(t *testing.T) {
	longString := "blabarfoothefoobarman"
	wordParts := []string{"foo", "bar"}
	expectedResult := []int{3, 12}
	if reflect.DeepEqual(startingIndices(longString, wordParts), expectedResult) {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", expectedResult,
			longString, wordParts)
	}
}

func TestStartingIndicesExample2(t *testing.T) {
	longString := "aaaa"
	wordParts := []string{"a", "a"}
	expectedResult := []int{0, 1, 2}
	if reflect.DeepEqual(startingIndices(longString, wordParts), expectedResult) {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", expectedResult,
			longString, wordParts)
	}
}

func TestStartingIndicesExample3(t *testing.T) {
	longString := "bbarfoo"
	wordParts := []string{"bar", "foo"}
	expectedResult := []int{1}
	if reflect.DeepEqual(startingIndices(longString, wordParts), expectedResult) {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", expectedResult,
			longString, wordParts)
	}
}

func TestStartingIndicesEmptyResult(t *testing.T) {
	longString := "bbarfoo"
	wordParts := []string{"hello", "world"}
	if startingIndices(longString, wordParts) != nil {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", nil,
			longString, wordParts)
	}
}

func TestStartingIndicesEmptyString(t *testing.T) {
	longString := ""
	wordParts := []string{"hello", "world"}
	if startingIndices(longString, wordParts) != nil {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", nil,
			longString, wordParts)
	}
}

func TestStartingIndicesEmptyWordParts(t *testing.T) {
	longString := "bbarfoo"
	var wordParts []string
	if startingIndices(longString, wordParts) != nil {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", nil,
			longString, wordParts)
	}
}

func TestStartingIndicesWordPartsWithDifferentLength(t *testing.T) {
	longString := "bbarfoo"
	wordParts := []string{"hello", "bar"}
	if startingIndices(longString, wordParts) != nil {
		t.Errorf("Expected to have starting indices %v for example string %s and parts %v", nil,
			longString, wordParts)
	}
}
