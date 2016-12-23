def is_this_a_palindrome (str):
  return 'Yes.' if (str == str[::-1]) else 'No.'

print(is_this_a_palindrome('foof'))
## => Yes.
print(is_this_a_palindrome('foo'))
## => No.
