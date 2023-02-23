import random
from tkinter import *
import sys
import os


otvety = ('Да', 'Однозначно\n', '42', 'К бабке\n  не\n ходи', '     Не\nрассчитывай\n   на это\n', 'Подумай\n   еще\n   раз', ' Ты точно\nхочешь это\n   знать?', 'Сам то как\n думаешь?', 'Нет', 'Возможно', 'Спросите\n  снова', 'Будущее\nтуманно', ' Духи\nговорят\n  нет', '  Мне\nкажется\n   да', '    Без\nсомнения\n', '     Не\nдождешься\n', 'Ыыыыыы\n', 'Не судьба!\n', 'Потряси\n  меня\n  ещё', 'Ты говоришь\n  с шаром\n', 'Звёзды\nговорят\n  да', '50 \ 50', '  Надо\nподумать\n', '  Тебе\nповезёт!', 'Точно\n нет', 'Поверь\n   в\n себя', 'Наверняка', 'Сбудется', ' Мало\nшансов', ' Шансы\nхорошие\n', '  Пока\nне ясно', 'Спроси\nточнее')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def reload():

    image = canvas.create_image(0, 0, anchor='nw', image=img1)
    canvas.create_window((300, 30), anchor='center', window=b)

def otvet():

    canvas.delete('all')
    reload()
    text2 = random.choice(otvety)
    text1 = canvas.create_text(300, 300, anchor='center', text=text2, font=('Comic Sans MS', 13, 'bold'), fill='white')

root = Tk()
root.title("Магический шар")
root.geometry("600x630")
root.resizable(False, False)
root.configure(bg='white')
root.iconbitmap(default=resource_path('favicon.ico'))

canvas = Canvas(root, width=600, height=630)
img1 = PhotoImage(file=resource_path('Magic_8_Ball.gif'))
image = canvas.create_image(0, 0, anchor='nw', image=img1)
canvas.pack()

b = Button(canvas, bg='white', font=('Comic Sans MS', 10, 'bold'), text='Встряхнуть', width='10', height='1', command=otvet)
text1 = canvas.create_text(300, 300, text='Задай\nвопрос', anchor='center', font=('Comic Sans MS', 14, 'bold'), fill='white')
b.pack(anchor='center', expand=1)

canvas.create_window((300, 30), anchor='center', window=b)

root.mainloop()

