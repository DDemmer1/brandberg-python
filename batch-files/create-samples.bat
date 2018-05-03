REM zu eurer opencv location navigieren und eure Dateien eintragen
f:
cd F:\OpenCV\opencv\build\x64\vc15\bin

REM mit -info kann eine img collection in .vec umgewandelt werden
REM opencv_createsamples  -info workspace\pos\pos.txt -vec pos.vec -num 8 -w 50 -h 50

REM beispielhaft wurde nur ein jpg verwendet um 2000 samples als vec datei zu erstellen
opencv_createsamples  -img workspace\pos\pos.jpg -bg workspace\neg\bg.txt -vec pos.vec -num 2000 -w 50 -h 50
pause
