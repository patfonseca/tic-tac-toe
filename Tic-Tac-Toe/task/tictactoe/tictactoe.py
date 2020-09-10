def print_field(array):
    print('---------')
    for n in range(3):
        row = '| '
        for m in range(3):
            row = row + array[n][m] + ' '
        print(row + '|')
    print('---------')


def evaluate_game(array):
    win_x = 0
    win_o = 0
    play_x = 0
    play_o = 0

    for n in range(3):
        for m in range(3):
            if array[n][m] == 'X':
                play_x += 1
            elif array[n][m] == 'O':
                play_o += 1

    if array[0][0] == array[0][1] == array[0][2] == 'X':  # rows
        win_x += 1
    if array[1][0] == array[1][1] == array[1][2] == 'X':
        win_x += 1
    if array[2][0] == array[2][1] == array[2][2] == 'X':
        win_x += 1
    if array[0][0] == array[1][0] == array[2][0] == 'X':  # columns
        win_x += 1
    if array[0][1] == array[1][1] == array[2][1] == 'X':
        win_x += 1
    if array[0][2] == array[1][2] == array[2][2] == 'X':
        win_x += 1
    if array[0][0] == array[1][1] == array[2][2] == 'X':  # diagonals
        win_x += 1
    if array[0][2] == array[1][1] == array[2][0] == 'X':
        win_x += 1

    if array[0][0] == array[0][1] == array[0][2] == 'O':  # rows
        win_o += 1
    if array[1][0] == array[1][1] == array[1][2] == 'O':
        win_o += 1
    if array[2][0] == array[2][1] == array[2][2] == 'O':
        win_o += 1
    if array[0][0] == array[1][0] == array[2][0] == 'O':  # columns
        win_o += 1
    if array[0][1] == array[1][1] == array[2][1] == 'O':
        win_o += 1
    if array[0][2] == array[1][2] == array[2][2] == 'O':
        win_o += 1
    if array[0][0] == array[1][1] == array[2][2] == 'O':  # diagonals
        win_o += 1
    if array[0][2] == array[1][1] == array[2][0] == 'O':
        win_o += 1

    if win_x == 1 and win_o == 0:
        return 'x'
    elif win_x == 0 and win_o == 1:
        return 'o'
    elif win_x + win_o > 1 or abs(play_x - play_o) > 1:
        return 'i'
    elif play_x + play_o == 9:
        return 'd'
    else:
        return ''


field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

cells = '         '
result = ''
turn = 'x'

i = 0
for n in range(3):
    for m in range(3):
        field[n][m] = cells[i]
        i += 1

print_field(field)

while True:  # evaluate game

    while turn == 'x':  # Player X
        choice = input('Enter the coordinates:').split()
        try:
            if int(choice[0]) < 1 or int(choice[0]) > 3 or int(choice[1]) < 1 or int(choice[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            else:
                column = int(choice[0]) - 1
                row = 3 - int(choice[1])
                if field[row][column] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    field[row][column] = 'X'
                    turn = 'o'
        except:
            print('You should enter numbers!')

    print_field(field)
    result = evaluate_game(field)
    if result != '':
        break

    while turn == 'o':  # Player O
        choice = input('Enter the coordinates:').split()
        try:
            if int(choice[0]) < 1 or int(choice[0]) > 3 or int(choice[1]) < 1 or int(choice[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            else:
                column = int(choice[0]) - 1
                row = 3 - int(choice[1])
                if field[row][column] in ['X', 'O']:
                    print('This cell is occupied! Choose another one!')
                else:
                    field[row][column] = 'O'
                    turn = 'x'
        except:
            print('You should enter numbers!')

    print_field(field)
    result = evaluate_game(field)
    if result != '':
        break

if result == 'x':
    print('X wins')
elif result == 'o':
    print('O wins')
elif result == 'i':
    print('Impossible')
elif result == 'd':
    print('Draw')
