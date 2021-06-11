import itertools

# Константы / настройки

# Размерность карты
dimension = 3
# Значение пустой клетки
placeholder = ' '


def init_field():
    """Инициализация объекта поля для новой игры"""
    field = []
    for i in range(dimension):
        row = [placeholder] * dimension
        field.append(row)
    return field


def print_field(field):
    """Вывод карты на экран"""
    print("")
    for i in range(dimension):
        print(field[i])
    print("")


def input_coords(play_side):
    """Метод получения координат от пользователя, валидации"""
    user_input = ''
    while not validate_user_input(user_input):
        user_input = input(f"Ход {play_side}: введите координаты: x y\n")
    return parse_user_input(user_input)


def validate_user_input(user_input):
    """Метод валидации строки пользовательского ввода"""
    user_input_list = str.split(user_input)
    return len(user_input_list) == 2 and \
           str.isdigit(user_input_list[0]) and \
           str.isdigit(user_input_list[1]) and \
           0 < int(user_input_list[0]) <= dimension and \
           0 < int(user_input_list[1]) <= dimension


def validate_field_place(field, examine_coords):
    """Метод проверки, что планируемая к заполнению ячейка не занята"""
    return field[examine_coords[0]][examine_coords[1]] == placeholder


def parse_user_input(user_input):
    """Метод парсинга пользовательского воода"""
    user_input_list = str.split(user_input)
    return int(user_input_list[0]) - 1, int(user_input_list[1]) - 1


def check_tuple_win(args):
    """Метод проверки того, что кортеж полон и
    полностью заполнен символом одного из игроков"""
    distinct_args = set(args)
    return len(args) == dimension and \
           len(distinct_args) == 1 and \
           placeholder not in distinct_args


def parse_filed_for_win_check(field):
    """Парсим поле и проверяем каждый вариант на победу
    строки, столбцы, две диагонали"""
    is_win = False
    slash = ''
    back_slash = ''
    for i in range(dimension):
        slash += field[i][i]
        back_slash += field[i][dimension - 1 - i]
        if check_tuple_win(list(field[i])):
            is_win = True
        column = ''
        for j in range(dimension):
            column += field[j][i]
        if check_tuple_win(list(column)):
            is_win = True
    if check_tuple_win(slash) or check_tuple_win(back_slash):
        is_win = True
    return is_win


def get_play_side():
    """Генератор для определения очередности ходов"""
    side_sequence = 'X0'
    for play_side in itertools.cycle(side_sequence):
        yield play_side


def game_cycle():
    """Основной цикл игры"""
    field = init_field()
    print(f"Крестики-нолики. Игра на поле { dimension }x{ dimension }")
    for side in get_play_side():
        coords = input_coords(side)
        while not validate_field_place(field, coords):
            print(f"Координаты { coords[0] } { coords[1] } уже заняты. Нужно бы повторить ход")
            coords = input_coords(side)
        field[coords[0]][coords[1]] = side
        print_field(field)
        if parse_filed_for_win_check(field):
            print(f"Конец истории. Победил { side }")
            break


game_cycle()
