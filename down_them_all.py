#!/usr/bin/env python3
import sys
import os
import time
os.chdir (sys.path[0])
os.popen(f"echo '{os.getpid()}' >> PID")

dbs = open("./dbs.conf", "r").read().split()
arch= open("./arch.conf", "r").read().split()[0]
url = open("./url.conf", "r").read().split()[0]
preset=open("./preset.conf",'r').read().split()

for db in dbs:
    fd = open(f"./mirror/{arch}/{db}.list", "r")
    df = open(f"./mirror/{arch}/{db}/{db}.fetch", "w")
    for o in fd:
        value=""
        for i in preset:
            if i == 'db':
                value += db
            elif i == 'arch':
                value+= arch
            else:
                value+=i
        print (f"{url}{value}/{o}", file=df)

for db in dbs:
    #os.popen(f"cp ./mirror/{arch}/{i}.list ./mirror/{arch}/{i}/{i}.fetch")
    time.sleep (1)
    # start the Download :)
    
    
#    os.popen(f"aria2c -x 4 -j 4 -k 1M --auto-file-renaming=false -l ./aria2c.log  -i ./mirror/{arch}/{db}/{db}.fetch -d ./mirror/{arch}/{db}/").read()
    


