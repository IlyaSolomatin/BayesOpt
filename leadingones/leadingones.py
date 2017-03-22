import sys
import numpy as np

def main():
    seed = sys.argv[5]
    inputs = []
    for i in range(0,32,2):
        inputs.append(float(sys.argv[7+i]))
    tmp = leading_ones(inputs)
    print('Result for SMAC: SUCCESS, -1, -1, %f, %s' % (tmp, seed))

def leading_ones(x):

    count = 0
    for i in x:
        if i != 1:
            break
        else:
            count += 1

    return -count

if __name__ == '__main__':
    main()
