import sys
user_input = input('Enter a word or phrase to check for palindrome-ness:')
def is_this_a_palindrome (str):
  clean_str = str.lower()
  return 'Yes, "' + str + '" is a palindrome.' if (clean_str == clean_str[::-1]) else 'Nope, "' + str + '" is not a palindrome.'

#print(is_this_a_palindrome(user_input))

print(re.sub('\s', '', 'foo bar baz'))

