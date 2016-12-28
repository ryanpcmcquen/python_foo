# alien_0 = {
#     'color': 'green',
#     'points': 5
# }
# alien_1 = {
#     'color': 'yellow',
#     'points': 10
# }
# alien_2 = {
#     'color': 'red',
#     'points': 15
# }

# aliens = [
#     alien_0,
#     alien_1,
#     alien_2
# ]

# for alien in aliens:
#     print(alien)

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)


## Make an empty list for storing aliens.
aliens = []

## Make 30 green aliens:
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

## Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

## Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))