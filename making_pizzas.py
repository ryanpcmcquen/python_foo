import pizza
##
## You can give aliases to individual functions you import:
##
##     from pizza import make_pizza as mp
##
## Or modules you import:
##
##     import pizza as p
##
## You may also import all functions into the namespace:
##
##     from pizza import *
##
## But this can pollute the namespace,
## so should be avoided.
##

pizza.make_pizza(16, 'pineapple')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'cauliflower')
