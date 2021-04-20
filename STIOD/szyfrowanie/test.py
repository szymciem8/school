import cv2
import os

img = cv2.imread(os.getcwd() + "/szyfrowanie/b.png", 0)
print(os.getcwd())
cv2.imshow("obrazek", img)

cv2.waitKey(0)
cv2.destroyAllWindows()