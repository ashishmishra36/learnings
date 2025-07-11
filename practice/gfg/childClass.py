from Tiago import Tiago

class Engine(Tiago):
    size=1600

    # either we need to create won constructor and pass attribute to the parent constructor
    # or pass attribute when object is being created !
    # def __init__(self):
    #     Tiago.__init__(self,'blue','xz','gas' )

    def has_noise(self):
        print(f'it has noise {self.size*4}')

    def working(self):
        print('no its not working ! ')

# my_engine = Engine(color='blue', model='xz', fuel='gas')
# my_engine.has_noise()
# print(f'upgraded model of my car is : {my_engine.upgrade_model()}')


class BasicCalculator:

    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def addition(self):
        print(self.number1 , self.number2)
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 / self.number2


cal = BasicCalculator(20, 10)
cal.addition()

print(f'Addition: {cal.addition()}')
print(f'Subtraction: {cal.subtraction()}')
print(f'Multiplication: {cal.multiplication()}')
print(f'Division: {cal.division()}')



