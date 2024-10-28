from tkinter import *
import tkinter as tk


class Vocab:

    def __init__(self):

        self.vocab_frame = Frame(padx=5, pady=5)
        self.vocab_frame.grid()

        self.to_hiragana = Button(text="Vocabulary",
                                  font=("Arial", "16", "bold"),
                                  bg="green",
                                  fg="white",
                                  command=self.display_vocab)
        self.to_hiragana.grid()

    def display_vocab(self):
        Display_Table()


class Display_Table:

    def __init__(self):

        self.chart_box = Toplevel()

        self.label_frame = Frame(self.chart_box, padx=5, pady=5)
        self.label_frame.grid()

        image = tk.PhotoImage(file="jap_eng_vocab.png")
        smaller_image = image.subsample(1, 1)

        self.chart_image = Label(self.label_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0)




if __name__ == "__main__":
    root = Tk()
    root.title("Vocabulary")
    Vocab()
    root.mainloop()