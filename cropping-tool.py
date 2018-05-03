import os
import cv2
from os import listdir
from os.path import isfile, join


# Hier die Breite einstellen um das Bild im ganzen auf eurem Bilschirm zu sehen
screen_width = 1500


# Pfad zu den Bildern hier hinzufuegen
mypath = 'C:\Users\Dennis\Desktop\img'

# Pfad zum gewuenschten Speicherort
save_path = 'C:\Users\Dennis\Desktop\save-img'

# endung der ausgeschnitten Bilder
extension = 'roi.jpg'

# Auf true stellen wenn ausgeschnittenes Bild nochmal angezeigt werden soll
show_ROI = False

file_images = []
refPt = []
overall_rect = []

# Nur Files aus dem Ordner filtern
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Den Pfad des Programms auf den Bilder Ordner legen
os.chdir(mypath)



# Mehtode um Bilder zu verkleinern um sie an den Bildschirm anzupassen
def resize_to(width, image):
    r = float(width) / image.shape[1]
    dim = (width, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


# Mouse Listener Methode
def click_drag(event, x, y, flags, param):
    global refPt, overall_rect

    # Linke Maustaste nach unten
    if event == cv2.EVENT_LBUTTONDOWN:
        # Anfangspunkt des Rechtecks speichern
        refPt = [(x, y)]

    # Linke Maustaste wieder hoch
    elif event == cv2.EVENT_LBUTTONUP:
        # Endpunkt des Rechtecks speichern
        refPt.append((x, y))
        # Anfangs und Endpunkt zum Rechteck array hinzufuegen
        overall_rect.append(refPt)
        #Rechteck auf das Bild zeichnen
        cv2.rectangle(image, refPt[0], refPt[1], (0, 0, 255), 2)



#Bilder aus den Files filtern
for i in onlyfiles:
    if i.endswith('.jpeg') or i.endswith('.jpg') or i.endswith('.png'):
        file_images.append(i)

#Namen und Anzahl der gefundenen Bilder ausgeben
print file_images
print len(file_images), "images in ", mypath



# Ueber alle Bilder iterieren
for i in file_images:
    file_name = i.split('.')
    save_name = file_name[0]
    image = cv2.imread(i)

    # Bild an den Bildschirm anpassen
    image = resize_to(screen_width, image)

    cv2.imshow(i, image)

    clone = image.copy()
    image_name = i
    cv2.namedWindow(image_name)
    cv2.setMouseCallback(image_name, click_drag)

    # Auf Tastatureingabe warten
    while True:
        cv2.imshow(i, image)
        key = cv2.waitKey(1) & 0xFF

        # n = next
        if key == ord("n"):
            refPt = []
            cv2.destroyWindow(i)
            break

        # r = remove
        elif key == ord("r"):
            image = clone.copy()
            overall_rect.remove(refPt)
            refPt = []

    # ueber alle eingezeichneten Rechtecke iterieren
    for rect in range(overall_rect.__len__()):

        os.chdir(save_path)

        # ROI(region of interest) ausschneiden und darstellen
        roi = clone[overall_rect[rect][0][1]:overall_rect[rect][1][1], overall_rect[rect][0][0]:overall_rect[rect][1][0]]
        if show_ROI:
            cv2.imshow("ROI", roi)
            cv2.namedWindow("ROI")

        # ROI abspeichern
        index = str(rect)
        # cv2.imwrite(save_name + "-" + index + extension , roi)
        dim = (50, 50)
        roi = cv2.resize(roi, dim)
        interpolation = cv2.INTER_AREA
        cv2.imwrite(index + extension , roi)
        os.chdir(mypath)

        if show_ROI:
            cv2.waitKey(0)
            cv2.destroyWindow("ROI")

    overall_rect = []

cv2.destroyAllWindows()
