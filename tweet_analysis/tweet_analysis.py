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

#接続情報
dbh = pymysql.connect(
         host='localhost',
         user='root',
         password='',
         db='machine_learning',
         charset='utf8',
         cursorclass=pymysql.cursors.DictCursor
    )

#カーソル
stmt = dbh.cursor()


sql = "SELECT * FROM tweets where query = 'from:inosenaoki'"

#実行
stmt.execute(sql)

#取得
rows = stmt.fetchall()

#ループ
for row in rows:
    print(row)

#掃除
stmt.close();
dbh.close();

