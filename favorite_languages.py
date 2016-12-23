favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# print("Sarah's favorite language is " +
#     favorite_languages['sarah'].title() +
#     "."
# )

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + "."
    )

## Less efficient way to write this:
#for name in favorite_languages.keys():
for name in favorite_languages:
    print(name.title())