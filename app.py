from tkinter import *
from cell import Cell
from utils import height_perc, width_perc
import settings


root = Tk()


if __name__ == '__main__':
    # Override the windows settings
    root.configure(bg='black')
    root.title('Minesweeper Game')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.resizable(False, False)

    top_frame = Frame(
        root,
        bg = 'black',
        width = width_perc(100),
        height = height_perc(25),
    )

    top_frame.place(
        x=0, 
        y=0
    )

    left_frame = Frame(
        root,
        bg = 'black',
        width = width_perc(25),
        height = height_perc(75),
    )

    left_frame.place(
        x=0,
        y=height_perc(25)
    )

    center_frame = Frame(
        root,
        bg = 'black',
        width = width_perc(75),
        height = height_perc(75),
    )

    center_frame.place(
        x=width_perc(25), 
        y=height_perc(25)
    )

    c1 = Cell()
    c1.create_btn_object(center_frame, "red", "first button")
    c1.cell_place(0, 0)

    # window run function
    root.mainloop()