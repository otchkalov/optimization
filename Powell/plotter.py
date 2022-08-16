'''
    Plot contour graph for two-dim function
'''
from tkinter import W
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

#Plot the objective function
def plot_graph(x1, x2, objFun, path):
    clear_output(wait=True)

    fig,ax=plt.subplots(1,1)
    # cp = ax.contour(x1, x2, objFun)
    # Levels for quadratic function
    cp = ax.contour(x1, x2, objFun, [-1.95, -1.8, -1.2, 1.0, 8, 16, 24, 32, 40, 48, 56])
    fig.colorbar(cp) # Add a colorbar to a plot
    ax.set_title('Object Function Contour Plot')
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    for i in range(len(path)-1):
        xp, yp = [path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]]
        plt.plot(xp, yp, marker = '.')
    plt.show()
    

# Plot a vector field of object function gradient 
def vector_plot(x1,x2, ObjFun, gradOf):
    # clear_output(wait=True)

    fig,ax=plt.subplots(1,1)
    cp = ax.contour(x1, x2, ObjFun)
    fig.colorbar(cp) # Add a colorbar to a plot
    plt.quiver( x1, x2, gradOf[0], gradOf[1])
    ax.set_title('Object Function Antigradient')
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    plt.show()
    