# SPRINT 01

#Bibliotecas
import math

# Exibe uma mensagem de boas-vindas ao usuário
print('*' * 60)
print('* SEJA BEM-VINDO A MEGA CALCULADORA DA FÓRMULA E EM PYTHON *')
print('*' * 60)

# Função para validar a entrada do usuário
def validar_input(tipo, mensagem):
    while True:
        entrada = input(mensagem)  # Solicita a entrada do usuário
        if tipo == 'nome':  # Se o tipo for 'nome'
            if entrada.strip() == '':  # Verifica se o nome está vazio
                print("O nome não pode ser vazio. Por favor, tente novamente.")
            else:
                return entrada  # Retorna o nome válido
        elif tipo == 'numero':  # Se o tipo for 'numero'
            try:
                valor = float(entrada)  # Converte a entrada para float
                if valor == 0:  # Verifica se o número é zero
                    print("O número não pode ser zero. Por favor, tente novamente.")
                else:
                    return valor  # Retorna o número válido
            except ValueError:  # Captura erro de conversão para float
                print("Entrada inválida. Por favor, digite um número.")

# Função para exibir o menu de opções
def exibir_menu():
    print('1 - Calcular o tempo médio das voltas dos pilotos')
    print('2 - Calcular a velocidade média do piloto em cada volta')
    print('3 - Calcular o número de voltas de uma pista')
    print('4 - Sair')
    try:
        opcao = int(input('Digite a opção desejada: '))  # Solicita a opção do usuário
    except ValueError:
        print('Opção inválida! Por favor, digite um número.')
        exibir_menu()
        return

    # Seleciona a opção do usuário usando a estrutura 'match'
    match opcao:
        case 1:
            print('----- Calculadora de Tempo Médio do Corredor -----')
            calc_media_tempo_corredor()  # Chama a função para calcular a média de tempo do corredor
        case 2:
            print('2 - Calcular a velocidade média do piloto em cada volta')
            calc_velocidade_media()  # Chama a função para calcular a velocidade média
        case 3:
            print('3 - Calcular o número de voltas de uma pista')
            calc_voltas_corrida()  # Chama a função para calcular o número de voltas
        case 4:
            print('Saindo do programa...')
            return  # Encerra o programa
        case _:
            print('Opção indisponível! Digite uma opção válida: ')
            exibir_menu()  # Exibe o menu novamente

# Função para voltar ao menu principal
def voltar_ao_menu():
    opcao = input('Deseja voltar ao menu principal? (s/n): ').strip().lower()
    if opcao == 's':
        exibir_menu()  # Chama o menu principal novamente
    else:
        print('Saindo do programa...')
        return  # Encerra o programa

# Função para converter tempo de segundos para minutos e segundos
def converter_segundos(media_tempo):
    minutos = int(media_tempo // 60)
    segundos = int(media_tempo % 60)
    print(f'{minutos}m{segundos}s')  # Exibe o tempo convertido

# Função para calcular a média de tempo das voltas dos corredores
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
    voltar_ao_menu()  # Pergunta se o usuário deseja voltar ao menu

# Função para calcular a velocidade média dos corredores
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
    
    array.sort(key=lambda x: x[2], reverse=True)
    print('=' * 60)
    cont = 1
    for n in array:
        print(f'{cont}. Corredor: {n[0]} | Volta: {n[1]} | Velocidade Média: {n[2]:.2f} km/h')
        cont += 1
    print('=' * 60)
    voltar_ao_menu()  # Pergunta se o usuário deseja voltar ao menu

# Função para calcular o número de voltas de uma corrida
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
    voltar_ao_menu()  # Pergunta se o usuário deseja voltar ao menu

# Inicializa o programa exibindo o menu principal
exibir_menu()
