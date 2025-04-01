import one

def method_two():
    print('this is method_two of second.py')

print('its a print statement on second.py')

one.method_one()

if __name__ == '__main__':
    print('second.py is being called directly')