import numpy as np
import matplotlib.pyplot as plt


n=int(input())

intitalConcentration=0.000122

def valueOfFun(x):
    return ((6.73*x+0.00000006725+0.0005*0.000726)/(3.62* 10**-12 * x+ 3.908*10**-8*x* .0005))

def TrapezoidalRule(a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(1,n):
        sum+=valueOfFun(a+i*h)
    sum = valueOfFun(a) + 2 * sum + valueOfFun(b)
    result=(sum*(b-a))/(2*n)
    return result


def simpsonsRule(a,b,n):
    h=(b-a)/(2*n)
    sum=0
    for i in range(1,2*n):
        if(i%2==0):
            sum+=2*valueOfFun(a+h*i)
        elif(i%2!=0):
            sum+=4*valueOfFun(a+h*i)
    sum=valueOfFun(a)+sum+valueOfFun(b)

    result= (sum*(b-a))/(3*2*n)
    return result


def errorPrint(a,b,n):
    if(n==1):
        print("1. Trapezoidal Method: ")
        print(f' n=1 \t\t Result= {TrapezoidalRule(a, b, 1)} seconds\t\tError=N/A')

    else:
        print("2.Simpson's 1/3rd Rule: ")
        print(f' n=1 \t\t Result= {simpsonsRule(a, b, 1)} seconds\t\tError=N/A')

    for i in range(2,6):
        if(n==1):
            out1=TrapezoidalRule(a,b,i-1)
            out2=TrapezoidalRule(a,b,i)
        else:
            out1 = simpsonsRule(a, b, (i - 1))
            out2 = simpsonsRule(a, b,  i)

        error=abs((out2-out1)/out2)*100

        print(f' n={i} \t\t Result= {out2} seconds\t\tError={error}%')


print(f'Required time for the value of {n} using Trapezoidal Method= {TrapezoidalRule(intitalConcentration*0.5,intitalConcentration,n)}  seconds')
print(f'Required time for the value of {n} using Simpsons 1/3rd Rule= {simpsonsRule(intitalConcentration*0.5,intitalConcentration,n)}  seconds')
TrapezoidalRule(intitalConcentration*0.5,intitalConcentration,5)
errorPrint(intitalConcentration*0.5,intitalConcentration,1)
simpsonsRule(intitalConcentration*0.5,intitalConcentration,5)
errorPrint(intitalConcentration*0.5,intitalConcentration,2)

x=np.array([1.22*10**-4,1.20*10**-4,0.0001,0.00008,0.00006,0.00004,0.00002])
t=[]
def graphPlot():
    for i in range(len(x)):
        t.append(simpsonsRule(x[i],intitalConcentration,5))

    plt.plot(x,t, marker='o')
    plt.xlabel("Number of Days")
    plt.ylabel(" Closing index of DSE")
    plt.grid(color='green', linestyle='--', linewidth=0.5)

    plt.show()


graphPlot()