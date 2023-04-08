import random
# exemplo 1: Estrutura 
numero_sorteado = random.randint(1,100)
# print(numero_sorteado)
numero_escolhido = int(input("Informe um numero entre 1 e 100 ->  "))

# if numero_sorteado == numero_escolhido:
#     print("Você acertou! ")
# else:
#     print('Voce errou! ')

while numero_escolhido != numero_sorteado:
    print("Você errou o número, tente novamente...")
    if numero_escolhido < numero_sorteado:
        print("Dica: o numero " , numero_escolhido , " é menor que o numero procurado " )
    else:
        print("Dica: o numero " , numero_escolhido , " é maior que o numero procurado " )
    numero_escolhido = int(input("Informe um numero entre 1 e 20 ->  "))
    
print("Parabéns! Você acertou!")

# exemplo 2: Estrutura com contador

contador = 0
while contador < 5 :
    print(contador)
    contador = contador + 1