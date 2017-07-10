import signal
import sys
import logging
import logging.handlers

# 1億行のrowを持つtsvファイルを出力するプログラムを作成

LOG = 'logging.out'
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    LOG, maxBytes=10000, backupCount=5,)
my_logger.addHandler(handler)



# 一行カラム作成 tsvファイル

column_args = {
    'column_1':'int',
    'column_2':'short',
    'column_3':'long',
    'column_4':'double',
    'column_5':'bool',
    'column_6':'char[4]',
    'column_7':'varchar(utf-8)	',
    'column_8':'iso8601形式日時文字列',
    'column_9':'iso8601形式日付文字列',
    }
def make_column(column_args):
    return ("\t").join(column_args.values())

# def write_rows():


if __name__ == '__main__':
    print(make_column(column_args))
