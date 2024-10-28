from functools import partial
from tkinter import *
import tkinter as tk


class Tutorial_Page:

    def __init__(self):

        self.vocab_frame = Frame(padx=5, pady=5)
        self.vocab_frame.grid()

        self.to_tutorial = Button(text="Tutorial",
                                  font=("Arial", "16", "bold"),
                                  bg="#D2B55B",
                                  fg="white",
                                  command=self.display_tutorial)
        self.to_tutorial.grid(row=0, column=0)

    def display_tutorial(self):
        Display_Tutorial(self)


class Display_Tutorial:

    def __init__(self, partner):
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        self.tutorial_box = Toplevel()

        partner.to_tutorial.config(state=DISABLED)

        self.tutorial_box.protocol('WM_DELETE_WINDOW',
                                   partial(self.close_chart, partner))

        self.close_button = Button(self.tutorial_box,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0)

    def close_chart(self, partner):
        # put button back to normal
        partner.to_tutorial.config(state=NORMAL)
        self.tutorial_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Start")
    Tutorial_Page()
    root.mainloop()