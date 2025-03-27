#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser_of_even(a,b):
    if a%2 ==0 and b%2 ==0:
        print(min(a,b))
    else:
        print(max(a,b))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(str):
    l = str.split(' ')
    return l[0][0] == l[1][0]

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
# if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    return a ==20 or b ==20 or a+b ==20
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(str):
    x = ''
    for a in range(len(str)):
        if a ==0 or a==3:
            x = x + str[a].upper()
        else:
            x = x+str[a]
    print(x)


#MASTER YODA: Given a sentence, return a sentence with the words reversed
def reverse_words(sentence):
    # l=sentence.split(' ')
    r = ' '.join([a[::-1] for a in sentence.split(' ')])
    print(r)

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost(number):
    return 111 > number > 89 or 211 > number > 189

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(qwe):
    return ''.join([a*3 for a in qwe])
# print(paper_doll('12'))

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def myfunc(numbers):
    c=''
    for x in numbers:
        if x == 0 or x == 7:
            c= c+str(x)
    print(c)
    return '007' in c


print(myfunc([1,7,2,0,4,5,0]))


