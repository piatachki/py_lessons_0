# Константы / настройки
x_dimension = 3
y_dimension = 3


# Инициализация объекта поля для новой игры
def init_field():
    row = [' '] * x_dimension
    field = [row.copy(), row.copy(), row.copy()]
    return field


# Вывод карты на экран
def print_field(field):
    print("")
    print("   1 2 3")
    for i in field:
        print(f" - { i[0] } { i[1] } { i[2] } ")
    print("")


# Функция получения координат от пользователя, валидации и записи в поле
def input_coords(field, play_side):
    user_input = list(map(int, str.split(input(f"Ход {play_side}: введите координаты x y"))))
    y, x = user_input[0], user_input[1]
    if x <= len(field) and y <= len(field[0]) and field[x-1][y-1] == ' ':
        field[x-1][y-1] = play_side


field = init_field()
input_coords(field, 'X')
print_field(field)
