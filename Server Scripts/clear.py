#!/usr/bin/python
from subprocess import call

call(['rm ~/spearmint/spearmint/examples/braninpy/branin.pyc'],shell=True)
call(['rm ~/spearmint/spearmint/examples/braninpy/best_job_and_result.txt'],shell=True)
call(['rm ~/spearmint/spearmint/examples/braninpy/chooser.GPEIOptChooser.pkl'],shell=True)
call(['rm ~/spearmint/spearmint/examples/braninpy/chooser.GPEIOptChooser_hyperparameters.txt'],shell=True)
call(['rm ~/spearmint/spearmint/examples/braninpy/expt-grid.pkl'],shell=True)
#call(['rm ~/spearmint/spearmint/examples/braninpy/expt-grid.pkl.lock'],shell=True)
call(['rm ~/spearmint/spearmint/examples/braninpy/trace.csv'],shell=True)
call(['rm -rf ~/spearmint/spearmint/examples/braninpy/output'],shell=True)
call(['rm -rf ~/spearmint/spearmint/examples/braninpy/jobs'],shell=True)

