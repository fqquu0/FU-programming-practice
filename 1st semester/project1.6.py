field = []
for i in range(10):
    string = '-'*10
    field.append(string)
print('\n'.join(field))
moves = 0
print('При выборе уже занятой клетки, игроку засчитывается пропуск хода. Приятной игры!')
def move(moves):
    if moves % 2 == 0:
        print('Сейчас ход игрока номер 1')
    else:
        print('Сейчас ход игрока номер 2')
    s = input('Введите номер строки, в которой хотите сделать ход:')
    while not s.isdigit() or int(s) < 1 or int(s) > 10:
        print('Номер строки должен быть числом от 1 до 10')
        s = input('Введите номер строки, в котором хотите сделать ход:')
    s = int(s) - 1
    c = input('Введите номер столбца, в котором хотите сделать ход:')
    while not c.isdigit() or int(c) < 1 or int(c) > 10:
        print('Номер строки должен быть числом от 1 до 10')
        c = input('Введите номер столбца, в котором хотите сделать ход:')
    c = int(c) - 1
    symbol = '1'
    field[s] = list(field[s])
    field[s].pop(c)
    field[s].insert(c, symbol)
    field[s] = ''.join(field[s])
    print('\n'.join(field))


def check_horizontal():
    count = 0
    for q in range(len(field)):
        for w in range(len(field[q])-3):
            if field[q][w] == field[q][w+1] == field[q][w+2] and not field[q][w] =='-':
                count +=1
    if count> 0:
        return False
    else:
        return True
def check_vertical():
    count = 0
    for q in range(len(field)-3):
        for w in range(len(field[q])):
            if field[q][w] == field[q+1][w]==field[q+2][w] and not field[q][w] =='-':
                count += 1
    if count>0:
        return False
    else:
        return True
def check_diagonal():
    count = 0
    for q in range(len(field)-3):
        for w in range(len(field[q])-3):
            if field[q][w] == field[q+1][w+1] == field[q+2][w+2] and not field[q][w] =='-':
                count += 1
    for q in range(len(field)-3):
        for w in range(len(field[q])-3):
            if field[q][w] == field[q+1][w-1] == field[q+2][w-2] and not field[q][w] =='-':
                count += 1
    if count>0:
        return False
    else:
        return True

a = True
b = True
c = True
while a == True and b == True and c == True:
    move(moves)
    moves +=1
    a = check_horizontal()
    b = check_vertical()
    c = check_diagonal()
else:
    if moves % 2 == 0:
        print('Игрок номер 2 програл')
    else:
        print('Игрок номер 1 проиграл')
    print('Спасибо за игру!')



