# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Definición recursiva de Fibonacci

def fibR(n):
    if n==0 :
        return 0
    if n==1 :
        return 1
    return fibR(n-1)+fibR(n-2)

#Definición de Fibonacci

def fib(n):
    if n==0 :
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b

#Librería

import time

#Datos base
num = 0

numFib = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
arrayFib = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
arrayFibR = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]    

for n in range (1, 44, 3):
    
    
    t0=time.clock()
    k0=fibR(n)
    tf0=time.clock()
    print ("n=",n,"fib(",n,")=",k0,"time",tf0 - t0, "seconds process time")
    arrayFibR[num] = tf0-t0
    

    t1 = time.clock()
    k1 = fib(n)
    tf1 =time.clock()
    print("n=",n,"fib(",n,")=",k1,"time",tf1 - t1, "seconds process time")
    arrayFib[num] = tf1-t1
    
    numFib [num] = n
    
    num = num + 1

#Gráfica

import pylab as pl
#%matplotlib inline

#ns = np.arange(1,5*10**60,10**50)

pl.ylabel("Segundos por procesamiento")
pl.xlabel('Número de Fibonacci')

pl.plot(numFib, arrayFib, 'bo', label='Fibonacci')
pl.plot(numFib, arrayFibR, 'ro', label='Fibonacci recursivo')
pl.legend()


#ns = np.arange(100,100,100)
#pl.ylabel("Segundos por procesamiento")
#pl.xlabel('Número de Fibonacci')
#pl.iplot(numFib ,arrayFib)

print (arrayFibR, numFib, arrayFib)







