cript, dcript, texto, textoScript, criptografia, descriptografia, chave, opcao = '','','','','','','','';
totalCharactere = 0
subs = dict()


print('\n\n', '_' * 80, '\n\n                    PROGRAMA DE CRIPTOGRAFIA/descriptografia') # Titulo inicial

# Modulo com MENU para guiar o usuário e selecionar sua opção.
def selecione(opcao):
    print('\n','_' * 80, '\n\n    MENU:\n\n   1 - Criptografar\n   2 - Descriptografar\n   3 - Sair \n\n', ('_') * 80)
    opcao = input('\n Selecione uma opção:\n\n >>> ')
    print('\n', '_' * 80)

    while opcao != '1' and opcao != '2' and opcao!='3':     # Enquanto a opção for diferente de 1, 2 e 3, solicitará a opção novamente.
        opcao = input('\n Opção inválida. Selecione uma opção:\n\n >>> ')
        print('\n', '_' * 80,)

    if opcao == '1':     # Opção 1 chamará o modulo para leitura e criptografia do texto, e criação da chave criptografica, para ao fim gravar o texto criptografado em um arquivo

        cripto(texto, cript)

    elif opcao == '2':     # Opção 2 chamará o modulo para leitura da chave criptografica e descriptografia do texto através da leitura do arquivo

        descript(dcript, descriptografia,totalCharactere, chave)

    elif opcao == '3': # Opção 3 encerrará o programa
        print('\n                           <<< PROGRAMA ENCERRADO >>>\n',('_')*80)
        exit()

# Modulo para criptografia do texto
def cripto(texto, cript):

    texto = input('\n\n Insira um texto a ser CRIPTOGRAFADO de até 128 caracteres:\n\n  >>> ')
    while len(texto) <= 0 or len(texto) >= 129:
        print(('_') * 80)
        texto = input('\n\n Insira um texto a ser CRIPTOGRAFADO de até 128 caracteres:\n\n  >>> ')

    # DECLARAÇÃO DE VARIÁVEIS
    substituicao = ''
    textoScript = ''
    textoScript = texto.strip()
    totalCharactere = len(textoScript)
    
    chave = totalCharactere * 2357 # A chave criptografica é igual a multiplicação do total de caracteres do texto por 2357, aleatóriamente escolhido


    # DUPLA criptografia: Primeiramente embaralha os caracteres e em seguida os substitui por outros caracteres

    # Primeira criptografia: EMBARALHAMENTO
    for C in range(totalCharactere):
        cript = textoScript[1::2] + textoScript[0::2]

    # Segunda criptografia: SUBSTITUIÇÃO
    subs ={'a': '%', 'b': '$', 'c': '9', 'd': '&', 'e': '(', 'f': ')', 'g': '*', 'h': '+', 'i': '-', 'j': '/', 'k': '<','l': '>', 'm': '@', 'n': '[', 'o': ' ', 'p': ']', 'q': '_', 'r': '{', 's': '|', 't': '}', 'u': '5', 'v': '÷','w': '°', 'x': '¨', 'z': '!', 'A': ':', 'B': '.', 'C': ',', 'D': ';', 'E': '?', 'F': '^', 'G': '`', 'H': '~','I': '¯', 'J': '´', 'K': '‘', 'L': '’', 'M': '“', 'N': '”', 'O': '„', 'P': 'ˆ', 'Q': '˜', 'R': 'â', 'S': 'à','T': 'á', 'U': 'Á', 'V': 'Â', 'W': 'À', 'X': 'ã', 'Y': 'Ã', 'Z': 'é', ' ': 'ê', '0': 'è', '1': 'É', '2': 'Ê','3': 'È', '4': 'ì', '5': 'í', '6': 'Í', '7': 'Ì', '8': 'ô', '9': 'ò', 'â': 't', 'à': 'u', 'á': 'v', 'Á': 'w','Â': 'x', 'À': 'y', 'ã': 'z', 'Ã': 'm', 'é': 'n', 'ê': 'o', 'è': 'p', 'É': 'q', 'Ê': 'r', 'È': 's', 'ì': 'a','í': 'b', 'Í': 'c', 'Ì': 'd', 'ô': 'e', 'ò': 'f', 'ó': 'g', 'Ô': 'h', 'Ó': 'i', 'Ò': 'j', 'õ': 'k', 'Õ': 'l','ü': 'A', 'û': 'B', 'ù': 'C', 'Ü': 'D', 'ú': 'E', 'Ú': 'F', 'Û': 'G', 'Ù': 'H', 'Ç': 'I', 'ç': 'J', 'ñ': 'K','Ñ': 'L', '!': 'ó', ',': 'Ô', '.': 'Ó', ':': 'Ò', ';': 'õ', '?': 'Õ', '^': 'ü', '`': 'û', '~': 'ù', '¯': 'Ü','´': 'ú', '‘': 'Ú', '’': 'Û', '“': 'Ù', '”': 'Ç', '„': 'ç', 'ˆ': 'ñ', '˜': 'Ñ', '{': 'M', '$': 'N', '%': 'O','&': 'P', '(': 'Q', ')': 'R', '*': 'S', '+': 'T', '-': 'U', '/': 'V', '<': 'W', '>': 'X', '@': 'Y', '[': 'Z',']': '0', '_': '1', 'y': '2', '|': '3', '}': '4', '÷': '6', '°': '7', '¨': '8'}
    c=int
    for c in range(totalCharactere):
        if cript[c] in subs :
            substituicao = substituicao + subs [cript[c]]

    # Exibição do texto CRIPTOGRAFADO
    print('\n Texto criptografado: ', substituicao)

    # Gravação do texto criptografado em um arquivo
    criptografia = open('Texto criptografado.txt','w')
    criptografia.write(substituicao)
    criptografia.close()

    # Exibiçao da mensagem sobre salvamento do arquivo e a chave criptografica para o usuário
    print('\n Texto criptografado salvo em arquivo: Texto criptografado.txt','\n\n Sua chave para descriptografia é: ', chave)
    

