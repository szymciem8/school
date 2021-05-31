import cv2
import numpy as np
from functions import *

#Zapis każdego znaku w 8 bitach nie 7
authors = "Szymon Ciemala i Kuba Kaniowski" 

img = cv2.imread("pepe_oryginal.bmp", 0)
img_to_hide = cv2.imread("do_schowania.bmp", 0)

hidden = hide_word_in_img(authors, img)
hidden_img = hide_img_in_img(img, img_to_hide)

cv2.imwrite("schowany_tekst.bmp", hidden)
cv2.imwrite("schowany_tekst.png", hidden)
cv2.imwrite("schowany_tekst.jpg", hidden)

cv2.imwrite("schowany_obraz.bmp", hidden_img)
cv2.imwrite("schowany_obraz.png", hidden_img)
cv2.imwrite("schowany_obraz.jpg", hidden_img)

bmp = cv2.imread("schowany_tekst.bmp", 0)
png = cv2.imread("schowany_tekst.png", 0)
jpg = cv2.imread("schowany_tekst.jpg", 0)

img_bmp = cv2.imread("schowany_obraz.bmp", 0)
img_png = cv2.imread("schowany_obraz.png", 0)
img_jpg = cv2.imread("schowany_obraz.jpg", 0)

file = bmp
print('')
print(file)
cv2.imshow('test', file)
print(get_word_from_img(file, len(authors)))
cv2.imshow('obraz', get_img_from_img(img_jpg))
cv2.imwrite('odnaleziony_obraz.jpg', get_img_from_img(img_jpg))

cv2.waitKey()
