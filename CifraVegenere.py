alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÉÊÍÓÔÕÚÇ0123456789abcdefghijklmnopqrstuvwxyzáàâãéêíóôõúç!@#$%&*?., ' # alfabeto estendido com letras e numeros
tamanhoAlfa = len(alfabeto) # Calcula o tamanho do alfabeto
limiteMens = 128 # Limite de caracteres para a mensagem

def cifra(mensagem, chave, modo):
    mensFinal = "" # variavel para resultado
    chaveM = chave.upper() #variavel para chave maiuscula
    contChave = 0 #contador para a posicao da chave
    for letra in mensagem: # percorre a mensagem
        if letra in alfabeto:
            locLetra = alfabeto.find(letra) # variavel para a posicao da letra
            locChaveCorreta = chaveM[contChave % len(chaveM)] # variavel para localizar a letra correta

            if locChaveCorreta in alfabeto: # verifica se a letra da chave esta no alfabeto
                locChave = alfabeto.find(locChaveCorreta) # variavel para posicao da chave

                if modo == 'a': #criptografar
                    newLoc = (locLetra + locChave) % tamanhoAlfa
                elif modo == 'b': # descriptografar
                    newLoc = (locLetra - locChave + tamanhoAlfa) % tamanhoAlfa
                mensFinal += alfabeto[newLoc] # acessa o caractere pela posicao
                contChave += 1
            else: # se nao tiver a letra no alfabeto, vai manter a letra original do texto
                mensFinal += letra
        else: # mantem tudo que nao esta no alfabeto conforme a mensagem original informada
            mensFinal += letra
    return mensFinal

def verificarMens(mensagemUser):
    if len(mensagemUser) > limiteMens: # verifica se a mensagem tem o limite pre definido
        print(f'\nPor favor, digite ate {limiteMens} caracteres.')
        return False
    else:
        return True

def salvarMensagemCriptografada(mensCriptografada):
    try:
        with open('mensagem_criptografada.txt', 'w') as file: # cria o arquivo de texto com a mensagem criptografada
            file.write(mensCriptografada)
        print("Mensagem criptografada salva no arquivo 'mensagem_criptografada.txt'")
    except Exception as e:
        print(f'Erro: {e}')

while True: # painel de acesso pelo usuario
    print('\n-------------CIFRA DE VIGENERE-------------')
    print('\n1 - Criptografar')
    print('2 - Descriptografar')
    print('3 - sair')
    opcao = input('\nInforme uma das opcoes: ')

    if opcao == '1':
        mensEntrada = input('Informe uma mensagem: ')
        if verificarMens(mensEntrada):
            chaveEntrada = 'unip'
            resultado = cifra(mensEntrada, chaveEntrada, 'a')
            print(f'Mensagem criptografada: {resultado}')
            salvarMensagemCriptografada(resultado)
    elif opcao == '2':
        mensEntrada = input('Informe a mensagem criptografada: ')
        if verificarMens(mensEntrada):
            chaveEntrada = 'unip'
            resultado = cifra(mensEntrada, chaveEntrada, 'b')
            print(f'Mensagem descriptografada: {resultado}')
    elif opcao == '3':
        print('Encerrando...')
        break
    else:
        print('Opcao invalida! Informe entre 1 e 3.')