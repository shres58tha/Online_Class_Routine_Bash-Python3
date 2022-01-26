#!/usr/bin/python3
"""
+March 2021 ;coded by umesh kr. shrestha BEI UMESH076BEI029@acem.edu.np on around during covid pandemic
created due to boredome and lazyness of opening the google classrooom each time checking the 
routine, opening respective teachers class and then clicking the link and opening the class.
intially implemented in bash then planned to do in c or c++ but as the code needs to be modified
implemented in python.
+2021 May 05;This program is  generalized and external data file have been added improvement made. 
same code and data works for 'posix' and 'nt'. option to generate the sample class.txt file added
code revised and improvment done as well as unnecessary debug line removed, jpg routine display removed
++tweaked for removal of app mode in the chrome... jan 26 2022
"""
    
#sample class.txt
text='''
# anything starting with # is a comment
# data base for the Class.txt
# | seperates the list 
#-END-  label control the start and end of data

#browser chromium / google-chrome
#this command gets excuted so be careful
#name_browser | options|?authuser=1  +> is the profile in which google account for meet is logged in

-BrowserCommand-
google-chrome|--new-window --kiosk --app=|?authuser=1
#example #google-chrome|--new-window --kiosk --app=|?authuser=1
-END-

# modify here to add or remove or update subjects
# sub   |full name of subject    |url  need to stat with https:// or http://         

-startListingClass-
Nice_song|Enigma_Mother                                  |https://www.youtube.com/watch?v=GmKUx0aIM-k
start    |Greeting the class for today has not begin yet |Beauty is in eye of Beholder 
# add lines here removing this line and below. DO NOT REME LINE WITH -END-
#........
Break    |Enjoy the Break time   |
-END-

# Routine
# name, day, is in specified order do not alter
# this pattern is mandatory otherwise program will crash
# name , day  start_time, subject , start_time, subject , ....... , start_time, NULL
# end the list with NULL
#Sun|700|EM    |840|Math |1020|Break |1250|Inst |1430|NULL   time_stamp n termination by NULL is mandatory
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

####################### defination ? functions #####################
NULL = "NULL"

if (os.name=='posix'):
    clear='clear'
else:
    clear='cls'
    
##################### timed input ##################################    
import sys, select

def timeout_input(prompt, timeout=3, default=""):
    print(prompt, end=': ', flush=True)
    ins, outs, errs = select.select([sys.stdin], [], [], timeout)
    print()
    return (0, sys.stdin.readline().strip()) if ins else (-1, default)
#inputs, outputs=timeout_input("Continue? (Y/n)", 3, "y")
#print(inputs, outputs)

#######################data spliter ################################
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

def string_to_list(seq, ch):
    lst=[]    
    for txt in seq:
        lst.append([i for i in split_seq(txt,ch)] )
    return lst

######################### display_info #############################
def display_info():
    os.system(clear)
    print ("routine")
    print ("+++++++++")
    print (*routine, sep = "\n")
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print (day_name, dt.strftime("%Y-%m-%d %H:%M"))
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
    
######################## time and day ##############################    
def current_time( t_offset ):                                                  # OFFSET TIME IN MINUTES +ve early  - late
    dt = datetime.datetime.now() #get the current date and time in dt varible datetime object time
    dt_plus_offset=dt + datetime.timedelta(minutes = t_offset)   # offset to login offset time piror
    HHMM= (dt_plus_offset.hour*100 + dt_plus_offset.minute  )         # 5 is the amount of time in min to login piror too actual start
    day_name = calendar.day_name[dt.weekday()]                                  # gets day_name from array in calendar object using dt.weekday
    return HHMM, day_name, dt                   #returns tuple

############################ data handling #########################
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
    exit (0)

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

# close the pointer to that file
filehandle.close()

##################### initialization of variables ##########################
brw=string_to_list(browser,'|')
subj=string_to_list(subject,'|')
classTime=string_to_list(routine,'|') 

try:
    browser_cmd=brw[0][0].strip()
    try:
        opts=brw[0][1].strip()
    except IndexError:
        opts=''
    try:
        usr_id=brw[0][2].strip()
    except IndexError:
        usr_id=''    
except:
    browser_cmd=''
else:
    print(browser_cmd + '|cmd options for browser_cmd' + '| :--> user_profile:' + usr_id)

######################## data handling complete ############################

# now the class name are accessiable in subj[x][0] and command in subj[x][1]
#and the days routine is available in days name classTime[x][0] first_period time in classTime[x][1] & subject in classTime[x][1], 2nd class starttime in classTime[x][3] subject in classTime[x][4] and so on

#super loop 
########################### class identification logics #############################
while True:  # put this big while loop in the try block to just catch the index error in class.txt funny
    HHMM, day_name, dt = current_time ( 0 ) #0 offset_time       
    
    if      (day_name == 'Sunday')      :  xyz=classTime[0]  # these codes here for simplyfing the code below
    elif    (day_name == 'Monday')      :  xyz=classTime[1]  # here we select the row of the routine
    elif    (day_name == 'Tuesday')     :  xyz=classTime[2]  # day of the routine
    elif    (day_name == 'Wednesday')   :  xyz=classTime[3]
    elif    (day_name == 'Thursday')    :  xyz=classTime[4]
    elif    (day_name == 'Friday')      :  xyz=classTime[5]
    elif    (day_name == 'Saturday')    :  xyz=classTime[6]
    else :  print ('This should never be printed')
   
    i=1                                                     # go through the list of day in routine to see
    sucess=0; 
    while (xyz[i+1] != 'NULL'):
        #print (xyz[i] , HHMM , day_name, dt )   #debug line
        display_info()
        HHMM, day_name1, dt = current_time ( 0 )
        if (day_name != day_name1):
            break   # miss you goto  python is really silly need a huge try block for nothing if needed to implement it or loginc flow change
            
        if ( HHMM >= int(xyz[i]) and HHMM<int(xyz[i+2])) :  # the class if from start time of this class to start time of next one
            mny=xyz[i+1].strip()                            # striping white characters otherwise error on comparison below
            s_index = 0
            while s_index < len(subj):
                if ( subj[s_index][0].strip() ==  mny ):    # the subj (name of class) stripped of white characters  compared
                    sucess=1;                           # subject found in list of class
                    try:
                        info=subj[s_index][1].strip() 
                    except:
                        print('error in "Class.txt" in subject lines')  
                    else:
                        print(*xyz,sep='|')
                        print ("++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print (mny +" : "+ info + " :--> " + xyz[i] + " to " + xyz[i+2])   # info of class     
                        print ("++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    try : 
                        link=subj[s_index][2].strip() # this try is needed absolutely and is not for error but for the default value
                    except IndexError:
                        link=''
                    else: 
                        if (link[0:8] =="https://" or link[0:7] =="http://" ):  # modify it to check if the mny is url or not here
                            if (os.name=='posix'):
                                cmd= browser_cmd +" "+ opts +" "+ link + usr_id + " >/dev/null 2>/dev/null &"  
                            else:
                                cmd= "start " + browser_cmd +" "+ opts +" "+ link + usr_id
                            print("opening link :\n" + link )
                            #print("cmd:", cmd)
                            os.system(cmd) # opening google meet here
                        else:
                            print(link)
                s_index += 1

            if (sucess != 1):
                print('Error! class', mny, 'not found in subject list')
            item=input ('\npress q to exit anykey to recheck :')
            if (item == 'q'):
                exit (0)                # exit(0) to indicate sucess
            else:
                i=1        #resetting the subject index
        else :
           i+=2                                            # iterete next item to check for  more class until class data is NULL
    
    print(day_name ,'=', day_name1)
    if (day_name == day_name1):
        break
                                                        
# while terminates and falls here if there is no classes remianing

##########################################################################################
display_info()
print (*xyz,sep='|')   #this is a risky line and count onwhile loop being operated once
ins, outs=timeout_input("\nWait? (y/n)",3, "n")
if outs == "n":
    exit(0)
if outs == "y":
    item=input ('press any to exit :')
    exit(0)
    

    

