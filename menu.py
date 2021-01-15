from config import *

from tkinter import *
from playsound import playsound
from threading import Thread
import highscores
from scene_manager import Scene_manager

root = Tk()


def start_game():
    global root
    root.destroy()
    s = Scene_manager()
    s.scenes_loop()  # Переходим в менеджер сцен
    root = Tk()
    Button_game()


def records():
    global root
    root.destroy()
    highscores.make_highscores()
    root = Tk()
    Button_game()


def music():
    for i in range(32):
        playsound('Mystery.mp3')


Thread(target=music, daemon=True).start()


def Button_game():
    background_image = PhotoImage(file=os.path.join(sprites_folder, "bg.gif"))
    background = Label(root, image=background_image, bd=0)
    background.pack()

    root.title("Game")
    root.geometry("1400x800")

    # При нажатии на кнопку start game запускаем игру
    start_button = Button(text="Start Game", background="#D2691E", foreground="#000000", padx="14", pady="7", font="13",
                          width="13", command=start_game)
    start_button.place(x=650, y=250)

    # При нажатии на кнопку records выводим счет по всем играм
    records_button = Button(text="Records", background="#D2691E", foreground="#000000", padx="14", pady="7", font="13",
                            width="13", command=records)
    records_button.place(x=650, y=350)

    # При нажатии на кнопку quit закрываем меню
    end_button = Button(text="Quit", background="#D2691E", foreground="#000000", padx="14", pady="7", font="13",
                        width="13", command=root.destroy)
    end_button.place(x=650, y=450)

    root.mainloop()
