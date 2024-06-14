from matplotlib import pyplot as plt
import math
import numpy as np


tm= float(input())



def lag(x,y,n,t):
    sum=0
    for i in range(n+1):
        product=y[i]
        for j in range(n+1):
            if(i != j):
                product=product*(t-x[j])/(x[i]-x[j])
        sum=sum+product
    return sum
def Quadinterpolation(x,y,t):
    sum = 0
    for i in range(3):
        product = y[i]
        for j in range(3):
            if (i != j):
                product = product * (t - x[j]) / (x[i] - x[j])
        sum = sum + product
        print(f'check: {sum}')
    return sum


a=[]
b=[]
def takeInput():
    file=open("gene.txt")
    for line in file:
        data=line.split()
        a.append(float(data[0]))
        b.append(float(data[1]))
    file.close()

takeInput()
x=np.array(a)
y=np.array(b)


xval=[]
yval=[]
i=0
while a[i]<tm:
    i+=1
j=i-1
xval.append(x[j])
yval.append(y[j])
xval.append(x[i])
yval.append(y[i])
j-=1
i+=1
pos=i
points=2
while points>0:
    if(j<0):
        xval.insert(0,x[i])
        yval.insert(0,y[i])
    elif(i>len(x)):
        xval.append(x[j])
        yval.append(y[j])
    elif(abs(x[j]-tm) < abs(x[i]-tm)):
        xval.insert(0,x[j])
        yval.insert(0,y[j])
        j-=1
    else:
        xval.append(x[i])
        yval.append(y[i])
        i+=1
    points-=1


print(xval)
print(yval)
val1=22
val2=interpolation(xval,yval,3,tm)
print(f'val1: {val1}  val2 : {val2}')
error=abs((val1-val2)/val1)*100
print(error)
plt.plot(a,b,marker='o')

plt.show()

