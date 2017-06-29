
# coding: utf-8

# In[3]:

import tensorflow as tf

# プレースホルダーを定義
a = tf.placeholder(tf.int32,[3]) #整列型の要素3個の配列
b = tf.constant(2)
x2_op = a * b
sess = tf.Session()
r1 = sess.run(x2_op, feed_dict={a:[1,2,3]})
# print(r1)
r2 = sess.run(x2_op, feed_dict={a:[10,20,10]})
# print(r2)


# In[ ]:



