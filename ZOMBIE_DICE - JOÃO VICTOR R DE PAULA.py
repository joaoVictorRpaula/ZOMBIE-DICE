'''
Pontifícia Universidade Católica do Paraná.
- Análise e desenvolvimento de sistemas.
Raciocínio computacional.
Olá, meu nome é João Victor Ribeiro de Paula.
Este é o projeto FINALIZADO da semana 8 do jogo "Zombie Dice".
A fase atual neste arquivo contém o jogo funcional estruturado de acordo com o solicitado.
'''

import random
import time
#Declarando as listas e dicionários usados.
jogador = dict()
jogadores = list()
placar = list()

#Função de INTRODUÇÃO na qual cadastra a quantidade e nome dos jogadores.
def introducao():
    quantPlayer=int()
    #Ao longo do código o try/except é sempre usado para algum caso quando o input ou a linha de código der algum erro.
    try:
        print('\033[1m'+"----------------INICIO----------------\n\n"+'\033[0;0m')
        quantPlayer = int(input("Quantos jogadores serão?\n(mínimo 2)\n"))
        #Se quantidade de jogadores menor que 2, repetirá o campo acima.
        if quantPlayer<2:
            print("\nQuantidade de jogadores insuficiente.")
            quantPlayer = 0
            introducao()
    except:
        print("Valor INCORRETO")
        introducao()
    #Laço para guardar o nome de cada jogador.
    for i  in range (quantPlayer):
        jogador.clear()
        jogador["nome"]=(input(f"Nome {str(i + 1)}° jogador:\n"))
        jogadores.append(jogador.copy())

#Função na qual retorna um manual de como jogar
def manual():
    print("Este jogo inclui estas regras, 13 dados e um tubo para guardá-los.\nO jogador que comer 13 cerebros primeiro VENCE!\nDois ou mais jogadores podem jogar")
    print("\nNo seu turno rode 3 dados.\nCada um deles representa uma pobre vítima a ser atacada.\nOs dados vermelhos são os mais difíceis.\nOs verdes são os mais fáceis\nOs amarelos são médios.\n")
    print("Os dados possuem 3 faces\nCEREBROS\nPEGADAS\nTIROS\n")
    print("Cérebro – Você devorou o cérebro de sua vítima.\nTIROS - Sua vítima revidou!")
    print("PEGADAS - Sua vítima escapou.Se você escolher rolar dados novamente, você vai re-rolar esses dados, juntamente com novos dados suficientes para rolar sempre 3 dados\n")
    print("Se você tiver 3 dados com a face da Espingarda virada para cima na mesa, em qualquer momento, seu turno acabou. Caso contrário, você pode optar por parar e marcar pontos ou continuar\n")
    print("VENCE QUEM DEVORAR 13 CERÉBROS PRIMEIRO!!\n\n")
    print("BOA SORTE!!\n\n")
    input("Para volta ao menu aperte ENTER")
    print("\n" * 130)
    menu()

#Função MENU, está é a primeira tela o qual aparece para o usuário com 2 opções, INICIAR O JOGO ou LER MANUAL
def menu():
    print('\033[1m'+"\n----------------Bem vindo ao Zombie Dice----------------\n"+'\033[0;0m')
    escolha=input("1 - Iniciar jogo\n2 - Ler manual\n")
    #Caso deseja iniciar, chamará  a função de INTRODUÇÃO.
    if escolha == '1':
        print("\n"*130)
        introducao()
    elif escolha == '2':
        print("\n" * 130)
        manual()
    else:
        print("\n" * 130)
        print("Opção inválida")
        menu()

#Função que reseta os dados do copo.
def resetCopo ():
    dados = [verde,verde,verde,verde,verde,verde,amarelo,amarelo,amarelo,amarelo,vermelho,vermelho,vermelho]
    return dados

#Definição das cores e faces de cada dado por uma tupla.
verde = ('C','P','C','T','P','C')
amarelo = ('T','P','C','T','P','C')
vermelho = ('T','P','T','C','P','T')
dados = (resetCopo())

#Função que sorteia a cor do dado
def colorSort():
    dadosrandom = random.choice(dados)
    return dadosrandom

#Função que remove o dado sorteado do copo
def removeCopo(colorSort):
    dados.remove(colorSort)

#Função que mostra a cor do dado sorteado
def showColor(colorSort):
    if colorSort == (verde):
        return('\033[32m'+"VERDE: "+'\033[0;0m')
    if colorSort == (amarelo):
        return('\033[33m'"AMARELO: "+'\033[0;0m')
    if colorSort == (vermelho):
        return('\033[31m'+"VERMELHO: "+'\033[0;0m')

