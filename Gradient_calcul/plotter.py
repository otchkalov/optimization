"""
    Plot contour graph for two-dim function
"""
import matplotlib.pyplot as plt


# Plot the objective function
def plot_graph(x1, x2, objFun, levels):
    fig, ax = plt.subplots(1, 1)
    cp = ax.contour(x1, x2, objFun, levels)
    fig.colorbar(cp)  # Add a colorbar to a plot
    ax.set_title('Object Function Contour Plot')
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    plt.show()


# Plot a vector field of object function gradient 
def vector_plot(x1, x2, objFun, gradOf, levels):
    # clear_output(wait=True)

    fig, ax = plt.subplots(1, 1)
    # cp = ax.contour(x1, x2, ObjFun)
    cp = ax.contour(x1, x2, objFun, levels)
    fig.colorbar(cp)  # Add a colorbar to a plot
    plt.quiver(x1, x2, gradOf[0], gradOf[1])
    ax.set_title('Object Function Antigradient')
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    plt.show()
