from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
import numpy as np

def f(x,u):
    xr,yr,θr,vr=x.flatten()
    u1,u2=u.flatten()
    return (np.array([[vr*np.cos(θr)],[vr*np.sin(θr)],[u1],[u2]]))


def control(x,w,dw):
    xr,yr,θr,vr=x.flatten()
    A = np.array([[-vr*np.sin(θr), np.cos(θr)],[vr*np.cos(θr), np.sin(θr)]])
    y = np.array([[xr], [yr]])
    dy = np.array([[vr*np.cos(θr)],[vr*np.sin(θr)]])
    v = (w-y)+2*(dw-dy)
    u = np.linalg.inv(A).dot(v)
    return u


ax=init_figure(-30,30,-30,30)

dt = 0.1
x_a = np.array([[10],[0],[pi/3],[1]])
x_b = np.array([[0],[0],[pi/3],[2]])
x_c = np.array([[-10],[0],[pi/3],[3]])
Lx = 15
Ly = 7
l = 6

for t in arange(0,60,dt) :
    clear(ax)
    # Consigne et commande robot A
    w_a = np.array([[Lx*np.sin(0.1*t)],[Ly*np.cos(0.1*t)]])
    dw_a= np.array([[Lx*0.1*np.cos(0.1*t)], [-Ly*0.1*np.sin(0.1*t)]])
    u_a = control(x_a,w_a,dw_a)
    # Consigne et commande robot B
    w_b = np.array([[x_a[0,0]-l*np.cos(x_a[2,0])], [x_a[1,0]-l*np.sin(x_a[2,0])]])
    dw_b = np.array([[x_a[3,0]*np.cos(x_a[2,0])+l*u_a[0,0]*np.sin(x_a[2,0])], [x_a[3,0]*np.sin(x_a[2,0])-l*u_a[0,0]*np.cos(x_a[2,0])]])
    u_b = control(x_b,w_b,dw_b)
    # Consigne et commande robot C
    w_c = np.array([[x_b[0,0]-l*np.cos(x_b[2,0])], [x_b[1,0]-l*np.sin(x_b[2,0])]])
    dw_c = np.array([[x_b[3,0]*np.cos(x_b[2,0])+l*u_b[0,0]*np.sin(x_b[2,0])], [x_b[3,0]*np.sin(x_b[2,0])-l*u_b[0,0]*np.cos(x_b[2,0])]])
    u_c = control(x_c,w_c,dw_c)
    # Dessin des trois robots
    draw_tank(x_a) 
    draw_tank(x_b, col="red")
    draw_tank(x_c, col="black")
    # Mis a jour des vecteurs d'etats 
    x_a = x_a+dt*f(x_a,u_a)	
    x_b = x_b+dt*f(x_b,u_b)
    x_c = x_c+dt*f(x_c,u_c)
    
pause(1)