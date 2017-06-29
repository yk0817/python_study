
# coding: utf-8

# ## jupyter notebook練習

# In[8]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

# a + b
a = tf.constant(100)
b = tf.constant(50)
add_op = a + b
v = tf.Variable(0)
let_op = tf.assign(v, add_op)

# セッションを開始
sess = tf.Session()
sess.run(tf.initialize_all_variables())
sess.run(let_op)
print(sess.run(v))


# In[ ]:



