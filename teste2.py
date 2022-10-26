import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

label = {}
a = [1,2,3,4,5]
b = [33,45,55,62,77]

x = np.array(a).reshape(-1,1)
reg = LinearRegression().fit(x,b)
a_coeff = reg.coef_
l_coeff = reg.intercept_

plt.plot(a,l_coeff+a_coeff*a,color='red')

plt.plot(a,b,label='Vestuario',marker='o',markerfacecolor = 'Blue')
plt.title('Gráficos de Despesas')
plt.ylabel('Despesas em R$')
plt.xlabel('Dia')
plt.legend(loc=2)
plt.show()



