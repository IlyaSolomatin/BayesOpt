#!/usr/bin/python
#from subprocess import call
import subprocess
from subprocess import call
import sys
import time
import csv

if sys.argv[1] == "sp" and sys.argv[2] == "branin":
    for i in range(int(sys.argv[4])):
        p = subprocess.Popen('~/spearmint/spearmint/bin/spearmint --max-concurrent=8 --max-finished-jobs='+str(sys.argv[3])+' ~/spearmint/spearmint/examples/braninpy/config.pb --driver=local --method=GPEIOptChooser --method-args=noiseless=1 > stdout.txt 2> stderr.txt',shell=True)
        time.sleep(3)
        while(1):
            time.sleep(1)
            results = []
            csvFile = csv.reader(open("spearmint/spearmint/examples/braninpy/trace.csv", "rb"))
            for row in csvFile:
                results.append(row[5])
            if results[-1] == sys.argv[3]:
                print "Executed run #" + str(i) + "."
                break
        #call(["mv spearmint/spearmint/examples/braninpy/trace.csv spearmint/spearmint/examples/braninpy/trace"+str(i)+".csv"],shell=True)
        call(["./clear_but_trace.py"],shell=True)
    #for i in range(int(sys.argv[4])):
        #call(["mkdir ~/spearmint/spearmint/examples/braninpy"+str(i)],shell=True)
        #call(["cp ~/spearmint/spearmint/examples/braninpy/config.pb ~/spearmint/spearmint/examples/braninpy"+str(i)+"/config.pb"],shell=True)
        #call(["cp ~/spearmint/spearmint/examples/braninpy/branin.py ~/spearmint/spearmint/examples/braninpy"+str(i)+"/branin.py"],shell=True)

    #p = subprocess.Popen('~/spearmint/spearmint/bin/spearmint --max-finished-jobs='+str(sys.argv[3])+' ~/spearmint/spearmint/examples/braninpy/config.pb --driver=local --method=GPEIOptChooser --method-args=noiseless=1 > stdout.txt 2> stderr.txt',shell=True)
    print "Experiments are done."
