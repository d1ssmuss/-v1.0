import tkinter as tk
from PIL import Image, ImageTk

# Создаем основное окно
root = tk.Tk()
root.title("Шашки")
root.geometry('%dx%d+%d+%d' % (800, 800, 520, 130))
root.resizable(False, False)

board = [
    [None, 'b', None, 'b', None, 'b', None, 'b'],
    ['b', None, 'b', None, 'b', None, 'b', None],
    [None, 'b', None, 'b', None, 'b', None, 'b'],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ['w', None, 'w', None, 'w', None, 'w', None],
    [None, 'w', None, 'w', None, 'w', None, 'w'],
    ['w', None, 'w', None, 'w', None, 'w', None]
]

# Создаем Canvas для отображения доски
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

# Загружаем изображение доски
board_image = Image.open("Board.jpg")
board_photo = ImageTk.PhotoImage(board_image)

# Отображаем изображение на Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=board_photo)

# Размер клетки
cell_size = 100

# Загружаем изображения шашек
white_checker_image = Image.open("white-regular.png")
black_checker_image = Image.open("black-regular.png")
white_queen_image = Image.open("white-queen.png")
black_queen_image = Image.open("black-queen.png")
# Словарь для хранения шашек и их позиций
checkers = {}
# Изменяем размер изображений шашек, чтобы они соответствовали размеру клетки
white_checker_image = white_checker_image.resize((cell_size, cell_size), Image.LANCZOS)
black_checker_image = black_checker_image.resize((cell_size, cell_size), Image.LANCZOS)

white_checker_photo = ImageTk.PhotoImage(white_checker_image)
black_checker_photo = ImageTk.PhotoImage(black_checker_image)

# Размещаем шашки на доске
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 1:  # Проверяем, что клетка чёрная
            if row >= 5:
                # Размещаем белые шашки в верхних трёх рядах
                checker  = canvas.create_image(col * cell_size, row * cell_size, anchor=tk.NW, image=white_checker_photo)
                checkers[checker] = (col, row)
            elif row < 3:
                # Размещаем чёрные шашки в нижних трёх рядах
                checker  = canvas.create_image(col * cell_size, row * cell_size, anchor=tk.NW, image=black_checker_photo)
                checkers[checker] = (col, row)


# Переменные для хранения выбранной шашки и её позиции
selected_checker = None
selected_position = None
# Функция выбора шашки
def select_checker(event):
    global selected_checker, selected_position
    item_id = canvas.find_closest(event.x, event.y)[0] # для чего нужна
    print(item_id)
    if item_id in checkers:
        selected_checker = item_id
        selected_position = checkers[item_id]
        print(f"Выбрана шашка на позиции {selected_position}")


# Функция для перемещения шашки
def move_checker(event):
    global selected_checker, selected_position
    print(selected_position, "!")
    if selected_checker:
        col = event.x // cell_size
        row = event.y // cell_size
        if (col + row) % 2 == 1 and abs(selected_position[0] - col) == 1 and abs(selected_position[1] - row) == 1:  # Проверяем, что целевая клетка чёрная
            canvas.coords(selected_checker, col * cell_size, row * cell_size)
            checkers[selected_checker] = (col, row)
            selected_checker = None
            selected_position = None
            print(f"Шашка перемещена на позицию ({col}, {row})")

canvas.bind("<Button-1>", select_checker)
canvas.bind("<Button-3>", move_checker)
# Запускаем главный цикл обработки событий
root.mainloop()
