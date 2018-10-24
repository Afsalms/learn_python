from random import shuffle
import math

"""
idea behind: It is easy to sort smaller list and easy to merge sorted list
Split the entire array to element
then group toghter in sorted order
Application: Used in e commerse websites for recomendation and price comparison

"""


def merge_sort(array):
	if not array:
		return None
	if len(array) == 1:
		return array
	middle = int(math.ceil(len(array)/2))
	left, right = merge_sort(array[0:middle]), merge_sort(array[middle:])
	return merge(left, right)

def merge(left, right):
	c = []
	while left and right:
		if left[0] > right[0]:
			c.append(right[0])
			del(right[0])
		else:
			c.append(left[0])
			del(left[0])
	while left:
		c.append(left[0])
		del(left[0])
	while right:
		c.append(right[0])
		del(right[0])
	return c


if __name__ == "__main__":

	a = list(range(10))
	shuffle(a)
	b = merge_sort(a)
	print(b)