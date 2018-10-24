
from random import shuffle


"""
Select last element as the pivot
Then move all element less than pivot to left of pivot and all
element greate to the right of pivot, Then split the array based on the current index of the pivot
Repeat this step till get sorted

application: Medical and industrial monitoring, Control for aircraft, Defence
"""

def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high] 
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 



if __name__ == '__main__':
    a = list(range(10))
    shuffle(a)
    print(a)
    quickSort(a, 0, len(a)-1)
    print(a)