dimensions = (200, 50)
## Not valid, because tuples are immutable:
#dimensions[0] = 250

print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
  
## But you can reassign the entire tuple:
dimensions = (400, 100)

print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)



