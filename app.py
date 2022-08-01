from tkinter import *
from utils import height_perc, width_perc
import settings

from cell import Cell


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

    for row in range(settings.GRID_SIZE):
        if row == 1 or row == 3 or row == 5:
            settings.COLOR_COUNT = 1
        else:
            settings.COLOR_COUNT = 0
        for column in range(settings.GRID_SIZE):
            cell = Cell(row, column)
            cell.add_cell(center_frame, settings.COLORS[settings.COLOR_COUNT], f"{row},{column}", column,  row)
            settings.COLOR_COUNT += 1
            if settings.COLOR_COUNT == 2:
                settings.COLOR_COUNT = 0

    # window run function
    root.mainloop()