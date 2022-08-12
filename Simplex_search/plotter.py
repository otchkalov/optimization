"""
    Plot contour graph for two-dim function
"""
import matplotlib.pyplot as plt


# Plot the objective function
def plot_graph(x1, x2, obj_fun, simplex_set):
    fig, ax = plt.subplots(1, 1)
    cp = ax.contour(x1, x2, obj_fun)
    fig.colorbar(cp)  # Add a colorbar to a plot
    ax.set_title('Object Function Contour Plot')
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    for i in range(len(simplex_set)):
        xp, yp = [[simplex_set[i][0][0], simplex_set[i][1][0]], [simplex_set[i][0][1], simplex_set[i][1][1]]]
        plt.plot(xp, yp, 'b-', marker='.', linewidth=0.5)
        xp, yp = [[simplex_set[i][1][0], simplex_set[i][2][0]], [simplex_set[i][1][1], simplex_set[i][2][1]]]
        plt.plot(xp, yp, 'b-', marker='.', linewidth=0.5)
        xp, yp = [[simplex_set[i][2][0], simplex_set[i][0][0]], [simplex_set[i][2][1], simplex_set[i][0][1]]]
        plt.plot(xp, yp, 'b-', marker='.', linewidth=0.5)
    plt.show()
