#!/bin/bash

for i in $( seq 1 10 )
do
    printf "%04d\t" "$i"
done
echo

for i in $( seq 1 10 )
do
    printf "%x\t" "$i"
done
echo

for i in $( seq 1 10 )
do
    printf "%X\t" "$i"
done
echo

for i in $( seq 10 15 )
do
    printf "%04d\t is %X\t in HEX.\n" "$i" "$i"
done

for i in $( seq 5 10 )
do
    printf "%.10s is %X in HEX.\n" "$i............." "$i"
done