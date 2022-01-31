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


Input: N = 5
arr[] = {10, 20, 3000, 9999, 200}
Output:  3000
Explanation: 3000 contains 3 zero's 
in it.