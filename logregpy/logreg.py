import subprocess
import os

import numpy as np
import sys
import math

from logreg_on_grid import *

def main(job_id, params):
  print('Anything printed here will end up in the output directory for job #:', str(job_id))
  print(params)
  return logreg_on_grid(params['lrate'],params['l2_reg'],params['batchsize'],params['n_epochs'],ret_type='validation')


