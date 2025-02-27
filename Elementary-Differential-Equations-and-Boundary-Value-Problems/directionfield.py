import numpy as np
import matplotlib.pyplot as plt

def show_direction_field(F, xr, yr):
    x_vals = np.linspace(xr[0], xr[1], 20)
    y_vals = np.linspace(yr[0], yr[1], 20)
    X, Y = np.meshgrid(x_vals, y_vals)
    M = F(X, Y)

    # Define direction vectors (1, M) and normalize if desired
    U = np.ones_like(M)
    V = M

    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', pivot='middle')
    plt.gca().set_aspect('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Direction Field with Arrows')
    plt.show()
