from common import *
# 1億行のrowを持つtsvファイルを出力するプログラムを作成

LOG = 'logging.out'
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    LOG, maxBytes=10000, backupCount=5,)
my_logger.addHandler(handler)

UNIX_START = 1429000000
UNIX_NOW_UTC = int(datetime.now().strftime('%s'))
# 一行カラム作成 tsvファイル
# print(datetime.fromtimestamp(random.randint(UNIX_START,UNIX_NOW_UTC)).strftime('%Y-%m-%d'))
# print(datetime.fromtimestamp(random.randint(UNIX_START,UNIX_NOW_UTC)).strftime('%Y-%m-%d %H:%M:%S'))

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
    return ("\t").join(column_args.values()) + "\n"

def make_values():
    y_m_d_H_M_S = datetime.fromtimestamp(random.randint(UNIX_START,UNIX_NOW_UTC)).strftime('%Y-%m-%d %H:%M:%S')
    y_m_d = datetime.fromtimestamp(random.randint(UNIX_START,UNIX_NOW_UTC)).strftime('%Y-%m-%d')

    return ("\t").join([
        str(random.randint(-2**31,2**31-1)),
        str(random.randint(-2**15,2**15-1)),
        str(random.randint(-2**31,2**31-1)),
        str(random.uniform(0.1,2.7)),
        str(random.randint(0, 1)),
        "tttt",
        "test",
        str(y_m_d_H_M_S),
        str(y_m_d)
        ]) + "\n"

def write_file(arg):
    

if __name__ == '__main__':
    while True:
