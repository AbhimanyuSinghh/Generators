#A very solid example of chaining generators
#here, two generators, fibonacci and square, fibonacci is giving the fibonacci series upto a number n and 
#square is giving square upto the number and our task is to print the square of those fibonacci series

def fibonacci(number):
    x, y = 0, 1
    for _ in range(number):
        x , y = y, x+y
        yield x
        
def square(number):
    for i in number:
        yield i**2
        
        
print(sum(square(fibonacci(10))))