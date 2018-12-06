# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:07:36 2018

@author: afsar
"""
import numpy as np
from math import gcd
import random
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.signal import welch
N = 17*7

while(1):
    a = random.randint(2,N-1)
    g = gcd(N,a)
    if g!=1:
        print(g,"is a non-trivial factor")
        break
    # Let's find the period of (a^(x))modN
    
    x = np.arange(1,3*N)    
    f = [(a**int(xv))%N for xv in x]
    plt.close('all')
    (F,freq,_) = plt.magnitude_spectrum(f-np.mean(f),Fs=1)
    peaks, _ = find_peaks(F, height=0)
    
#    freq,F = welch(f-np.mean(f)); peaks = []
    
    if not len(peaks):
        rr = np.abs(freq[np.argmax(F)])
    else:
        rr = np.min(freq[peaks])
    
    plt.plot(rr,F[freq==rr],'ro')
    r = int(1.0/rr)
    print("(a,r) = ",a,r)
    
    if r%2: #if r is odd
        continue
    ar = int(a**int(r/2))
    if (ar-1)%N==0:
        continue
    else:
        pq  = (gcd(ar+1,N),gcd(ar-1,N))
        if N in pq or pq==(1,1):
            continue
        print(pq)   

        plt.figure()
        plt.plot(x,f)
        plt.grid()
        break
        
            
    