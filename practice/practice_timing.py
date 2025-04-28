import time
import timeit
from tkinter.scrolledtext import example

from PIL import Image

mask = Image.open('mask.png')
print(mask.size)
mask =mask.resize((1055,559))
mask.putalpha(200)
print(mask.size)
mask.show()
matrix = Image.open('word_matrix.png')
print(matrix.size)
matrix.paste(mask,(0,0), mask)
mask.show()
matrix.show()


































def add_numbers(n):
    return sum([x for x in range(n)])

def add_numbers_other(n):
    s= 0
    for x in range(n):
        s = s+x
    return s


# first way by getting difference between after time-before time
# start_time = time.time()
# print(start_time)
# add_numbers(99999999)
# end_time = time.time()
# print(end_time)
# print(f'diff is : {end_time- start_time}')