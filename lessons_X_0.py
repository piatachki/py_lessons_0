# Константы / настройки
# Размерность карты
dimension = 3
# Значение пустой клетки
placeholder = ' '


# Инициализация объекта поля для новой игры
def init_field():
    field = []
    for i in range(dimension):
        row = placeholder * dimension
        field.append(row)
    return field


# Вывод карты на экран
def print_field(field):
    print("")
    print("   1 2 3")
    for i in field:
        print(f" - {i[0]} {i[1]} {i[2]} ")
    print("")


# Метод получения координат от пользователя, валидации и записи в поле
def input_coords(play_side):
    user_input = ''
    while not validate_user_input(user_input):
        user_input = input(f"Ход {play_side}: введите координаты x y")
    return parse_user_input(user_input)


# Метод валидации строки пользовательского ввода
def validate_user_input(user_input):
    user_input_list = str.split(user_input)
    return len(user_input_list) == 2 and \
           str.isdigit(user_input_list[0]) and \
           str.isdigit(user_input_list[1]) and \
           0 < int(user_input_list[0]) <= dimension and \
           0 < int(user_input_list[1]) <= dimension


# Метод парсинга пользовательского воода
def parse_user_input(user_input):
    user_input_list = str.split(user_input)
    return int(user_input_list[0]), int(user_input_list[1])


global_field = init_field()
print(input_coords('X'))
# print_field(global_field)
