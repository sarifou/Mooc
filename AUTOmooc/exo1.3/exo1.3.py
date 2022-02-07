from autolib import *

def f(x):
    return 4*x*(1-x)

def fi(x,i):
    if i==0 : return x
    return f(fi(x,i-1))

ax = init_figure(0,1,0,1)
X=arange(0,1,0.001)
plot(X,fi(X,1), 'red', linewidth = 2)
plot(X,fi(X,2), 'blue', linewidth = 2)
plot(X,fi(X,3), 'black', linewidth = 2)
plot(X,X, 'green', linewidth = 2)


pause(100)