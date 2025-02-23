import tkinter as tk
from PIL import Image, ImageTk

# Создаем основное окно
root = tk.Tk()
root.title("Шашки")
root.geometry('%dx%d+%d+%d' % (800, 800, 520, 130))
root.resizable(False, False)

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
                canvas.create_image(col * cell_size, row * cell_size, anchor=tk.NW, image=white_checker_photo)
            elif row < 3:
                # Размещаем чёрные шашки в нижних трёх рядах
                canvas.create_image(col * cell_size, row * cell_size, anchor=tk.NW, image=black_checker_photo)

# Запускаем главный цикл обработки событий
root.mainloop()
