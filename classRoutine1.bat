@echo off
:Start
title Class Loader
cls
echo.
echo Disclaimer warning :  I am not be responsible for damage this script.&echo may do if you monkey around it, and no ill intention is built in.&echo Any issue if happened will be support at my discretion.&echo Bug if present and any damage due it is out of my control.&echo umesh.acem@gmail.com&echo. &echo.

set hhmm=%time:~0,5%
echo %hhmm%
set day=%date:~0,4%
echo %day%
goto %day%

:Sun
if %hhmm% LSS 07:00  goto NoClassYet
if %hhmm% LSS 08:40  goto MM        
if %hhmm% LSS 10:20  goto GDC        
if %hhmm% LSS 12:50  goto BreakTime  
if %hhmm% LSS 14:30  goto LKC        
if %hhmm% GTR 14:30  goto NoClass    
                   
:Mon
if %hhmm% LSS 07:00  goto NoClassYet
if %hhmm% LSS 08:40  goto SKR
if %hhmm% LSS 10:20  goto JG
if %hhmm% GTR 10:20  goto NoClass
:Tue
if %hhmm% LSS 07:00  goto NoClassYet
if %hhmm% LSS 08:40  goto MM
if %hhmm% LSS 10:20  goto NPA
if %hhmm% LSS 12:00  goto BreakTime
if %hhmm% LSS 13:40  goto PCR
if %hhmm% LSS 15:20  goto LKC
if %hhmm% GTR 15:20  goto NoClass 
:Wed
if %hhmm% LSS 07:00  goto NoClassYet
if %hhmm% LSS 08:40  goto SA
if %hhmm% LSS 10:20  goto SKR
if %hhmm% LSS 12:00  goto BreakTime
if %hhmm% LSS 13:40  goto AKR
if %hhmm% GTR 13:40  goto NoClass
:Thu
if %hhmm% LSS 07:00  goto NoClassYet
if %hhmm% LSS 08:40  goto MM
if %hhmm% LSS 10:20  goto SS
if %hhmm% LSS 12:00  goto BreakTime
if %hhmm% LSS 13:40  goto AKR
if %hhmm% GTR 13:40  goto NoClass
:Fri
if %hhmm% LSS 07:00  goto NoClassYet
if %hhmm% LSS 07:50  goto GBJ
if %hhmm% LSS 08:40  goto BreakTime
if %hhmm% LSS 10:20  goto SKR
if %hhmm% LSS 12:00  goto BreakTime
if %hhmm% LSS 13:40  goto RS
if %hhmm% GTR 13:40  goto NoClass
:Sat
goto NoClass

:MM
echo ElectroMagnetics-MM.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau
:NPA
echo Math-NPA.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
 
:GBJ
echo Math-GDC.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:SG
echo Math-SG.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:GDC
echo Math-GDC.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:SKR
echo ControlSystem - SKR.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:AKR
echo Electronic Device and Circuits - AKR.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:PCR
echo ElectronicDevice^&Circuits - PCR.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:LKC
echo Instrumentation-LKC.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:RS
echo Instrumentation-RS.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:SS
echo Probability and Statics - SS.
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:JG
echo Probability and Statics - JG
start chrome "https://meet.google.com/lookup/###?authuser=1" &goto pau 
:NoClassYet
echo Class has not started yet. &goto pau
:BreakTime
echo Break time now. &goto pau
:NoClass
echo There is no class now. &goto pau

:pau
echo. &echo. &echo.
set ans=n
set /p ans="press q to quit, anything else to check :"
if %ans%==q exit /b 
goto Start
