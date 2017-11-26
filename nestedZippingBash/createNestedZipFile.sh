#!/bin/bash
filename=$1
zip_count=$2

if [ $# -ne 2  ]; then
  echo "Invalid arguments. Please use these parameters: [Filename] [Zip Count]"
  exit 1
fi 

if [ ! -f $filename ]; then
  echo "File $filename does not exist, so we create it."
  touch $filename
  echo "secret" >> $filename
fi

i=$zip_count
z=$((zip_count+1))
while [ "$i" -gt 0 ]; do
	echo "$i""th time"
	zip "$i" "$filename"
	filename="$i.zip"
	i=$((i-1))
	if [ $z -ne 1 ] && [ $z -ne $((zip_count+1)) ]; then
		rm $z.zip
	fi
	z=$((z-1))
done

rm -f $1
