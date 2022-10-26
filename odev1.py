#İlyas Ceren 02200201001
import cv2
import numpy
from matplotlib import pyplot as plt

adres= input("dosya adresini giriniz: \n")
foto=cv2.imread(adres)

# fotograf griye donusturuluyor
cv2.imshow("Fotograf", foto)
B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]
imgray= 0.2989 * R + 0.5870 * G + 0.1140 * B


#resmin boyutları aliniyor ve histogram icin dizi olusturuluyor.
x,y=imgray.shape
hist=[0]*255

#her pixelin degerine gore histogram arttıriliyor
for i in range(x):
    for j in range(y):
        a=int(imgray[i,j])
        hist[a]=hist[a]+1

plt.plot(hist)
plt.show()

cv2.waitKey()