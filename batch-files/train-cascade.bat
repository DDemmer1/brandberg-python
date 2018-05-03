REM zu eurer opencv location navigieren und eure Dateien eintragen

f:
cd F:\OpenCV\opencv\build\x64\vc15\bin

REM  -precalcValBufSize 6000 und -precalcIdxBufSize 6000 gibt an wieviel RAM ihr verwenden wollt (darf zusammen nicht euren max RAM ueberschreiten)  default ist jeweils 1gb 
opencv_traincascade -data workspace -vec pos.vec -bg workspace\neg\bg.txt -numPos 1800 -numNeg 900 -numStages 8 -precalcValBufSize 6000 -precalcIdxBufSize 6000   -w 50 -h 50

pause
