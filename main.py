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

def SAVE_GAME():
    with open("save.json","w") as f:
        json.dump(jogador,f,indent=4)

def LOAD_GAME():
    global jogador
    if os.path.exists("save.json"):
        with open("save.json","r") as f:
            jogador = json.load(f)

SAVE_GAME()
print("Jogo salvo com sucesso!")

# Jogar
def menu_Principal():
    print("Bem-vindo ao jogo!")
    print("1 - Começar")
    print("2 - Customizar")
    print("3 - Créditos")
    print("4 - Sair")

    escolha = input("Ação: ")
    if escolha == "1":
        print("Iniciando o jogo...")
    elif escolha == "2":
        print("Customizando o personagem...")
    elif escolha == "3":
        print("Créditos do jogo...")
    elif escolha == "4":
        print("Saindo do jogo...")
    
menu_Principal()
