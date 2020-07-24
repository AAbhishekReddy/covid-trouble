@echo off
echo Donot close this cmd or the new web browser that is gonna pop up
echo Summon GHOST if you are not sure about it.....GHOST

echo Running the extractor....

"C:\Users\ghost\AppData\Local\Programs\Python\Python38\python.exe" "E:\Code dump\covid\covid-trouble\xwala.py"

echo File has executed....
echo Updating github repo....

cd

git add .
git commit -m "%date%"
git push origin

echo Git updated.

pause