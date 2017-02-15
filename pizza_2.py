def make_pizza (*toppings):
    '''
    Summarize the pizza we are about to make.
    '''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())

make_pizza('pineapple')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
