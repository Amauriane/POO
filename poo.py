'''Questão 4. Crie um programa que vai ler vários números do usuário e colocá-los numa lista. Depois disso,
crie duas novas listas que vão conter apenas os valores pares digitados e a outra os valores
ímpares digitados. Ao final mostre as três listas.'''

numero = list()
numeros_impares = list()
numeros_pares = list()
while True:
    numero.append(int(input("Digite um número: ")))
    c = input("Deseja continuar [s/n]: ")
    if c in "Nn":
        break
for p, v in enumerate(numero):
    if v % 2 == 0:
        numeros_pares.append(v)
    elif v % 2 == 1:
        numeros_impares.append(v)
print(f'Lista de todos os números digitados: {numero}')
print(f'Lista dos números pares: {numeros_pares}')       
print(f'Lista dos números ímpares: {numeros_impares}') 


'''Questão 8. Crie um programa que represente uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
Ao final mostre essa lista de valores com o formato de uma matriz.'''

matriz = []
for linha in range(3):
    v = []
    for coluna in range(3):
        v.append(int(input(f'Digite um número para [{linha}, {coluna}]: ')))
    matriz.append(v)

print('------ MATRIZ ------\n')
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()


'''Questão 9. Faça um programa para gerar jogos para a MEGA SENA.
 O programa vai perguntar quantos jogos o usuário deseja e vai sortear N jogos de 6 números aleatórios (entre 1 e 60) 
 para cada jogo cadastrando tudo em uma lista composta ordenada. '''

from random import randint
print('='*15)
print(' MEGA SENA ')
print('='*15)
mega_sena = []

p = int(input("Digite quantos jogos você deseja: "))
for contagem in range(p):
    jogo = []
    for qtdValores in range(6):
        sorteio = randint(1, 60)

        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)
    jogo.sort()
    mega_sena.append(jogo[:])
    print(f'Jogo {contagem + 1}: {mega_sena[contagem]}')

'''Questão 3.  Crie um programa onde o usuário possa digitar 5 valores numéricos e armazene-os numa lista
ordenada já na posição correta (ordem crescente). Não utilize a função sort(). Ao final mostre
a lista.'''

lista = []
for v in range(0,5):
    q = int(input("Digite um valor: "))
    if v == 0 or q > lista[-1]:
        lista.append(q)
    else:
        p = 0
        while p < len(lista):
            if q <= lista[p]:
                lista.insert(p, q)
                
                break
            p += 1
print(f'Esses foram os valores digitados: {lista}')


'''Questão 2. Crie um programa onde o usuário possa digitar vários valores numéricos e armazene-os em uma
lista. Caso o número já exista na lista ele não deve ser adicionado. Ao final mostre todos os
valores na ordem decrescente.'''

lista = []
while True: 
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
    else:
        print("Esse valor já existe.")
    p = str(input("Deseja continuar [s/n]: "))
    if p in "Nn":
        break
print()
lista.sort(reverse = True)
print(lista)