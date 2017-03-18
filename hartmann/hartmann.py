import sys
import numpy as np

def main():
    seed = sys.argv[5]
    x = float(sys.argv[7])
    y = float(sys.argv[9])
    z = float(sys.argv[11])
    tmp = hartmann([x, y, z])
    print('Result for SMAC: SUCCESS, -1, -1, %f, %s' % (tmp, seed))

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

if __name__ == '__main__':
    main()
