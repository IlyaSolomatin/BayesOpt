import sys
import numpy as np

def main():
    seed = sys.argv[5]
    inputs = []
    for i in range(0,20,2):
        inputs.append(float(sys.argv[7+i]))
    tmp = plateau(inputs)
    print('Result for SMAC: SUCCESS, -1, -1, %f, %s' % (tmp, seed))

def plateau(x):
    return 30. + np.sum(np.floor(np.abs(x)))

if __name__ == '__main__':
    main()
