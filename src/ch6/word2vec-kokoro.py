from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

bindata = open('./kokoro.txt','rb').read()
text = bindata.decode('shift_jis')

text = re.split(r'\-{5,}',text)[2]
text = re.split(r'底本：',text)[0]
text = text.strip()

# 形態素
t = Tokenizer()
results = []

lines = text.split("\r\n")

for line in lines:
    s = line
    s = s.replace('｜','')
    s = re.sub(r'《.+?》','',s)
    s = re.sub(r'［＃.+?］','',s)
    tokens = t.tokenize(s)
    r = []
    for tok in tokens:
        if  tok.base_form == "*":
            w = tok.surface
        else:
            w = tok.base_form
        ps = tok.part_of_speech
        hinshi = ps.split(',')[0]
        if  hinshi in ['名詞','形容詞','動詞','記号']:
            r.append(w)
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl) # --- カチ割り
    
# 書き込み先テキストを開く
wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))

# word2vecでモデル作成
data = word2vec.LineSentene(wakati_file)
model = word2vec.Word2Vec(data,size=200,window=10,hs=1,min_count=2,sg=1)
model.save('kokoro.model')
print('ok')
