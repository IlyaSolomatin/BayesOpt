#!/usr/bin/python
import subprocess
from subprocess import call
import sys
import time
import csv
from spearmint.spearmint.examples.braninpy.branin import branin
from spearmint.spearmint.examples.hartmannpy.hartmann import hartmann
from RandomSearch import RS


optimizer = sys.argv[1]
experiment = sys.argv[2]
iterations = int(sys.argv[3])
repeats = int(sys.argv[4]) 

if optimizer == "sp":
    for i in range(repeats):
        p = subprocess.Popen('~/spearmint/spearmint/bin/spearmint --max-concurrent=8 --max-finished-jobs='+str(iterations)+' ~/spearmint/spearmint/examples/'+experiment+'py/config.pb --driver=local --method=GPEIOptChooser --method-args=noiseless=1 > stdout.txt 2> stderr.txt',shell=True)
        time.sleep(3)
        while(1):
            time.sleep(1)
            results = []
            csvFile = csv.reader(open("spearmint/spearmint/examples/"+experiment+"py/trace.csv", "rb"))
            for row in csvFile:
                results.append(row[5])
            if results[-1] == str(iterations):
                print "Executed run #" + str(i) + "."
                break
        call(["./clear_but_trace.py "+experiment],shell=True)
    print "Experiments are done."

if optimizer == "rs":
    if experiment == "branin":
        results = RS(branin,2,100,[[0,1],[0,1]],iterations,repeats)
        f = open("/home/isolomatin/spearmint/spearmint/examples/braninpy/RSresults.txt",'w')
        for i in range(len(results)):
            f.write(str(results[i])+"\n")
        f.close()
        print "Experiments are done."

    if experiment == "hartmann":
        results = RS(hartmann,3,100,[[0,1],[0,1],[0,1]],iterations,repeats)
        f = open("/home/isolomatin/spearmint/spearmint/examples/"+experiment+"py/RSresults.txt",'w')
        for i in range(len(results)):
            f.write(str(results[i])+"\n")
        f.close()
        print "Experiments are done."


                           

