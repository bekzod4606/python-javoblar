# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:41:13 2022

@author: bekzo
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2*np.random.randn(100,1)
y = 4+3*X+np.random.randn(100,1)
real = 4+3*X
plt.axis([0, 2, 0, 15])
plt.plot(X, y, "b.")
plt.plot(X,real, "r")
plt.show

alpha = 0.1
tolerance = 0.0001
theta_0 = np.random.random_sample()
theta_1 = np.random.random_sample()

print("Theta0: ", theta_0)
print("Theta1: ", theta_1)

def get_cost(theta_0, theta_1, X, y):
    sum = 0
    for i in range(len(X)):
        sum += (theta_0+theta_1*X[i]-y[i])**2
        return sum/len(X)
    
    def update_0(theta_0, theta_1, X, y):
        sum = 0
        for i in range(len(X)):
            sum += (theta_0+theta_1*X[i]-y[i])
            return 2*sum/len(X)

def update_1(theta_0, theta_1, X, y):
    sum = 0
    for i in range(len(X)):
        sum += (theta_0+theta_1*X[i]-y[i])*X[i]
        return 2*sum/len(X)
    
    print("Cost: ", get_cost(theta_0, theta_1, X, y))
    print("Theta0: ", update_0(theta_0, theta_1, X, y))
    print("Theta1: ", update_1(theta_0, theta_1, X, y))
    
    plt.axis([0, 2, 0, 15])
    estimated_func = theta_0+theta_1*X
    plt.plot(X, y, "b.")
    plt.plot(X, estimated_func,"g")
    plt.show()
    
    error = get_cost(theta_0, theta_1, X, y)
    while(True):
        temp_o = update_0(theta_0, theta_1, X, y)
        temp_1 = update_1(theta_0, theta_1, X, y)
        theta_0-= alpha*temp_0
        theta_1-= alpha*temp_1
        new_error = get_cost(theta_0, theta_1, X, y)
        if(abs(erorr-new_error)<tolerance):
            break
        eroor = new_error
        
        print("Theta0: ", theta_0)
        print("Theta1: ", theta_1 )
        
        plt.axis([0, 2, 0, 15])
        estimated_func = theta_0+theta_1*X
        plt.plot(X, y, "b.")
        plt.plot(X, estimated_func,"g")
        plt.show()