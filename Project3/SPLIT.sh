#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=SPLIT
#SBATCH --output=SPLIT.out         
#SBATCH --error=SPLIT.err          
#SBATCH --time=0-02:00:00       
#SBATCH --nodes=1               
#SBATCH --ntasks-per-node=1     


perl -p -e 's/>/\|\|>/g' $1 | perl -p -e 's/\n/--/g'|perl -p -e 's/\|\|/\n/g' |grep -v '^$' > new_test.pep

split -n l/10 new_test.pep 

files=`find x*`
echo $files

for name in $files
do 
  perl -p -e 's/--/\n/g' $name > $name.fa 
done
