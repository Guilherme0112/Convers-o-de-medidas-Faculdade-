#Projeto de Medidas em Geral
def celsius_para_fahrenheit(celsius):
  fahrenheit = (celsius * 9) / 5 + 32
  return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

def celsius_para_kelvin(celsius):
  kelvin = celsius + 273.15
  return kelvin

def kelvin_para_celsius(kelvin):
  celsius = kelvin - 273.15
  return celsius

def fahrenheit_para_kelvin(fahrenheit):
  kelvin = (fahrenheit + 459.67) * 5 / 9
  return kelvin

def kelvin_para_fahrenheit(kelvin):
  fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
  return fahrenheit


print('''
    [1] Distância
    [2] Temperatura
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
    elif start == '2':  # Opção Temperatura
        print('''
        [1] Celsius para Fahrenheit
        [2] Fahrenheit para Celsius
        [3] Celsius para Kelvin
        [4] Kelvin para Celsius
        [5] Fahrenheit para Kelvin
        [6] Kelvin para Fahrenheit
        ''')
        opcao_temperatura = input('Qual conversão você deseja? ').upper().strip() [0]
        print('=-' * 30)

        if opcao_temperatura == '1':  # Celsius para Fahrenheit
            medida_celsius = float(input('Digite a temperatura em Celsius: '))
            resultado_fahrenheit = celsius_para_fahrenheit (medida_celsius)
            print(f'{medida_celsius}°C equivalem a {resultado_fahrenheit:.2f}°F')

        if opcao_temperatura == "2": #Fahrenheit para Celsius
            medida_fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
            resultado_celsius = fahrenheit_para_celsius(medida_fahrenheit)
            print(f'{medida_fahrenheit:.2f}°F equivalem a {resultado_celsius:.2f}°C')

        elif opcao_temperatura == '3':  # Celsius para Kelvin
            medida_celsius = float(input('Digite a temperatura em Celsius: '))
            resultado_kelvin = celsius_para_kelvin(medida_celsius)
            print(f'{medida_celsius}°C equivalem a {resultado_kelvin:.2f}K')

        elif opcao_temperatura == '3':  # Celsius para Kelvin
            medida_celsius = float(input('Digite a temperatura em Celsius: '))
            resultado_kelvin = celsius_para_kelvin(medida_celsius)
            print(f'{medida_celsius}°C equivalem a {resultado_kelvin:.2f}K')

        elif opcao_temperatura == '4':  # Kelvin para Celsius
            medida_kelvin = float(input('Digite a temperatura em Kelvin: '))
            resultado_celsius = kelvin_para_celsius(medida_kelvin)
            print(f'{medida_kelvin:.2f}K equivalem a {resultado_celsius:.2f}°C')

        elif opcao_temperatura == '5':
          medida_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
          resultado_kelvin = fahrenheit_para_kelvin(medida_fahrenheit)
          print(f'{medida_fahrenheit:.2f}°F equivalem a {resultado_kelvin:.2f}K')

        elif opcao_temperatura == '6':  # Kelvin para Fahrenheit
          medida_kelvin = float(input('Digite a temperatura em Kelvin: '))
          resultado_fahrenheit = kelvin_para_fahrenheit(medida_kelvin)
          print(f'{medida_kelvin:.2f}K equivalem a {resultado_fahrenheit:.2f}°F')

    else:
        ("Opçaõ inválida")
