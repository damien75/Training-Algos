package tourgolang

import (
	"fmt"
	"math/rand"
	"reflect"
)

type Tree struct {
	Left  *Tree
	Value int
	Right *Tree
}

func New(k int) *Tree {
	var t *Tree
	for _, v := range rand.Perm(10) {
		t = insert(t, (1+v)*k)
	}
	return t
}

func insert(t *Tree, v int) *Tree {
	if t == nil {
		return &Tree{nil, v, nil}
	}
	if v < t.Value {
		t.Left = insert(t.Left, v)
	} else {
		t.Right = insert(t.Right, v)
	}
	return t
}

func (t *Tree) String() string {
	if t == nil {
		return "()"
	}
	s := ""
	if t.Left != nil {
		s += t.Left.String() + " "
	}
	s += fmt.Sprint(t.Value)
	if t.Right != nil {
		s += " " + t.Right.String()
	}
	return "(" + s + ")"
}

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *Tree, ch chan int, closeChannel bool) {
	if t.Left != nil {
		Walk(t.Left, ch, false)
	}
	ch <- t.Value
	if t.Right != nil {
		Walk(t.Right, ch, false)
	}
	if closeChannel {
		close(ch)
	}
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *Tree) bool {
	var t1Nodes, t2Nodes []int
	ch1 := make(chan int)
	ch2 := make(chan int)
	go Walk(t1, ch1, true)
	for i := range ch1 {
		t1Nodes = append(t1Nodes, i)
	}
	go Walk(t2, ch2, true)
	for i := range ch2 {
		t2Nodes = append(t2Nodes, i)
	}
	return reflect.DeepEqual(t1Nodes, t2Nodes)
}
