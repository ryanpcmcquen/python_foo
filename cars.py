cars = [
  'bmw',
  'audi',
  'toyota',
  'subaru'
]

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the reverse sorted list:')
print(sorted(cars, reverse=True))

print('\nHere is the original list again:')
print(cars)

cars.reverse()

print('-----------------------')

print(cars)
print(len(cars))
