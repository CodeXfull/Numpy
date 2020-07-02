import numpy as np  

array = np.arange(20)
print(array)
cond = array > 5 
contador = 0
for elemento in cond:
    if elemento:
        contador += 1

print("Contador: {}".format(contador))

