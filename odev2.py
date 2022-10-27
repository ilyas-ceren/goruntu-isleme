#ilyas ceren 02200201001
import cv2
import numpy as np
from matplotlib import pyplot as plt

adres= input("dosya adresini giriniz: \n")

img= cv2.imread(adres,0)
h,w=img.shape
max=0 #max deger saklanir

for i in range(h):
    for j in range(w):
        if img[i,j]>max:
            max=img[i,j]

#ayni boyutlarda bos bi matris olusturulur
invImg=np.zeros([h,w], dtype=np.uint8)

#tersine cevirme islemi
for i in range(h):
    for j in range(w):
        invImg[i,j]=max-img[i,j]

cv2.imshow("ters",invImg)

cv2.waitKey()
