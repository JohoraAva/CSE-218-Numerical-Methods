import numpy as np
import matplotlib.pyplot as plt

def funcX(x):
    return np.exp(-1*x)-x

def funcX1(x):
    return -np.exp(-1*x) -1


xvalues= np.array([i for i in range (-2,10)])
yvalues=[]


for i in xvalues:
    yvalues.append(funcX(i))
    # print(funcX(i))

def newtonRaphson(sp,es):
    ratio=funcX(sp)/funcX1(sp)
    while abs(ratio)> es:
        ratio=funcX(sp)/funcX1(sp)
        sp=sp-ratio
    print("The value of the root is : ","%.4f" % ratio)

plt.plot(xvalues,yvalues, marker = 'o')
plt.title("prac")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

newtonRaphson(3,0.5)
# for i in yvaluesTem:
#     yvalues.append()