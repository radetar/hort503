#!/bin/bash
blah=$(cat SRA_IDs.txt)
for item in $blah 
do
if [ -d $item ]
then
echo Directory already exists 	
else
    mkdir $item
fi 
done
