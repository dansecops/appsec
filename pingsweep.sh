#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Illegal number of parameters"
fi
IPADDR=$1
START=$2
END=$3

IPREGEX='\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b'
if [[ ! "$IPADDR" =~ $IPREGEX ]]
then
	echo "IP is incorrect"
	exit 1
fi
if [[ "$END" -lt 2 || "$END" -gt 255 ]];
then
	echo "End IP is incorrect"
	exit 1
fi
if [[ "$START" -lt 0 || "$START" -gt 255 ]];
then
	echo "Start IP is incorrect"
	exit 1
fi
if [[ "$START" -gt "$END" ]];
then    
	echo "Incorrect range"
	exit 1
fi
for i in `seq $START $END`;
do	
	#IP_FIRSTPART=$(echo $IPADDR | sed 's!/.*!!; s!.*\.!!')
	IP_WO_LAST_OCTET=$(echo $IPADDR | sed 's/\.[0-9]*$/./')
	NEWIP="$IP_WO_LAST_OCTET$i"
		ping -c 1 $NEWIP | tr \\n ' ' | awk '/1 received/ {print $2}' ;
done
