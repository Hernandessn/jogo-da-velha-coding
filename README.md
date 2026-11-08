# Jogo da Velha 3x3 (terminal)

Trabalho da 2ª avaliação de Coding, UNINASSAU. Escrito em Python 3, sem funções, sem bibliotecas e sem listas fora da matriz.

## Como executar

Na pasta do projeto, rode: `python jogo_da_velha.py`

## Menu

1 - Jogar | 2 - Ver regras | 3 - Ver placar | 4 - Sair (mostra as estatísticas da sessão)

## Regras

- Dois jogadores (X e O) alternam jogadas em um tabuleiro 3x3.
- Informe linha e coluna (1 a 3) de uma casa vazia.
- Vence quem completar linha, coluna ou diagonal. Tabuleiro cheio sem vencedor é empate.
- Entradas inválidas (letra, campo vazio, número fora de 1 a 3 ou casa ocupada) mostram uma mensagem e o jogo pede a jogada de novo.
- Série melhor de 3 ou 5: vence quem chegar primeiro à maioria das vitórias. Empate não conta ponto na série. Quem começa alterna a cada partida.

## Desafios escolhidos

1. Campeonato "melhor de N": opção 1 do menu, laço `while serie_x < vitorias_necessarias and serie_o < vitorias_necessarias`.
2. Estatísticas da sessão: atualizadas no bloco "Fim da partida: atualizo placar e estatisticas" e exibidas na opção 4 (total de partidas, vitórias e empates, porcentagem de vitórias e maior sequência de vitórias de cada jogador). Um empate interrompe a sequência.

## Divisão de tarefas

- Hernandes: matriz, exibição do tabuleiro, leitura com validação, integração da partida no menu e alternância de quem começa.
- Rony: vitória e empate por laços, alternância de vez, atualização do placar e estatísticas da sessão.
- Natan: menu, regras, opção de ver placar, reinício da matriz, série melhor de N e campeão, README.

## Links

- Vídeo: [https://youtu.be/oJs9pqzRMOk](https://youtu.be/oJs9pqzRMOk)
