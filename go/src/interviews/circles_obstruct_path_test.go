package interviews

import (
	"reflect"
	"testing"
)

// https://imgur.com/j2ygXn9
func TestGroupCirclesExample1(t *testing.T) {
	circles := []Circle{{10, 10, 30}, {25, 25, 20}}
	circleGroups := groupCircles(circles)
	for _, g := range circleGroups {
		if !reflect.DeepEqual(circles, g) {
			t.Errorf("Expected group to be equal to %v, got %v", circles, g)
		}
	}
}

// https://imgur.com/j2ygXn9
func TestPathBlockedExample1(t *testing.T) {
	circles := []Circle{{10, 10, 30}, {25, 25, 20}}
	if pathBlocked(circles, 0, 50) {
		t.Errorf("Path should not be blocked for Example 1 https://imgur.com/j2ygXn9")
	}
}

// https://imgur.com/oXdotwQ
func TestGroupCirclesExample2(t *testing.T) {
	circles := []Circle{{10, 10, 30},
		{25, 25, 20}, {70, 20, 15},
		{80, 35, 20}, {70, 10, 15}}
	circleGroups := groupCircles(circles)
	excpectedGroups := [][]Circle{{{10, 10, 30}, {25, 25, 20}},
		{{70, 20, 15}, {80, 35, 20}, {70, 10, 15}}}
	for i, g := range circleGroups {
		if !reflect.DeepEqual(excpectedGroups[i], g) {
			t.Errorf("Expected group to be equal to %v, got %v", circles, g)
		}
	}
}

// https://imgur.com/oXdotwQ
func TestPathBlockedExample2(t *testing.T) {
	circles := []Circle{{10, 10, 30},
		{25, 25, 20}, {70, 20, 15},
		{80, 35, 20}, {70, 10, 15}}
	if !pathBlocked(circles, 0, 50) {
		t.Errorf("Path should be blocked for Example 2 https://imgur.com/oXdotwQ")
	}
}

// https://imgur.com/Sn2qZIo
func TestGroupCirclesExample3(t *testing.T) {
	circles := []Circle{{10, 10, 30}, {25, 25, 20}, {70, 20, 15}, {80, 35, 20}}
	circleGroups := groupCircles(circles)
	excpectedGroups := [][]Circle{{{10, 10, 30}, {25, 25, 20}},
		{{70, 20, 15}, {80, 35, 20}}}
	for i, g := range circleGroups {
		if !reflect.DeepEqual(excpectedGroups[i], g) {
			t.Errorf("Expected group to be equal to %v, got %v", circles, g)
		}
	}
}

// https://imgur.com/Sn2qZIo
func TestPathBlockedExample3(t *testing.T) {
	circles := []Circle{{10, 10, 30}, {25, 25, 20}, {70, 20, 15}, {80, 35, 20}}
	if pathBlocked(circles, 0, 50) {
		t.Errorf("Path should not be blocked for Example 3 https://imgur.com/Sn2qZIo")
	}
}

// https://imgur.com/BMkITo9
func TestGroupCirclesExample4(t *testing.T) {
	circles := []Circle{{-10, -2, 3}, {10, 2, 3}, {5, 1, 3}, {0, 0, 3}, {-5, -1, 3}}
	circleGroups := groupCircles(circles)
	expectedGroup := []Circle{{10, 2, 3}, {5, 1, 3}, {0, 0, 3}, {-10, -2, 3}, {-5, -1, 3}}
	for _, g := range circleGroups {
		if !reflect.DeepEqual(expectedGroup, g) {
			t.Errorf("Expected group to be equal to %v, got %v", circles, g)
		}
	}
}

// https://imgur.com/BMkITo9
func TestPathBlockedExample4(t *testing.T) {
	circles := []Circle{{-10, -2, 3}, {10, 2, 3}, {5, 1, 3}, {0, 0, 3}, {-5, -1, 3}}
	if !pathBlocked(circles, -5, 5) {
		t.Errorf("Path should be blocked for Example 4 https://imgur.com/BMkITo9")
	}
}
