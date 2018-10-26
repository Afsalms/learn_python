from random import shuffle
import math

"""
idea behind: It is easy to sort smaller list and easy to merge sorted list
Split the entire array to element
then group toghter in sorted order
Application: Used in e commerse websites for recomendation and price comparison

"""

def merge_sort(a):
    total_number = len(a)
    if len(a) <= 1:
        return a
    partion_index = int(math.floor(total_number/2))
    left, right = merge_sort(a[0:partion_index]), merge_sort(a[partion_index:])
    return merge(left, right)
def merge(left, right):
    c = []
    while left and right:
        if left[0]> right[0]:
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

    a = list(range(100))
    shuffle(a)
    print(a)
    b = merge_sort(a)
    print(b)