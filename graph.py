import numpy as np
import matplotlib.pyplot as plt
size = 25


def plot(formula, x_range, x_coors, y_coors, title):
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
    f = formula.split('+')
    f[1] = round(float(f[1]), 3)
    f[0] = str(round(float(f[0].split('*')[0]), 3)) + "*x"
    plt.title(title+";   "+"y = " + str(f[0]) + '+' +str(f[1]))
    plt.show()

if __name__ == "__main__":
    plot("-x + 100", range(1, 101))
