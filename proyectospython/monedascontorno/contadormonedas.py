from cv2 import GaussianBlur, cv2
import numpy as np

valorGauss=3
valorKernel=3
img = cv2.imread('C:\proyectospython\monedascontorno\monedas.jpg')
gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gauss =cv2.GaussianBlur(gris, (valorGauss,valorGauss), 0)
canny=cv2.Canny(gauss, 60,100)
kernel=np.ones((valorKernel,valorKernel),np.uint8)
cierre=cv2.morphologyEx(canny, cv2.MORH_CLOSE, kernel)

contornos, jerarquia=cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#Mostrar resultados
cv2.imshow('Grises',gris)
cv2.imshow('gauss',gauss)
cv2.imshow('canny',canny)
cv2.waitKey(0)
