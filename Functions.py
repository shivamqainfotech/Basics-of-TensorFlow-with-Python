from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)



def plus(a,b):
    print ("Sum is ",a + b)
if(7>5):
    print("you are right")
plus(510, 65)


# Create a `Summation` class
class Summation(object):    
    def sum(self,a, b):   
        return (a + b)

# Instantiate `Summation` class to call `sum()`
sumInstance = Summation()
print(sumInstance.sum(1,2)) 

"""Prints "Hello World".

Returns:
    None
"""
def hello():
    name =input("Enter your name: ")
    
    if name:
        print ("Hello " ,name)
    else:
        print("Hello World") 
    return 
  
hello()




# Define `plus()`
def plu(a,b):
    sum1 = (a + b)
    return (sum1, a)

# Call `plus()` and unpack variables 
    sum1, a = plu(3,4)

# Print `sum()`
    print(sum1,a)