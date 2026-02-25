import json
import os
import tkinter as tk

# SYSTEM
jogador = {
    "nome": "Diggo",
    "nivel": 1,
    "hp": 100,
    "ouro": 0
}

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

def showCredits():
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

def startRound():
    print("Iniciando nova rodada...")
    # Lógica da rodada aqui
    jogador

# Jogar
def startGame():
    print("Bem-vindo ao jogo!")
    print("1 - Começar")
    print("2 - Customizar")
    print("3 - Créditos")
    print("4 - Fechar")

    select = input("Ação: ")
    if select == "1":
        startRound()

    elif select == "2":
        print("Customizando o personagem...")
        # customizeCharacter()
    elif select == "3":
        print("Carregando os créditos do jogo...")
        showCredits()

    elif select == "4":
        print("Saindo do jogo...")
        endGame()
    else:
        print("Opção inválida. Tente novamente.")
        startGame()

def endGame():
    print("Fim de jogo! Obrigado por jogar.")
    exit()



startGame()