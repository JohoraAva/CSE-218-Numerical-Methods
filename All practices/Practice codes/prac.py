import numpy as np
import matplotlib.pyplot as plt

#functions
def fX(x):
    return  x **3 - 0.165*x*x + 0.0003993
def fX1(x):
    return 3*x **2 - 0.33*x

xvalues=np.array([(i/100) for i in range (1,12)])
yvalues=[]

for i in xvalues:
    yvalues.append(fX(i))

plt.plot(xvalues,yvalues,marker="o")
plt.grid(color="green",linestyle='--')
plt.show()

def newtonRaphson(sp,es,iter):
   # sp=sp-fX(sp)/fX1(sp)
    error=100
    i=0
    while i<=iter:
        if(abs(error)<=es):
            return sp
        spNew=sp-fX(sp)/fX1(sp)
        error=abs((spNew-sp)/spNew)*100
        sp=spNew
        i=i+1

        print("The value of the root is : ", "%.4f" % error)

print(newtonRaphson(0.05,0.5,20))