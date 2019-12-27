package main

import "testing"

func TestBirthdayCakeCandles(t *testing.T) {
	candles := []int32{3, 2, 1, 3}
	blownCandles := birthdayCakeCandles(candles)
	if blownCandles != 2 {
		t.Errorf("birthdayCakeCandles returned %d for input %v, expected 2", blownCandles, candles)
	}
}
