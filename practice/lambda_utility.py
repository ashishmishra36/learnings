import os


def square(num):
    return num**2
l = [1,2,3,4,5,6]
# print(list(map(square,l)))

#lambda functions
# print(list(map(lambda num: num**2, l)))

def missing_char(str, n):
  result = ''
  for x in range(len(str)):
    if x != n:
      result = result + str[x]
  return result


print("Text to clear")

os.system('cls')  # Windows

print("Cleared!")


