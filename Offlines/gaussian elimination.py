import numpy as np
np.set_printoptions(formatter={'float':lambda x: "{0:0.4f}".format(x)})

# input taking
numOfVar=int(input())
a=np.zeros((numOfVar,numOfVar),dtype=float)
b=np.zeros((numOfVar,1),dtype=float)

for i in range(numOfVar):
    a[i]=np.array(list(map(float,input().split())),dtype=float)

for i in range(numOfVar):
    b[i][0]=np.array(float(input()))

#printing method
def printTheMat(A):
    for r in A:
        for c in r:
            print( "%.4f" %c,end=" ")
        print()
    print()

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
    out=np.zeros((len(A),1),dtype=float)
    out[len(A)-1][0]=B[len(A)-1][0]/A[len(A)-1][len(A)-1]
    for i in range(len(A)-2,-1,-1):
        out[i]=B[i]

        for j in range(i+1,len(A)):
            out[i][0]=out[i][0]-A[i][j]*out[j][0]
        out[i][0]=out[i][0]/A[i][i]

    return out


result=GaussianElimination(a,b,True,True)
print("Print output:")
printTheMat(result)