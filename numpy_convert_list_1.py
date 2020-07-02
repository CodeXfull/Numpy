"""
O fato de tds os dados serem iguais é q fazem o numpy ter velocidade e performace

Tiver uma String tds os dados serão do tipo string
Tiver um float e nem uma string tds os dados serão do tipo float
Tiver nem float e String tds os dados serão do tipo int
"""
import numpy as np

# transformar lista para array
lista = [1,2.3, 'Oi', True]
a = np.array(lista)
print(a)
print(type(a)) # td tipo string

lista1 = [1, 2.3, 4]
b = np.array(lista1)
print(b)
print(type(b))

# True = 1
# False = 0
lista2 = [1, 2.3, 4, True]
c = np.array(lista2)
print(c)
print(type(c))

lista3 = [True, False, True, 1 ]
d = np.array(lista3)
print(d)
print(type(d))

lista4 = [True, False, True, 1.0 ]
e = np.array(lista4)
print(e)
print(type(e))