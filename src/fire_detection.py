# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:10:12 2023

@author: rayan
"""

#V0 - OpenCV
import cv2
import numpy as np

# Initialiser la capture vidéo de la webcam
cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Ajustez ces valeurs en fonction de vos besoins
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Appliquer un filtre morphologique pour nettoyer le masque
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Detection de Feu', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# V1 - YoloV8






































