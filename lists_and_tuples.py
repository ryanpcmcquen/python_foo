tuple = (100, 200, 300)
list = [100, 200, 300]

#print(list.map())
#print(tuple.map())
def addTwo (num):
    return num + 2

print(map(addTwo, tuple))
print(tuple)
print(map(addTwo, list))
print(list)

for value in list:
  	value = value + 2
  	print(value)

print(list)