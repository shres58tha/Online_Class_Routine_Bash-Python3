#! /usr/bin/python3
# modified to run
# coded by umesh kr. shrestha
# fisrt year UMESH076BEI029@acem.edu.np
# contact due to boredome and lazyness of opening the
# google classrooom each time checking the routine, opeming respective teachers
# class and then clicking the link and opening the class
# class routine of Advanced College of Engineering and Management. 3rd sem.BEI
# request all to not misuse the code and misue any information given here.
# thought of using the bash script first and sucessfully made a sucessful code
# but self unstaisfied as it is full of bugs.
# planned to do in c or c++ but since i am not sure when the code needs to be modified
# so did not wanted to do a compile
# this code is the second version  here improvement is done for editiability of the routine
# basic OOP object concept is used here to organize.the routine and making the code
# univesally extensible.. a vast improvemnt over the first iteration of equivalent
# program
# This program is  generalized and external data file have been added
#2021 May 05 improvement made. same code and data works for 'posix' and 'nt'
# option to generate the sample class.txt file added
# code revised and improvment done as well as unnecessary debug line removed

#sample class.txt
text='''# anything starting with # is a comment
# data base for the Class.
# modify here to add or remove or update routine
# example format

# for windows do following  no quotes
# micro |microprocessor && start chrome --app=URL_GOOGLE MEET?authuser=1

#-END-  lable control the start and end of data

#browser chromium / chrome
# this command gets excuted so be careful
#name_browser | ?authuser=1  +> is the profile in which google account for meet is logged in
-BrowserCommand-
chromium|?authuser=0
-END-


# sub   |full name of subject    |url  need to stat with https:// or http://         

-startListingClass-
Nice_song|Enigma_Mother                                  |https://www.youtube.com/watch?v=GmKUx0aIM-k
start    |Greeting the class for today has not begin yet |Beauty is in eye of Beholder 
# add lines here removing this line and below
#........
Break    |Enjoy the Break time   |
-END-

# Routine
# name, day, 1st period start_time hhmm, sub, 2nd period start_time hhmm, sub, .... end_time, NULL
# example entry   teminate list with NULL
# this pattern is mandatory otherwise program will crash
# name , day  start_time, subject , start_time, subject , ....... , start_time, NULL
# end the list with NULL
#Sun|700|EM-MM   |840|Math-GDC|1020|Break |1250|Inst-LKC|1430|NULL   time_stamp n termination by NULL is mandatory
-ClassTimeTable-
Sun|0|start|700|Nice_song|1430|NULL
Mon|0   |NULL 
Tue|0   |NULL 
Wed|0   |NULL 
Thu|0   |NULL 
Fri|0   |NULL  
Sat|0   |NULL
-END-
'''

import datetime
import os
import calendar
import time
NULL = "NULL"
if (os.name=='posix'):
    clear='clear'
else:
    clear='cls'

browser=[]
subject=[]
routine=[]
flag=0

try:
    filehandle = open('Class.txt', 'r')
except (FileNotFoundError, IOError):  # pytho3 gives FileNotFoundError but 2.7 or windows give IOError
    print ('Error! Class.txt data file not found.')
    respone=input('Input "yes" to create sample class.txt file :')
    if (respone == 'yes'):
        with open('Class.txt', 'w') as fp:
            fp.write(text)
            fp.close()
    exit (1)

while True:
    # read a single line
    line= filehandle.readline()
    #print (line)
    if not line:
        break
    elif (line[0]=='#' or line[0]=='\n'):
        pass
    else:
        line_strp = line.strip()
        if (flag==0):
            if ("-BrowserCommand-" in line_strp):
                flag= 1
        elif (flag==1):
            if(line_strp.find("-END-")<0):
                browser.append(line_strp)
            else:
                flag=2
        elif (flag==2):
            if ("-startListingClass-" in line_strp):
                flag = 3
        elif (flag==3):
            if(line_strp.find("-END-")<0):
                subject.append(line_strp)
            else:
                flag=4        
        elif (flag==4):
            if ("-ClassTimeTable-" in line_strp):
                flag= 5
        elif (flag==5):
            if(line.find("-END-")<0):
                routine.append(line_strp)


print (browser)
print ("routine")
print ("+++++++++")
print (*routine, sep = '\n')
print ("++++++++++++++++++++++++++++++++++++++++++++++++++")

# close the pointer to that file
filehandle.close()

# debug line below
#for x in range(len(subj)):   # tough really tough is the python
#    print (subj[x][0])

def split_seq(seq, sep):            # function for spliting to the string to list
    start = 0                       # default functions can be used too
    while start < len(seq):
        try:
            stop = start + seq[start:].index(sep)
            yield seq[start:stop]
            start = stop + 1
        except ValueError:
            yield seq[start:]
            break

# example usage of above function
#ll = ["data","more data","","data 2","more data 2","danger","","date3","lll"]
#p = [i for i in split_seq(ll,"")]
#print (p)

#all these are 2-D Array

brw=[]              #process command string to include the authorized user
for txt in browser:
    brw.append([i for i in split_seq(txt,'|')] )
    
