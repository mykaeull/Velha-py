import random

def tabuleiro():
    print('+---+---+---+')
    print('| 1 | 2 | 3 |')
    print('+---+---+---+')
    print('| 4 | 5 | 6 |')
    print('+---+---+---+')
    print('| 7 | 8 | 9 |')
    print('+---+---+---+')

def verificar(posicoes):
    # Verifica se o jogo terminou e quem é o vencedor ou verifica se o jogo terminou em empate
    # 0 para empate / 1 para player vencedor / 2 para vencedor NPC
    global peca
    global pecaNPC
    for i in range(0, 9, 3):
        if posicoes[i] == peca and posicoes[i+1] == peca and posicoes[i+2] == peca:
            return 1
        elif posicoes[i] == pecaNPC and posicoes[i+1] == pecaNPC and posicoes[i+2] == pecaNPC:
            return 2
    for i in range(0, 3):
        if posicoes[i] == peca and posicoes[i+3] == peca and posicoes[i+6] == peca:
            return 1
        elif posicoes[i] == pecaNPC and posicoes[i+3] == pecaNPC and posicoes[i+6] == pecaNPC:
            return 2
    if posicoes[0] == peca and posicoes[4] == peca and posicoes[8] == peca:
        return 1
    elif posicoes[0] == pecaNPC and posicoes[4] == pecaNPC and posicoes[8] == pecaNPC:
        return 2
    if posicoes[2] == peca and posicoes[4] == peca and posicoes[6] == peca:
        return 1
    elif posicoes[2] == pecaNPC and posicoes[4] == pecaNPC and posicoes[6] == pecaNPC:
        return 2
    if  posicoes[0] != ' ' and posicoes[1] != ' ' and posicoes[2] != ' ' and posicoes[3] != ' ' and posicoes[4] != ' ' and posicoes[5] != ' ' and posicoes[6] != ' ' and posicoes[7] != ' ' and posicoes[8] != ' ':
        return 0

posicoesTabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('+———————————————————————————————————————————+')
print('|               JOGO DA VELHA               |')
print('+———————————————————————————————————————————+')
print('')
peca = str(input('Escolha a peça com a qual deseja jogar[X/O]: ')).upper()
while peca != 'X' and peca != 'O':
    print('[*] Escolha inválida...')
    peca = str(input('Escolha a peça com a qual deseja jogar[X/O]: ')).upper()

if peca == 'X':
    pecaNPC = 'O'
elif peca == 'O':
    pecaNPC = 'X'

# Posições válidas de jogadas
posicoesValidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Mostra o tabuleiro e suas possíveis posições de jogadas
tabuleiro()

while True:
    # Jogada do player
    jogadaPlayer = int(input('Escolha a posição que deseja marcar: '))
    while jogadaPlayer not in posicoesValidas:
        print('[*] Posição inválida...')
        jogadaPlayer = int(input('Escolha a posição que deseja marcar: '))
    jogadaPlayer -= 1
    while posicoesTabuleiro[jogadaPlayer] != ' ':
        print('[*] Posição já preenchida...')
        jogadaPlayer = int(input('Escolha a posição que deseja marcar: '))
        while jogadaPlayer not in posicoesValidas:
            print('[*] Posição inválida...')
            jogadaPlayer = int(input('Escolha a posição que deseja marcar: '))
        jogadaPlayer -= 1
    posicoesTabuleiro[jogadaPlayer] = peca
    print("""
    +---+---+---+
    | {} | {} | {} |
    +---+---+---+
    | {} | {} | {} |
    +---+---+---+
    | {} | {} | {} |
    +---+---+---+""".format(posicoesTabuleiro[0], posicoesTabuleiro[1], posicoesTabuleiro[2],
                            posicoesTabuleiro[3], posicoesTabuleiro[4], posicoesTabuleiro[5],
                            posicoesTabuleiro[6], posicoesTabuleiro[7], posicoesTabuleiro[8]))

    # Verifica a cada rodada do jogador player se há algum vencedor e quem é este
    vencedor = verificar(posicoesTabuleiro)
    if vencedor == 1:
        print("Você venceu!")
        break
    elif vencedor == 2:
        print('Você perdeu!')
        break
    elif vencedor == 0:
        print('Empate!')
        break

    # Jogada NPC
    jogadaNPC = random.randint(0, 8)
    while posicoesTabuleiro[jogadaNPC] != ' ':
        jogadaNPC = random.randint(0, 8)
    posicoesTabuleiro[jogadaNPC] = pecaNPC
    print("""
    +---+---+---+
    | {} | {} | {} |
    +---+---+---+
    | {} | {} | {} |
    +---+---+---+
    | {} | {} | {} |
    +---+---+---+""".format(posicoesTabuleiro[0], posicoesTabuleiro[1], posicoesTabuleiro[2],
                            posicoesTabuleiro[3], posicoesTabuleiro[4], posicoesTabuleiro[5],
                            posicoesTabuleiro[6], posicoesTabuleiro[7], posicoesTabuleiro[8]))

    # Verifica a cada rodada do jogador NPC se há algum vencedor e quem é este
    vencedor = verificar(posicoesTabuleiro)
    if vencedor == 1:
        print("Você venceu!")
        break
    elif vencedor == 2:
        print('Você perdeu!')
        break
    elif vencedor == 0:
        print('Empate!')
        break







