package tourgolang

import (
	"testing"
)

// https://tour.golang.org/concurrency/7
func TestWalkTree(t *testing.T) {
	tree := Tree{
		Left: &Tree{
			Left: &Tree{
				Left:  nil,
				Value: 1,
				Right: nil,
			},
			Value: 1,
			Right: &Tree{
				Left:  nil,
				Value: 2,
				Right: nil,
			},
		},
		Value: 3,
		Right: &Tree{
			Left: &Tree{
				Left:  nil,
				Value: 5,
				Right: nil,
			},
			Value: 8,
			Right: &Tree{
				Left:  nil,
				Value: 13,
				Right: nil,
			},
		},
	}
	c := make(chan int)
	expectedNodes := []int{1, 1, 2, 3, 5, 8, 13}
	currentIndex := 0
	go Walk(&tree, c, true)
	for i := range c {
		if i != expectedNodes[currentIndex] {
			t.Errorf("Expected side view of tree to have node %d for index %d, got %d", expectedNodes[currentIndex], currentIndex, i)
		}
		currentIndex += 1
	}
}

func TestConstructSameSizeSideViewEqual(t *testing.T) {
	tree1, tree2 := New(1), New(1)
	if !Same(tree1, tree2) {
		t.Errorf("Expected to have the same side view for 2 ordered binary tree with same node values, got %s != %s", tree1, tree2)
	}
}

func TestConstructDifferentSizesSideViewNotEqual(t *testing.T) {
	tree1, tree2 := New(1), New(2)
	if Same(tree1, tree2) {
		t.Errorf("Expected to have different side view for 2 ordered binary tree with different node values, got %s == %s", tree1, tree2)
	}
}
