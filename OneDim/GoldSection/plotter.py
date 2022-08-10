"""
    Plot demo graph for one-dim search algorithms
"""

import matplotlib.pyplot as plt
from IPython.display import clear_output


# Plot the objective function
def plot_graph(x, y, func, xl, xr, x1, x2, xm=31415):
    clear_output(wait=True)
    
    # plot function graph
    plt.plot(x, y)
    plt.plot([xl, xr], [0, 0], 'k')
    
    # plot x1 point
    plt.plot(x1, func(x1), 'ro', label='x1')
    plt.plot([x1, x1], [0, func(x1)], 'k')
    
    # plot x2
    plt.plot(x2, func(x2), 'bo', label='x2')
    plt.plot([x2, x2], [0, func(x2)], 'k')
    
    # plot xl line
    plt.plot([xl, xl], [0, func(xl)])
    plt.annotate('xl', xy=(xl-0.01, -0.2))
        
    # plot xr line
    plt.plot([xr, xr], [0, func(xr)])
    plt.annotate('xu', xy=(xr-0.01, -0.2))
        
    # plot x1 line
    plt.plot([x1, x1], [0, func(x1)], 'k')
    plt.annotate('x1', xy=(x1-0.01, -0.2))
        
    # plot x2 line
    plt.plot([x2, x2], [0, func(x2)], 'k')
    plt.annotate('x2', xy=(x2-0.01, -0.2))

    # plot xm point
    if xm != 31415:
        plt.plot(xm, func(xm), 'go', label='xm')
        plt.plot([xm, xm], [0, func(xm)], 'k')

    plt.show()
