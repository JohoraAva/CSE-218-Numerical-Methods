import numpy as np
import matplotlib.pyplot as plt
import math

# polynomial

tvalues=np.array([80,40,-40,-120,-200,-280,-340],dtype=np.float64)
Alphavalues=np.array([6.47* 10**-6,6.24* 10**-6,5.72* 10**-6,5.09* 10**-6,4.30* 10**-6,3.33* 10**-6,2.45* 10**-6],dtype=np.float64)



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
n=len(tvalues)
n2=len(Alphavalues)


xvalues=np.array([[n,detTheSum(tvalues,1,n), detTheSum(tvalues,2,n)],[detTheSum(tvalues,1,n),detTheSum(tvalues,2,n), detTheSum(tvalues,3,n)],[detTheSum(tvalues,2,n),detTheSum(tvalues,3,n), detTheSum(tvalues,4,n)]],dtype=np.float64)
yvalues=np.array([[detTheSum(Alphavalues,1,n2)],[detSum2(tvalues,1,Alphavalues,1,n2)],[detSum2(tvalues,2,Alphavalues,1,n2)]],dtype=np.float64)

#gaussian elimination

print("check:")
print(xvalues)
print(yvalues)
result=GaussianElimination(xvalues,yvalues,False,True)

print(result)
