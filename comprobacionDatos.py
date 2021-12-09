import cv2
import pytesseract

base_datos = ['PRECIEUX ANDRIU']

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

imagen = cv2.imread('prueba.png')
texto_extraido = pytesseract.image_to_string(imagen, lang='spa')

for nombre in base_datos: 
    if texto_extraido.find(nombre) != -1:
        print(nombre, 'esta registrado.')
        
cv2.imshow('Tarjeta de identidad', imagen)
cv2.waitKey(0)
