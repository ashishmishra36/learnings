# Binary search on sorted array
# time complexity is O(log n)
a = [1,9,9,19,4,5,7, 0,1,3]
def binary_search(a, target):
    # left : start of array / right = end of the array
    left, right = 0 , len(a)-1
    print(left,right)
    # run the loop until left is equal to right
    while left<=right:
        mid = (left + right) // 2
        print(left, right, mid)
        if a[mid] == target:
            return mid
        # if target is bigger than middle element it means target is present on right side of the mid
        # since previous steps we already checked that its not equal to mid so lets make left = next of mid index
        elif a[mid]<target:
            print(left, right, mid)
            left = mid+1
        else:
            print(left, right, mid)
            right = mid-1
    return -1


# quick sort
# time complexity is O(nlog n), worst case - n^2, its in-place
def quick_sort(a):
    #Base case:  if array length is one then just return the array
    if len(a)<=1:
        return a
    # find a pivot against which we will be dividing the array/list
    pivot = len(a)//2
    # create three different list
    middle = [x for x in a if x==a[pivot]]
    left = [x for x in a if x < a[pivot]]
    right = [x for x in a if x > a[pivot]]
    # divide the array in recursion and conquer
    # Apply the same process to the left and right parts of the partitioned array.
    return quick_sort(left) + middle + quick_sort(right)


# merge sort
# time complexity nO(logn) and its not in place as it create one more array as a result set
def merge_sort(a):
    # Base Case: if array length is one then just return the array
    if len(a) <= 1:
        return a
    # divide the array in two parts left of the mid and right of the mid
    mid = len(a)//2
    left= a[:mid]
    right = a[mid:]
    # recursion on left and right side
    sorted_left= merge_sort(left)
    sorted_right = merge_sort(right)
    print(f'inside - the merge_sort functions- {left}, {right}')

    return merge(sorted_left, sorted_right)


def merge(sorted_left,sorted_right):
    # initialize an empty result list
    result=[]
    i,j = 0,0
    while i<len(sorted_left) and j< len(sorted_right):
        print(f'before the merging- {sorted_left}, {sorted_right}')
        if sorted_left[i]<sorted_right[j]:
            result.append(sorted_left[i])
            i = i+1
        else:
            result.append(sorted_right[j])
            j = j + 1
        print(f'After the sorting- {result}')
    result.extend(sorted_left[i:])
    result.extend(sorted_right[j:])
    print(f'After merging results is : {result}')
    return result

print(quick_sort(a))

