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
