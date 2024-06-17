import math

print('*' * 60)
print('* SEJA BEM-VINDO A MEGA CALCULADORA DA FÓRMULA E EM PYTHON *')
print('*' * 60)

def validar_input(tipo, mensagem):
    while True:
        entrada = input(mensagem)
        if tipo == 'nome':
            if entrada.strip() == '':
                print("O nome não pode ser vazio. Por favor, tente novamente.")
            else:
                return entrada
        elif tipo == 'numero':
            try:
                valor = float(entrada)
                if valor == 0:
                    print("O número não pode ser zero. Por favor, tente novamente.")
                else:
                    return valor
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

def exibir_menu():
    print('1 - Calcular o tempo médio das voltas dos pilotos')
    print('2 - Calcular a velocidade média do piloto em cada volta')
    print('3 - Calcular o número de voltas de uma pista')
    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Opção inválida! Por favor, digite um número.')
        exibir_menu()
        return

    match opcao:
        case 1:
            print('----- Calculadora de Tempo Médio do Corredor -----')
            calc_media_tempo_corredor()
        case 2:
            print('----- Calculadora de Velocidade Média Do piloto -----')
            calc_velocidade_media()
        case 3:
            print('3 - Calculadora de Voltas da Pista')
            calc_voltas_corrida()
        case _:
            print('Opção indisponível! Digite uma opção válida: ')
            exibir_menu()

def converter_segundos(media_tempo):
    minutos = int(media_tempo // 60)
    segundos = int(media_tempo % 60)
    print(f'{minutos}m{segundos}s')

def calc_media_tempo_corredor():
    array = []
    numero_voltas = int(validar_input('numero', 'Digite o número de voltas da corrida: '))
    while True:
        nome_corredor = validar_input('nome', 'Nome do Corredor: ')
        soma_tempo = 0
        for i in range(numero_voltas):
            tempo_volta = validar_input('numero', f'Digite o tempo da {i + 1}ª volta (em segundos): ')
            soma_tempo += tempo_volta

        media_tempo = soma_tempo / numero_voltas
        print(f'Média de {nome_corredor}: {media_tempo:.2f} segundos')
        tupla = (nome_corredor, media_tempo)
        array.append(tupla)
        
        continuar = input('Deseja adicionar outro corredor? (s/n): ').strip().lower()
        if continuar != 's':
            break

    array.sort(key=lambda x: x[1])
    print('=' * 50)
    cont = 1
    for n in array:
        print(f'{cont}. Corredor: {n[0]} | Tempo: {n[1]:.2f} segundos')
        cont += 1
    print('=' * 50)

def calc_velocidade_media():
    array = []
    numero_voltas = int(validar_input('numero', 'Digite o número de voltas: '))
    dist_pista = int(validar_input('numero', 'Digite a distância da pista (em metros): '))
    while True:
        nome_corredor = validar_input('nome', 'Nome do Corredor: ')
        for i in range(numero_voltas):
            volta = i + 1
            tempo_volta = validar_input('numero', f'Digite o tempo da {volta}ª volta (em segundos): ')
            velocidade_media = dist_pista / tempo_volta
            velocidade_media_convertida = velocidade_media * 3.6
            tupla = (nome_corredor, volta, velocidade_media_convertida)
            array.append(tupla)
        
        continuar = input('Deseja adicionar outro corredor? (s/n): ').strip().lower()
        if continuar != 's':
            break
    
    array.sort(key=lambda x: x[2])
    print('=' * 60)
    cont = 1
    for n in array:
        print(f'{cont}. Corredor: {n[0]} | Volta: {n[1]} | Velocidade Média: {n[2]:.2f} km/h')
        cont += 1
    print('=' * 60)

def calc_voltas_corrida():
    dist_total = validar_input('numero', 'Digite a distância total da corrida (em km): ')
    comp_pista = validar_input('numero', 'Digite o comprimento da pista (em km): ')

    numero_voltas = dist_total / comp_pista
    resto = dist_total % comp_pista
    if resto != 0:
        voltas_totais = math.ceil(numero_voltas)
        numero_voltas_completas = dist_total // comp_pista
        dist_ultima_volta = dist_total - (numero_voltas_completas * comp_pista)
        print('=' * 50)
        print(f'Voltas totais = {voltas_totais}')
        print(f'Número de voltas completas da pista: {numero_voltas_completas}')
        print(f'A última volta será parcial de {dist_ultima_volta:.2f} km')
        print('=' * 50)
    else:
        print('=' * 50)
        print(f'Número de voltas da corrida =  {numero_voltas}')
        print('=' * 50)

exibir_menu()
