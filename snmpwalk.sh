#/bin/bash
if [ "$#" -ne "1" ]
    then echo "please provide input file:\n snmp-scan.sh <input list>"
    exit 1
fi
while read line; do
  echo "Scannning $line:"
  snmpwalk -c public -v1 $line 1.3.6.1.2.1.25.4.2.1.2
done <$1
