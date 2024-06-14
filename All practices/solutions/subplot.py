import numpy as np
from matplotlib import pyplot as plt
x=np.random.normal(loc=0.0,scale=1.0,size=(1000))
plt.subplot(2,2,1)
plt.hist(x,bins=100)

plt.subplot(2,2,2)
x=np.random.uniform(low=0.0,high=1.0,size=(1000))
plt.hist(x,bins=100)
