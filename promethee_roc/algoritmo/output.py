import numpy as np
import matplotlib.pyplot as plt

def print_graph(nodes):
    # coordenadas dos nós
    x = np.array([1, 1, 1, 1, 1])
    y = np.array([5, 4, 3, 2, 1])

    # printa arestas
    for i in range(1, len(x)):
        plt.plot([x[i - 1], x[i]], [y[i - 1], y[i]], color='black', zorder=1)

    # printa nós
    plt.scatter(x, y, s=500, color='lightblue', zorder=2)

    # printa labels
    padding = 0.2
    for i, node in enumerate(nodes):
        plt.text(x[i] + padding, y[i], node, horizontalalignment='left', verticalalignment='center', color='black')

    plt.xlim(0.5, 1.5)
    plt.ylim(0, 6)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()
