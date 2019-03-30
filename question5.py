import sys
import math

def mergeSortInversions(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = math.floor(len(arr) / 2) # determine middle
        left = arr[:mid]
        right = arr[mid:]
        left, leftInv = mergeSortInversions(left) # split into left and right
        right, rightInv = mergeSortInversions(right)
        temp = []
        i = 0
        j = 0
        inv = 0 + leftInv + rightInv # count number of inversions before merging
        
    while i < len(left) and j < len(right): # merge the results
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
            inv += (len(left)-i) # because the rest of the left is then greater as well
    temp += left[i:] # add the rest of the left side
    temp += right[j:] # then add the remaining right side
    return temp, inv

arr = sys.argv[1:]
arr = [int(i) for i in arr]
print("The intial array is", arr)
print("The sorted array is", mergeSortInversions(arr)[0])
print("There were", mergeSortInversions(arr)[1], "inversions in total")
