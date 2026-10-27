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

# Estatisticas da sessao (Rony)
total_partidas = 0
seq_x = 0
seq_o = 0
maior_seq_x = 0
maior_seq_o = 0

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
        # ---------- 4. PARTIDA ----------
        # 4.0 Variaveis de controle da partida (Hernandes)
        vez_x = True          # booleano: True = vez do X, False = vez do O
        simbolo = "X"         # texto: simbolo do jogador atual
        jogadas = 0           # inteiro: jogadas feitas na partida
        linha_escolhida = 0   # indice 0 a 2 da linha jogada
        coluna_escolhida = 0  # indice 0 a 2 da coluna jogada
        fim_partida = False   # booleano: vira True quando alguem vence ou da empate

        # 4.1 Reinicio da matriz com for aninhado   (Natan)
        for i in range(3):
            for j in range(3):
                tab[i][j] = " "
        melhor_de = 0
        while melhor_de == 0:
            escolha = input("Serie melhor de 3 ou melhor de 5? (3 ou 5): ")
            if escolha == "3":
                melhor_de = 3
            elif escolha == "5":
                melhor_de = 5
            else:
                print("Entrada invalida! Digite 3 ou 5.")
        vitorias_necessarias = melhor_de // 2 + 1   # 2 na de 3, 3 na de 5

        # Repete exibicao, leitura e checagem de vitoria ate a partida acabar
        while fim_partida == False:
            # 4.2 Exibicao do tabuleiro com for aninhado (Hernandes)
            # Cabecalho com os numeros das colunas, para o jogador se orientar
            print("     1   2   3")
            # Laco de fora: i percorre as LINHAS da matriz (0, 1 e 2)
            for i in range(3):
                # Comeca o texto da linha com o numero dela (i + 1, pois o jogador conta a partir de 1)
                texto_linha = " " + str(i + 1) + "  "
                # Laco de dentro: para cada linha i, j percorre as COLUNAS (0, 1 e 2).
                # tab[i][j] e o conteudo da casa na linha i, coluna j
                for j in range(3):
                    texto_linha = texto_linha + " " + tab[i][j] + " "
                    # Barra vertical so ENTRE as casas, nao depois da ultima coluna
                    if j < 2:
                        texto_linha = texto_linha + "|"
                # Passadas as 3 colunas, imprime a linha ja montada
                print(texto_linha)
                # Separador horizontal so ENTRE as linhas, nao depois da ultima
                if i < 2:
                    print("    ---+---+---")
            # 4.3 Leitura da jogada com validacao        (Hernandes)
            # Repete linha + coluna ate o jogador escolher uma casa livre
            casa_livre = False
            while casa_livre == False:
                # --- leitura da linha ---
                valida = False                              # so vira True com entrada "1", "2" ou "3"
                while valida == False:
                    entrada = input("Linha (1 a 3): ")      # entrada e texto
                    # k NAO e indice da matriz: e cada opcao que o jogador pode digitar (1, 2, 3).
                    # O for compara o texto digitado com str(k) para cada opcao
                    for k in range(1, 4):
                        if entrada == str(k):
                            valida = True
                            linha_escolhida = k - 1         # converte 1..3 para indice 0..2
                    if valida == False:
                        print("Entrada invalida! Digite um numero de 1 a 3.")

                # --- leitura da coluna ---
                valida = False                              # zera antes de ler a coluna, senao ela seria pulada
                while valida == False:
                    entrada = input("Coluna (1 a 3): ")
                    for k in range(1, 4):                   # mesma validacao da linha
                        if entrada == str(k):
                            valida = True
                            coluna_escolhida = k - 1
                    if valida == False:
                        print("Entrada invalida! Digite um numero de 1 a 3.")

                # --- casa livre ou ocupada ---
                if tab[linha_escolhida][coluna_escolhida] == " ":
                    casa_livre = True
                else:
                    print("Casa ocupada! Escolha outra posicao.")

            # grava o simbolo na casa escolhida e conta a jogada
            tab[linha_escolhida][coluna_escolhida] = simbolo
            jogadas = jogadas + 1
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

            # Conto quantas casas ainda estao vazias
            # Comeco supondo que nao ha nenhuma casa vazia
            vazias = 0
            # Percorro as 3 linhas do tabuleiro
            for i in range(3):
                # Para cada linha i, olho as 3 colunas j
                # Em cada linha, percorro as 3 colunas
                for j in range(3):
                    # Se a casa esta vazia, somo 1 no contador
                    if tab[i][j] == " ":
                        vazias = vazias + 1
            # Se alguem venceu ou o tabuleiro encheu, a partida acaba
            if venceu == True or vazias == 0:
                fim_partida = True
            else:
                # O jogo continua: passo a vez para o outro jogador
                # Inverto a vez: True vira False e False vira True
                vez_x = not vez_x
                # Atualizo o simbolo de acordo com a vez
                if vez_x == True:
                    simbolo = "X"
                else:
                    simbolo = "O"

        # Resultado: mostro o tabuleiro final e quem venceu (ou empate)
        # Mesmo bloco 4.2, copiado para depois do while
        print("     1   2   3")
        for i in range(3):
            texto_linha = " " + str(i + 1) + "  "
            for j in range(3):
                texto_linha = texto_linha + " " + tab[i][j] + " "
                if j < 2:
                    texto_linha = texto_linha + "|"
            print(texto_linha)
            if i < 2:
                print("    ---+---+---")
        if venceu == True:
            print("O jogador", simbolo, "venceu!")
        else:
            print("Deu empate!")

        # Fim da partida: atualizo as estatisticas
        if venceu == True or vazias == 0:
            total_partidas = total_partidas + 1
            if venceu == True and simbolo == "X":
                seq_x = seq_x + 1
                seq_o = 0
                if seq_x > maior_seq_x:
                    maior_seq_x = seq_x
            elif venceu == True and simbolo == "O":
                seq_o = seq_o + 1
                seq_x = 0
                if seq_o > maior_seq_o:
                    maior_seq_o = seq_o
            else:
                seq_x = 0
                seq_o = 0
    elif opcao == "2":
        print("- Dois jogadores (X e O) alternam jogadas em um tabuleiro 3x3.")
        print("- Informe linha e coluna (1 a 3) de uma casa vazia.")
        print("- Vence quem completar linha, coluna ou diagonal.")
        print("- Tabuleiro cheio sem vencedor: empate.")
    elif opcao == "3":
        print("PLACAR -> X:", vit_x, "| O:", vit_o, "| Empates:", empates)
    elif opcao == "4":
        sair = True
        # Ao sair, mostro as estatisticas da sessao
        if total_partidas > 0:
            # Porcentagem de vitorias de X com uma casa decimal (sem usar round)
            pct_x = int(vit_x / total_partidas * 1000 + 0.5) / 10
            print("Porcentagem de vitorias de X:", str(pct_x) + "%")
        else:
            print("Nenhuma partida jogada.")
        print("Maior sequencia de X:", maior_seq_x)
    else:
        print("Opcao invalida! Digite 1, 2, 3 ou 4.")


# ---------- 5. ESTATISTICAS DA SESSAO (ao sair) ----------
# (Rony: total, porcentagens e maior sequencia)