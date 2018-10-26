from random import shuffle

"""
loop though all the indices then
    Select a index then compare the element left to it
    if left greater than right swap the element
        decrement the value of the index, repeat the same step
        until position become zero

application: Small list and list with disorder is very less
"""


def insertion_sort_algorithm(a):
    for i in range(len(a)-1):
        for j in range(i+1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a


if __name__ == '__main__':
    a = list(range(100))
    shuffle(a)
    print(a)
    b = insertion_sort_algorithm(a)
    print(b)