import re


text = 'My 203 phone number is 203-424-6599 but this is 12 my old phone numbene '
pattern ='203'

# it matches if pattern is in entire string
print(re.search(pattern,text))
m = re.search(pattern,text)
# this will return position related to first search only
print(m.start(), m.end())
print(m.string)
# it matches if pattern is in beginning
print(re.match(pattern,text))

# to find all searches

ma = re.findall(pattern,text)
print(ma)
print(len(ma))

print("--------#use '|' operator to apply OR condition in regex----------------------------------------")
#use "|" operator to apply OR condition in regex
m = re.search('12|qq', text)
print(m.start())

#use "." wildcard operator to fetch big string
m = re.findall('.ne', text)
print(m)

print('--------# starts with a number--------------')
c = '125465 is a number'
m= re.findall(r'^\d', c)
print(m)

print('--------# ends with a number--------------')
# ends with a number
q = 'what is the 125465'
n= re.findall(r'\d$', q)
print(n)


print('----------------to exclude number from a string-----------------------------')
phrase = 'there are 5 numbers in 12345 but a a digit 8.'
n = re.findall(r'[^\d]+', phrase)
print(n)


print('----------------to exclude "-" ish words from a string-----------------------------')
phrase = 'I want to follow-up to dig-up about that set-up'
# pattern = r'[\w]'                # it will give all the alphanumerics
# pattern = r'[\w]+-'            # it will return one or more alphanumerics followed by -
pattern = r'[\w]+-[\w]+'       # it will return one or more alphanumerics followed by - and starts with -
n = re.findall(pattern, phrase)
print(n)