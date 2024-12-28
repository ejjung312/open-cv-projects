from easyocr import Reader
from PIL import Image

reader = Reader(['en'])

results = reader.readtext(Image.open("data.jpg"))

print(results)