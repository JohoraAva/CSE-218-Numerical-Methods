import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
np.set_printoptions(formatter={'float':lambda x: "{0:0.4f}".format(x)})

xvalues =np.array([0,0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19,0.21])
yvalues =np.array([1,1.03,1.06,1.38,2.09,3.54,6.41,12.6,22.1,39.05,65.32,99.78])

def detTheValue(xvalue,powX,yvalue,powY,n):
    sum=0
    for i in range(n):
        sum+=xvalue[i] **powX * math.log(yvalue[i]) ** powY
    return sum

def fun(a,b,val):
    return a* (math.exp(b*val))
n=len(xvalues)
numerator= n*detTheValue(xvalues,1,yvalues,1,n)- (detTheValue(xvalues,1,yvalues,0,n)*detTheValue(xvalues,0,yvalues,1,n))
denominator= n*detTheValue(xvalues,2,yvalues,0,n) -((detTheValue(xvalues,1,yvalues,0,n)) **2)

value=numerator/denominator
xAverage= detTheValue(xvalues,1,yvalues,0,n)/n
yAverage=detTheValue(xvalues,0,yvalues,1,n)/n

value0=yAverage- value* xAverage
print(f' a0= {value0}  a1={value}')

print(f'so the value is {fun(math.exp(value0),value,0.16)}')


#for sat model
#a= 1/value0 , value*a=b ; so y=(a*x)/(b+x)


#for power model
# a= math.exp(value0) value=b, soo y= a* x**b