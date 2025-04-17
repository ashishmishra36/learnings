# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'
# l = st.split(' ')
# lss = ' '.join([word for word in l if word.startswith('s')])
# print(lss)
from itertools import count

arr =  [90,4,4,4,44,7777,0]
def arraySortedOrNot(arr):
    f,g = 1,1
    if len(arr)>1:
        for i in range(len(arr)-1):
            if arr[i]< arr[i+1]:
                f= 0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                g= 0
        return f+g==1
    return True

print(arraySortedOrNot(arr))






# # Use range() to print all the even numbers from 0 to 10.
# print([a for a in range(0,11) if a%2==0])

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# print([a for a in range(0,101) if a%3==0])


# Go through the string below and if the length of a word is even print "even!"
#
# st = 'Print every word in this sentence that has an even number of letters'
# ls = st.split(' ')
# lss = ' '.join([word for word in ls if len(word)%2 ==0])
# print(lss)


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#
# def my_func(param ='fixed_value'):
#     print(param)
# my_func('ertyuio')
# my_func()

# def myfunc(*args, **kwargs):
#     print(f' my list of argument is : {args}')
#     print(f' my list of argument is : {kwargs}')
#     for x in args:
#         print(sum(args))
#     print(f'my name is : {kwargs['name']}')

# User function Template for python3

# Given an array arr of positive integers. Reverse every sub-array group of size k.
# Note: If at any instance, k is greater or equal to the array size, then reverse the entire array.
# You shouldn't return any array, modify the given array in place.

# n = 204
# def evenlyDivides(n):
#     # code here
#     a = n
#     r,c = 0,0
#     while a > 0:
#         r = a%10
#         if r !=0:
#             if n%r ==0:
#                 c= c+1
#         a = a//10
#     return c

# print(evenlyDivides(n))

#input = ABCDEFGHIJKLIMNOQRSTUVWXYZ
output
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
return textwrap.fill(s,w)

# to print value having 2 decimal points
print(format(a,'.2f'))













