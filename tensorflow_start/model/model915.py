
# coding: utf-8

# ## リスト2.1 : model915

# In[ ]:



from __future__ import absolute_import
from __future__ import print_function

import tensorflow as tf

NAME = 'model915'
OUTPUT_SIZE = INPUT_SIZE - (9 - 1) - (5 - 1) 
CHANNELS = 1

def inference(lr_images):
  conv1 = conv2d('conv1',
                 input_layer=lr_images,
                 weights_shape=[9, 9, CHANNELS, 64],
                 weight_stddev=1e-1,
                 biases_shape=[64], biases_value=0.0,
                 strides=[1, 1, 1, 1],
                 padding='VALID')
  conv1 = tf.nn.relu(conv1)

  conv2 = conv2d('conv2',
                 input_layer=conv1,
                 weights_shape=[1, 1, 64, 32],
                 weight_stddev=1e-1,
                 biases_shape=[32], biases_value=0.0,
                 strides=[1, 1, 1, 1],
                 padding='VALID')
  conv2 = tf.nn.relu(conv2)

  conv3 = conv2d('conv3',
                 input_layer=conv2,
                 weights_shape=[5, 5, 32, CHANNELS],
                 weight_stddev=1e-3,
                 biases_shape=[CHANNELS], biases_value=0.0,
                 strides=[1, 1, 1, 1],
                 padding='VALID')
  conv3 = tf.nn.relu(conv3)

  return conv3

