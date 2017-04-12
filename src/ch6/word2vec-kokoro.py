from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

bindata = open('kokoro.txt.sjis','rb').read()
text = bindata.decode('shift_jis')

text = re.split(r'\-{5,}',text)[2]
text = re.split(r'底本：',text)[0]
text = text.strip()

# 形態素