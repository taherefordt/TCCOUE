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
        self.to_hiragana.grid()

    def display_hiragana(self):
        Display_Chart()


class Display_Chart:

    def __init__(self):

        self.chart_box = Toplevel()

        self.label_frame = Frame(self.chart_box, padx=5, pady=5)
        self.label_frame.grid()

        image = tk.PhotoImage(file="hiragana_chart.png")
        smaller_image = image.subsample(2, 2)

        self.chart_image = Label(self.label_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0)



if __name__ == "__main__":
    root = Tk()
    root.title("Vocabulary")
    Vocab()
    root.mainloop()