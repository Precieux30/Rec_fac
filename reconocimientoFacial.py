import cv2
import os

ruta_datos = './Datos'
ruta_imagen = os.listdir(ruta_datos)

# Cargar el modelo
face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer.read('modeloEntrenado.xml')

imagen = cv2.imread('prueba.png')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

face_classif = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

auxiliar = gray.copy()
rostros = face_classif.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in rostros:
    rostro = auxiliar[y:y+h, x:x+w]
    rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
    resultado = face_recognizer.predict(rostro)

    # Comprobacion de rostro
    if resultado[1] < 5700:
        cv2.putText(imagen, '{}'.format(
            ruta_imagen[resultado[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)
    else:
        cv2.putText(imagen, 'Desconocido', (x, y-20), 2,
                    0.8, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 0, 255), 2)
 

cv2.imshow('Tarjeta identidad', imagen)
cv2.waitKey()
