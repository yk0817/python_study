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

def make_values():
    return ("\t").join([
        random.randint(-2**31,2**31-1),
        random.randint(-2**15,2**15-1),
        random.randint(-2**31,2**31-1),
        random.uniform(0.1,2.7),
        random.randint(0, 1),
        "tttt",
        "test",
        datetime.fromtimestamp(random.randint(UNIX_START,UNIX_NOW_UTC)).strftime('%Y-%m-%d %H:%M:%S'),
        datetime.fromtimestamp(random.randint(UNIX_START,UNIX_NOW_UTC)).strftime('%Y-%m-%d'),
        ]) + "\n"

if __name__ == '__main__':
    # print(make_column(column_args))
    print(make_values())
    # while True:
