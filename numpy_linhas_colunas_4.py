import numpy as np 

array = np.arange(12)
print(array)

print(array.shape) # shape -> (nº linhas, nº colunas), mas sozinho é só 1 linha
x = array.reshape(3,4) # múltiplo de nº elementos no array
print(x)
print(x[1])
print(x[1][1])
print(x.shape)

print("-"*20)
y = array.reshape(2,2,3) # 2x2x3 = 12 elementons
print(y)
print(y[0])
print("-"*20)
print(y[0][1])
print(y[0][1][1])
print(y.shape)