from random import shuffle

"""
Simple sort algoritm
compare each element with the other element
application: For academic purpose only
"""


def bubble_sort_algorithm(a):
    number_of_iteration = 0
    for i in range(len(a)-1):
        swapped = False
        for j in range(len(a)-1-i):
            number_of_iteration += 1
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    print("number_of_iteration: ", number_of_iteration)
    return a


if __name__ == '__main__':
    a = list(range(10))
    shuffle(a)
    print(a)
    b = bubble_sort_algorithm(a)
    print(b)


