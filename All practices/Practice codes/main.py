import numpy as np
from matplotlib import pyplot as plt


def form_table(x, y):
    for j in range(1, 4):
        for i in range(4-j):
            y[i][j] = (y[i+1][j-1] - y[i][j-1])/(x[i+j] - x[i])


def interpol_cubic(x, y, T):
    val = 0
    for i in range(4):
        p = y[0][i]
        for j in range(i):
            p = p*(T - x[j])
        val += p
    return val


def interpol_quad(x, y, T):
    if x[3]>T and x[2]<T:
        n = 1
    elif x[0]<T and x[1]>T:
        n = 0
    elif abs(x[0]-T) <= abs(x[3]-T):
        n = 0
    else:
        n = 1
    val = 0
    for i in range(3):
        p = y[n][i]
        for j in range(i):
            p = p * (T - x[j+n])
        val += p
    return val


x1 = list()
y1 = list()
with open("gene.txt") as f:
    lines =f.readlines()
    for line in lines:
        words = line.split()
        x1.append(float(words[0]))
        y1.append(float(words[1]))
    f.close()
xf = np.array(x1)
yf = np.array(y1)
T = float(input())
xs = list()
ys = list()
i = 0
while xf[i]<T:
    i += 1
place = i
j = i-1
xs.append(xf[j])
ys.append(yf[j])
j -= 1
xs.append(xf[i])
ys.append(yf[i])
i += 1
k = 2
while k>0:
    if j<0:
        xs.append(xf[i])
        ys.append(yf[i])
        i += 1
    elif i>=len(xf):
        xs.insert(0, xf[j])
        ys.insert(0, yf[j])
        j -= 1
    elif abs(xf[i]-T)>=abs(xf[j]-T):
        xs.insert(0, xf[j])
        ys.insert(0, yf[j])
        j -= 1
    else:
        xs.append(xf[i])
        ys.append(yf[i])
        i += 1
    k-=1
x = np.array(xs)
y = np.zeros((4, 4))
for i in range(4):
    y[i][0] = ys[i]
form_table(x, y)
val = interpol_cubic(x, y, T)
print("value at "+str(T)+" using cubic interpolation: "+str(val))
val2 = interpol_quad(x, y, T)
print("value at "+str(T)+" using quadratic interpolation: "+str(val2))
error = abs((val-val2)/val)*100
print("relative approximate error: "+str(error))
x1.insert(place, T)
y1.insert(place, val)
plt.plot(x1, y1, marker='o')
plt.show()


