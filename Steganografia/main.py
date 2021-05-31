import cv2
import numpy as np
from functions import *

#Zapis każdego znaku w 8 bitach nie 7
authors = "Szymon Ciemala i Kuba Kaniowski" 

img = cv2.imread("pepe_oryginal.bmp", 0)
img_to_hide = cv2.imread("do_schowania.bmp", 0)

# cv2.imshow("pepe", img)

hidden = hide_word_in_img(authors, img)
# cv2.imshow("zmienione", hidden)
cv2.imwrite("Zaszyfrowany_tekst.bmp", hidden)
found = get_word_from_img(hidden, len(authors))


#rotation
hidden_90 = cv2.rotate(hidden, cv2.ROTATE_90_CLOCKWISE)
found_90 = get_word_from_img(hidden_90, len(authors))
hidden_180 = cv2.rotate(hidden_90, cv2.ROTATE_90_CLOCKWISE)
found_180 =  get_word_from_img(hidden_180, len(authors))
hidden_270 = cv2.rotate(hidden_180, cv2.ROTATE_90_CLOCKWISE)
found_270 = get_word_from_img(hidden_270, len(authors))


size = lambda scale, img: (int(img.shape[1] * scale/100), int(img.shape[0] * scale / 100))
print(size(99, img))
dim = size(50, img)
resized = cv2.resize(hidden, dim)
# cv2.imshow("resized", resized)
found_resized = get_word_from_img(resized, len(authors))
print('Po zmniejszeniu')
print(found_resized)

print()
print("Znaleziony tekst bez obrotu:")
print(found)
print("Znaleziony tekst z obrotem o 90 stopni w prawo:")
print(found_90)
print("Znaleziony tekst z obrotem o 180 stopni w prawo:")
print(found_180)
print("Znaleziony tekst z obrotem o 270 stopni w prawo:")
print(found_270)
print()

img_with_hidden_img = hide_img_in_img(img, img_to_hide)
# cv2.imshow("Schowany obraz", img_with_hidden_img)
cv2.imwrite("img_with_hidden_img.bmp", img_with_hidden_img)

img_90 = cv2.rotate(img_with_hidden_img, cv2.ROTATE_90_CLOCKWISE)
img_180 = cv2.rotate(img_90, cv2.ROTATE_90_CLOCKWISE)
img_270 = cv2.rotate(img_180, cv2.ROTATE_90_CLOCKWISE)

found_img = get_img_from_img(img_with_hidden_img)
found_img_90 = get_img_from_img(img_90)
found_img_180 = get_img_from_img(img_180)
found_img_270 = get_img_from_img(img_270)

#cv2.imshow('Znaleziony obraz', found_img)
cv2.imwrite("found_img.bmp", found_img)
cv2.imwrite("found_img_90.png", found_img_90)
cv2.imwrite("found_img_180.png", found_img_180)
cv2.imwrite("found_img_270.png", found_img_270)

cv2.waitKey()

