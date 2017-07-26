from xml.etree import ElementTree
# https://docs.python.jp/3/library/xml.etree.elementtree.html

x = 'sample.xml'               # 読み込むxmlファイルのパスを変数に記憶させる
tree = ElementTree.parse(x)    # xmlファイルを読み込む
# print(tree)
root = tree.getroot()          # ルートを取得する


print(root.findall('country'))
print(root[0][0].tag)
print(root[0][0].text)
# xpath *→直接の子要素 .→現在の要素
# //→現在の要素配下のすべてのレベル上のすべての子要素を選択

print(tree.findall("*/rank"))
print(tree.findall(".//*[@name='Singapore']"))
print(tree.findall(".//"))
for child in root:
    print(child.tag, child.attrib)
