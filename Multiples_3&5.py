#! /bin/env python3.4
def problem1(num):
	sum = 0 
	for i in range (num):
		if ( i%5==0 or  i%3==0):
			sum += i
	return sum  
