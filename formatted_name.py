def get_formatted_name(first_name, last_name, middle_name = ''):
    """ Return a full name, neatly formatted. """
    middle_name = " " + middle_name + " " if middle_name else ' '
    full_name = first_name + middle_name + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print(get_formatted_name('john', 'hooker', 'lee'))

'''
## This is how the book had it:
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
'''
