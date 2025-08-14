# def mensagem():
#     print('Curso de pyton insano')


# mensagem()

# def soma(a,b):
#     print(a+b)


# soma(8,9)


# def mult(x,y):
#     return x*y

# a = 8
# b = 10
# c = mult(a,b)

# print(f'A multiplicação de {a} e {b} é igual a {c}')


# def div(x,y):
#     if y != 0:
#         return x / y
#     else:
#         return 'Impossivel dividir por zero!'

# if __name__=='__main__':
#     a = int(input('Digite o primeiro número: '))
#     b = int(input('Digite o segundo número: '))

#     r = div(a,b)

#     print(f'O valor {a} dividido pelo {b} é : {r}')


def quadrado(val):
    quadrados = []
    for i in val:
        quadrados.append(i ** 2)
    return quadrados

if __name__ == '__main__':

    valores = [2,5,72,12]

    resultados = quadrado(valores)

    for i in resultados:
        print(i)
