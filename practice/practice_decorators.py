'''
why we need decorators:
suppose you add some extra logic in an existing method. but later you want to use only new code OR
you just want to use old code , either way - it's not easy
'''

def hello(name):
    print('in Hello ! Good morning ')
    def greet():
        return '\t in Greet !  Good evening'

    def bye():
        return '\t in Bye !  Good night'

    if len(name)>5:
        return greet
    else:
        return bye

# func = hello('ashish')
# print('----------------------')
# func())

def feed():
    def food():
        return ' I am eating !!!'
    return food

# it will simply print the thing what it is returning , means the name of inside method - food
# print(feed())
# # it is just passing the feed function name to tummy
# tummy = feed
# print(tummy())

# this will put in tummy, whatever feed method is returning ie. - food method name
# tummy = feed()
# print(tummy)
#
# print(tummy())


def func_one():
    return 'hello !  '

def demo_func(other_func):
    print('lets call other function inside this')
    print(other_func())



def new_decorator(func_to_be_decor):

    def wrap_it():
        print('lets decorate it !')
        func_to_be_decor()
        print('Its decorated now !')
    return wrap_it

def decoration():
    print('Please decorate me !')

# decorated = new_decorator(decoration)
# decorated()
# @new_decorator
def decoration():
    print('Please decorate me !')

decoration()