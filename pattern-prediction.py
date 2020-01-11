import sys
import tensorflow as tf
import numpy as np

def main():
    print("This program will take a series of points on a cartesian grid and pattern matches\n"
          "in order to determine the value or weight of a given input in relation to the pattern\n"
          "Try it your self by entering a pattern of points. To get the idea, enter a series of\n"
          "points from the function 3x + 5. The neural network will be able to predict the pattern\n"
          "and tell you the given output.\n")
    xList = []
    yList =[]
    inputPoints(xList, yList)
    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    xs = np.array(xList, dtype=float)
    ys = np.array(yList, dtype=float)

    model.fit(xs, ys, epochs=1000)

    while True:
        inp = input("Enter an input (or 'q' to quit): ")
        if inp == 'q':
            sys.exit()
        x = [float(inp)]
        print(model.predict(x))

def inputPoints(xs, ys):
    while True:
        x = input("Enter x-value or 'q' to quit: ")
        y = input("Enter y=value or 'q' to quit: ")
        if x == 'q' or y == 'q':
            return;
        xs.append(float(x))
        ys.append(float(y))

main()
