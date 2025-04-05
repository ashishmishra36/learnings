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

def binarysearch( arr, k):
    # Code Here
    s= []
    l = 0
    r = len(arr)-1
    result =-1
    while l <= r:
        mid = (l+r) // 2
        print(l,r,mid)
        if arr[mid] == k:
            result = mid
            r = mid-1
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid -1
    return result

arr= [1, 2,2,2,2, 5, 5,78,99]
print(binarysearch(arr,5))







