import numpy as np
from branin import branin

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

def RS():

    EXPERIMENTS = 1000
    R = 0.048
    ITERATIONS = 50

    results = []
    for j in range(EXPERIMENTS):

        experiment_results = []

        x = [np.random.uniform(),np.random.uniform()]
        current_result = np.inf

        i = 0
        while i < ITERATIONS:
            while(1):
                x_new = x + R*sample_spherical(1,ndim=len(x)).T[0]
                if 0. < x_new[0] < 1. and 0. < x_new[1] < 1.:
                    break
            if branin(x_new.copy()) < current_result:
                current_result = branin(x_new.copy())
                x = x_new
            i += 1
            experiment_results.append(current_result)
        results.append(experiment_results)
    results = np.asarray(results).T
    mean_results = []
    for i in range(len(results)):
        mean_results.append(results[i].mean())
    mean_results = np.asarray(mean_results).T
    return mean_results



