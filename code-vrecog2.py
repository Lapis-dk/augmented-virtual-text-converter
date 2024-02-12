# adds more image processing capabilities
from PIL import Image, ImageEnhance
# will convert the image to text string
from pytesseract import pytesseract
# assigning an image from the source path
# img = Image.open(r"C:\Pytemp1\Myvenv1\mini-project-1\picsave21_42_24.jpg")
img = r"C:\Pytemp1\Myvenv1\mini-project-1\sampletext.png"

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# adding some sharpness and contrast to the image 
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)
# save the new image
img_edit.save("edited_image.png")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img_edit)
print(result)
