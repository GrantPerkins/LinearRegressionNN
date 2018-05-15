import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, size, n=0):
        self.size = size
        self.n = n

    def plot_line(self, formula, x_range, x_coors, y_coors, title):
        assert "x" in formula
        #assert all x values git on graph
        assert all([0 < x <= 100 for x in x_range])

        axes = plt.gca()
        axes.set_xlim([0, 100])
        axes.set_ylim([0, 100])
        for i in range(self.size):
            plt.plot(x_coors[i], y_coors[i], 'ro')
        x = np.array(x_range)
        y = eval(formula)
        plt.plot(x, y)
        f = formula.split('+')
        f[1] = round(float(f[1]), 3)
        f[0] = str(round(float(f[0].split('*')[0]), 3)) + "*x"
        plt.title(title+";   "+"y = " + str(f[0]) + '+' +str(f[1]))
        # plt.savefig("images/step_"+str(self.n)+".png")
        plt.show()
        self.n += 1

    def plot_parabola(self, formula, x_range, x_coors, y_coors, title):
        pass

if __name__ == "__main__":
    plotter = Plotter(25)
    plotter.plot("-x + 100", range(1, 101), range(1, 101), "Test")
