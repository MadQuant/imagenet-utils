#!/bin/bash
 
#for i in `ls $1` 
a=0
for fs in n*
do
	if [[ $a -eq $2 ]]; then
		echo "Exit..."
		exit
	fi
#	echo `file $fs`
	JPGCHECK=`file $fs | grep "JFIF" | wc -l`

	#echo $test
	#echo $JPGCHECK

if [ "$JPGCHECK" -gt 0 ]; then
	mv $fs ../goodimages/$1/$fs
#	echo "Won't move $JPGCHECK"
else
	mv $fs ../badimages/$fs
#	echo "Will move $JPGCHECK"
#deletecount=$((deletecount+1))
#echo $i "to be deleted, $JPGCHECK"

#rm $1/$i

#else
#echo $i "is fine , $JPGCHECK"
fi
#Totalcount=$((Totalcount+1))

((a++))

done

