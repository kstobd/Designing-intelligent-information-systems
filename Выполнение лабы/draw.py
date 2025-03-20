import matplotlib.pyplot as plt
import numpy as np

# Функция для рисования


def draw_image():
    # Создаем белое полотно
    canvas = np.ones((28, 28)) * 0  # белый фон
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.set_title('Рисуйте здесь')
    image_plot = ax.imshow(canvas, cmap='gray', vmin=0, vmax=255)

    # Переменная для отслеживания состояния кнопки
    is_drawing = False

    # Функция для начала рисования при нажатии кнопки мыши
    def on_press(event):
        nonlocal is_drawing
        if event.button == 1:  # Левая кнопка мыши
            is_drawing = True

    # Функция для завершения рисования при отпускании кнопки мыши
    def on_release(event):
        nonlocal is_drawing
        if event.button == 1:  # Левая кнопка мыши
            is_drawing = False

    # Функция для рисования при движении курсора
    def on_move(event):
        if is_drawing and event.xdata is not None and event.ydata is not None:
            x, y = int(event.xdata), int(event.ydata)
            if 0 <= x < 28 and 0 <= y < 28:
                # Добавляем черный цвет на месте кисти 2x2 пикселя
                canvas[max(0, y-1):min(28, y+1),
                       max(0, x-1):min(28, x+1)] = 255
                image_plot.set_data(canvas)
                fig.canvas.draw_idle()

    def on_key(event):
        if event.key == '0':
            canvas_scaled = canvas / 255.0
            canvas_scaled.reshape((1, 28, 28, 1))
            plt.imsave('drawn_digit.png', canvas_scaled, cmap='gray')
            print("Изображение сохранено как 'drawn_digit.png'")
            exit()

    # Подключаем обработчики событий
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('button_release_event', on_release)
    fig.canvas.mpl_connect('motion_notify_event', on_move)
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

    # Нормализуем и изменяем форму для подачи в модель
    canvas_scaled = canvas / 255.0
    return canvas_scaled.reshape((1, 28, 28, 1))


draw_image()
