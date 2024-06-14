import matplotlib.pyplot as plt
import numpy as np

def valOfFun(x):
    return x **3 - 0.18*x*x + 0.0004752

#r=0.06 ms
xvalues=np.array([i/100 for i in range(1,12) ])
yvalues=[]

for i in xvalues:
    yvalues.append(valOfFun(i))

y2=0
plt.plot(xvalues,yvalues, marker = 'o')
plt.title("F(x)=x³-0.18x²+0.0004752")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

# 0<=x<=0.12
low=float(input("Enter the lower bound:"))
high=float(input("Enter the upper bound:"))
def findTheRoot(low,high,error,iter):

    i=0
    midOld=0
    while(i<iter) :
        mid = (low + high) / 2
        if (abs(error) < 0.5):
            return mid
           # break
        if(midOld!=0.0):
            error = (midOld - mid) / midOld * 100

        if (valOfFun(mid) * valOfFun(high) > 0):
                high = mid
        elif (valOfFun(mid) * valOfFun(low) > 0):
                low = mid
        # error count
        midOld=mid

        i=i+1


def printTheTable(low, high, error, iter):
    i = 0
    midOld = 0
    print("Table:")
    print()
    print(f'Iteration No.\t\tAbsolute Relative Approximate Error')
    while (i < iter):
        mid = (low + high) / 2

        if (midOld != 0.0):
            error = (midOld - mid) / midOld * 100
        if(i==0):
            print(f'{i+1}\t\t\t\t\tNo Absolute Relative Approximate Error')
        elif ( i<10):
            print(f'{i+1}\t\t\t\t\t{abs(error)}%')
        elif(i>=10 and i<20):
            print(f'{i+1}\t\t\t\t\t{abs(error)}%')

        if (valOfFun(mid) * valOfFun(high) > 0):
            high = mid
        elif (valOfFun(mid) * valOfFun(low) > 0):
            low = mid
        # error count
        midOld = mid


        i = i + 1
root="{:.5f}".format(findTheRoot(low,high,0.5,20))
print(f'Root ={root}')
printTheTable(low,high,0.5,20)

