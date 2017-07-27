import openpyxl
import glob
import sys
import xlrd
import re

# xlsm用の
# DIRECTORY = ARGV[0]
# worksheets = glob.glob('./*')
#
# for worksheet in worksheets:
#     ws = openpyxl.load_workbook(worksheet)
#     sheet_names = ws.get_sheet_names()
#     print(sheet_names)
#     sys.exit()

# ワークシート(xlsのモジュール)
worksheets = glob.glob('./*')

for worksheet in worksheets:
    print("worksheet名:",worksheet)
    if re.match(r".+【開示先限定】共通_コード定義書.xls",worksheet):
        continue
    books = xlrd.open_workbook(worksheet)

    # テーブル名
    print(books.sheet_by_index(1).cell_value(rowx=5, colx=19))
    # テーブル説明
    print(books.sheet_by_index(1).cell_value(rowx=6, colx=1))
