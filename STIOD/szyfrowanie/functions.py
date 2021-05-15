import numpy as np 
import scipy.signal as sig 
import matplotlib.pyplot as plt

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
        encoded += chr((ord(text[ch]) + (direction * key[ch % len(key)])) % 256)

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
            img[px][py] = (img[px][py] + direction * key[i % len(key)]) % 256
            i += 1

    return img


def decode_key_binary(text, key):
    decoded = []

    for ch in text:
        decoded.append( (ch - key[ch % len(key)]) % 256)

    return decoded

def get_hist_text(text):
    histogram = [0] * 256
    
    for el in text:
        histogram[ord(el)] += 1

    return histogram

def get_hist_img(img):
    histogram = [0] * 256

    img = img.ravel()
    for el in img:
        histogram[el] += 1

    return histogram
