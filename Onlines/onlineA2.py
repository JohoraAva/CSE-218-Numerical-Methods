import numpy as np
import matplotlib.pyplot as plt
import math

year=np.array([(i*10) for i in range (190,201)],dtype=np.float64)
population=np.array([10.3,13.5,13.9,14.2,11.6,10.3,9.7,9.6,14.1,19.8,31.1],dtype=np.float64)

print(year)



def detTheSum(xvalue,power,n):
    sum=0
    for i in range(n):
        sum+=xvalue[i]**power
    return sum

def detSum2(xvalue,powX,yvalue,powY,n):
    sum = 0
    for i in range(n):
        sum += xvalue[i] ** powX *yvalue[i] ** powY
    return sum

def  GaussianElimination(A,B,pivot,showall):
    for i in range(len(A)):
        if(i+1<len(A)):
            print(f'Step {i + 1}:')
        c=1
        if(pivot):
            j=i+1
            while j<len(A):
                if(abs(A[i][i])<abs(A[j][i])):
                    A[[i,j],:]=A[[j,i],:]
                    B[[i,j],0]= B[[j,i],0]

                j=j+1
        #forward elimination
        j=i+1
        while(j< len(A)):
            ratio=A[j][i]/A[i][i]
            A[j]=A[j]-ratio*A[i]
            B[j][0]=B[j][0]-ratio * B[i][0]

            j=j+1
            if (showall):
                print(f'sub Step {c}:')
                print()
                print("Matrix A:")
                print(A)
                print()
                print("Matrix B:")
                print(B)
                print()
                c+=1


    #back substitution
    out=np.zeros((len(A),1),dtype=np.float64)
    out[len(A)-1][0]=B[len(A)-1][0]/A[len(A)-1][len(A)-1]
    for i in range(len(A)-2,-1,-1):
        out[i]=B[i]

        for j in range(i+1,len(A)):
            out[i][0]=out[i][0]-A[i][j]*out[j][0]
        out[i][0]=out[i][0]/A[i][i]

    return out

n=len(year)
n2=len(population)
xvalues=np.array([  [n,detTheSum(year,1,n), detTheSum(year,2,n),detTheSum(year,3,n)],
                    [detTheSum(year,1,n),detTheSum(year,2,n), detTheSum(year,3,n),detTheSum(year,4,n)],
                    [detTheSum(year,2,n),detTheSum(year,3,n), detTheSum(year,4,n),detTheSum(year,5,n)],
                    [detTheSum(year,3,n),detTheSum(year,4,n), detTheSum(year,5,n),detTheSum(year,6,n)]
                ],dtype=np.float64)
yvalues=np.array([[detTheSum(population,1,n2)],
                  [detSum2(year,1,population,1,n2)],
                  [detSum2(year,2,population,1,n2)],
                  [detSum2(year,3,population,1,n2)]
                  ],dtype=np.float64)


result=GaussianElimination(xvalues,yvalues,True,True)

print(result)

def popCount(x):
    sum=0
    for i in range(len(result)):
        sum+=result[i]* (x **i)

    return sum

print(f'result = {popCount(2010)}')

year=np.append(year, 2010)
population=np.append(population, popCount(2010))

print(len(population) )
yvalues2=[]
for i in range(len(year)):
    yvalues2.append(popCount(year[i]))

def graphPlot():


    plt.plot(year,population,year,yvalues2, marker='o')
    plt.xlabel("Number of Days")
    plt.ylabel(" Closing index of DSE")
    plt.grid(color='green', linestyle='--', linewidth=0.5)

    plt.show()


graphPlot()