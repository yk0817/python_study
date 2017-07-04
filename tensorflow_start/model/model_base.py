
# coding: utf-8

# ## リスト2.2 model_base

# In[ ]:


from __future__ import absolute_import
from __future__ import division 
from __future__ import print_function
import tensorflow as tf

def  variable_on_cpu(name,shape,initializer,trainable=True):
#     http://qiita.com/kikusumk3/items/907565559739376076b9
    with tf.device('/cpu:0'):
        var = tf.get_variable(name, shape, initialzer=initializer, trainable=trainable)
        return var

def _get_weights(shape, stddev=1.0):
    var = variable_on_cpu()

