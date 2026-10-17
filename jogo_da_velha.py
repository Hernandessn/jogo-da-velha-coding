# =====================================================
# Jogo da Velha 3x3 - Coding (UNINASSAU)
# Integrantes: Hernandes, Rony, Natan
# Desafios: Campeonato "melhor de N" + Estatisticas da sessao
# Restricoes: sem def, import, append, try/except, listas 1D
# =====================================================

# ---------- 1. TABULEIRO (matriz 3x3 declarada por extenso) ----------
# tab[i][j]: i = linha (0 a 2), j = coluna (0 a 2). " " = casa vazia
tab = [[" ", " ", " "],
       [" ", " ", " "],
       [" ", " ", " "]]

# ---------- 2. PLACAR E ESTATISTICAS (variaveis) ----------
# (Natan e Rony declaram aqui os contadores)

# ---------- 3. MENU PRINCIPAL ----------
# (Natan: while com opcoes jogar, regras, placar, sair)

# ---------- 4. PARTIDA ----------
# 4.0 Variaveis de controle da partida (Hernandes)
vez_x = True          # booleano: True = vez do X, False = vez do O
simbolo = "X"         # texto: simbolo do jogador atual
jogadas = 0           # inteiro: jogadas feitas na partida
linha_escolhida = 0   # indice 0 a 2 da linha jogada
coluna_escolhida = 0  # indice 0 a 2 da coluna jogada

# 4.1 Reinicio da matriz com for aninhado   (Natan)
# 4.2 Exibicao do tabuleiro com for aninhado (Hernandes)
# 4.3 Leitura da jogada com validacao        (Hernandes)

# 4.4 Vitoria e empate por lacos             (Rony)
# Comeco assumindo que ninguem ganhou ainda
venceu = False       
# Vejo as 3 linhas do tabuleiro, uma de cada vez
for i in range(3):   
    # Se as 3 casas da linha i tem o simbolo do jogador, ele ganhou
    if tab[i][0] == simbolo and tab[i][1] == simbolo and tab[i][2] == simbolo:
        venceu = True
     # Coluna i: aqui o i fica na segunda posicao, e a linha varia de 0 a 2
    if tab[0][i] == simbolo and tab[1][i] == simbolo and tab[2][i] == simbolo:
        venceu = True  

# ---------- 5. ESTATISTICAS DA SESSAO (ao sair) ----------
# (Rony: total, porcentagens e maior sequencia)