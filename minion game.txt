import re
s = 'BANANA'
n =6
# declare vowel
# all possible substring starting with conso
# all possible string starting with vowel
# start from left -> take till end 

def func(s, n):
    vowel = ['A', 'E', 'I', 'O', 'U']
    k = []
    t = []
    l = 0
    for i in range(n):
        if s[i] in vowel:
            k.append(s[i:])
            for j in range(i,n-1):
                k.append(s[i:j+1])
        else:
            t.append(s[i:])
            for j in range(i,n-1):
                t.append(s[i:j+1])
    # print(f'keven is {k} \n sturat is {t}' )
    if len(t) >len(k):
        print (f'Stuart {len(t)}' )
    else:
        print (f'Kevin {len(k)}' )
    
print(func(s, n))