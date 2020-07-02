import numpy as np 

array = np.arange(10)
print(array)

print(array[0])
print(array[5])
print(array[-1])
print(array[-2])

print('-'*20)
texto = "Duas coisas são infinitas: o universo e a estupidez humana. Mas, em relação ao universo, ainda não tenho certeza absoluta"
texto = texto.split()
print(texto)
print(len(texto)) # 20 elementos na lista

array_new = np.array(texto)
print(
    array_new[3]
)
print(array_new[5])

print('-'*20)
nova_frase = array_new[4:10]
curso =" ".join(nova_frase) # transformar pra string
print(curso)
print(array_new[10:]) # pegar tudo do 10 pra frente
print(array_new[:10]) # até o 10
print(array_new[::-1]) # inverter

