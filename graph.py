import numpy as np
import matplotlib.pyplot as plt
size = 3

def plot(formula, x_range, x_coors, y_coors):
    print(formula)
    assert "x" in formula
    #assert all x values git on graph
    assert all([0 < x <= 100 for x in x_range])

    axes = plt.gca()
    axes.set_xlim([0, 100])
    axes.set_ylim([0, 100])
    for i in range(size):
        plt.plot(x_coors[i], y_coors[i], 'ro')
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    plot("-x + 100", range(1, 101))
