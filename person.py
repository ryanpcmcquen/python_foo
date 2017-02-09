def build_person (first_name, last_name):
    ''' Return a dictionary of information about a person. '''
    return {'first': first_name, 'last': last_name}

musician = build_person('jimi', 'hendrix')
print(musician)
