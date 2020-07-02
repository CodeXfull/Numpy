"""
Recomenda-se fazer operações com numpy pela performace
Dps retorna para o padrão de dados 
"""

import numpy as np 

lista = [1,2,3,4]
array = np.array(lista)
print(array)
array_multiplicado = array*2
array_soma = array+20
array_raiz_quadrada = np.sqrt(array)

print(array_multiplicado)
print(array_soma)
print(array_raiz_quadrada)

lista_new = list(array_soma)
print(type(lista_new))
print(lista_new)

print("-"*20)

lista_float = [1, 2.6, 4.5, 6.32]
array1 = np.array(lista_float)
array_teto = np.ceil(array1) # arredondar pra baixo
array_chao = np.floor(array1) # arredondar pra cima
array_casas = np.around(array1, 2) # arredondar >.5
array2 = np.around(array1)
print(array_teto)
print(array_chao)
print(array_casas)
print(array2)