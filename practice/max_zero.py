def MaxZero(arr, n):
    # Your code goes here
    m = 0
    highest =0
    for i in range(n):
        z = str(arr[i]).count('0')
        if z > m:
            m = z
            highest = arr[i]
        elif z==m:
            highest = max(arr[i],highest)
    if m >0:
        return highest
    else:
        return -1

def max_zero(arr, n):
    # create a dictionary , start from left to right get the count of zeros for each string
    # take the maximum of the dict , if not in dict then return -1
    freq={}
    for i in range(n):
        freq[i] = str(arr[i]).count('0')
    print(freq)
    # m = max(freq.values())
    # for i in freq:
    #     if freq[i] == m and m>0:
    #         return arr[i]
    m =0
    result =-1
    for i in freq:
        if freq[i] > m :
            m = freq[i]
            result= arr[m]
    return result

arr = [1, 20, 3, 9999, 2]
n=5
print(max_zero(arr, n))
