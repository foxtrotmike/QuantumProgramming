# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:40:00 2018
A simple classical solution of Simon's Problem
The objective of the Simon's problem is to find the period (under xor) a of a
2 to 1 function f(x) which satisfies f(x)=f(x xor a).
@author: afsar
"""
class memoryFunction:
    """
    Forces a one-on-one function g(x) defined to a 2-to-1 function f(x) over n bits such
    that f(x)=f(x xor a). Requires O(2^n) storage.
    """
    def __init__(self,g,n=10,a=100,enforcen=False):
        """
        g: a function
        n: number of bits
        a: a
        enforcen: Boolean, forces the output of g(x) to g(x) mod N
        """
        self.n = n
        self.a = a
        self.d = {}
        self.MAX = 2**n
        self.func = g
        self.enforcen = enforcen
    def f(self,x):
        try: #return if f(x) is available
            v = self.d[x]
        except KeyError: # else get g(x) and save it as f(x) and f(x xor a)
            v = self.func(x)
            if self.enforcen:
                v = v%self.MAX
            self.d[x] = v
            self.d[x^a] = v
        return v

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    import collections
    n = 12
    a = np.random.randint(2**n-1)
    # Let's make a function
    def g(x):
        return x
    # Let's convert it to a 2-to-1 function with a randomly picked a
    f = memoryFunction(g = g, n=n,a=a)
    X = range(2**n)
    Y = [f.f(x) for x in X]
    plt.scatter(X,Y)
    plt.grid()
    assert(set(collections.Counter(Y).values())=={2}) #verify that the function is indeed 2 to 1    
    #Using a conventional O(2^n) algo for determining "a"
    for j in range(1,len(X)):            
        if f.f(X[0])==f.f(X[j]):
            a0 = X[0]^X[j]
            print("The value of a found through linear search is:",a0)
            break
    
    print("The true value of a is:",a)