import numpy as np
import sys
import math
import time
import sys

def plateau(x):
    return 30. + np.sum(np.floor(np.abs(x)))


def main(job_id, params):
  print('Anything printed here will end up in the output directory for job #:', str(job_id))
  print(params)
  return plateau(params['X'])
