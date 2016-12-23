def is_this_a_palindrome (str):
  return 'Yes.' if (str is str[::-1]) else 'No.'

print(is_this_a_palindrome('foof'))
## => Yes.
print(is_this_a_palindrome('foo'))
## => No.

#print(reversed(list('foof')))

#print(['f', 'o', 'o'].reverse())
#print(reversed(['f', 'o', 'o']))

#print(['foo', 'bar'].reverse())