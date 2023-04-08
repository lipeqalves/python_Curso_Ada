# > Listas

# antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista

notas = [7.9, 9.7, 8.2]

# Criando Listas

lista = []
lista = list()
lista = [26, "lipe", 3.1444, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [26, "lipe", 3.1444, False]
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])

# slices

lista = [10, 50, 30, 40, 25, 60, 5]

# print(lista[0:3])
# print(lista[3:6])
# print(lista[3:])
# print(lista[2:6:2])

# > Interação co For

# 1. Utilizando os proprios elemntos da lista
# for elemento in lista:
#     print(elemento)

# 2. Utilizando os indices

# print("comprimento da lista: ", len(lista))

# for i in range(len(lista)):
#     print(lista[i])

# > Métodos de listas

lista = [1, 3, 12, 8, 2]

# append
print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# insert

lista.insert(2,10)
print('Depois do insert: ', lista)

# extend 

lista2 = [1,2,3]

lista.extend(lista2)
print('Depois do extend: ', lista)

# pop

lista.pop()
print('Depois do pop: ', lista)

lista.pop(0)
print('Depois do pop com parametro: ', lista)

# remove 

lista.remove(3)
print('Depois do remove: ', lista)

# count

print('quantidade de 2 na lista: ', lista.count(2))

# index

print('indece do elemento 12: ', lista.index(12))

# sort

lista.sort()

print(lista)
lista.sort(reverse=True)
print(lista)

# Funçoes para listas

# len

print(len(lista))

# sum

print(sum(lista))

# max

print('maior elemento da lista: ', max(lista))

# min

print('menor elemento da lista: ', min(lista))