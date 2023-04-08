# > Estruturas Condicionais

idade = 17

if idade >= 18:
    print("Você é maior de Idade.")
else:
    print("Você é menor de idade.") 
    
"""
Imagine que você queira imprimir "Aprovada(o)", caso o estudante tenha uma média
superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7

"""

media = float(input("Digite a  média do aluno: "))
presenca = float(input("Digite a precensa do aluno: "))
# if media >= 7:
#     print("Você foi Aprovada(o)")
# elif media >= 5: 
#     print("Você foi para Recuperação") 
# else:
#     print("Você foi Reprovada(o)")

if media >= 7 and presenca >= 70:
    print("aprovado")
else:
    print("reprovado")