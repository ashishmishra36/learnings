import math

from sqlalchemy.sql.functions import count

# Function to check if given number n is a power of two.
# def isPowerofTwo(n):
#     while n>=1:
#         if n ==1:
#             return True
#         if n%2==0:
#             n=n//2
#             print(n)
#         else:
#             return False


# Function is to check whether two strings are anagram of each other or not.
# def areAnagrams(s1, s2):
#     # code here
#     a, b = list(s1) , list(s2)
#     a.sort()
#     b.sort()
#     if a==b:
#         return True
#     else:
#         return False



#Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j
# and arr[i] + arr[j] == 0.
#Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the
# answer must not contain any duplicate pairs.
arr = [-1, 0, 1, 2, -1, -4]

def getPairs( arr):
    n = len(arr)
    l =[]
    seen = set()
    for x in arr:
        if -x in seen:
            s = sorted([x,-x])
            if s not in l:
                l.append(s)
        seen.add(x)
    return sorted(l)


def floorSqrt(n):
    #Your code here
    x = math.sqrt(n)
    if x**2 == n:
        return int(x)
    else:
        return math.isqrt(n)

# arr = [0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0, -1]
# arr = [10, 20, 30]
# arr = [0, 0]

def pushZerosToEnd(arr):
    # x = [i for i in arr if i!=0]
    # arr[:] = x + [0]*(len(arr)-len(x))
    n = len(arr)
    left =0
    for right in range(n):
        if arr[right]!=0:
            arr[left], arr[right]= arr[right],arr[left]
            left=left+1
    return arr

def firstRepeated(arr):
    for x in range(len(arr)):
        if arr.count(arr[x])>1:
            return x+1
    return -1

# BInary search on sorted array
a = [1,2,5,7,8,9,9,9,11,18,26]
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

# print(binary_search(a,18))







