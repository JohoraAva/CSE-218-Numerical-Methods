import numpy as np
import matplotlib.pyplot as plt
#plot exp(-ax)
x=np.arange(0,10,0.1)
y1=np.exp(-0.5*x)
plt.plot(x,y1)
y2=np.exp(-1.0*x)
plt.plot(x,y2)
y3=np.exp(-2.0*x)
plt.plot(x,y3)
plt.xlabel('x from 0 to 10')
plt.ylabel('exp(-ax)')
plt.legend(['a=-0.5','a=1.0','a=2.0'])

plt.show()