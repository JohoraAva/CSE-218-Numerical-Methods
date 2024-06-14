import numpy as np
import matplotlib.pyplot as plt
import math

hours=np.array([(i*5) for i in range (0,7)],dtype=np.float64)
dragAmount=np.array([1000,550,316,180,85,56,31],dtype=np.float64)


def Sum(xa,powX,ya,powY,n):
    sum=0
    for i in range(n):
        sum+=xa[i] **powX * math.log(ya[i]) ** powY
    return sum

def valueOfFunc(a,b,x):
    return a*(math.exp(b*x))


n=len(hours)
numerator= n*Sum(hours,1,dragAmount,1,n)- (Sum(hours,1,dragAmount,0,n)*Sum(hours,0,dragAmount,1,n))
denominator= n*Sum(hours,2,dragAmount,0,n) -((Sum(hours,1,dragAmount,0,n)) **2)

#tranformed constants
a1=numerator/denominator
xAverage= Sum(hours,1,dragAmount,0,n)/n
yAverage=Sum(hours,0,dragAmount,1,n)/n

a0=yAverage- a1* xAverage

#real constants
a=math.exp(a0)
b=a1
print(f'So, the equation: y= {a} e^({b}x)')
print(f'the amount of drug in body after 40 hours= {valueOfFunc(a,b,40)} mg')


yvalues=[]
for i in range(len(hours)):
    yvalues.append(valueOfFunc(a,b,hours[i]))
def graphPlot():
    plt.plot(hours,dragAmount, hours,yvalues,marker='o')
    plt.xlabel("Passed Hours")
    plt.ylabel(" Amount of Drugs in body (mg)")
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.scatter(40, valueOfFunc(a, b, 40), c="r")
    plt.show()



graphPlot()