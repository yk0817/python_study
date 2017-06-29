
# coding: utf-8

# In[3]:

import tensorflow as tf

# プレースホルダーを定義
a = tf.placeholder(tf.int32,[None])

# 配列を10倍にする演算を定義
b = tf.constant(10)
x10_op = a * b

sess = tf.Session()
r1 = sess.run(x10_op, feed_dict={a: [1,2,3,4,5]})
print(r1)

r2 = sess.run(x10_op,feed_dict={a: [10,20]})


# In[ ]:



