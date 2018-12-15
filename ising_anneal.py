# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:53:12 2018
Simple demo of how adiabatic quantum programming models are made
Using the ising problem to implement gates
Run the code multiple times to see the effect
For more details: read "The Ising model : teaching an old problem new tricks"
@author: afsar
"""
import numpy as np
def ising(q):
    q = 2*(q>0)-1
    H = np.dot(q,w)
    #q = np.atleast_2d(q)
    H+=np.dot(q,np.dot(v,q))
    return H

from scipy import optimize

# implementation of the and gate as in "The Ising model : teaching an old problem new tricks"
w = np.array([-1,-1,2]) 
v = np.array([[0,1,-2],[1,0,-2],[-2,-2,0]])/2.0
# implementation of the OR gate as in "The Ising model : teaching an old problem new tricks"
w = np.array([1,1,-2]) 
v = np.array([[0,1,-2],[1,0,-2],[-2,-2,0]])/2.0
x0 = np.array(2*np.random.rand(len(w))-1) #starting point
res = optimize.basinhopping(ising, x0)
print("Initial optimization score:",ising(x0))
print("Final solution:",2*(res.x>0)-1)
print("Final Score:",res.fun)