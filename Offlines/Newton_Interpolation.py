import numpy as np

from matplotlib import pyplot as plt
import math

x=[]
y=[[0 for i in range(5)]
        for j in range(5)]
a=[]
b=[]

def take_input():
    file=open("gene.txt")
    for line in file:
        data=line.split("\t")
        a.append(int(data[0]))
        b.append(float(data[1]))
        #y[len(x)-1][0]=int(data[1])
    file.close()

def plot_graph(p,q,inp,cubic):
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    p.append(inp)
    q.append(cubic)
    final=dict()
    for i in range(len(p)):
        final[p[i]]=q[i]
    p=sorted(p)
    for i in range(len(p)):
        q[i]=final[p[i]]
    plt.plot(p,q,color='g',marker='o')
    plt.show()

def product(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro

def dividedDifference(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]))
    return y


def applyFormula(value, x, y, n):
    sum = y[0][0]

    for i in range(1, n):
        sum = sum + (product(i, value, x) * y[0][i])

    return sum

#main function
take_input()
inp=input("Enter the value of time: ")
inp=int(inp)
temp1={}
n=4
for i in range(len(a)):
    #temp1.append(a[i],abs(a[i]-inp))
    temp1[a[i]]=abs(a[i]-inp)
d = sorted(temp1, key = temp1.get)
#print(d)
for i in range(4):
    x.append(d[i])
x=sorted(x)
for i in range(4):
    for j in range(len(a)):
        if(a[j]==x[i]):
            y[i][0] = b[j]
            break

y=dividedDifference(x, y, n)
cubic=applyFormula(inp, x, y, n)
print("\nValue at", inp, "is",
        round(applyFormula(inp, x, y, n), 2))

x.clear()
for i in range(3):
    x.append(d[i])
x=sorted(x)
for i in range(3):
    for j in range(len(a)):
        if(a[j]==x[i]):
            y[i][0] = b[j]
            break
n=n-1
y=dividedDifference(x, y, n)
quadratic=applyFormula(inp, x, y, n)

error=math.fabs((cubic-quadratic)/cubic)*100
print("\nAbsolute relative Approximate error: ",error)

plot_graph(a,b,inp,cubic)