#Função que retorna um input "PRESSIONE ENTER PARA JOGAR"
def pergunta ():
    resposta = input('pressione ENTER para JOGAR\n')
    return resposta


# Função que retorna a cor do dado
def corDado(colorP):
    if colorP == ('C', 'P', 'C', 'T', 'P', 'C'):
        corDado = 'VERDE'
        return corDado
    elif colorP == ('T', 'P', 'C', 'T', 'P', 'C'):
        corDado = 'AMARELO'
        return corDado
    elif colorP == ('T', 'P', 'T', 'C', 'P', 'T'):
        corDado = 'VERMELHO'
        return corDado

#Função que mostra o copo com os dados atualizados naquele momento
def showDados(dados):
    copo = list()
    for dado in dados:
        copo.append(corDado(dado))
    print(f'O copo possui {len(copo)} DADOS\n{copo}')


#Função que "joga" UM dado
def jogarDado(colorSort):
    face= str()
    #cada 'if' tem a função de selecionar uma das faces e retornar como valor da função.
    if colorSort == verde:
        faceVerde = random.choice(verde)
        print(showColor(colorSort),faceVerde)
        face=faceVerde
    if colorSort == amarelo:
        faceAmarelo = random.choice(amarelo)
        print(showColor(colorSort),faceAmarelo)
        face = faceAmarelo
    if colorSort == vermelho:
        faceVermelho = random.choice(vermelho)
        print(showColor(colorSort),faceVermelho)
        face= faceVermelho
    #Se o dado NÃO for pegada, ele remove do copo o dado
    if face !=  "P":
        removeCopo(colorSort)
    return face

