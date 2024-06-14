import numpy as np
import matplotlib.pyplot as plt

def Fx(x):
    return -298*(x **3) + 3*x*x +1000

def F1x(x):
    return -894*x*x + 6*x

xvalues=np.array([(i/10) for i in range(1,20)])
yvalues=[]

for i in xvalues:
    yvalues.append(Fx(i))


plt.plot(xvalues,yvalues,marker='o')
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid()

plt.show()


def newtonRaphson(x,est):
    error=100
    i=1
    while(True):
        if(error<=est):
            break
        else:
            xNew=x-Fx(x)/F1x(x)
            error=abs((xNew-x)/xNew)*100
            x=xNew
            print(f'{i}\t\t\t\t{x}\t\t\t{error}')
            i = i + 1
    return x


print(newtonRaphson(1,0.05))
q=newtonRaphson(1,0.05)
ans = q ** 3
print(ans)