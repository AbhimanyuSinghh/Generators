#generator
def square(number):
    for i in range(1, number):
        yield i**2

#generator object to store the value yielded by the generator function
generator_object = square(10)
#getting values via next method, value is stored
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
#when loop starts, it does not start all over from 1, it knows what was the last value of i via yield statement
for i in generator_object:
    print(i)
        