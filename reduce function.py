import functools

#letters = ["H", "E", "L", "L", "O"]
#hello = functools.reduce(lambda x, y :x+y,letters)
#print(hello)

numbers = [5,4,3,2,1]
factorial = functools.reduce(lambda x, y, : (x*y), numbers)
print(factorial)
