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
vit_x = 0
vit_o = 0
empates = 0

# ---------- 3. MENU PRINCIPAL ----------
sair = False
while sair == False:
    print("")
    print("===== JOGO DA VELHA =====")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")


    if opcao == "1":
        print("(partida entra aqui)")
    elif opcao == "2":
        print("- Dois jogadores (X e O) alternam jogadas em um tabuleiro 3x3.")
        print("- Informe linha e coluna (1 a 3) de uma casa vazia.")
        print("- Vence quem completar linha, coluna ou diagonal.")
        print("- Tabuleiro cheio sem vencedor: empate.")
    elif opcao == "3":
        print("PLACAR -> X:", vit_x, "| O:", vit_o, "| Empates:", empates)
    elif opcao == "4":
        sair = True
    else:
        print("Opcao invalida! Digite 1, 2, 3 ou 4.")


# ---------- 4. PARTIDA ----------
# 4.0 Variaveis de controle da partida (Hernandes)
vez_x = True          # booleano: True = vez do X, False = vez do O
simbolo = "X"         # texto: simbolo do jogador atual
jogadas = 0           # inteiro: jogadas feitas na partida
linha_escolhida = 0   # indice 0 a 2 da linha jogada
coluna_escolhida = 0  # indice 0 a 2 da coluna jogada

# 4.1 Reinicio da matriz com for aninhado   (Natan)
# 4.2 Exibicao do tabuleiro com for aninhado (Hernandes)
print("     1   2   3")
for i in range(3):                      # i percorre as linhas
    texto_linha = " " + str(i + 1) + "  "
    for j in range(3):                  # j percorre as colunas da linha i
        texto_linha = texto_linha + " " + tab[i][j] + " "
        if j < 2:
            texto_linha = texto_linha + "|"
    print(texto_linha)
    if i < 2:
        print("    ---+---+---")
# 4.3 Leitura da jogada com validacao        (Hernandes)
valida = False
while valida == False:
    entrada = input("Linha (1 a 3): ")      # entrada e texto
    for k in range(1, 4):                   # opcoes validas: "1", "2", "3"
        if entrada == str(k):
            valida = True
            linha_escolhida = k - 1         # indice da matriz
    if valida == False:
        print("Entrada invalida! Digite um numero de 1 a 3.")
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

# Conto quantas casas de cada diagonal sao do jogador
cont_principal = 0
cont_secundaria = 0
for i in range(3):
    # Diagonal principal: linha e coluna iguais
    if tab[i][i] == simbolo:
        cont_principal = cont_principal + 1
    # Diagonal secundaria: a coluna e 2 menos a linha
    if tab[i][2 - i] == simbolo:
        cont_secundaria = cont_secundaria + 1
# Se alguma diagonal tem as 3 casas, o jogador ganhou
if cont_principal == 3 or cont_secundaria == 3:
    venceu = True 

# ---------- 5. ESTATISTICAS DA SESSAO (ao sair) ----------
# (Rony: total, porcentagens e maior sequencia)