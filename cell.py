from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location, bgcolor, text):
        btn = Button(
            location,
            bg = bgcolor,
            text = text
        )
        self.cell_btn_object = btn

    def cell_place(self, x, y):
        self.cell_btn_object.place(
            x = x,
            y = y
        )