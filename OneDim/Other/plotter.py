'''
    Plot demo graph for one-dim search algorithms
'''
import matplotlib.pyplot as plt

#Plot the objective function
def plot_graph(x, y, approx, xl, xr):

    #plot function graph
    plt.plot(x, y)
    plt.plot(x, approx)
    # plt.plot([xl, xr],[0,0],'k')
    plt.show()
