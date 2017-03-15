#!/usr/bin/python
from subprocess import call
import sys

folder = sys.argv[1]

call(['rm ~/spearmint/spearmint/examples/'+folder+'py/'+folder+'.pyc'],shell=True)
call(['rm ~/spearmint/spearmint/examples/'+folder+'py/best_job_and_result.txt'],shell=True)
call(['rm ~/spearmint/spearmint/examples/'+folder+'py/chooser.GPEIOptChooser.pkl'],shell=True)
call(['rm ~/spearmint/spearmint/examples/'+folder+'py/chooser.GPEIOptChooser_hyperparameters.txt'],shell=True)
call(['rm ~/spearmint/spearmint/examples/'+folder+'py/expt-grid.pkl'],shell=True)
#call(['rm ~/spearmint/spearmint/examples/braninpy/expt-grid.pkl.lock'],shell=True)
#call(['rm ~/spearmint/spearmint/examples/braninpy/trace.csv'],shell=True)
call(['rm -rf ~/spearmint/spearmint/examples/'+folder+'py/output'],shell=True)
call(['rm -rf ~/spearmint/spearmint/examples/'+folder+'py/jobs'],shell=True)

