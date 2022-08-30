'''
    Plot demo graph for one-dim search algorithms
'''
import matplotlib.pyplot as plt
from IPython.display import clear_output

#Plot the objective function
def plot_graph(x, y, approx, xl, xr):
    clear_output(wait=True)
    
    #plot function graph
    plt.plot(x, y)
    plt.plot(x, approx)
    # plt.plot([xl, xr],[0,0],'k')
    plt.show()
