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
# 4.1 Reinicio da matriz com for aninhado   (Natan)
# 4.2 Exibicao do tabuleiro com for aninhado (Voce)
# 4.3 Leitura da jogada com validacao        (Voce)
# 4.4 Vitoria e empate por lacos             (Rony)

# ---------- 5. ESTATISTICAS DA SESSAO (ao sair) ----------
# (Rony: total, porcentagens e maior sequencia)