guest_list = [
  'alicia',
  'penumbra',
  'shadow',
  'stew'
]


def invite_all (list):
  print('---------------------------')
  for person in list:
    print('You are cordially invited to a magnificent festival of enjoyment, ' + person.title() + '.')
  print('---------------------------')

invite_all(guest_list)

print('Unfortunately, ' + guest_list.pop(-1).title() + ' cannot make it.')

guest_list.append('matt')

invite_all(guest_list)

guest_list.insert(0, 'mom')

guest_list.insert(4, 'dad')

invite_all(guest_list)

print('Unfortunately there has been an incident with the essential party ware. As such, only 5 guests may attend.')

guest_list.pop()

invite_all(guest_list)