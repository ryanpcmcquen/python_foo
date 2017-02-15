def describe_pet (pet_name, animal_type = 'cat'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'snowball', animal_type = 'cat')

'''
## Prints:
I have a cat.
My cat's name is Snowball.
'''