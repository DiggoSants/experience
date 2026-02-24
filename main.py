import json
import os
import tkinter as tk

# SYSTEM
jogador = {
    "nome": "Heroi",
    "nivel": 1,
    "hp": 100,
    "ouro": 50
}

def SAVE_GAME():
    with open("save.json","w",indent=4) as f:
        json.dump(jogador,f)

def LOAD_GAME():
    global jogador
    if os.path.exists("save.json"):
        with open("save.json","r") as f:
            jogador = json.load(f)

SAVE_GAME()
print("Jogo salvo com sucesso!")