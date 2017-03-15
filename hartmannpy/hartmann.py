import numpy as np
import sys
import math
import time
import sys

#sys.path.insert(0, '/home/isolomatin/ampgo/ampgo')

#from go_benchmark import Hartmann3

def hartmann(x):
    a = np.asarray([[3.0,  0.1,  3.0,  0.1],
                     [10.0, 10.0, 10.0, 10.0],
                     [30.0, 35.0, 30.0, 35.0]])
    p = np.asarray([[0.36890, 0.46990, 0.10910, 0.03815],
                     [0.11700, 0.43870, 0.87320, 0.57430],
                     [0.26730, 0.74700, 0.55470, 0.88280]])

    c = np.asarray([1.0, 1.2, 3.0, 3.2])

    d = np.zeros_like(c)

    for i in range(4):
        d[i] = np.sum(a[:, i]*(x - p[:, i])**2)

    return -np.sum(c*np.exp(-d))

#def hartmann(x):
#  bench = Hartmann3()
#  return bench.evaluator(x)

def main(job_id, params):
  print 'Anything printed here will end up in the output directory for job #:', str(job_id)
  print params
  return hartmann(params['X'])
