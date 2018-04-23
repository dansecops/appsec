#/bin/bash
#script to enumerate specific information about the SNMP protocol
#usage ./snmp-scan.sh 
if [ "$#" -ne "1" ]
    then echo "please provide input file:\n snmp-scan.sh <input list>"
    exit 1
fi
while read ip; do
  echo "Scannning IP: \t$ip:\n" >> snmp-scan-output.txt
  
  echo "Scanning Windows Users...\n" >> snmp-scan-output.txt >> snmp-scan-output.txt 
  snmpwalk -c public -v1 $ip 1.3.6.1.4.1.77.1.2.25  >> snmp-scan-output.txt 

  echo "Scanning Windows Processes...\n" >> snmp-scan-output.txt
  snmpwalk -c public -v1 $ip 1.3.6.1.2.1.25.4.2.1.2 >> snmp-scan-output.txt 
  
  echo "Scanning Open TCP ports...\n" >> snmp-scan-output.txt 
  snmpwalk -c public -v1 $ip 1.3.6.1.2.1.6.13.1.3  >> snmp-scan-output.txt 
  
  echo "Scanning Installed software...\n" >> snmp-scan-output.txt
  snmpwalk -c public -v1 $ip 1.3.6.1.2.1.25.6.3.1.2 >> snmp-scan-output.txt  

  echo "Finished Scanning \t$ip!\n" >> snmp-scan-output.txt
done <$1