subj=[]
for txt in subject:
    subj.append([i for i in split_seq(txt,'|')] )
    # print(subj[1][1])          # debug line

classTime=[]
for txt in routine:
    classTime.append([i for i in split_seq(txt,'|')] )
    #print (routine)

try:
    browser_cmd=brw[0][0].strip()
    try:
        usr_id=brw[0][1].strip()
    except IndexError:
        usr_id=''    
except:
    browser_cmd=''
else:
    print(browser_cmd + ':--> user_profile:' + usr_id)
    
print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
# now the class name are accessiable in subj[x][0] and command in subj[x][1]
#and the days routine is available in days name classTime[x][0] first_period time in classTime[x][1] & subject in classTime[x][1], 2nd class starttime in classTime[x][3] subject in classTime[x][4] and so on

dt = datetime.datetime.now() #get the current date and time in dt varible datetime object time
t_offset=5                                              # offset time
dt_plus_5=dt + datetime.timedelta(minutes = t_offset)   # offset to login offset time piror

HHMM= (dt_plus_5.hour*100 + dt_plus_5.minute  )         # 5 is the amount of time in min to login piror too actual start
day_name = calendar.day_name[dt.weekday()]              # gets day_name from array in calendar object using dt.weekday

if      (day_name == 'Sunday')      :  xyz=classTime[0]  # these codes here for simplyfing the code below
elif    (day_name == 'Monday')      :  xyz=classTime[1]  # here we select the row of the routine
elif    (day_name == 'Tuesday')     :  xyz=classTime[2]  # day of the routine
elif    (day_name == 'Wednesday')   :  xyz=classTime[3]
elif    (day_name == 'Thursday')    :  xyz=classTime[4]
elif    (day_name == 'Friday')      :  xyz=classTime[5]
elif    (day_name == 'Saturday')    :  xyz=classTime[6]
else :  print ('This should never be printed')

print (day_name, dt.strftime("%Y-%m-%d %H:%M"))
print ("++++++++++++++++++++++++++")

i=1                                                     # go through the list of day in routine to see
sucess=0;                                               # for checking if the subject is found or not
while (xyz[i+1] != 'NULL'):                             # which class is currenty being active
    if ( HHMM >= int(xyz[i]) and HHMM<int(xyz[i+2])) :  # the class if from start time of this class to start time of next one
        mny=xyz[i+1].strip()            # striping white characters otherwise error on comparison below

        s_index = 0
        while s_index < len(subj):
            if ( subj[s_index][0].strip() ==  mny ):    # the subj (name of class) stripped of white characters  compared
                sucess=1;                           # subject found in list of class
                try:
                    info=subj[s_index][1].strip() 
                except:
                    print('error in "Class.txt"')  
                else:
                    print(*xyz,sep='|')
                    print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print (mny +" : "+ info + " :--> " + xyz[i] + " to " + xyz[i+2])   # info of class     
                    print ("++++++++++++++++++++++++++++++++++++++++++++++++++") 
                try : 
                    link=subj[s_index][2].strip()
                except IndexError:
                    link=''
                else: 
                    if (link[0:8] =="https://" or link[0:7] =="http://" ):  # modify it to check if the mny is url or not here
                        if (os.name=='posix'):
                            cmd= browser_cmd + " --new-window --app=" + link + usr_id + " >/dev/null 2>/dev/null &"  
                        else:
                            cmd= "start " + browser_cmd + " --new-window --app=" + link + usr_id
                       
                        print("opening link :\n" + link )
                        #print("cmd:", cmd)
                        os.system(cmd) 
                    else:
                        print(link)
                                         # opening google meet here
                    time.sleep(1)
            s_index += 1

        if (sucess != 1):
            print('Error! class', mny, 'not found in subject list')

        item=input ('\npress q to exit anykey to recheck :')
        if (item == 'q'):
            exit (0)                # exit(0) to indicate sucess
        else:
            os.system(clear)
            print('\n\nchecking again')
            dt = datetime.datetime.now() #get the current date and time in dt varible datetime object time                                             # offset time
            dt_plus_5=dt + datetime.timedelta(minutes = t_offset)
            HHMM= (dt_plus_5.hour*100 + dt_plus_5.minute  ) # keep window open if closed in time range restart again
            print ("routine")
            print ("+++++++++")
            print (*routine, sep = "\n")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
            print ('HHMM', HHMM)
            print (day_name, dt.strftime("%Y-%m-%d %H:%M"))
            print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
            print (*xyz,sep='|')
            i=1        #resetting the subject index
    else :
        #print ('looping')                              # debug line
        i+=2                                            # iterete next item to check for  more class until class data is NULL

# while terminates and falls here if there is no classes remianing
os.system(clear)
print ('No class scheduled NoW')
# displays the routing in the path file:///home/shr/Desktop/routine.jpg put absolut path after file:///
#Image.open('./routine.jpg').show()                      # open image module in python
print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("routine")
print ("+++++++++")
print (*routine, sep = "\n")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
print ('HHMM', HHMM)
print (day_name, dt.strftime("%Y-%m-%d %H:%M"))
print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
print (*xyz,sep='|')
time.sleep(10)                                          # sleep sometime so the output remain visible for set amount in second



