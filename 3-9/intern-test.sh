#!/bin/bash


STRING= "start"
echo $STRING

cd /Users/brownscholar/desktop/BridgeUp_Internship/InternGit/ocean-motion-2021/2-25

#compiling files
gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegeinv.f

datelist= '/Users/brownscholar/desktop/BridgeUp_Internship/InternGit/ocean-motion-2021/3-23/date_list-t5.txt'

while read p; do
	echo $p
	#creating exec files with all dates
	python write_exec_files.py $p 
	./vectorq.exec
	./omegainv.exec
done </Users/brownscholar/desktop/BridgeUp_Internship/InternGit/ocean-motion-2021/3-23/date_list-t5.txt

STRING="DONE"
echo $STRING


