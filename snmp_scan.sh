#/bin/bash
echo public > community
echo private >> community
echo manager >> community
for ip in $(seq 0 254); do echo 10.11.1.$ip;done > snmp_inputlist.txt
onesixtyone -c community -i snmp_inputlist.txt
