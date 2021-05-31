#file.txt
#name age
#alice 21
#ryan 30

ncol=`head -n1 file.txt | wc -w` 

for i in `seq 1 $ncol`
do
    echo `cut -d' ' -f$i file.txt`
done