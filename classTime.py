#! /usr/bin/python3

# coded by umesh kr. shrestha due to boredome and lazyness of opening the
# google classrooom each time checking the routine, opeming respective teachers
# class and then clicking the link and opening the class
# class routine of Advanced College of Engineering and Management. 2nd sem.
# request all to not misuse the code and misue any information given here.
# thought of using the bash script first and sucessfully made a sucessful code
# but self unstaisfied as it is full of bugs.
# planned to do in c or c++ but since i am not sure when the code needs to be modified
# so did not wanted to do a compile
# this code is the second version  here improvement is done for editiability of the routine
# basic OOP object concept is used here to organize.the routine and making the code
# univesally extensible.. a vast improvemnt over the first iteration of equivalent
# program
# This program is highly compact and consise

import datetime
import os
import subprocess
import calendar
import time
import sys
from PIL import Image

# uses chromium browser if used in windows replace chromium with  absolute path to chrome excetuable
# defining classTime variables with the appropriate permalinks opening in the chromium app mode
# same commannd as that to be used while using CLI to open link in app mode 
# <Class_url> put each subjects class's meeting urls here
micro = "echo microprocessor; chromium --app=<Class_url> 1>/dev/null 2>/dev/null &"
MatRP = "echo math RP; chromium --app=<Class_url> 2>/dev/null &"
elect = "echo electric technology; chromium --app=<Class_url> 2>/dev/null &"
chem = "echo chemistry; chromium --app=<Class_url> 2>/dev/null &"
MatNPA = "echo math NPA; chromium --app=<Class_url> 2>/dev/null &"
OOP = "echo OOP; chromium --app=<Class_url> 2>/dev/null &"
WS = "echo Workshop; chromium --app=<Class_url> 2>/dev/null &"
NULL = "NULL"

# Routine in list of tuple form
# day =[(1st period start  time hhmm, sub),(2nd period start time hhmm, sub), .... (endtime, NULL)]

Sun = [(700,OOP)  ,(840,chem)     ,(1020,NULL)  ]
Mon = [(700,micro),(840,MatNPA)   ,(930,NULL)  ]
Tue = [(700,MatRP),(840,elect)    ,(1020,NULL)  ]
Wed = [(700,micro),(840,chem)     ,(1020,NULL)  ]
Thu = [(700,OOP)  ,(750,elect)    ,(930,NULL)   ]
Fri = [(700,WS)   ,(750,MatNPA)   ,(930,NULL)   ]
Sat = [(0,NULL)]


dt = datetime.datetime.now() #get the current date and time in dt varible datetime object time
print(dt)

HHMM=dt.hour*100 + dt.minute + 5                # 5 is the amount of time in min to login piror too actual start
day_name = calendar.day_name[dt.weekday()] #gets date name from array in the calerder object using dt.weekday as index

if      (day_name == 'Sunday')      :  xyz=Sun  # these codes here for simplyfing the code below
elif    (day_name == 'Monday')      :  xyz=Mon  # here we select the row of the routine or day of the routine
elif    (day_name == 'Tuesday')     :  xyz=Tue
elif    (day_name == 'Wednesday')   :  xyz=Wed
elif    (day_name == 'Thursday')    :  xyz=Thu
elif    (day_name == 'Friday')      :  xyz=Fri
elif    (day_name == 'Saturday')    :  xyz=Sat
else :  print ('This should never be printed')

print (day_name, 'Class at time', HHMM-5)
i=0                                                     # go through the list of day in routine to see
while (xyz[i][1] != 'NULL'):                            # which class is currenty being active
    if ( HHMM >= (xyz[i][0]) and HHMM< xyz[i+1][0]) :   # the class if from start time of this class to start time of next one
        #print (xyz[0])
        #os.system(xyz[i][1])
        subprocess.Popen ( (xyz[i][1]) , preexec_fn=os.setsid)
                                                        # actual execution of the meeting in app mode in chrome/chromium
        time.sleep(5)                                   # may be needed for spawn to be detached
        exit(0)                                         # class launched hece task is done exit(0) to indicate sucess
    else :
        #print ('looping')                              # debug line
        i+=1                                            # iterete next item to check for  more class until class data is NULL

# while terminates and falls here of there is no classes remianing

print ('No class scheduled')
# displays the routing in the path file:///home/shr/Desktop/routine.jpg put absolut path after file:///
#os.system('chromium --app="file:///home/shr/Desktop/routine.jpg"')
Image.open('./routine.jpg').show()                      # open image module in python
time.sleep(5)                                           # sleep sometime so the output remain visible for set amount in second



