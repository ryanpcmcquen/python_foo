cars = [
    'audi',
    'bmw',
    'subaru',
    'toyota'
]

def print_car (car):
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

map(print_car, cars)
