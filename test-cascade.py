import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
Kurzes script um die cascade zu testen
'''


#cascade laden
rock_art_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('065.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



rock_art = rock_art_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in rock_art:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]


#img fuer pyplot vorbereiten
rgb = np.fliplr(img.reshape(-1,3)).reshape(img.shape)

imgplot = plt.imshow(rgb)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()