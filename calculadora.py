import os

operacao = {
    '+': 'Soma',
    '-': 'Subração',
    '*': 'Multiplicação',
    '/': 'Divisão',
    '^': 'Exponenciação'
}

continuar = 0

while continuar == 0:
    
    i = 0
    for op, name in operacao.items():
        print(f'{i}: {name}')
        i += 1

    resultado = 0
    op = int(input('Escolha a operação que deseja realizar: '))
    
    op_str = list(operacao.keys())[op]

    print(f'>>> {op_str} escolhida')

    n1 = float(input('Qual é o primeiro valor? '))
    n2 = float(input('Qual é o segundo valor? '))

    if op == 0: # soma
        resultado = n1 + n2

    elif op == 1: # subtração
        resultado = n1 - n2

    elif op == 2: # multiplicação
        resultado = n1 * n2

    elif op == 3: # divisão
        resultado = n1 / n2

    elif op == 4: # exponenciação
        resultado = n1 ** n2

    print(f'{n1} {op_str} {n2} = {resultado}')

    print('Deseja fazer outra operação? ')
    continuar = int(input('0 - SIM, 1 - NÃO '))
    os.system('cls')