from PIL import Image
import pytesseract


im = Image.open('img/sparta.jpeg')
text = pytesseract.image_to_string(im)
print(text)
