import tkinter
from functools import partial
from tkinter import *


class practice_button:

    def __init__(self):

        self.mode_selected = StringVar()
        self.mode_selected.set("practice")

        # sets up GUI widget
        self.vocab_frame = Frame(padx=5, pady=5)
        self.vocab_frame.grid()

        self.mode_select = Button(self.vocab_frame,
                                  command=lambda: (self.change_mode(self.mode_selected.get())),
                                  text=self.mode_selected.get(),
                                  font=("Arial", "16", "bold"),
                                  bg="green",
                                  fg="white")
        self.mode_select.grid()

    def change_mode(self, selected_mode):

        if selected_mode == "practice":
            new_mode_selected = "test"

        elif selected_mode == "test":
            new_mode_selected = "practice"

        else:
            new_mode_selected = "practice"

        self.mode_selected.set(new_mode_selected)
        self.mode_select.config(text=new_mode_selected)


if __name__ == "__main__":
    root = Tk()
    root.title("proof of concept")
    practice_button()
    root.mainloop()
