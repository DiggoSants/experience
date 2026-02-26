import json
import os

primeira_vez = True
jogador = None
inimigo = None

def saveGame():
    dados = {
        "jogador": jogador,
        "inimigo": inimigo
    }
    with open("save.json", "w") as f:
        json.dump(dados, f, indent=4)

def loadGame():
    global jogador, inimigo
    if os.path.exists("save.json"):
        with open("save.json", "r") as f:
            dados = json.load(f)
        jogador = dados["jogador"]
        inimigo = dados["inimigo"]
    else:
        # valores padrão caso não exista save.json
        jogador = {"nome": "Player", "nivel": 1, "hp": 50, "ouro": 0}
        inimigo = {"nome": "Goblin", "nivel": 2, "hp": 10}

def deleteSave():
    if os.path.exists("save.json"):
        os.remove("save.json")
        print("Salvamento excluído com sucesso.")
    else:
        print("Nenhum salvamento encontrado.")

def checkFirstTime():
    global primeira_vez
    if primeira_vez:
        print("Bem-vindo ao jogo!")
        primeira_vez = False
    else:
        print("Bem-vindo de volta!")

def showCredits():
    while True:
        print("Créditos do Jogo:")
        print("Desenvolvedor: DiggoSants")
        print("Versão: 1.0")
        print("Obrigado por jogar!")
        print("1 - voltar")

        select = input("Ação: ").strip()
        if select == "1":
            start()  # volta ao menu principal
            break
        else:
            print("Opção inválida. Tente novamente.")

def customizeCharacter():
    while True:
        print("Customizando seu personagem...")
        print("1 - Alterar nome")
        print("2 - Voltar")

        select = input("Ação: ").strip()
        if select == "1":
            if jogador["nivel"] < 5:
                print("Você precisa ser nível 5 para alterar o nome do personagem.")
            else:
                nome = input("Digite o novo nome do personagem: ").strip()
                if nome:
                    jogador["nome"] = nome
                    saveGame()
                    print(f"Nome alterado para {nome}!")
                    start()  # volta o principal
                    break
                else:
                    print("Nome inválido. Tente novamente.")
        elif select == "2":
            return  # volta ao menu principal

def startRound():
    print("Iniciando nova rodada...")
    # Lógica da rodada aqui

def endGame():
    print("Fim de jogo! Obrigado por jogar.")
    exit()

def start():
    loadGame()
    checkFirstTime()
    while True:
        print("1 - Começar")
        print("2 - Customizar")
        print("3 - Créditos")
        print("4 - Fechar")

        select = input("Ação: ").strip()
        if select == "1":
            startRound()
            break
        elif select == "2":
            customizeCharacter()
            break
        elif select == "3":
            showCredits()
            break
        elif select == "4":
            endGame()
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do jogo
start()