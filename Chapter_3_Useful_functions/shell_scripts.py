#!/usr/bin/env python

import os
os.system("echo Hello from the other side!")

import subprocess

list_files_1 = subprocess.run(["ls", "-lh"])
print("The exit code was: %d" % list_files_1.returncode)

list_files_echo = subprocess.run(["echo", "hello", "world"])
print(list_files_echo.returncode)

subprocess.run(["ls", "-l"],stdout=subprocess.DEVNULL)
#command now pipes to the special /dev/null device, which means the output would not appear on our console

list_files_2 = subprocess.run(["ls", "-l"] ,stdout=subprocess.PIPE, text=True)
print(list_files_2.stdout)

with open('Chapter_3_Useful_functions/output.txt','w') as f:
    subprocess.run(["ls", "-l"] ,stdout=f, text=True)
