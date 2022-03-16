import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse



lc2=pd.read_csv('./lc.csv')
rate=lc2['RATE']
times=lc2['TIME']
#df=[lc2.iloc[:,1][i] for i in range(len(lc2.iloc[:,1]))]
df=rate.to_numpy()
# print(df.shape)
time=[x-times[0] for x in times]
lre=lr()
lre.fit(df[:,np.newaxis],time)
output = lre.predict([[14]])
print(output[0])
