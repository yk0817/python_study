
# coding: utf-8

# In[4]:

import ngram as ng
import  sys
text = 'あいうえお'
print(ng)
# sys.exit()
index = ng.NGram(N=2)
for  term  in  index.ngrams(index.pad(text)):
    print(term)


# In[ ]:



