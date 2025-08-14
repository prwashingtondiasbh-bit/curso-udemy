elemento = {
    'Z':3,
    'nome':'Lítio',
    'grupo':'Metais alcalinos',
    'densidade':0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionario possui {len(elemento)} elementos')

elemento['grupo'] = 'Alcalinos'

elemento['periodo'] = 1
print(elemento)
# del elemento['periodo']

# print(elemento)

# elemento.clear()
# print(elemento)


print(elemento.items())

for i in elemento.items():
    print(i)


for i in elemento.keys():
    print(i)


for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}:{j}')