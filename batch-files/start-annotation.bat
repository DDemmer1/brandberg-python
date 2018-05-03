REM zu eurer opencv location navigieren und eure Dateien eintragen
f:
cd F:\OpenCV\opencv\build\x64\vc15\bin
pause
opencv_annotation --annotations=workspace\pos\pos.txt --images=workspace\pos\pos-img --maxWindowHeight=1000 --resizeFactor=4
pause