# DECLARAÇÃO DE VARIÁVEIS
L = len(cript)
M = L // 2
D = M

# Modulo para leitura do arquivo criptografado e descriptografia deste arquivo
def descript(dcript, descriptografia, totalCharactere, chave):
    # Leitura do arquivo
    # Tratamento de erro para que, caso o usuario tente selecionar para descriptografar sem houver um arquivo criptografado, irá retornar ao menu
    try:
        Dcript_ARQ = open('Texto criptografado.txt','r')
        descriptografia = descriptografia + Dcript_ARQ.readline()
    except:
        print('\n Primeiramente, insira um texto CRIPTOGRAFADO!')
        opcao
    else:


        # DECLARAÇÃO DE VARIÁVEIS
        substituicao = ''
        totalCharactere = len(descriptografia)
        L = len(descriptografia)
        M = L // 2
        D = M

        # Solicitação da chave criptografica para  a descriptografia
        for CONT in range(0,1):
            chave = input('\n\n Insira a chave para descriptografar: \n\n >>> ')
            if chave != str(totalCharactere * 2357):
                print('\n','_'*80)
                print('\n Chave inválida! ULTIMA TENTATIVA! \n','_'*80)
                chave = input('\n Insira a chave para descriptografar: \n\n >>> ')
                if chave != str(totalCharactere * 2357):
                    break
            
            # DUPLA descriptografia: Primeiramente irá reverter a substituição de caracteres, para que assim desembaralhe o texto

            # Descriptografia: SUBSTITUIÇÃO
            subs  = {'8': '¨', '7': '°', '6': '÷', '4': '}', '3': '|', '2': 'y', '1': '_', '0': ']', 'Z': '[', 'Y': '@',
                    'X': '>', 'W': '<', 'V': '/', 'U': '-', 'T': '+', 'S': '*', 'R': ')', 'Q': '(', 'P': '&', 'O': '%',
                    'N': '$', 'M': '{', 'Ñ': '˜', 'ñ': 'ˆ', 'ç': '„', 'Ç': '”', 'Ù': '“', 'Û': '’', 'Ú': '‘', 'ú': '´',
                    'Ü': '¯', 'ù': '~', 'û': '`', 'ü': '^', 'Õ': '?', 'õ': ';', 'Ò': ':', 'Ó': '.', 'Ô': ',', 'ó': '!',
                    'L': 'Ñ', 'K': 'ñ', 'J': 'ç', 'I': 'Ç', 'H': 'Ù', 'G': 'Û', 'F': 'Ú', 'E': 'ú', 'D': 'Ü', 'C': 'ù',
                    'B': 'û', 'A': 'ü', 'l': 'Õ', 'k': 'õ', 'j': 'Ò', 'i': 'Ó', 'h': 'Ô', 'g': 'ó', 'f': 'ò', 'e': 'ô',
                    'd': 'Ì', 'c': 'Í', 'b': 'í', 'a': 'ì', 's': 'È', 'r': 'Ê', 'q': 'É', 'p': 'è', 'o': 'ê', 'n': 'é',
                    'm': 'Ã', 'z': 'ã', 'y': 'À', 'x': 'Â', 'w': 'Á', 'v': 'á', 'u': 'à', 't': 'â', 'ò': '9', 'ô': '8',
                    'Ì': '7', 'Í': '6', 'í': '5', 'ì': '4', 'È': '3', 'Ê': '2', 'É': '1', 'è': '0', 'ê': ' ', 'é': 'Z',
                    'Ã': 'Y', 'ã': 'X', 'À': 'W', 'Â': 'V', 'Á': 'U', 'á': 'T', 'à': 'S', 'â': 'R', '˜': 'Q', 'ˆ': 'P',
                    '„': 'O', '”': 'N', '“': 'M', '’': 'L', '‘': 'K', '´': 'J', '¯': 'I', '~': 'H', '`': 'G', '^': 'F',
                    '?': 'E', ';': 'D', ',': 'C', '.': 'B', ':': 'A', '!': 'z', '¨': 'x', '°': 'w', '÷': 'v', '5': 'u',
                    '}': 't', '|': 's', '{': 'r', '_': 'q', ']': 'p', ' ': 'o', '[': 'n', '@': 'm', '>': 'l', '<': 'k',
                    '/': 'j', '-': 'i', '+': 'h', '*': 'g', ')': 'f', '(': 'e', '&': 'd', '9': 'c', '$': 'b', '%': 'a'}
            c = int
            for c in range(totalCharactere):
                if descriptografia[c] in subs :
                    substituicao = substituicao + subs [descriptografia[c]]



            # Descriptografia: DESEMBARALHAMENTO

            # Caso o total de caracteres do texto seja IMPAR
            if totalCharactere % 2 != 0:
                for A in range(M + 1):
                    if len(dcript) == L:
                        break
                    dcript = dcript + substituicao[D]
                    if len(dcript) == L:
                        break
                    dcript = dcript + substituicao[A]
                    D = D + 1
                    if len(dcript) == L:
                        break
                print('\n Texto descriptografado: ', dcript)

            # Caso o total de caracteres do texto seja PAR
            elif totalCharactere % 2 == 0:
                for A in range(M):
                    dcript = dcript + substituicao[D]
                    dcript = dcript + substituicao[A]
                    D = D + 1
                print('\n Texto descriptografado: ', dcript)
        return dcript

# Looping infinito para solicitação da opção do usuário, que poderá ser parado caso o usuário escolha a opção sair
while True:
    selecione(opcao)
