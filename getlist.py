#!/usr/bin/env python3
import os
import sys
os.chdir(sys.path[0])

dbs=open("dbs.conf", "r").read().split()
arch=open("arch.conf", "r").read().split()[0]
url=open("url.conf", "r").read().split()[0]
total= 0
fore= open(f"./mirror/{arch}/size", "w")
for db in dbs:
    value=""
    preset=open("./preset.conf",'r').read().split()
    for i in preset:
        if i == 'db':
            value += db
        elif i == 'arch':
            value+= arch
        else:
            value+=i
    print (value)
    os.system(f"/usr/bin/w3m -dump {url}{value}/ > /tmp/dump")

    fd = open("/tmp/dump","r")
    file = open(f"./mirror/{arch}/{db}.list","w")
    counter= 0.0

    for i in fd:
        if not "pkg.tar." in i:
            continue
    
        token = i.split()
        for i in token:
            if not '.' in i or len(i) < 6:
                continue
            else:
                print (i, file=file)
        if token[-1] == "KB":
            counter += int(token[-2])
        #else:
        #    counter += int(token[-1])

    print (f"{db.upper()}\t\t %.2f MB " % (counter / 1000), file=fore)
    total += counter / 1000
    fd.close()

print (f"TOTAL\t\t %.2f MB" %(total), file=fore)
