#!/usr/bin/python
import subprocess
from subprocess import call
import sys
import time
import csv
import os
import json
import os.path
from spearmint.spearmint.examples.braninpy.branin import branin
from spearmint.spearmint.examples.hartmannpy.hartmann import hartmann
from RandomSearch import RS
from numpy.random import randint

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
                print("Executed run #" + str(i) + ".")
                break
        call(["./clear_but_trace.py "+experiment],shell=True)
    print("Experiments are done.")

if optimizer == "rs":
    if experiment == "branin":
        RS(branin,2,100,[[0,1],[0,1]],iterations,repeats)
        print("Experiments are done.")

    if experiment == "hartmann":
        RS(hartmann,3,100,[[0,1],[0,1],[0,1]],iterations,repeats)
        print("Experiments are done.")

if optimizer == "SMAC":
    if experiment == "branin":
        os.chdir("./SMAC3-master/examples/branin/")
        call(["rm branin_scenario.txt"],shell=True)
        scenario = open('branin_scenario.txt','a')
        scenario.write("algo = python branin.py\n")
        scenario.write("paramfile = branin_pcs.pcs\n")
        scenario.write("run_obj = quality\n")
        scenario.write("runcount_limit = "+str(iterations)+"\n")
        scenario.write("deterministic = 1\n")
        scenario.write("output_dir = SMAC_output")
        scenario.close()
        for i in range(repeats):
            seed = randint(1,100000)
            #print(seed)
            call(["python ../../scripts/smac --seed "+str(seed)+" --scenario branin_scenario.txt > SMACout.txt 2> SMACerr.txt &"],shell=True)
            while (1):
                time.sleep(1)
                if os.path.isfile("./SMAC_output/runhistory.json"):
                    print("Executed run #" + str(i) + ".")
                    break
            call(["mv ./SMAC_output/runhistory.json ./SMAC_output/runhistory" + str(i) + ".json"],shell=True)
            call(["rm ./SMAC_output/traj_aclib2.json"],shell=True)
            call(["rm ./SMAC_output/traj_old.csv"], shell=True)
        print("Experiments are done.")
        output_file = open("SMAC_results.csv",'a')
        for j in range(repeats):
            with open('./SMAC_output/runhistory'+str(j)+'.json') as data_file:
                data = json.load(data_file)

            results = []
            for i in range(len(data["data"])):
                results.append(data["data"][i][1][0])

            best_result = results[0]
            for i in range(1, len(results)):
                if results[i] < best_result:
                    best_result = results[i]
                else:
                    results[i] = best_result
            for i in range(len(results)):
                output_file.write(str(i))
                output_file.write(",")
                output_file.write(str(results[i]))
                output_file.write("\n")
        output_file.close()

    if experiment == "hartmann":
        os.chdir("./SMAC3-master/examples/hartmann/")
        call(["rm hartmann_scenario.txt"],shell=True)
        scenario = open('hartmann_scenario.txt','a')
        scenario.write("algo = python hartmann.py\n")
        scenario.write("paramfile = hartmann_pcs.pcs\n")
        scenario.write("run_obj = quality\n")
        scenario.write("runcount_limit = "+str(iterations)+"\n")
        scenario.write("deterministic = 1\n")
        scenario.write("output_dir = SMAC_output")
        scenario.close()
        for i in range(repeats):
            seed = randint(1,100000)
            #print(seed)
            call(["python ../../scripts/smac --seed "+str(seed)+" --scenario hartmann_scenario.txt > SMACout.txt 2> SMACerr.txt &"],shell=True)
            while (1):
                time.sleep(1)
                if os.path.isfile("./SMAC_output/runhistory.json"):
                    print("Executed run #" + str(i) + ".")
                    break
            call(["mv ./SMAC_output/runhistory.json ./SMAC_output/runhistory" + str(i) + ".json"],shell=True)
            call(["rm ./SMAC_output/traj_aclib2.json"],shell=True)
            call(["rm ./SMAC_output/traj_old.csv"], shell=True)
        print("Experiments are done.")
        output_file = open("SMAC_results.csv",'a')
        for j in range(repeats):
            with open('./SMAC_output/runhistory'+str(j)+'.json') as data_file:
                data = json.load(data_file)

            results = []
            for i in range(len(data["data"])):
                results.append(data["data"][i][1][0])

            best_result = results[0]
            for i in range(1, len(results)):
                if results[i] < best_result:
                    best_result = results[i]
                else:
                    results[i] = best_result
            for i in range(len(results)):
                output_file.write(str(i))
                output_file.write(",")
                output_file.write(str(results[i]))
                output_file.write("\n")
        output_file.close()
