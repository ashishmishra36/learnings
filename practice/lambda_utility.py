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


# os.system('cls')  # Windows

def add_numbers():
  try:
    print (1+2)
    print('can it be printed ???')
  except:
    print('Error ! It seems you are not adding correctly !')
  else:
    print('we are good to add two numbers ! ')


def number_division():
  try:
    print (2/'78687687687')
    print('can it be printed ???')
  except ZeroDivisionError as e:
    print(f'Error ! It seems you are not adding correctly ! {e}')
  except TypeError as e:
    print(f'Error ! It seems you are not adding correctly ! {e}')
  else:
    print('we are good to add two numbers ! ')
  finally:
    print('this print statement will always run !! ')


def ask_for_integer():
  while True:
    try:
      result = int(input('Please inter a number: '))
      print(f'number is : {result}')
    except:
      print('Error ! oh Its not a number')
    else:
      break
    # finally:
    #   print('now finally it will will be printed')


ask_for_integer()




