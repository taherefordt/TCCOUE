from tkinter import *
import csv
import random


class Word_Generator:

    def __init__(self):
        self.vocab_frame = Frame(padx=5, pady=5)
        self.vocab_frame.grid()

        self.all_translations = []

        file = open("C00_japanese_vocab_backup.csv", "r", encoding="UTF-8")
        self.all_translations = (list(csv.reader(file, delimiter=",")))
        print(self.all_translations)

        self.all_translations.pop(0)
        print(self.all_translations)

        self.generate_button = Button(text="Hiragana",
                                      font=("Arial", "16", "bold"),
                                      bg="green",
                                      fg="white",
                                      command=self.generate_word)
        self.generate_button.grid(row=0, column=0)

        self.word = Button(text="Vocabulary",
                           font=("Arial", "16", "bold"),
                           bg="green",
                           fg="white")
        self.word.grid(row=0, column=1)

        self.generate_word()

    def generate_word(self):
        new_word = self.all_translations[random.randint(1, 47)][1]
        self.word.config(text=str(new_word))


if __name__ == "__main__":
    root = Tk()
    root.title("Combined_Vocabulary")
    Word_Generator()
    root.mainloop()
