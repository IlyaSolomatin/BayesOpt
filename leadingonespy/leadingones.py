import numpy as np
import sys
import math
import time

def leadingones(x):

    count = 0
    for i in x:
        if i != 1:
            break
        else:
            count += 1

    return -count

# Write a function like this called 'main'
def main(job_id, params):
  print 'Anything printed here will end up in the output directory for job #:', str(job_id)
  print params
  return leadingones(params['X'])
