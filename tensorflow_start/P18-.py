
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


# ## リスト1.3 add_opをprint文で表示

# In[2]:

const1 = tf.constant(2)
const2 = tf.constant(3)
add_op = tf.add(const1, const2)
print(add_op)


# ## リスト1.4 mul_opとadd_opを実行

# In[4]:

const1 = tf.constant(2)
const2 = tf.constant(3)
add_op = tf.add(const1,const2)
mul_op = tf.multiply(add_op,const2)

with tf.Session() as sess:
    mul_result, add_result = sess.run([mul_op,add_op])
    print(mul_result)
    print(add_result)


# ## リスト1.5 変数の宣言と代入

# In[8]:

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(mul_op))
    print(sess.run(mul_op))


# ## リスト 1.6　変数を初期化し、オペレーションを実行

# In[7]:

var1 = tf.Variable(0)
const2 = tf.constant(3)

add_op = tf.add(var1,const2)
update_var1 = tf.assign(var1, add_op)
mul_op = tf.multiply(add_op, update_var1)
# 変数をつかうには　tf.global_variables_initializer()


# ## リスト 1.7 異なるセッションの変数

# In[10]:

# 1つ目のセッション
with  tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(mul_op))
    print(sess.run([mul_op,mul_op]))
# 2つ目のセッション
with  tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(mul_op))
    print(sess.run([mul_op,mul_op]))


# ## リスト 1.8 スコープの宣言

# In[ ]:

with  tf.variable_scope('scope1'):
    var1 = tf.Variable(name="var1",initial_value=1.0)

with  tf.

