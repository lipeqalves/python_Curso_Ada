print("####### - Questao 1 - ##########")

x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"

if x % 2 == 0:
    resp2 = "par"
else:
    resp2 = "impar"


print(f"O número {x} é {resp1} e {resp2}.".format(x, resp1, resp2))

print("####### - Questao 2- ##########")

cont = 0
resultado = 0
n = 1000

while cont != n:
    resultado = resultado + 1 / (2**cont)

    cont = cont + 1

print(resultado)

print("####### - Questao 3 - ##########")

# for _ in range(10):

#    print("Olá, mundo!")
# print('####### - Questao3 - A  - ##########')
# for _ in "let's code":
#   print("Olá, mundo!")
# print('####### - Questao3 - B  - ##########')

# for _ in " "*10:
#     print("Olá, mundo!")

# print('####### - Questao3 - C  - ##########')

# for _ in range(10, 20, 1):
#     print("Olá, mundo!")

# print('####### - Questao3 - D  - ##########')

# for _ in [10]:
#     print("Olá, mundo!")

# print('####### - Questao3 - E  - ##########')

# for _ in [10]*10:
#     print("Olá, mundo!")

print("####### - Questao 4 - ##########")

lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:
    if item % 2 == 0:
        if item < 0:
            lista_final.append(-item)

        else:
            lista_final.append(item)
    else:
        if item < 0:
            lista_final.append(-2*item)

        else:
            lista_final.append(2*item)

print(lista_final)


print("####### - Questao 5 - ##########")
animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))