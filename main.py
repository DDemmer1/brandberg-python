import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#Mindest groesse um als objekt erkannt zu werden
MIN_CONTOUR_AREA = 1000

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

brandberg_065 = cv2.imread("065.jpg")

if brandberg_065 is None:
    print "error: kein Bild gefunden \n\n"
    os.system("pause")

imgGray = cv2.cvtColor(brandberg_065, cv2.COLOR_BGR2GRAY)
imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)
#cv2.imshow("Blurred", imgBlurred)

imgThresh = cv2.adaptiveThreshold(imgBlurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

imgThreshCopy = imgThresh.copy()

imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

npaFlattenedImages = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))


for npaContour in npaContours:

    if cv2.contourArea(npaContour) > MIN_CONTOUR_AREA:
        [intX, intY, intW, intH] = cv2.boundingRect(npaContour)

        cv2.rectangle(brandberg_065, (intX, intY), (intX + intW, intY + intH),(255, 0, 0),2)

        imgROI = imgThresh[intY:intY + intH, intX:intX + intW]
        # imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH,RESIZED_IMAGE_HEIGHT))

        imgROI = cv2.bitwise_not(imgROI)
        #cv2.imshow("imgROI", imgROI)
        # cv2.imshow("imgROIResized", imgROIResized)
        cv2.waitKey(0)
        cv2.destroyWindow("imgROI")



# Verkleinert ein Bild um die haelfte
#small = cv2.resize(brandberg_065, (0,0), fx=0.5, fy=0.5)


#Besser mit pyplot darstellen wegen Zoom etc.
#cv2.imshow("pic", brandberg_065)

imgplot = plt.imshow(brandberg_065)

plt.show()

cv2.waitKey(0)
