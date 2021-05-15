import cv2
from functions import *
from matplotlib import pyplot as plt 

lines = []
with open('szyfrowanie/TI4B/hasla.txt') as f:
    n_of_keys = int(f.readline())
    for i in range(n_of_keys):
        lines.append(list(map(int, f.readline().split(' '))))
        del lines[i][0]
        
    #print(lines)

# for i in range(n_of_keys):
#     print(line[i])

with open('szyfrowanie/TI4B/2_tekst.txt', 'rb') as f:
    text_bin = f.read()
    text = ''

    for el in text_bin:
        text += chr(el)
    
    #print(text)


for i, key in enumerate(lines):

    new_text = key_code(text, key, 'decode')
    hist = get_hist_text(new_text)

    if max(hist) > 100:
        print('found')
        print(i)
        print(hist)
        print(key)
        print(new_text)


img = cv2.imread("szyfrowanie/TI4B/2.png", 0)

for i, key in enumerate(lines):

    #if i>1200:

    new_img = key_img_code(img, key, 'decode')

    hist = get_hist_img(new_img)
    #print(hist)

    print(i)
    if max(hist) > 1200:
        print(key)
        print('found')
        print(hist)
        cv2.imshow("Decoded", new_img)
        break

cv2.imshow("Original", img)
cv2.waitKey(0)

cv2.destroyAllWindows()