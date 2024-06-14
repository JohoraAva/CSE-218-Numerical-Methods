import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data=pd.read_csv('e:\company_sales_data.csv')
x=np.array(data['month_number'])
y1=np.array(data['facecream'])
y2=np.array(data['toothpaste'])

plt.plot(x,y1,y2)

plt.show()