from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x-3)*(x-2)*(x-1)*(x+1)*(x+2)*(x+3)

def k(x):
    return np.exp(-0.5*x**2)

space = np.linspace(-3.1,3.1,num=100)
F = [f(x) for x in space]


known_points_x = [0.2,1.1,-1,-3.1,3.1,-2.03,2.244,-2.67,1.6,-0.32,2.67,-1.6]
known_points_y = [f(x) for x in known_points_x]
# known_points_y = [f(0.2),f(1.1),f(-1),f(-3.1),f(3.1),-2.03]
K = []
for i in range(len(known_points_x)):
    buf = []
    for j in range(len(known_points_x)):
        buf.append(k(known_points_x[i]-known_points_x[j]))
    K.append(buf)

test_space = np.linspace(-3.1,3.1,num=30)
vars = []
for point in test_space:

    target_x = point
    K_star = []
    for i in range(len(known_points_x)):
        K_star.append(k(target_x-known_points_x[i]))
    K_inv = np.linalg.inv(K)
    K_star_star = [1.]
    buf = np.dot(K_star,K_inv)
    var = K_star_star[0] - np.dot(buf,np.asarray(K_star).T)
    vars.append([var,target_x])
    y_new = np.dot(buf,known_points_y)
    plt.plot([target_x], [y_new], '.')
    plt.errorbar([target_x], [y_new],yerr=10*np.sqrt(var))

vars = sorted(vars)
print vars[-1]
plt.plot(space,F)
plt.plot(known_points_x,known_points_y,'*')
plt.show()

# def kernel(a,b):
#     sqdist = np.sum(a**2,1).reshape(-1,1) + np.sum(b**2,1) - 2*np.dot(a,b.T)
#     return np.exp(-.5*sqdist)
#
# n = 100
# X_test = np.linspace(-5,5,n).reshape(-1,1)
# K_ = kernel(X_test,X_test)
#
# L = np.linalg.cholesky(K_+1e-6*np.eye(n))
# f_prior = np.dot(L,np.random.normal(size=(n,1)))
#
# plt.plot(X_test,f_prior)
# plt.show()