import random

# Função para inicializar um tabuleiro vazio
def criar_tabuleiro():
    return [[0] * 9 for _ in range(9)]

# Função para verificar se um número pode ser colocado em uma determinada célula
def numero_valido(tabuleiro, linha, coluna, numero):
    # Verificar se o número já está presente na linha ou coluna
    for i in range(9):
        if tabuleiro[linha][i] == numero or tabuleiro[i][coluna] == numero:
            return False

    # Verificar se o número já está presente no bloco 3x3
    bloco_linha = linha // 3
    bloco_coluna = coluna // 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[bloco_linha * 3 + i][bloco_coluna * 3 + j] == numero:
                return False

    return True

# Função para preencher o tabuleiro usando backtracking
def preencher_tabuleiro(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for numero in range(1, 10):
                    if numero_valido(tabuleiro, linha, coluna, numero):
                        tabuleiro[linha][coluna] = numero
                        if preencher_tabuleiro(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                return False
    return True

# Função para gerar um jogo de Sudoku aleatório
def gerar_jogo_sudoku():
    tabuleiro = criar_tabuleiro()
    preencher_tabuleiro(tabuleiro)
    return tabuleiro

# Função para exibir o tabuleiro de Sudoku
def exibir_tabuleiro(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            print(tabuleiro[linha][coluna], end=" ")
            if coluna == 2 or coluna == 5:
                print("|", end=" ")
        print()
        if linha == 2 or linha == 5:
            print("-" * 22)

# Função para verificar se o jogador venceu o jogo
def verificar_vitoria(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return False
    return True

# Função para obter uma dica
def obter_dica(tabuleiro):
    while True:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if tabuleiro[linha][coluna] == 0:
            return linha, coluna

# Função principal do jogo
def jogar_sudoku():
    jogo = gerar_jogo_sudoku()
    exibir_tabuleiro(jogo)

    while not verificar_vitoria(jogo):
        linha_jogada = int(input("Digite a linha da célula que deseja preencher (0-8): "))
        coluna_jogada = int(input("Digite a coluna da célula que deseja preencher (0-8): "))

        if jogo[linha_jogada][coluna_jogada] != 0:
            print("Essa célula já está preenchida. Tente novamente.")
            continue

        jogada = int(input("Digite o número que deseja inserir (1-9): "))

        if not numero_valido(jogo, linha_jogada, coluna_jogada, jogada):
            print("Número inválido. Tente novamente.")
            continue

        jogo[linha_jogada][coluna_jogada] = jogada
        exibir_tabuleiro(jogo)

        dica = input("Deseja obter uma dica? (S/N): ")
        if dica.upper() == "S":
            linha_dica, coluna_dica = obter_dica(jogo)
            print(f"Dica: Coloque o número {jogo[linha_dica][coluna_dica]} na linha {linha_dica} e coluna {coluna_dica}.")

    print("Parabéns! Você venceu o jogo!")

# Iniciar o jogo
jogar_sudoku()
