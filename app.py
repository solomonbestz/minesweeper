from tkinter import *
import settings
from utils import height_perc, width_perc

root = Tk()


if __name__ == '__main__':
    # Override the windows settings
    root.configure(bg='black')
    root.title('Minesweeper Game')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.resizable(False, False)

    top_frame = Frame(
        root,
        bg = 'red',
        width = width_perc(100),
        height = height_perc(25),
    )

    top_frame.place(x=0, y=0)

    left_frame = Frame(
        root,
        bg = 'blue',
        width = width_perc(25),
        height = height_perc(75),
    )

    left_frame.place(x=0, y=height_perc(25))


    # window run function
    root.mainloop()