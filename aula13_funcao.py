# > Função

# 1. O quu são funções por que utiliza-las?

#Funções que já utilizamos anteriomente...

# print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
# input() # - Retorna um dado informado pelo usuário (entarda padrão) e pode receber uma string
# len() # - recebe uma lista e retorna o tamanho dessa lista
# max() # - retorna o maior valor de uma lista

# 2. Criação de Funçoes

# Função inicial

def saudacao01():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao01()

# Função com parâmetros

def saudacao02(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao02("Filipe", "Python")

# Função com parametros default

def saudacao03(nome, curso="Python"):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao03("Filipe", "C++")
saudacao03("Filipe")

# Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)

print('O resultado da soma é ', resultado)


def calculadora(num1, num2, operacao= "+"):
    if operacao == "+":
        return soma(num1, num2)
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10,20)

print(resultado)