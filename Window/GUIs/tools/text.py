

import easyocr
reader = easyocr.Reader(['ch_sim', 'en'])
#result = reader.readtext('C:\\Users\\29296\\Pictures\\text.jpg', detail=0)
result = reader.readtext('C:/Users/29296/Pictures/photo3.jpg', detail=0)
article = ''  # 定义一个空的字符串
for i in range(len(result)):
    article += result[i]  # 将列表中的字符串依次拼接在一起
print(article)
