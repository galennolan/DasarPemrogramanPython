class Car:
    def fuel(self):
        return 'gas'
class Honda(Car):
    pass
class Tesla(Car):
    def fuel(self):
        return 'electricity'
def get_fuel(car):
    print(car.fuel())
get_fuel(Tesla())
get_fuel(Honda())