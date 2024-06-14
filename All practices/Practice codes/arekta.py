import numpy as np
import matplotlib.pyplot as plt

a=[]
b=[]

def takeInput():
    file=open("stock.txt")
    file.readline()
    for line in file:
        data=line.split()
        a.append(int(data[0]))
        b.append(float(data[1]))
    file.close()

def InterPolation(x,y,n,t):
    sum=0
    for i in range(n+1):
        product=y[i]
        for j in range(n+1):
            if(i != j):
                product=product*(t-x[j])/(x[i]-x[j])
        sum=sum+product
    return sum

day=int(input())
takeInput()


#select points
xpoints=[]
ypoints=[]

i=0
while a[i]<day:
    i+=1
pos=i
j=i-1  #before
xpoints.append(a[j])
ypoints.append(b[j])
xpoints.append(a[i]) #after
ypoints.append(b[i])
j-=1
i+=1

xpoints.append(a[i])
ypoints.append(b[i])
xpoints.insert(0,a[j])
ypoints.insert(0,b[j])



val1=InterPolation(xpoints,ypoints,3,day)
val2=InterPolation(xpoints,ypoints,2,day)
print(f'Value for Cubic Interpolatin: {val1}')
print(f'Value for Quadric Interpolation: {val2}')
error=abs((val1-val2)/val1)*100
print(f'Absolute approximate relative error: {error}%')
a.insert(pos,day)
b.insert(pos,val1)

plt.plot(a,b, marker = 'o')
plt.xlabel("Number of Days")
plt.ylabel(" Closing index of DSE")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

