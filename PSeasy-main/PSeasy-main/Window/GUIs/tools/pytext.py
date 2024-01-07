import pytesseract
from PIL import Image

image = Image.open('C:\\Users\\29296\\Pictures\\yuanse1.png')
code = pytesseract.image_to_string(image, lang='eng')
print(code)