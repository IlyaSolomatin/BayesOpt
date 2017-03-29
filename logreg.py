import sys
import numpy as np

from logreg_on_grid import *

def main():
    seed = sys.argv[5]
    tmp = logreg_on_grid(int(sys.argv[7]),int(sys.argv[9]),int(sys.argv[11]),int(sys.argv[13]),ret_type='validation')
    print('Result for SMAC: SUCCESS, -1, -1, %f, %s' % (tmp, seed))

if __name__ == '__main__':
    main()
