import csv
from matplotlib import pyplot as plt
import numpy as np
from RandomSearch import RS

results = []
csvFile = csv.reader(open("trace.csv", "rb"))
for row in csvFile:
    results.append(row[1])
results = map(float, results)
for i in range(len(results)-1,-1,-1):
    if np.isnan(results[i]):
        del results[i]
results = np.asarray(results)
results = np.reshape(results, (100, 50)).T
mean_results = []
for i in range(len(results)):
    mean_results.append(results[i].mean())
mean_results = np.asarray(mean_results).T
mean_results_RS = RS()

plt.plot(range(50),mean_results[:50],'.r',label="Spearmint")
plt.plot(range(50),mean_results_RS,'.b',label="Random Search")
plt.legend(loc=0)
plt.ylabel("y")
plt.xlabel("# of iterations")
plt.savefig('foo2.pdf')
plt.show()
