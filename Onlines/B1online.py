import numpy as np
import matplotlib.pyplot as plt


def Fx(x):
    return 3.1416*(x ** 3) - 12*3.1415*(x ** 2) +15

def F1x(h):
    return 3*3.1416*h*h - 24*3.1416*h


xvalues=np.array([(i/10) for i in range(1,10)])
yvalues=[]

for i in xvalues:
    yvalues.append(Fx(i))

plt.plot(xvalues,yvalues,marker='o')
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid()
plt.show()

print("No of it. \t\t\testimate root\t\t\tapp error")
def newTonRaphson(x,est):
    error=100
    i=1
    while abs(error)>est:
        xNew=x-Fx(x)/F1x(x)
        error=abs((xNew-x)/xNew)*100
        x=xNew
        print(f'{i}\t\t\t\t{x}\t\t\t{error}')
        i=i+1
     #   print("The value of the root is : ", "%.4f" % error)
    return xNew

print(newTonRaphson(0.5,0.05))