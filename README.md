# brandberg-python

Respository zum Aufbauseminar "Künstliche Intelligenz und Cultural Heritage: Upper Brandberg – Im Louvre der Felsmalerei" an der Universität zu Köln.
http://www.lehre.jan-wieners.de/sosem18-kuenstliche-intelligenz-und-cultural-heritage-upper-brandberg-im-louvre-der-felsmalerei/

Mithilfe des Frameworks OpenCV und Haar Cascade Classifiern wird versucht eine Objekterkennug von Höhlenmalereien zu implementieren. Dazu wurde sich für die Scriptsprache Python entschieden.

Das Script "cropping-tool" dient dazu Trainingsdaten zu erstelllen. Im "contour-recognition" Script ist ein erster Ansatz zu sehen per Kontur Erkennung an das Problem heran zu gehen.
Es wurde sich dann dazu entschieden per Machine Learning Haar Cascade Classifier zu erstellen und diese anzuwenden (siehe "test-cascade.py")
Die Batch-Files wurden erstellt um mit den vorgefertigten tools von OpenCV effizienter arbeiten zu können

TODO:
- Bestmögliche Trainingsdaten für die Haar Cascade erstellen
- Haar Cascade Erfolg testen
- eventuell noch Tensorflow oder Caffe2 hinzuziehen um Ergebnisse zu verbessern
