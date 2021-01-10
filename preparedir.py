#!/usr/bin/env python3
import sys
import os

os.chdir(sys.path[0])
d = json.load("config.json")
dbs= d['dbs']
arch=d['arch']


for i in range(len(dbs)):
    os.popen(f"mkdir -p ./mirror/{arch}/{dbs[i]}")
