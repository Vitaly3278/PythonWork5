# Создайте программу для игры в ""Крестики-нолики"".

print('-------- Игра КРЕСТИКИ НОЛИКИ----------\n')


def board():
    for i in range(3):
        print('|', i * 3 + 1, '|', i * 3 + 2, '|', i * 3 + 3, '|')

board()
player = 1
move2 =None
player1 = []
player2 = []


def move(player):
    x = int(input(f' Игрок {player} выберите свободную ячейку'))
    return x


def win(player):
    win == ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for i in win:
        if player[i[0]] == player[i[1]] == player[i[2]]:
            return True


while True:
    for player in range(1, 3):
        move = move(player)
        player1.append(move)
        print(f'Игрок {player} вы поставили Х на {move} ячейке')
        win = win(player1)
        if win == True:
            print(f'Поздравляем игрок {player} вы выиграли!!!')
            exit()
    else:
        move = move(player)
        player2.append(move)
        print(f'Игрок {player+1} вы поставили 0 на {move} ячейке')
        win = win(player2)
        if win == True:
            print(f'Поздравляем игрок {player}б вы выиграли!!!')
            exit()


