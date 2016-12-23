favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = [
    'phil',
    'sarah'
]

## Less efficient way to write this:
#for name in favorite_languages.keys():
for name in favorite_languages:
    print(name.title())
    
    if name in friends:
        print("  Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")