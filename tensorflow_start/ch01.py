
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

# In[3]:

const1 = tf.constant(2)
const2 = tf.constant(3)
add_op = tf.add(const1,const2)
mul_op = tf.multiply(add_op,const2)

with tf.Session() as sess:
    mul_result, add_result = sess.run([mul_op,add_op])
    print(mul_result)
    print(add_result)


# ## リスト1.5 変数の宣言と代入

# In[4]:

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(mul_op))
    print(sess.run(mul_op))


# ## リスト 1.6　変数を初期化し、オペレーションを実行

# In[5]:

var1 = tf.Variable(0)
const2 = tf.constant(3)

add_op = tf.add(var1,const2)
update_var1 = tf.assign(var1, add_op)
mul_op = tf.multiply(add_op, update_var1)
# 変数をつかうには　tf.global_variables_initializer()


# ## リスト 1.7 異なるセッションの変数

# In[6]:

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

# In[7]:

with  tf.variable_scope('scope1'):
    var1 = tf.Variable(name="var1",initial_value=1.0)

with  tf.variable_scope('scope2-1'):
    var2 = tf.Variable(name="var2",initial_value=1.9)

print(var1.name)
print(var2.name)


# ## リスト 1.9 tf.Variableによる変数の宣言

# In[8]:

with tf.variable_scope('scope1'):
    var1_1 = tf.Variable(name="var1", initial_value=1.0)
    var1_2 = tf.Variable(name="var1", initial_value=1.0)
    print(var1_1.name)
    print(var1_2.name)


# ## リスト 1.10 tf.get_variableによる変数の宣言

# In[9]:

with tf.variable_scope('scope1'):
    var1_1 = tf.get_variable('var1', shape=[],initializer=tf.constant_initializer(1.0))
    var1_2 = tf.get_variable('var1',shape=[],initializer=tf.constant_initializer(1.0))


# 

# ## リスト 1.12 プレースホルダーの宣言

# In[14]:

var1 = tf.Variable(0)
holder2 = tf.placeholder(tf.int32)

add_op = tf.add(var1,holder2)
update_var1 = tf.assign(var1, add_op)
mul_op = tf.multiply(add_op,update_var1)


# ## リスト 1.13 プレースホルダーに値を与える

# In[15]:

with tf.Session()  as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run(mul_op,
                     feed_dict = {
            holder2 : 5
        })
    print(result)


# ## リスト 1.14 tf.addと演算子＋は同じ意味

# In[19]:

var1 = tf.constant(1)
var2 = tf.constant(2)
result1 = tf.add(var1, var2)
result2 = var1 + var2
print(result1)
print(result2)


with tf.Session() as sess:
    print(sess.run(result1))
    print(sess.run(result2))


# ## リスト 1.15 Numpyのブロードキャスティング

# In[21]:

import numpy as np

array1 = np.array([1,2,3,4])
value1 = 5

result = array1 + value1
print(result)


# ## リスト 1.16 Tensorflowのブロードキャスティング

# In[22]:

import tensorflow as tf

array1 = tf.constant([1,2,3,4])
value1 = tf.constant(5)
result = array1 + value1

with tf.Session() as sess:
    print(sess.run(result))


# ## リスト 1.17 TensorBoardにデータを書き出す

# In[23]:

const1 = tf.constant(2)
const2 = tf.constant(3)
add_op = tf.add(const1,const2)
mul_op = tf.multiply(add_op, const2)

with tf.Session()  as sess:
    mul_result, add_result = sess.run([mul_op, add_op])
    print(mul_result)
    print(add_result)

tf.summary.FileWriter('./',sess.graph)


# In[ ]:



