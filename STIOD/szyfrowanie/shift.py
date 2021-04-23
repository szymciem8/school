import random
import cv2

def rot_code(text, shift):
    encoded = ""

    for ch in range(len(text)):
        encoded += chr(ord(text[ch]) + shift)

    return encoded

def key_code(text, key, flag='encode'):
    encoded = ""

    if flag == 'encode': direction=1
    if flag == 'decode': direction=-1
    else: direction = 1

    for ch in range(len(text)):
        encoded += chr((ord(text[ch]) + direction * key[ch % len(key)]) % 255)

    return encoded

def rot_img_code(img, shift):

    for px in range(len(img)):
        for py in range(len(img[px])):
            img[px][py] = img[px][py] + shift
    return img

def key_img_code(img, key, flag='encode'):
    i=0

    if flag == 'encode': direction=1
    if flag == 'decode': direction=-1
    else: direction = 1

    for px in range(len(img)):
        for py in range(len(img[px])):
            img[px][py] = img[px][py] + direction * (key[i % len(key)] % 255)
            i += 1

    return img


example = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
key = [random.randint(0,255) for i in range(65000)]

enc_exmpl = rot_code(example, 5)
print(enc_exmpl)
print(rot_code(enc_exmpl, -5))

key_encoded = key_code(example, key, 'encode')
print(key_encoded)
print(key_code(key_encoded, key, 'decode'))

img = cv2.imread("szyfrowanie/b.png", 0)
cv2.imshow("Original", img)
#print(img[0:100])

encoded_img = rot_img_code(img, 201)
cv2.imshow("encoded img", encoded_img)

decoded_img = rot_img_code(img, -201)
cv2.imshow("decoded img", decoded_img)

#Maksymalny klucz to 65536

key_encoded_img = key_img_code(img, key, 'encode')
cv2.imshow("key encoded img", key_encoded_img)

key_decoded_img = key_img_code(key_encoded_img, key, 'decode')
cv2.imshow("key decoded img", key_decoded_img)

#DOŁOŻYĆ HISTOGRAM NAJLEPIEJ ZA POMOCĄ OPENCV

cv2.waitKey(0)
cv2.destroyAllWindows()