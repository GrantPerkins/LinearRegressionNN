import tensorflow as tf
import numpy as np
from random import randint
from graph import plot

size = 25
slope = -.5
intercept = 50
diff = 12
x_coors = np.array(sorted([float(randint(0, min(100, abs((100//slope)-intercept)))) for _ in range(size)]))
y_coors = np.array([float(slope * x_coors[i] + randint(-diff, diff) + intercept) for i in range(size)])

def neuralnet(unused):
    sess = tf.InteractiveSession()
    x = tf.placeholder("float", [size,], name="x")
    y = tf.placeholder("float", [size,], name="x")
    m = tf.Variable(0.0, name="m")
    b = tf.Variable(0.0, name="b")
    loss = tf.reduce_sum(tf.abs(y-(tf.scalar_mul(m, x)+ tf.multiply(100., b))))

    train_step = tf.train.GradientDescentOptimizer(0.00001).minimize(loss)

    tf.global_variables_initializer().run()

    feed = {x: x_coors, y: y_coors}

    for i in range(300):
        sess.run(train_step, feed_dict=feed)
        if (i+1) % 20 == 0:
            error = sess.run(tf.reduce_sum(tf.abs(y-(tf.scalar_mul(m, x) +
                    tf.multiply(100., b)))), feed_dict=feed)
            slope, y_intercept = sess.run([m, b], feed_dict=feed)
            equation = str(slope) + "*x+" + str(abs(y_intercept*100))
            plot(equation, range(1, 101),x_coors, y_coors,
                 "Round: " + str(i+1) + ";    Error: " + str(round(error, 2)))


if __name__ == "__main__":
    tf.app.run(main=neuralnet)
