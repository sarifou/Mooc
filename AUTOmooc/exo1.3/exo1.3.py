from autolib import *

def f(x):
    return 4*x*(1-x)

def fi(x,i):
    if i==0 : return x
    return f(fi(x,i-1))

ax = init_figure(0,1,0,1)
X=arange(0,1,0.001)
plot(X,f(X), 'red', linewidth=1)
plot(X,X, 'green', linewidth=1)
#plot(X,fi(X,1), 'red', linewidth = 2)
#plot(X,fi(X,2), 'blue', linewidth = 2)
#plot(X,fi(X,3), 'black', linewidth = 2)
#plot(X,X, 'green', linewidth = 2)

x1=0.2
x2=0.2000001
for i in range(100):
    print(x1-x2)
    y1=f(x1)
    y2=f(x2)
    plot([x1,x1,y1],[x1,y1,y1], 'black')
    plot([x2,x2,y2],[x2,y2,y2], 'red')
    x1=y1
    x2=y2


pause(100)