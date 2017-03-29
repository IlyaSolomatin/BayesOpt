#!/home/isolomatin/anaconda2/envs/py3/bin/python3
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
from spearmint.spearmint.examples.leadingonespy.leadingones import leadingones
from spearmint.spearmint.examples.plateaupy.plateau import plateau
from logreg import logreg
from RandomSearch import RS
from Bergstra import Bergstra
from numpy.random import randint
import hyperopt
from HyperOpt import HO
import HyperOpt

optimizer = sys.argv[1]
experiment = sys.argv[2]
iterations = int(sys.argv[3])
repeats = int(sys.argv[4]) 

#Spearmint
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

#RastriginRandomSearch
if optimizer == "rs":
    if experiment == "branin":
        RS(branin,2,100,[[0,1],[0,1]],iterations,repeats)
        print("Experiments are done.")

    if experiment == "hartmann":
        RS(hartmann,3,100,[[0,1],[0,1],[0,1]],iterations,repeats)
        print("Experiments are done.")

    if experiment == "leadingones" or experiment == "logreg":
        print("This optimizer works only with continuous parameters.")

    if experiment == "plateau":
        array = []
        for i in range(10):
            array.append([-2.34, 5.12])
        RS(plateau, 10, 100, array, iterations, repeats)
        print("Experiments are done.")

#SMAC
if optimizer == "smac":
    sys.path.append('./anaconda2/envs/py3/lib/python3.6/site-packages/')
    sys.path.append('./anaconda2/envs/py3/lib/python3.6/site-packages/ConfigSpace')
    print("sys path changed.")
    print("Experiment is "+experiment)
    os.chdir("./SMAC3-master/examples/"+experiment+"/")
    print("Entered experiment directory")
    call(["rm "+experiment+"_scenario.txt"],shell=True)
    print("Removed current scenario file")
    scenario = open(experiment+"_scenario.txt",'a')
    scenario.write("algo = python "+experiment+".py\n")
    scenario.write("paramfile = "+experiment+"_pcs.pcs\n")
    scenario.write("run_obj = quality\n")
    scenario.write("runcount_limit = "+str(iterations)+"\n")
    scenario.write("deterministic = 1\n")
    scenario.write("output_dir = SMAC_output")
    scenario.close()
    print("New scenario file is submitted.")
    for i in range(repeats):
        print("Start repeating.")
        print("Repeat # "+str(i))
        seed = randint(1,100000)
        print("Seed is: "+str(seed))
        call(["python ../../scripts/smac --seed "+str(seed)+" --scenario "+experiment+"_scenario.txt > SMACout.txt 2> SMACerr.txt &"],shell=True)
        print("SMAC script called.")
        while (1):
            time.sleep(1)
            print("Checking runhistory.json...")
            if os.path.isfile("./SMAC_output/runhistory.json"):
                print("File is found")
                print("Executed run #" + str(i) + ".")
                break
            print("File not found.")
        call(["mv ./SMAC_output/runhistory.json ./SMAC_output/runhistory" + str(i) + ".json"],shell=True)
        print("Output file is renamed.")
        call(["rm ./SMAC_output/traj_aclib2.json"],shell=True)
        call(["rm ./SMAC_output/traj_old.csv"], shell=True)
        print("Other files are removed.")
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

#HyperOpt
if optimizer == "ho":
    if experiment == "branin":
        HO(branin,2,[[0,1,"cont"],[0,1,"cont"]],iterations,repeats)

    if experiment == "hartmann":
        HO(hartmann,3,[[0,1,"cont"],[0,1,"cont"],[0,1,"cont"]],iterations,repeats)

    if experiment == "leadingones":
        array = []
        for i in range(10):
            array.append([0, 1,"discr"])
        HO(leadingones, 10, array, iterations, repeats)

    if experiment == "plateau":
        array = []
        for i in range(10):
            array.append([-2.34,5.12,"cont"])
        HO(plateau, 10, array, iterations, repeats)

    if experiment == "logreg":
        HO(logreg, 4, [[0, 10, "discr"], [0, 10, "discr"], [0, 7, "discr"], [0, 9, "discr"]], iterations, repeats)

#BergstraRandomSearch
if optimizer == "brs":
    if experiment == "branin":
        Bergstra(branin,2,[[0,1,"cont"],[0,1,"cont"]],iterations,repeats)

    if experiment == "hartmann":
        Bergstra(hartmann, 3, [[0, 1,"cont"], [0, 1,"cont"], [0, 1,"cont"]], iterations, repeats)

    if experiment == "leadingones":
        array = []
        for i in range(10):
            array.append([0, 1, "discr"])
        Bergstra(leadingones, 10, array, iterations, repeats)

    if experiment == "plateau":
        array = []
        for i in range(10):
            array.append([-2.34,5.12,"cont"])
        Bergstra(plateau, 10, array, iterations, repeats)

    if experiment == "logreg":
        Bergstra(logreg, 4, [[0,10, "discr"],[0,10, "discr"],[0,7, "discr"],[0,9, "discr"]], iterations, repeats)
