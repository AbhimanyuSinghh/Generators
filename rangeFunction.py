def myRange(start, end):
    while start<=end:
        yield start
        start+=1
        
for i in myRange(1,10):
    print(i)