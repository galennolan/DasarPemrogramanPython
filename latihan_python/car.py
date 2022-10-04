class Car:
    color = 'black'
    transmission = 'manual'
    gear_position = 'N'
def __init__(self, transmission):
        self.transmission = transmission
        print('Engine is ready!')
def drive(self):
        self.gear_position = 'D'
        print('Drive')
def reverse(self):
        self.gear_position = 'N'
        print('Reverse. Please check your behind.')
def change_gear(self, gear='N'):
        self.gear_position = gear
        ('Gear position on: ' + self.gear_position)
def get_gear_position(self):
    return self.gear_position


car1 = Car('manual')
car1.change_gear('D-1')

car2 = Car('automatic')
gear_position = car2.get_gear_position()
print(gear_position)