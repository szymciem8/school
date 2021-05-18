import cv2
import numpy as np

# 1. Ukrywanie tekstu w obrazie ok
# 2. Ukrywanie obrazu w obrazie -> TODO
# Obraz ukrywany musi być takiego rozmiaru jak obraz, który ukrywa
# Obraz ukrywany ma być czarno-biały -> wysepują tylko 2 kolory: biały i czarny
# Obracanie obrazu oraz tekstu przy obracaniu o 30 stopni, 90 stopni itd
# Powiększanie, pomniejszanie, zmienianie typu (png, jpg, bmp)
# Trzy przykładu
# Wniosek: jak odporne są te metody
# Raport możliwie jak najkrótszy

def hide_word_in_img(word, img):
    list_chr = []
    temp = []

    for ch in word: 
        list_chr.append('{0:08b}'.format(ord(ch), 'b'))

    k=0
    y=0
    for i in range(len(word)):
        for j in range(8):
            temp = list('{0:08b}'.format(img[i*8+j][y], 'b'))
            temp[7] = list_chr[i][j]
            img[i*8+j][y] = int(''.join(temp), 2)

            if k%500 == 0 and k != 0:
                y += 1
            k += 1 

    return img

def get_word_from_img(img, length):
    found = ""
    letter = ''

    for i in range(length):
        for j in range(8):  
            letter = letter + '{0:08b}'.format(img[i*8+j][0], 'b')[7]

        found = found + chr(int(letter, 2))
        letter = ''
    
    return(found)

#Zakładamy, że oba obrazy są tego samego rozmiaru -> 500x500
def hide_img_in_img(img, img_to_hide):

    for x in range(len(img)):
        for y in range(len(img[x])):
            temp = list('{0:08b}'.format(img[x][y], 'b'))

            if img_to_hide[x][y] == 255:
                temp[7] = '1'
            else:
                temp[7] = '0'

            img[x][y] = int(''.join(temp), 2)

    return img

def get_img_from_img(img):
    found = np.zeros((500, 500))

    for x in range(len(img)):
        for y in range(len(img[x])):
            val = '{0:08b}'.format(img[x][y], 'b')[7]
            
            if val == '1':
                found[x][y] = 255
            else:
                found[x][y] = 0

    return found


#Zapis każdego znaku w 8 bitach nie 7
authors = "Szymon Ciemala i Kuba Kaniowski" 

img = cv2.imread("pepe.png", 0)
img_to_hide = cv2.imread("do_schowania.png", 0)

cv2.imshow("pepe", img)

hidden = hide_word_in_img(authors, img)
cv2.imshow("zmienione", hidden)

found = get_word_from_img(hidden, len(authors))
print(found)

img_with_hidden_img = hide_img_in_img(img, img_to_hide)
cv2.imshow("Schowany obraz", img_with_hidden_img)

found_img = get_img_from_img(img_with_hidden_img)
cv2.imshow('Znaleziony obraz', found_img)

cv2.waitKey()

