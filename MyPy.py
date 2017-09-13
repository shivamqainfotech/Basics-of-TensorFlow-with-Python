import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf


#Global function
def global_function(a,b):
    return a+b

#Anonymous function/ Lambda Function 
double = lambda x,y: x**y
                       


#Global function with var args
def plus(*nums):
    total=0
    for i in nums:
        total +=i
    return total


#class
class MyTensor(object):
#Class method/function
    def hello_tensor(self):
        hello = tf.constant("Hello, TensorFlow!")
        sess = tf.Session()
        print((sess.run(hello)).decode())
        a = tf.constant(10)
        b = tf.constant(32)
        c=a+b
        print("TensorFlow addition ->",sess.run(c))
        sess.close()
        print("session closed")
        
#object creation
t=MyTensor()
#calling method
t.hello_tensor()
#Calling Anonymous function/ Lambda Function 
print("Calling anonymous lambda ->",double(5,3))
#calling global function
print("calling global function ->",global_function(5, 10))
# Calculate the sum of var args function
print("Calculate the sum of var args function ->",plus(1,4,5,6))

