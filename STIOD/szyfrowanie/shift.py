import random
import cv2
from functions import *
import numpy
from matplotlib import pyplot as plt 

example = "Ogolnie znana teza glosi, iz uzytkownika moze rozpraszac zrozumiala zawartosc strony, kiedy ten chce zobaczyc sam jej wyglad. Jedna z mocnych stron uzywania Lorem Ipsum jest to, ze ma wiele roznych kombinacji zdan, slow i akapitow, w przeciwienstwie do zwyklego: ,,tekst, tekst, tekst, sprawiajacego, ze wyglada to ,,zbyt czytelnie po polsku. Wielu webmasterow i designerow uzywa Lorem Ipsum jako domyslnego modelu tekstu i wpisanie w internetowej wyszukiwarce 'lorem ipsum' spowoduje znalezienie bardzo wielu stron, ktore wciaz sa w budowie. Wiele wersji tekstu ewoluowalo i zmienialo sie przez lata, czasem przez przypadek, czasem specjalnie (humorystyczne wstawki itd). Lorem Ipsum jest tekstem stosowanym jako przykladowy wypelniacz w przemysle poligraficznym. Zostal po raz pierwszy uzyty w XV w. przez nieznanego drukarza do wypelnienia tekstem probnej ksiazki. Piec wiekow pozniej zaczal byc uzywany przemysle elektronicznym, pozostajac praktycznie niezmienionym. Spopularyzowal sie w latach 60. XX w. wraz z publikacja arkuszy Letrasetu, zawierajacych fragmenty Lorem Ipsum, a ostatnio z zawierajacym rozne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji drukow na komputerach osobistych, jak Aldus PageMaker"
key = [random.randint(0,255) for i in range(len(example))] #65536

# print("klucz")
# print(key)

# print('\n\n')
# print('Nowy run')
# print('\n\n')


# shift=125
# enc_exmpl = rot_code(example, shift)
# # print("Szyfr rotacyjny")
# # print(enc_exmpl)
# # print(rot_code(enc_exmpl, -shift))
# # print('\n\n')
# print('\n\n')

print('Szyfr z kluczem')
key_encoded = key_code(example, key, 'encode')
print(key_encoded)
print('\n\n')
key_decoded = key_code(key_encoded, key, 'decode')
print(key_decoded)

num_example = []
for el in key_encoded:
    num_example.append(ord(el))

plt.hist(num_example, 128, [0,255], label='test')
plt.title('Histogram dla szyfru z kluczem równym długości tekstu')
plt.show()

# img = cv2.imread("szyfrowanie/b.png", 0)
# cv2.imshow("Original", img)
#print(img[0:100])

# encoded_img = rot_img_code(img, 100)
# cv2.imshow("encoded img", encoded_img)

# decoded_img = rot_img_code(img, -100)
# cv2.imshow("decoded img", decoded_img)

#Maksymalny klucz to 65536

# key_encoded_img = key_img_code(img, key, 'encode')
# cv2.imshow("key encoded img", key_encoded_img)

# key_decoded_img = key_img_code(key_encoded_img, key, 'decode')
# cv2.imshow("key decoded img", key_decoded_img)

#DOŁOŻYĆ HISTOGRAM NAJLEPIEJ ZA POMOCĄ OPENCV

# plt.hist(img.ravel(), 256, [0,256], label='test')
# plt.title('Histogram oryginału b.png')
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()