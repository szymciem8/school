import cv2

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

line = []
with open('szyfrowanie/TI4B/hasla.txt') as f:
    n_of_keys = int(f.readline())
    for i in range(n_of_keys):
        line.append(list(map(int, f.readline().split(' '))))

# for i in range(n_of_keys):
#     print(line[i])

# with open('szyfrowanie/TI4B/1_tekst.txt', encoding="US-ASCII") as fi:
#     text = fi.readline()
#     print(text)

img = cv2.imread("szyfrowanie/TI4B/3.png", 0)
cv2.imshow("Original", img)

for i in range(n_of_keys):
    del line[i][0]
    key = line[i]

    key_decoded_img = key_img_code(img, key, 'decode')
    cv2.imshow("key decoded img", key_decoded_img)

    cv2.waitKey(0)

cv2.destroyAllWindows()