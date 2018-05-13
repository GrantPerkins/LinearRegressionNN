import tensorflow as tf
import numpy as np
from random import randint
from graph import plot
from  random import triangular
size = 3
x_coors = np.array([randint(0, 99) for _ in range(size)])
y_coors = np.array([randint(0, 99) for _ in range(size)])


def neuralnet(unused):
    sess = tf.InteractiveSession()
    x = tf.placeholder("float", [size,], name="x")
    y = tf.placeholder("float", [size,], name="x")
    m = tf.Variable(tf.zeros([1]), name="m")
    b = tf.Variable(tf.zeros([1]), name="b")
    y_intercept = tf.convert_to_tensor([b[0]]*size)
    y_ = tf.scalar_mul(m[0], x) + tf.scalar_mul(100.0, y_intercept)

    cross_entropy = [0]
    for i in range(size):
        cross_entropy[0] += abs(y[i]-y_[i])
    cross_entropy[0] /= size
    cross_entropy = tf.convert_to_tensor(cross_entropy)
    train_step = tf.train.GradientDescentOptimizer(0.00005).minimize(cross_entropy)

    tf.global_variables_initializer().run()

    for i in range(10000):
        sess.run(train_step, feed_dict={x: x_coors, y: y_coors})
        if (i+1)%1000==0:
            slope, y_intercept = sess.run([m, b], feed_dict={x:x_coors, y:y_coors})
            op = '-' if y_intercept < 0 else '+'
            plot(str(slope)+"*x"+op+str(abs(y_intercept*100)), range(1, 101), x_coors, y_coors)

    print(sess.run(cross_entropy, feed_dict={x: x_coors,
                                        y: y_coors}))


if __name__ == "__main__":
    tf.app.run(main=neuralnet)
