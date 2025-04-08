# Reverse a String
def reverse_string(s):
    # take two pointers left and right, start swapping left most with right most
    # after every swap make left = left+1 and right = right-1, until left<=right(while condition)
    left, right  =0, len(s)-1
    s= list(s)
    while left<right:
        s[left],s[right]=s[right], s[left]
        left=left+1
        right=right-1
    return ''.join(s)

# Longest Substring Without Repeating Characters