package interviews

import "math"

// Description
// The lines parallel to the x axis describe a pavement and the circles describe obstacles.
// Assume the path starts on the left side at x = -2^31 and ends on the right side at x = 2^31-1.
// We want to find if the path is completely blocked by obstacles or not

type Circle struct {
	x, y, radius int
}

func euclidianDistance(c1 Circle, c2 Circle) float64 {
	return math.Sqrt(math.Pow(float64(c1.x-c2.x), 2) + math.Pow(float64(c1.y-c2.y), 2))
}

func circlesOverlap(c1 Circle, c2 Circle) bool {
	return euclidianDistance(c1, c2) <= float64(c1.radius+c2.radius)
}

// Input
// List of circles = [(10, 10, 30), (25, 25, 20)]
// Each tuple contains information about the obstacle (center_x, center_y, radius)
// Two integers a and b representing the lines parallel to x axis y = a, and y = b
// is_overlap(circle1, circle2) -> returns a boolean, if circle touches, it’s an overlap.
// Group all circles that overlap and form a continuous blob
func groupCircles(circles []Circle) map[int][]Circle {
	groupCircle := make(map[int][]Circle)
	circleGroup := make(map[Circle]int)
	maxGroupCount := 0
	for i, c1 := range circles {
		for j := i + 1; j < len(circles); j++ {
			c2 := circles[j]
			g1, exists1 := circleGroup[c1]
			g2, exists2 := circleGroup[c2]
			if circlesOverlap(c1, c2) {
				if exists1 {
					if exists2 {
						if g2 != g1 {
							for _, c := range groupCircle[g2] {
								groupCircle[g1] = append(groupCircle[g1], c)
								circleGroup[c] = g1
							}
							delete(groupCircle, g2)
						}
					} else {
						groupCircle[g1] = append(groupCircle[g1], c2)
						circleGroup[c2] = g1
					}
				} else {
					groupCircle[maxGroupCount] = []Circle{c1, c2}
					circleGroup[c1] = maxGroupCount
					circleGroup[c2] = maxGroupCount
					maxGroupCount += 1
				}
			} else {
				if !exists1 {
					circleGroup[c1] = maxGroupCount
					groupCircle[maxGroupCount] = []Circle{c1}
					maxGroupCount += 1
				}
				if !exists2 {
					circleGroup[c2] = maxGroupCount
					groupCircle[maxGroupCount] = []Circle{c2}
					maxGroupCount += 1
				}
			}
		}
	}
	return groupCircle
}

func pathBlocked(circles []Circle, bottomYAxis float64, topYAxis float64) bool {
	groups := groupCircles(circles)
	for _, g := range groups {
		minY := math.MaxFloat64
		maxY := -math.MaxFloat64
		for _, c := range g {
			minY = math.Min(minY, float64(c.y-c.radius))
			maxY = math.Max(maxY, float64(c.y+c.radius))
		}
		if minY <= bottomYAxis && maxY >= topYAxis {
			return true
		}
	}
	return false
}
