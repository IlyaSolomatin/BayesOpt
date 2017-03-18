#!/usr/bin/python
from hyperopt import fmin, tpe, hp, STATUS_OK
import numpy as np

best_result = np.inf
experiment_result = []

def HO(function, ndimensions, ranges, ITERATIONS, EXPERIMENTS):

    global best_result
    global experiment_result

    space = {}

    for i in range(ndimensions):
        space["x"+str(i)] = hp.uniform('x'+str(i), ranges[i][0], ranges[i][1])

    def f(x):
        global best_result
        global experiment_result

        argument = []
        for i in range(len(x)):
            argument.append(x["x"+str(i)])

        result = function(argument)
        if result < best_result:
            best_result = result
        experiment_result.append(best_result.copy())
        return {'loss': result, 'status': STATUS_OK}

    result = []
    for i in range(EXPERIMENTS):
        experiment_result = []
        best_result = np.inf
        best = fmin(f, space, algo=tpe.suggest, max_evals=ITERATIONS)
        result.append(experiment_result)
        print("Executed run #" + str(i) + ".")

    out = open("HOResults.csv",'a')
    for i in range(len(result)):
        for j in range(len(result[i])):
            out.write(str(j))
            out.write(",")
            out.write(str(result[i][j]))
            out.write("\n")
    print("Experiments are done.")
    return 0
