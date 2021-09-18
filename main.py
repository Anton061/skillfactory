def privetstvie():
    print('Добро пожаловать в игру "Крестики-нолики" ')
    global player_1
    player_1 = input("Введите имя первого игрока: ")
    print("Приветствую, {player_1}, ты играешь крестиками ")
    global player_2
    player_2 = input("Введите имя второго игрока: ")
    print("Приветствую, {player_2}, ты играешь ноликами ")
    print("Для того, чтобы походить, введите координаты ячейки ")
    print("Номер строки, номер столбца")


privetstvie()

field = [[" "] * 3 for i in range(3)]


def create_field():
    print('\n  |  0  |  1  |  2  |')
    print('---------------------')
    for i in range(len(field)):
        print(str(i) + " |  " + "  |  ".join(field[i]) + "  |  ")

        print("---------------------")


def hod():
    while True:
        hod = input("Ваш ход, сначала строки, затем столбцы: ").split()
        if len(hod) != 2:
            print("Введите две координаты через пробел! ")
            continue
        x, y = map(int, hod)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введенные координаты выходят за пределы поля! ')
            continue
        if field[x][y] != " ":
            print("Клетка занята, введи другие координаты ")
            continue
        break
    return x, y


def win_check():
    win_coord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for coord in win_coord:
        marks = []
        for c in coord:
            marks.append(field[c[0]][c[1]])
        if marks == ["X", "X", "X"]:
            create_field()
            print(f"Поздравляю, {player_1}, ты победил! ")
            return True
        if marks == ["0", "0", "0"]:
            create_field()
            print(f"Поздравляю, {player_2}, ты победил! ")
            return True
    return False


count = 0
while True:
    count += 1
    create_field()

    if not count % 2 == 0:
        print("Ход крестиками ")
    else:
        print("Ход ноликами ")

    x, y = hod()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        break

    if count == 9:
        print("Ничья ")
        break