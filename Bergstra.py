from numpy.random import random
from numpy import inf
from numpy.random import choice

def Bergstra(function, ndimensions, ranges, ITERATIONS, EXPERIMENTS):

    for experiment in range(EXPERIMENTS):
        best_result = inf
        for iteration in range(ITERATIONS):

            x = []
            for i in range(ndimensions):
                if ranges[i][-1] == "cont":
                    var = random()
                    var = var*(ranges[i][1]-ranges[i][0]) + ranges[i][0]
                    x.append(var)
                if ranges[i][-1] == "discr":
                    options = []
                    for j in range(len(ranges[i]) - 1):
                        options.append(ranges[i][j])
                    x.append(choice(options))

            result = function(x)

            if result < best_result:
                best_result = result

            out = open("BergstraResults.csv",'a')
            out.write(str(iteration)+","+str(best_result)+"\n")
            out.close()

