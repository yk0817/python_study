# 機械学習プログラムで遊んでみる
# 1.ツイートテキストを全て取得
# 2.ユーザーが特定の単語でどんな事をしているのか把握
# 3.例えば　仕事→楽しい、辛い　など　→特定のキーワードに対してその人がどんな印象を抱いているかわかる
# ビジュアルはD3で作れたらいいなー
#coding:utf-8
# mecabは使わない方針→辞書使わないしね〜
import pymysql
from janome.tokenizer import Tokenizer
import re
from gensim.models import word2vec
import sys

#接続情報
dbh = pymysql.connect(
         host='localhost',
         user='root',
         password='',
         db='machine_learning',
         charset='utf8',
         cursorclass=pymysql.cursors.DictCursor
    )

# 形態素解析
t = Tokenizer()
results = []
r = []
#カーソル
stmt = dbh.cursor()



tokyo_politic_array = ['kayoko49430','inosenaoki','ecoyuri','MasuzoeYoichi','i_shintaro','katsuhikoasano','miwako_azegami','kouji_ueki','uedareiko','ozaki_ayako','otokita','kamibayashi210','kawamatsushin16','koiso_akira','komatsu_daisuke','komachisa','KoyamaKunihiko','yasuhirosaitou','sakiyamac','yumisatoyoshi','shiomura','simizuhideko','tamioshiraishi','helibon1','tanakaasako','tokutomemtnb','nagahashikeiich','Nakamura_Mitaka','fnakayaka','nobudon7','nishizawakeita','nogamiyukie','nomuraarinobu','horikoudou1964','maeda_kazushige','tomosanma','miyase_eiji','morozumi_m','yanagase_ootaku','akira_yamauchi8','yoshida_nobuo','yonekura_haruna','tomoharu_arai','ishikawaryo1','tizumihcc','ito_shinagawa','ootsu_hiroko','akiraoomatsu','ohyamajim','kawai_shigeo','motonari_ldp','kurinori_tokyo','201Kuriyama','kounoyurie','kobaken_komei','SakuraiHiroyuki','suzuki_jm','tryosei','gambaretanaka','ta_tanimura','nakajimayoshio','junko_nogami116','mrbousai','FunasakaTikao','YoshiwaraO','morimasakosangi','miharajunco']


sql = "SELECT * FROM tweets where query = 'from:{tokyo_politic_array[0]}'".format()
print(sql)
sys.exit()

#実行
stmt.execute(sql)

#取得
rows = stmt.fetchall()


# 形態素解析

#Tokenizer出力例
# 英国	名詞,固有名詞,地域,国,*,*,英国,エイコク,エイコク
tokyo_politic_file = 'tokyo.wakati'

#ループ
for row in rows:
    tokens = t.tokenize(row["text"])
    with open(tokyo_politic_file,'a',encoding='utf-8')  as fp:
        for tok in tokens:
            if tok.base_form == "*":
                w = tok.surface
            else:
                w = tok.base_form
            ps = tok.part_of_speech #瀕死情報
            hinsi = ps.split(',')[0]
            if hinsi in ['名詞','形容詞']:
                r.append(w)
        rl = (" ".join(r)).strip()
        fp.write(rl)
        fp.write("\n")
        r = []
        rl = ""


# Word2Vecモデル
data = word2vec.LineSentence(tokyo_politic_file)
model = word2vec.Word2Vec(data,size=500,window=10,hs=1,min_count=10,sg=1)
model.save('tokyo_model')

#掃除
stmt.close();
dbh.close();

