# > Dicionario

# Criando dicionario

dicionario = {}
dicionario = dict()

dicionario = {
    'nome': 'Filipe',
    'idade': 28,
    'altura': 1.77
}

print(dicionario)

print(dicionario['idade'])

# Adicionando elemento em um dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario['altura'])

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave)
    print(chave,dicionario[chave])
    
    
# Testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)