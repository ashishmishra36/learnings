# create a class and understand the functions/attributes to it
import math


class Tiago:
    vehicle = 'car'

# attributes given in constructor definition need to be given at the of initialization
    # self.attribute - means we are attaching the attribute with the class,
    # right side of self.attribute will be set as the value given at the time initialization
    def __init__(self, color, model, fuel):
        self.color = color
        self.model = model
        self.fuel = fuel
        print('This is Tiago car')


    def speed(self, distance, time):
        print(f'Speed of my {self.vehicle} which runs on {self.fuel} has speed of {distance/time}')

    def working(self):
        print('yes , it is working')

    # special method / magic or dunder method :: to print string representation of the class object
    def __str__(self):
        return f'my car has {self.color} and it runs on {self.fuel} '

    def __del__(self):
        return 'Tiago object has been deleted'




class Engine(Tiago):

    def __int__(self):
        print('this is engine of a car!!')
        Tiago.__init__()

    def has_noise(self):
        print('it has noise ')

    def working(self):
        print('no its not working ! ')

my_car = Tiago(color='yellow', model=2025, fuel='diesel')


# my_engine = Engine(color='black', model=2020, fuel='gas')
# my_engine.speed(5000,100)
# my_engine.working()
# my_car.working()
# print(my_car)
# del my_car
# print(my_car)

#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:

    def __init__(self, coor1, coor2):
        self.coor1= coor1
        self.coor2 = coor2


    def distance(self):
        print (math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2 ))

    def slope(self):
        a = self.coor2[1] - self.coor1[1]
        b = self.coor2[0] - self.coor1[0]
        print (a/b)

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()




