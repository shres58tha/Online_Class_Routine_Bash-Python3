#!/bin/sh
echo $(date  )
DOW=$(date +"%-u") 
#1 = mon; 2=tue ....7=Sun
# echo $DOW
HH=$(date +"%-H")
#echo $HH
MM=$(date +"%-M")
#echo $MM
# debug line
DOW=7
#HH=8
#MM=30 

NN=$(($HH*100 + $MM))   # learned spaces cause error in bash
NN=700
#echo $NN

case "$DOW" in

7)  echo "sunday" $NN
            if  (( "$NN" > "655"))&&(("$NN" < "835" ))  ; then
            echo  7:00  OOP class by Ranjan Shrestha
            chromium --app=<class url> 2>null &
            elif (( $NN > 835 && $NN < 1020 )) ; then
            echo  8:40  Chem by S Subedi
            chromium --app=<class url> 2>null &
            else
            echo "Class Finished"
            fi

    ;;
    
1)  echo  "monday" $NN
            if (( $NN > 655 && $NN < 835 )); then
            echo  7:00  microprocessor by Laxmi KC
            chromium --app=<class url> 2>null &
            elif (( $NN > 835 && $NN < 1020 )) ; then
            echo  8:40  math by Narayan Prasad Adhakari
            chromium --app=<class url> 2>null &
            else
            echo "Class Finished"
            fi
    ;;
    
2)  echo  "tuesday" $NN
            if (( $NN > 655 && $NN < 835 )); then
            echo  7:00  math by Rajendra Paudel
            chromium --app=<class url> 2>null &
            elif (( $NN > 835 && $NN < 1020 )) ; then
            echo  8:40  electric by Babita singh
            chromium --app=<class url> 2>null &
            else
            echo "Class Finished"
            fi
    ;;
    
    
3) echo  "wednesday" $NN
            if (( $NN > 655 && $NN < 835 )); then
            echo  7:00  microprocessor by Laxmi KC
            chromium --app=<class url> 2>null &
            elif (( $NN > 835 && $NN < 1020 )) ; then
            echo  8:40  Chem by S Subedi
            chromium --app=<class url> 2>null &
            else
            echo "Class Finished"
            fi
    ;;
    
4) echo  "thursday" $NN
            if (( $NN > 655 && $NN < 745 ))  &&  (( $MM < 35 )) ; then
            echo  7:00  OOP class by Ranjan Shrestha
            chromium --app=<class url> 2>null &
            elif (( $NN > 750 && $NN < 930 )) ; then
            echo  7:50  electric by Babita singh
            chromium --app=<class url> 2>null &
            else
            echo "Class Finished"
            fi
    ;;

5) echo  "friday" $HH   "hour and" $MM "min"
            if (( $NN > 655 && $NN < 745 ))  &&  (( $MM < 35 )) ; then
            echo  7:00  Workshop by Sanjeev Kumar
            chromium --app=<class url> 2>null &
            elif (( $NN > 750 && $NN < 930 )) ; then
            echo  7:50   math by Narayan Prasad Adhakari
            chromium --app=<class url> 2>null &
            else
            echo "Class Finished"
            fi
    ;;

6) echo  "saturday" $HH   "hour and" $MM "min"
            echo  NO CLASS
                    
    ;;

*) echo "NO CLASS right now or ERROR IN SCRIPT"
            exec gwenview ~/Desktop/routine.jpg  2>null &
      ;;      
esac
