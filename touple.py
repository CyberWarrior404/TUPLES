tuple=("red","orange","yellow","green","blue","purple")
print(tuple)
print(type(tuple))

for item in tuple:
    print(item)

print(len(tuple))
print(tuple)
del tuple
print(tuple)

numbers = (0,0,7,2,4,6,31,5)
print(numbers)
print(max(numbers))
print(min(numbers))

print(sorted(numbers))

D = numbers.count(0)
print(D)    
print(numbers[2:6:])
print(numbers[::-1])
print(-1 in numbers)