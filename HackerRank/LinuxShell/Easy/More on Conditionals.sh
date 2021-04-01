read a
read b
read c 
cnt=0
if [[ $a == $b ]]
then
((cnt +=1 ))
fi
if [[ $c == $b ]]
then
((cnt +=1 ))
fi
if [[ $a == $c ]]
then
((cnt +=1 ))
fi
if [ $cnt -eq 0  ]
then
echo "SCALENE"
elif [ $cnt -eq 1 ]
then
echo "ISOSCELES"
else
echo "EQUILATERAL"
fi
