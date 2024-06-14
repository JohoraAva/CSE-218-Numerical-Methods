import numpy as np
import matplotlib.pyplot as plt


x=[1,2,3,4,5,6,7]
t=[0.5,2.5,2,4,3.5,6,5.5]

def graphPlot():

    plt.plot(x,t, marker='o')
    plt.xlabel("Number of Days")
    plt.ylabel(" Closing index of DSE")
    plt.grid(color='green', linestyle='--', linewidth=0.5)

    plt.show()


graphPlot()