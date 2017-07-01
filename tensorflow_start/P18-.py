
# coding: utf-8

# In[1]:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

const1 = tf.constant(2)
const2 = tf.constant(3)
add_op = tf.add(const1,const2)
            
with tf.Session() as sess:
    result = sess.run(add_op)
    print(result)


# ## add_opをprint文で表示

# In[2]:

const1 = tf.constant(2)
const2 = tf.constant(3)
add_op = tf.add(const1, const2)
print(add_op)


# In[ ]:



