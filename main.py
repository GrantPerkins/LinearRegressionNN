import tensorflow as tf
import numpy as np
from random import randint
from graph import Plotter
import argparse


class LinearRegressor:
    """
    Finds line of best fit with a linear scatter plot
    """
    def __init__(self, size, spread, slope, intercept):
        self.plotter = Plotter(size)
        self.spread = spread
        self.x_coors = np.array(sorted([float(randint(0,
                                min(100, abs((100 // slope) - intercept)))) for _ in range(size)]))
        self.y_coors = np.array([float(slope *
                                self.x_coors[i] + randint(-spread, spread) + intercept) for i in range(size)])


    def train(self, unused):
        sess = tf.InteractiveSession()
        x = tf.placeholder("float", [size,], name="x")
        y = tf.placeholder("float", [size,], name="x")
        m = tf.Variable(0.0, name="m")
        b = tf.Variable(0.0, name="b")
        loss = tf.reduce_sum(tf.abs(y-(tf.scalar_mul(m, x)+ tf.multiply(100., b))))

        train_step = tf.train.GradientDescentOptimizer(0.00001).minimize(loss)

        tf.global_variables_initializer().run()

        feed = {x: self.x_coors, y: self.y_coors}

        for i in range(300):
            sess.run(train_step, feed_dict=feed)
            if (i+1) % 20 == 0:
                error = sess.run(tf.reduce_sum(tf.abs(y-(tf.scalar_mul(m, x) +
                        tf.multiply(100., b)))), feed_dict=feed)
                slope, y_intercept = sess.run([m, b], feed_dict=feed)
                equation = str(slope) + "*x+" + str(abs(y_intercept*100))
                self.plotter.plot_line(equation, range(1, 101), self.x_coors, self.y_coors,
                                       "Round: " + str(i+1) + ";    Error: " + str(round(error, 2)))


class ParabolicRegressor:
    """
    Finds line of best fit with a parabolic scatter plot
    """
    def __init__(self, size, spread, a, b, c):
        self.plotter = Plotter(size)
        self.x_coors = np.array(sorted([float(randint(0, 100)) for _ in range(size)]))
        self.y_coors = np.array([a*(self.x_coors[i])**2 + b*self.x_coors[i] + c +
                                randint(-spread, spread)for i in range(size)])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find line of best fit from scatter plot.')
    parser.add_argument('--size', help='set the amount of points in the scatter plot')
    parser.add_argument('--slope', help='sets the overall slope of the data of the scatter plot')
    parser.add_argument('--intercept', help='sets the overall y intercept of the data of the scatter plot')
    parser.add_argument('--spread', help='sets the maximum spread of the y_coordinate from its actual value in the random data')

    args = vars(parser.parse_args())
    size = 25 if args["size"] is None else int(args["size"])
    slope = -.5 if args["slope"] is None else float(args["slope"])
    intercept = 50. if args["intercept"] is None else float(args["intercept"])
    spread = 12 if args["spread"] is None else int(args["spread"])
    print(size, slope, intercept, spread)
    regressor = LinearRegressor(size, spread, slope, intercept)
    tf.app.run(main=regressor.train)
