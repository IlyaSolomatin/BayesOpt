import numpy as np

def RS(function, ndimensions, R_steps, ranges, ITERATIONS, EXPERIMENTS):

    def sample_spherical(ndim=ndimensions):
        vec = np.random.randn(ndim,1)
        vec /= np.linalg.norm(vec, axis=0)
        return vec

    widths = []
    for i in range(len(ranges)):
        widths.append(ranges[i][1]-ranges[i][0])

    max_width = max(widths)/2.

    R_list = []
    step = max_width / float(R_steps)
    for i in range(R_steps):
        R_list.append(step*(i+1))

    results_of_R = []

    for R in R_list:
        results = []
        for _ in range(EXPERIMENTS):

            experiment_results = []

            x = []
            for i in range(ndimensions):
                x.append(np.random.uniform(low=ranges[i][0],high=ranges[i][1]))

            current_result = np.inf

            i = 0
            while i < ITERATIONS:
                while(1):
                    x_new = x + R*sample_spherical().T[0]
                    is_in_ranges = 1
                    for j in range(ndimensions):
                        if x_new[j] > ranges[j][1] or x_new[j] < ranges[j][0]:
                            is_in_ranges = 0
                            break
                    if is_in_ranges == 1:
                        break

                f = function(x_new.copy())
                if f < current_result:
                    current_result = f
                    x = x_new
                i += 1
                experiment_results.append(current_result)
            results.append(experiment_results)

        results = np.asarray(results).T
        mean_results = []
        for i in range(len(results)):
            mean_results.append(results[i].mean())
        mean_results = np.asarray(mean_results).T
        results_of_R.append([mean_results[-1],R])

    results_of_R = sorted(results_of_R)
    best_R = results_of_R[0][1]
    #print "Best R: ",best_R

    results = []
    for _ in range(EXPERIMENTS):

        experiment_results = []

        x = []
        for i in range(ndimensions):
            x.append(np.random.uniform(low=ranges[i][0], high=ranges[i][1]))

        current_result = np.inf

        i = 0
        while i < ITERATIONS:
            while (1):
                x_new = x + best_R * sample_spherical().T[0]
                is_in_ranges = 1
                for j in range(ndimensions):
                    if x_new[j] > ranges[j][1] or x_new[j] < ranges[j][0]:
                        is_in_ranges = 0
                        break
                if is_in_ranges == 1:
                    break

            f = function(x_new.copy())
            if f < current_result:
                current_result = f
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



