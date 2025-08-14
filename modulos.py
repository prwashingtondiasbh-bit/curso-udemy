# import math as w
# import numpy as np

# if __name__ == '__main__':


#     L = np.array([1,2,3,4,5,6,7,8,9])

#     print(L)

# # print(w.sqrt(121))


import random

# print(f'Gerar valores aleatorios entre 1 e 50: \n')

# for i in range(5):
#     n = random.randint(1,50)
#     print(f'O valor gerado é: {n}')


# valor = random.random()

# print(f'Valor gerado é: {round(valor * 10, 2)}')


# valor = random.uniform(1,100)

# print(f'Valor gerado é: {round(valor,4)}')


l = [1,8,75,89,2,3,5,8,74,25,26]

# n = random.choice(l)
# n = random.sample(l,5)

# print(f'O numero escolhido é: {n}')

print(f'Mostrar a lista original: {l}')
print(f'Mostrar a lista embaralhada:')
n = random.shuffle(l)
print(l)
