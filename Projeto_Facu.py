#Projeto de Medidas em Geral

print('''
    [1] Distância
    [2] Tempo
    [3] Temperatura
''')
start = input('Qual opção você deseja? ').upper().strip() [0]
print('=-' * 30)
while True:
    if start == '1':
        print('''
    [1] Quilômetros
    [2] Metros
    [3] Centímetros
            ''')
        print('=-' * 30)
        time_1 = input('De qual unidade de medida você quer converter? ').upper().strip() [0]
        print('=-' * 30)
        if time_1 == '1': #De Quilômetros para Metros/Centímetros
            medida = float(input('Digite sua medida em quilômetros: '))
            print('=-' * 30)
            print('''
                [1] Metros
                [2] Centímetros
            ''')
            time_2 = input('Para qual unidade de medida você quer converter? ').upper().strip() [0]
            print('=-' * 30)
            if time_2 == '1': 
                metros = medida * 1000
                print(f'{medida} quilômetros são {metros} metros!')
                print('=-' * 30)
            elif time_2 == '2':
                centimetros = medida * 100000
                print(f'{medida} quilômetros são {centimetros * 100} centímetros!')
                print('=-' * 30)
        elif time_1 == '2': #De Metros para Quilômetros/Centímetros
            medida = float(input('Digite sua medida em metros: '))
            print('=-' * 30)
            print('''
                [1] Quilômetros
                [2] Centímetros
            ''')
            time_2 = input('Para qual unidade de medida você quer converter? ').upper().strip() [0]
            print('=-' * 30)
            if time_2 == '1': 
                metros = medida / 1000
                print(f'{medida} metros são {metros} quilômetros!')
                print('=-' * 30)
            elif time_2 == '2':
                centimetros = medida * 100
                print(f'{medida} metros são {centimetros} centímetros!')
                print('=-' * 30)
            break
        elif time_1 == '3': #De Centímetros para Quilômetros/Metros
            medida = float(input('Digite sua medida em centímetros: '))
            print('=-' * 30)
            print('''
                [1] Quilômetros
                [2] Metros
            ''')
            time_2 = input('Para qual unidade de medida você quer converter? ').upper().strip() [0]
            print('=-' * 30)
            if time_2 == '1': 
                metros = medida / 100000
                print(f'{medida} centímetros são {metros} quilômetros!')
                print('=-' * 30)
            elif time_2 == '2':
                centimetros = medida / 100
                print(f'{medida} centímetros são {centimetros} metros!')
                print('=-' * 30)
            break
    elif start == '2':
        print('bloco2')
        break
    elif start == '3':
        print('bloco3')
        break