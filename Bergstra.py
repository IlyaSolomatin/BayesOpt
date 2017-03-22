from numpy.random import random
from numpy import inf

from numpy import square, cos
from math import pi

def Bergstra(function, ndimensions, ranges, ITERATIONS, EXPERIMENTS):

    for experiment in range(EXPERIMENTS):
        best_result = inf
        for iteration in range(ITERATIONS):

            x = []
            for i in range(ndimensions):
                var = random()
                var = var*(ranges[i][1]-ranges[i][0]) + ranges[i][0]
                x.append(var)

            result = function(x)

            if result < best_result:
                best_result = result

            out = open("BergstraResults.csv",'a')
            out.write(str(iteration)+","+str(best_result)+"\n")
            out.close()

