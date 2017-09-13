import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# Import `tensorflow` 
import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
x2 = tf.constant([5,6,7,8,9,5,6,7,8,9,5,6,7,8,9,5,6,7,8,9,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,5,6,7,8,9,5,6,7,8,9,5,6,7,8,9,5,6,7,8,9,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])

# Multiply
result = tf.multiply(x1[6], x2[1])

# # Intialize the Session
# sess = tf.Session()
# 
# # Print the result
# print(sess.run(result))
# 
# # Close the session
# sess.close()

with tf.Session() as sess:
 output = sess.run(result)
print(output)