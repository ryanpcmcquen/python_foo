favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
## Using `set()` removes any duplicates:
for language in set(favorite_languages.values()):
    print(language.title())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

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


