# Conversão de Tipos
print("############## -Exemplo- ########################")
idade = "26"
# numero1 = "10"
# numero2 = '20'

# print(numero1 + numero2)

print(idade, type(idade))
print("############## Mudando o tipo de str para int/float ########################")
idadeInteira = int(idade)

print(idadeInteira, type(idadeInteira))

# int() converto qualquer variavel para o tipo inteiro
# str() converto qualquer variavel para o tipo string
# float() converto qualquer variavel para o tipo float
# bool() converto qualquer variavel para o tipo boleano

altura = float(input("Informe a sua altura: "))

print(altura, type(altura))

print("##################-Questão 3-####################")
x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x * y, num <= x + y, num * y != x * y)
print("######################################")
print(num == x * y, num * y == x * y, y > x + num)

print("################-Questão 4-######################")

x = 4.2

y = 10

z = "42"

print(not (((x * y == z) and not (x < y)) or y % 2 == 0))
print("######################################")

print(not (not (x < y and x * y == z)) or (x >= y or y % 2 == 0))
print(not False)
print(not ((x == y or True) and ((int(z) < x * y) and (type(y) == type(int(z))))))
print(
    not (
        ((not True) or int(z) % 7 == 0)
        and ((str(int(x * y)) == z) and (type(x) != type(z)))
    )
)
print((True and True) or not True)
