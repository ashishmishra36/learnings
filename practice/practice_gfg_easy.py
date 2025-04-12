import math
from collections import Counter
from ntpath import split
import shutil
from sqlalchemy.sql.functions import count
import datetime

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
import os
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

arr=  [8]
target = 80
# fid a number less than or equal to the given number
# if there is a repetition then take max index
def findFloor(arr, target):
    result = -1
    for i in range(len(arr)):
        if arr[i]<=target:
            result =i
    return result

# find the dupe element in a given list , and return a list
a = [1,2,3,9,8,4,6,2,1,7,8,1]
def find_dupe(a):
    seen = set()
    dupe=set()
    for i in a:
        if i in seen:
            dupe.add(i)
        seen.add(i)
    return list(dupe)


#Given an array arr[], find the first repeating element. The element should occur more than once and the
# index of its first occurrence should be the smallest.
# Note:- The position you return should be according to 1-based indexing.
arr = [1, 5, 3, 4, 3, 5, 6]
def first_Repeated(arr):
    n = len(arr)
    seen= []
    repeated=0
    result = -1
    for i in range(n):
        if arr[i] in seen and i>repeated:
            repeated =arr[i]
            result = arr.index(repeated)+1
        seen.append(arr[i])
    return result

#Return the first non-repeating
str = "a"
def nonRepeatingChar(s):
    # result=-1
    seen = set()
    if len(s)==1:
        return s
    for i in range(len(s)-1):
        if s[i] not in s[i+1:] and s[i] not in seen:
            return s[i]
        seen.add(s[i])
    return '$'

str = "aa"
def first_non_repeating_char(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    for i in d:
        if d[i]==1:
            return i
    return -1

# a = [1,1,1,1,2,2,2,2,3,3,3,3]
a ='aabbnnhhbbhhaamm'
b =Counter(a)
# b={}
# for i in a:
#     b[i] = b.get(i,0)+1
# print(b.most_common(3))

# shutil and OS module : move file between directories
print(os.getcwd())
print(os.listdir())
with open('modules.txt','a+') as f:
    f.write('this if fos os and shutil module \n \t')

# for x in os.listdir():
#     if not x.startswith('practice'):
#         shutil.move(x,'gfg')

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.time.min)
print(datetime.time(2,20))
print(datetime.date(2024,4,30))
print(datetime.date(2024,4,30)-datetime.date(2000,4,30))



















