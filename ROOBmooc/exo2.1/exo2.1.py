from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
import numpy as np

def draw_crank(x): 
    global y
    θ1=x[0,0]
    θ2=x[1,0]
    z=L1*np.array([[cos(θ1)],[sin(θ1)]])
    y=z+L2*np.array([[cos(θ1+θ2)],[sin(θ1+θ2)]])
    plot( [0,z[0,0],y[0,0]],[0,z[1,0],y[1,0]],'magenta', linewidth = 2)   
    draw_disk(ax,c,r,"cyan")


L1,L2 = 4,3
c = np.array([[1],[2]])
r=4
dt = 0.05

x = np.array([[-1],[1]])


def f(t,x):
    θ1=x[0,0]
    θ2=x[1,0]
    w=c+r*np.array([[np.cos(t)], [np.sin(t)]])
    dw = r*np.array([[-np.sin(t)],[np.cos(t)]])
    v= (w-y)+dw
    A = np.array([[-y[1,0], -L2*np.sin(θ1+θ2)],[y[0,0], L2*np.cos(θ1+θ2)]])
    u = np.linalg.inv(A).dot(v)
    return u

ax=init_figure(-4,8,-4,8)

for t in arange(0,30,dt) :
    clear(ax)
    draw_crank(x)
    x = x + dt*f(t,x)  