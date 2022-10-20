'''
    Plot contour graph for two-dim function
'''
from tkinter import W
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output


# Plot the objective function
def plot_graph(x1, x2, objFun, points, best_point):
    clear_output(wait=True)

    fig, ax = plt.subplots(1, 1)
    cp = ax.contour(x1, x2, objFun)
    fig.colorbar(cp)  # Add a color bar to a plot
    ax.set_title('Object Function Contour Plot')
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    n_points = len(points) - 1
    for i in range(len(points)):
        if i == best_point:
            plt.plot(points[i][0], points[i][1], 'ro')
        else:
            plt.plot(points[i][0], points[i][1], 'b.')
    # Plot the result of regular search
    plt.plot(points[n_points][0], points[n_points][1], 'go')
    plt.show()
