import json
import os

primeira_vez = True  # flag para controlar se é a primeira vez

def saveGame():
    with open("save.json","w") as f:
        json.dump(jogador,f,indent=4)

def loadGame():
    global jogador
    if os.path.exists("save.json"):
        with open("save.json","r") as f:
            jogador = json.load(f)

def deleteSave():
    if os.path.exists("save.json"):
        os.remove("save.json")
        print("Salvamento excluído com sucesso.")
    else:
        print("Nenhum salvamento encontrado.")

def checkFirstTime(): #verifica se é a primeira vez que o jogador está jogando
    global primeira_vez
    if primeira_vez:
        print("Bem-vindo ao jogo!")  # primeira vez
        primeira_vez = False
    else:
        print("Bem-vindo de volta!")  # nas próximas vezes


def showCredits(): #mostra os créditos do jogo
    print("Créditos do Jogo:")
    print("Desenvolvedor: DiggoSants")
    print("Versão: 1.0")
    print("Obrigado por jogar!")
    print("1 - voltar")

    select = input("Ação: ")
    if select == "1":
        startGame()
    else:
        print("Opção inválida. Tente novamente.")
        showCredits()

def customizeCharacter():
    print("Customizando seu personagem...")
    print("1 - Alterar nome")
    print("2 - Voltar")

    select = input("Ação: ")
    if select == "1":
        if jogador["nivel"] < 5:
            print("Você precisa ser nível 5 para alterar o nome do personagem.")
            customizeCharacter()
        else:
            nome = input("Digite o novo nome do personagem: ")
            jogador["nome"] = nome
            saveGame()
            print(f"Nome alterado para {nome}!")
            startGame()

    elif select == "2":
        print("Voltando...")
        startGame()

def startRound():
    print("Iniciando nova rodada...")
    # Lógica da rodada aqui

def endGame():
    print("Fim de jogo! Obrigado por jogar.")
    exit()
    

def startGame():
    loadGame()  # Carrega o jogo salvo, se existir
    checkFirstTime() #verifica se é a primeira vez
    while True:

        print("1 - Começar")
        print("2 - Customizar")
        print("3 - Créditos")
        print("4 - Fechar")

        select = input("Ação: ")
        if select == "1":
            startRound()
        elif select == "2":
            print("Carregando...")
            customizeCharacter()
        elif select == "3":
            print("Carregando...")
            showCredits()
        elif select == "4":
            print("Carregando...")
            endGame()
        else:
            print("Opção inválida. Tente novamente.")

# Início do jogo
startGame()