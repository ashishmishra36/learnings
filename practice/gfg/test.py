arr = [4,7,8,1,2,4,1,0,9,1]
n =2
def highest(arr, n):
    # convert it to set, check id set has length> n if yes , make it sorted and find nth
    s = sorted(set(arr))
    print(s[-n])

highest(arr, n)


