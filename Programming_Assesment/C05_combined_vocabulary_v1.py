from functools import partial
from tkinter import *
import tkinter as tk


class Vocab:

    def __init__(self):
        self.vocab_frame = Frame(padx=5, pady=5)
        self.vocab_frame.grid()

        self.to_hiragana = Button(text="Hiragana",
                                  font=("Arial", "16", "bold"),
                                  bg="green",
                                  fg="white",
                                  command=self.display_hiragana)
        self.to_hiragana.grid(row=0, column=0)

        self.to_vocabulary = Button(text="Vocabulary",
                                    font=("Arial", "16", "bold"),
                                    bg="green",
                                    fg="white",
                                    command=self.display_vocab)
        self.to_vocabulary.grid(row=0, column=1)

    def display_vocab(self):
        Display_Table(self)

    def display_hiragana(self):
        Display_Chart(self)


class Display_Chart:

    def __init__(self, partner):
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        self.chart_box = Toplevel()

        partner.to_hiragana.config(state=DISABLED)
        self.chart_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_chart, partner))

        self.cheatsheet_frame = Frame(self.chart_box, padx=5, pady=5)
        self.cheatsheet_frame.grid()

        image = tk.PhotoImage(file="hiragana_chart.png")
        smaller_image = image.subsample(2, 2)

        self.chart_image = Label(self.cheatsheet_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0)

        self.close_button = Button(self.cheatsheet_frame,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0)

    def close_chart(self, partner):
        # put button back to normal
        partner.to_hiragana.config(state=NORMAL)
        self.chart_box.destroy()


class Display_Table:

    def __init__(self, partner):
        self.chart_box = Toplevel()

        partner.to_vocabulary.config(state=DISABLED)
        self.chart_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_chart, partner))

        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        self.cheatsheet_frame = Frame(self.chart_box, padx=5, pady=5)
        self.cheatsheet_frame.grid()

        image = tk.PhotoImage(file="jap_eng_vocab.png")
        smaller_image = image.subsample(1, 1)

        self.chart_image = Label(self.cheatsheet_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0)

        self.close_button = Button(self.cheatsheet_frame,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0)

    def close_chart(self, partner):
        # put button back to normal
        partner.to_vocabulary.config(state=NORMAL)
        self.chart_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Combined_Vocabulary")
    Vocab()
    root.mainloop()
