# Константы / настройки
# Размерность карты
import itertools

dimension = 3
# Значение пустой клетки
placeholder = ' '


# Инициализация объекта поля для новой игры
def init_field():
    field = []
    for i in range(dimension):
        row = [placeholder] * dimension
        field.append(row)
    return field


# Вывод карты на экран
# ToDo сделать независимым от размера поля
def print_field(field):
    print("")
    print("   1 2 3")
    for i in field:
        print(f" idx {i[0]} {i[1]} {i[2]} ")
    print("")


# Метод получения координат от пользователя, валидации и записи в поле
def input_coords(play_side):
    user_input = ''
    while not validate_user_input(user_input):
        user_input = input(f"Ход {play_side}: введите координаты: x y\n")
    return parse_user_input(user_input)


# Метод валидации строки пользовательского ввода
def validate_user_input(user_input):
    user_input_list = str.split(user_input)
    return len(user_input_list) == 2 and \
           str.isdigit(user_input_list[0]) and \
           str.isdigit(user_input_list[1]) and \
           0 < int(user_input_list[0]) <= dimension and \
           0 < int(user_input_list[1]) <= dimension


# Метод проверки, что планируемая к заполнению ячейка не занята
def validate_field_place(examine_coords):
    return global_field[examine_coords[0]][examine_coords[1]] == placeholder


# Метод парсинга пользовательского воода
def parse_user_input(user_input):
    user_input_list = str.split(user_input)
    return int(user_input_list[0]) - 1, int(user_input_list[1]) - 1


# Метод проверки того, что кортеж полон и
# полностью заполнен символом одного из игроков
def check_tuple_win(*args):
    distinct_args = set(args)
    return len(args) == dimension and \
           len(distinct_args) == 1 and \
           placeholder not in distinct_args


# Генератор для определения очередности ходов
def get_play_side():
    side_sequence = 'X0'
    for play_side in itertools.cycle(side_sequence):
        yield play_side


# Точка входа
global_field = init_field()
for side in get_play_side():
    coords = input_coords(side)
    while not validate_field_place(coords):
        print(f"Координаты { coords[0] } { coords[1] } уже заняты. Нужно бы повторить ход")
        coords = input_coords(side)
    global_field[coords[0]][coords[1]] = side
    print_field(global_field)