#Função "PRINCIPAL", dentro dela temos grande parte da lógica do jogo, é uma função com outras funções dentro dela.
def jogada(pont):
    cerebros = pont
    tiros = 0
    pegadas = 0

    #Função que aumenta a pontuação de cerebros, pegadas e tiros.
    def contador(dadoSort, cerebros, pegadas, tiros):
        if str(dadoSort) == "C":
            cerebros += 1
        if str(dadoSort) == "P":
            pegadas += 1
        if str(dadoSort) == "T":
            tiros += 1
        return cerebros, pegadas, tiros

    #Laço WHILE o qual "JOGA" 3 dados.
    while True:
        colorP = list()
        time.sleep(0.5)
        for q in range (0,3):
            color = colorSort()
            dadoSort = jogarDado(color)
            if dadoSort == 'P' :
                colorP.append(color)
            c = contador(dadoSort, cerebros, pegadas, tiros)

            cerebros = c[0]
            pegadas = c[1]
            tiros =  c[2]

        print()
        print('cerebros: ', cerebros)
        print('pegadas: ', pegadas)
        print('tiros: ', tiros)
        time.sleep(0.5)


        #Função que CHECKA quantidade de tiros, cerebros e pegadas
        def check(dados, cerebros, pegadas, tiros):
            if tiros > 2:
                print(f'\nVocê levou {tiros} tiros e acabou morrendo !!\n')
                print()
                return False
            elif cerebros >= 13:
                return cerebros, pegadas, tiros, True
            elif len(dados) < 3 and tiros>2:
                print(f'Você levou {tiros} tiros e acabou morrendo !!\n')
                return False
            elif len(dados) < 3:
                print("\nOS DADOS ACABARAM")
                return cerebros, pegadas, tiros, True
            elif tiros > 2:
                print(f'\nVocê levou {tiros} tiros e acabou morrendo !!\n')
                print()
                return False
            #Caso caia "PEGADA", aqui mostrará os dados que cairam como "PEGADA", dará opção de roda-los novamente
            #Caso escolha rodar, chamará a função CONTADOR e CHECK novamente.
            elif pegadas>0:
                print("\nVOCÊ TIROU UMA PEGADA O ZOMBIE ESCAPOU!!")
                cerebrosP = 0
                pegadasP= 0
                tirosP = 0
                pegadas = 0
                corDadoPasso = list()
                if len(corDadoPasso) >0:
                    for i in corDadoPasso:
                        corDadoPasso.remove(i)
                for p in (colorP):
                    corDadoPasso.append(corDado(p))
                print(f'OS ZUMBIS QUE ESCAPARAM FORAM {corDadoPasso}\n\n')
                while True:
                    print("\nDIGITE 'n' para PARAR de jogar, 'd' para ver os dados no COPO\nou")
                    resp = pergunta()
                    if len(dados) < 3:
                        print("\nOS DADOS ACABARAM")
                        return cerebros, pegadas, tiros, True
                    if resp == 'n':
                        return cerebros, pegadas, tiros, True
                    elif resp == 'd':
                        showDados(dados)
                        print()
                    elif resp == '':
                        break
                time.sleep(0.3)
                pegadasP = 0
                colorP2 = list()
                #para cada dado P, ele sorteia e joga novamente
                for p in (colorP):
                    time.sleep(0.3)
                    dadoSortP = jogarDado(p)
                    c = contador(dadoSortP, cerebros,pegadas,tiros)
                    cerebros = c[0]
                    pegadas = c[1]
                    tiros = c[2]
                    if dadoSortP == 'P':
                        colorP2.append(p)
                #para cada dado que não for P, ele sorteia um dado novo até fechar os 3 dados
                if len(colorP) < 3:
                    i = len(colorP)
                    while i < 3:
                        color = colorSort()
                        dadoSortP = jogarDado(color)
                        if dadoSortP == 'P':
                            colorP2.append(color)
                        time.sleep(0.2)
                        c = contador(dadoSortP, cerebros, pegadas, tiros)
                        cerebros = c[0]
                        pegadas = c[1]
                        tiros = c[2]
                        i+=1
                if len(corDadoPasso) > 0:
                    for a in range(len(corDadoPasso)):
                        corDadoPasso.pop(0)
                for j in range(len(colorP)):
                    colorP.pop(0)
                for p in (colorP2):
                    corDadoPasso.append(corDado(p))
                    colorP.append(p)
                time.sleep(0.3)
                print()
                print('cerebros: ', cerebros)
                print('pegadas: ', pegadas)
                print('tiros: ', tiros)
                checkP = check(dados ,cerebros, pegadas, tiros)
                try:
                    if checkP[3] == True:
                        cerebrosP = checkP[0]
                        return cerebrosP, pegadas, tiros, True
                except:
                    if type(checkP) != bool:
                        cerebrosP = checkP[0]
                        pegadasP = checkP[1]
                        tirosP = checkP[2]
                    elif checkP == True:
                        cerebrosP = checkP[0]
                        return cerebrosP, pegadas, tiros, True
                    elif checkP == False:
                        return False
                return (cerebrosP,pegadasP,tirosP)
            pegadas = 0
            return(cerebros, pegadas, tiros)
        check = check(dados, cerebros, pegadas, tiros)
        try:
            if check[3] == True:
                cerebros = check[0]
                return cerebros
            elif type(check) != bool:
                cerebros = check[0]
                pegadas = check[1]
                tiros = check[2]
            if check == True:
                return cerebros
            if check == False:
                return 0
        except:
            if type(check) != bool:
                cerebros = check[0]
                pegadas = check[1]
                tiros = check[2]
            elif check == True:
                return cerebros
            elif check == False:
                return 0
        print()
        # Pergunta se o jogador deseja jogar novamente, caso SIM ele repete tudo, caso NÃO, ele para a função e retorna CEREBROS.
        while True:
            print("\nDIGITE 'n' para PARAR de jogar, 'd' para ver os dados no COPO\nou")
            resp = pergunta()
            if resp == '':
                break
            elif resp == 'd':
                # Informação de DADOS no copo.
                showDados(dados)
                print()
            elif resp == 'n':
                return cerebros

#Função de PONTUAÇÃO, aqui mostra o PLACAR da partida.
def pontuacao():
    x = 0
    print('\033[1m'+"\n----------------PLACAR----------------\n"+'\033[0;0m')
    for j in jogadores:
        try:
            print(f'jogador {j["nome"]} cerebros: {placar[x]}')
            x +=1
        except:
            print(f'jogador {j["nome"]} cerebros: 0')


menu()

#Laço while que roda o TURNO de cada jogador até que algum VENÇA.
#Para cada JOGADOR[] na lista ele atribui o valor de cérebros no PLACAR[], ou seja o JOGADOR[0] possui o PLACAR[0] e assim por diante.
while True:
    pontuacao()
    i = 0
    for j in jogadores:
        placar.append(0)
        while True:
            print(f'\nJogador {j["nome"]}\n')
            resp = pergunta()
            print("\n"*130)
            if resp == '':
                break
        dados = resetCopo()
        print('\033[1m'+f'\n----------------JOGADOR {j["nome"]}----------------\n''\033[0;0m')
        placar[i] = (jogada(placar[i]))
        if placar[i] >=13 :
            print('\033[1m'+f'\n----------------PARABÉNS {j["nome"]}, VOCÊ DEVOROU 13 CEREBROS E VENCEU!!----------------\n\nO jogo acabou!!''\033[0;0m')
            break
        i +=1
    try:
        if placar[i] >= 13:
            print()
            pontuacao()
            break
    except:
        print()