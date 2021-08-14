import cv2
import numpy as np
import matplotlib.pyplot

#img = cv2.imread('opencv-logo.png',0)
img = cv2.imread('40.jpg',0)
#img = cv2.imread('przyklad.jpg',0)
img = cv2.medianBlur(img,5)

szar_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

kolka = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=170,param2=15,minRadius=0,maxRadius=0)
wszkolka = np.uint16(np.around(kolka))
print(kolka)
print(wszkolka.shape)
print('kropek ' + str(wszkolka.shape[1]))
licz=1
for i in wszkolka[0,:]:
     # wyznaczenie obwodu kropki
     cv2.circle(szar_img,(i[0],i[1]),i[2],(0,255,0),2)
    # wyznaczenie srodka kropki
     cv2.circle(szar_img,(i[0],i[1]),2,(0,0,255),3)
     #cv2.putText(img, "Kolka "+ str(licz), (i[0]-70,i[1]+30), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255,0,0), 2)
     licz +=1

cv2.imshow('Wykryte kropki',szar_img)
cv2.imwrite('wynik.jpg', szar_img)
cv2.waitKey(0)
cv2.destroyAllWindows()