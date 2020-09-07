#! /usr/bin/python3\
# due laziness this was born
# for class scheduel of the ACEM online session 2nd Sem

import datetime
import os
import calendar
import time

# defining class variables  sorry cannot publish the private data class url
micro = "chromium --app=<class url>"
MatRP = "chromium --app=<class url>"
elect = "chromium --app=<class url>"
chem = "chromium --app=<class url>"
MatNPA = "chromium --app=<class url>"
OOP = "chromium --app=<class url>"
WS = "chromium --app=<class url>"


print(datetime.datetime.now())
dt = datetime.datetime.now()

#print (dt.year)
#print (dt.hour)

day_name = calendar.day_name[dt.weekday()]
#print('Day of Week (name): ', day_name)
# j = 0
# for i in calendar.day_name:  // dat_name is an string array
#    print(j,'-',i)
#    j+=1
#0 - Monday 1 - Tuesday 2 - Wednesday 3 - Thursday 4 - Friday 5 - Saturday 6 - Sunday

day=dt.weekday()
HH= dt.hour
MM= dt.minute
HHMM=HH*100 + MM

print ( 'Today is ', day_name ,'; time is ', HH,':',MM)

# switch (day)  python does not have a switch () :(\

if   (day_name == 'Sunday')  :   
    print (day_name," ", HHMM)
    if (HHMM >=700 and HHMM <840)  :
        print ("Ist class")
        os.system (OOP)
    elif ((HHMM >=840 and HHMM <1020) ) :
        print("IInd class")
        os.system (chem)
    else :
        print ("NO CLASS")
elif day_name == 'Monday':     
    print (day_name," ", HHMM)
    if (HHMM >=700 and HHMM <840)  :
        print ("Ist class")
        os.system (micro)
    elif (HHMM >=840 and HHMM <1020)  :
        print("IInd class")
        os.system (MatNPA)
    else :
        print ("NO CLASS")
elif day_name == 'Tuesday':     
    print (day_name," ", HHMM)
    if (HHMM >=700 and HHMM <840)  :
        print ("Ist class")
        os.system (MatRP)
    elif (HHMM >=840 and HHMM <1020)  :
        print("IInd class")
        os.system (elect)
    else :
        print ("NO CLASS")
elif day_name == 'Wednesday':     
    print (day_name," ", HHMM)
    if (HHMM >=700 and HHMM <840)  :
        print ("Ist class")
        os.system (micro)
    elif (HHMM >=840 and HHMM <1020)  :
        print("IInd class")
        os.system (chem)
    else :
        print ("NO CLASS")
elif day_name == 'Thursday':     
    print (day_name," ", HHMM)
    if (HHMM >=700 and HHMM <750)  :
        print ("Ist class")
        os.system (OOP)
    elif (HHMM >=750 and HHMM <930)  :
        print("IInd class")
        os.system (elect)
    else :
        print ("NO CLASS")
elif day_name == 'Friday':    
    print (day_name," ", HHMM)
    if (HHMM >=700 and HHMM <750)  :
        print ("Ist class")
        os.system (WS)
    elif (HHMM >=750 and HHMM <930)  :
        print("IInd class")
        os.system (Math)
    else :
        print ("NO CLASS")
else :               
    print (day_name," ", HHMM)
    print ("NO CLASS")
    
time.sleep(5)




