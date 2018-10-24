from random import shuffle

"""
loop though all the indices then
    Select a index then compare the element left to it
    if left greater than right swap the element
        decrement the value of the index, repeat the same step
        until position become zero

application: Small list and list with disorder is very less
"""


def insertion_sort_method(a):
    for i in range(len(a)):
        position = int(i)
        while (position> 0 and a[position-1]> a[position]):
            a[position-1], a[position] = a[position], a[position-1]
            position -= 1
    return a


if __name__ == '__main__':
    a = list(range(100))
    shuffle(a)
    print(a)
    b = insertion_sort_method(a)
    print(b)