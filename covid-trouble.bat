@echo off

echo -------------------------------------------------------------------------------------------------------
echo -                  Donot close this cmd or the new web browser that is gonna pop up                   - 
echo -                  Summon GHOST if you are not sure about it.....GHOST                                -
echo -------------------------------------------------------------------------------------------------------

echo.
echo.

echo                                    Running the extractor....


"C:\Users\ghost\AppData\Local\Programs\Python\Python38\python.exe" "E:\Code dump\covid\covid-trouble\scripts\xwala.py"

"C:\Users\ghost\AppData\Local\Programs\Python\Python38\python.exe" "E:\Code dump\covid\covid-trouble\scripts\aftermath.py"

echo.
echo                                      File has executed....
echo.
echo.

echo                                     Updating github repo....
echo.
echo                                     Moving into the Git Repo
echo.
cd

E:

cd E:\Code dump\covid\covid-trouble

cd


git add .
git commit -m "%date%"
git push origin

echo                                            Git updated.
echo.
echo                                      ---  %Date%  ---  
echo.
echo                                       ---  %time%  ---  


pause