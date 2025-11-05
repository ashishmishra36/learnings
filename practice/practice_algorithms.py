# Binary search on sorted array, because we take advantage of the sorted collections means why to
# go in sequential way
# time complexity is O(log n)
# its a divide and conquer -> divide in between in each loop
a = [1,9,9,11,14,15,17]
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
        # since previous steps we already checked that it's not equal to mid so lets make left = next of mid index
        elif a[mid]<target:
            print(left, right, mid)
            left = mid+1
        else:
            print(left, right, mid)
            right = mid-1
    return -1


# quick sort

# divide and conquer
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


# Two pointer algorithm
def reverse_string(s):
    # take two pointers left and right, start swapping left most with right most
    # after every swap make left = left+1 and right = right-1, until left<right(while condition)
    left, right  =0, len(s)-1
    s= list(s)
    while left<right:
        s[left],s[right]=s[right], s[left]
        left=left+1
        right=right-1
    return ''.join(s)

# sliding window algorithm
# problem: Find a maximum sum of three elements from the list
def sliding_window(arr, k):
    # get the length of the list
    n = len(arr)
    # base case
    if n<=k:
        print('invalid list !')
        return -1
    else:
        # get the sum of first k elements
        window_sum = sum(arr[:k])
        # make this sum as max sum
        max_sum = window_sum
        # since the last window ends on (n-k)th position
        for i in range(n-k):
            window_sum = window_sum - arr[i] + arr[i+k]
            max_sum = max(window_sum, max_sum)
        return max_sum

a = [3,4,5,-1,0,9,1,8]
print(sliding_window(a, 3))







