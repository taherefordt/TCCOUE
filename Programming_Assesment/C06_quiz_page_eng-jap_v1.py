from functools import partial
from tkinter import *
import tkinter as tk


class Quiz_Page:

    def __init__(self):
        self.quiz_frame = Frame(padx=5, pady=5)
        self.quiz_frame.grid()

        ### INFO FRAME###

        self.info_frame = Frame(self.quiz_frame)
        self.info_frame.grid(row=0, padx=5, pady=20)

        self.remaining_questions = Label(self.quiz_frame,
                                         text="question\n x/y",
                                         font=("Arial", "7"))
        self.remaining_questions.grid(row=0, column=0, sticky=NE)

        self.answers_correct = Label(self.quiz_frame,
                                     text="x/y correct",
                                     font=("Arial", "7"))
        self.answers_correct.grid(row=0, column=0, sticky=NW)

        ### SUBMISSION FRAME ###

        self.question_frame = Frame(self.quiz_frame)
        self.question_frame.grid(row=1, padx=5, pady=20)

        self.question = Label(self.quiz_frame,
                              text="what is '____' in japanese?",
                              font=("Arial", "11", "bold"))
        self.question.grid(row=0, pady=20, sticky=NS)

        self.submit_button1 = Button(self.question_frame,
                                    text="option 1",
                                    font=("Arial", "11", "bold"),
                                    bg="grey",
                                    fg="white",
                                    width=12)
        self.submit_button1.grid(row=1, column=0, padx=30, pady=5)

        self.submit_button2 = Button(self.question_frame,
                                    text="option 2",
                                    font=("Arial", "11", "bold"),
                                    bg="grey",
                                    fg="white",
                                    width=12)
        self.submit_button2.grid(row=1, column=1, padx=30, pady=5)

        self.submit_button3 = Button(self.question_frame,
                                     text="option 3",
                                     font=("Arial", "11", "bold"),
                                     bg="grey",
                                     fg="white",
                                     width=12)
        self.submit_button3.grid(row=2, column=0, padx=30, pady=5)

        self.submit_button4 = Button(self.question_frame,
                                     text="option 4",
                                     font=("Arial", "11", "bold"),
                                     bg="grey",
                                     fg="white",
                                     width=12)
        self.submit_button4.grid(row=2, column=1, padx=30, pady=5)

        ### HELP FRAME ###

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=2, padx=5)

        # button that opens the hiragana page
        self.to_hiragana = Button(self.help_frame,
                                  text="Hiragana",
                                  font=("Arial", "16", "bold"),
                                  bg="green",
                                  fg="white",
                                  width=12,
                                  command=self.display_hiragana)
        self.to_hiragana.grid(row=0, column=0, padx=15, pady=5)

        # button that opens the vocabulary page
        self.to_vocabulary = Button(self.help_frame,
                                    text="Vocabulary",
                                    font=("Arial", "16", "bold"),
                                    bg="green",
                                    fg="white",
                                    width=13,
                                    command=self.display_vocab)
        self.to_vocabulary.grid(row=0, column=1, padx=15, pady=5)

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

        self.label_frame = Frame(self.chart_box, padx=5, pady=5)
        self.label_frame.grid()

        image = tk.PhotoImage(file="hiragana_chart.png")
        smaller_image = image.subsample(2, 2)

        self.chart_image = Label(self.label_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0, padx=5, pady=5)

        self.close_button = Button(self.label_frame,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   width=13,
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0, padx=5, pady=5)

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

        self.label_frame = Frame(self.chart_box, padx=5, pady=5)
        self.label_frame.grid()

        image = tk.PhotoImage(file="jap_eng_vocab.png")
        smaller_image = image.subsample(1, 1)

        self.chart_image = Label(self.label_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0, padx=5, pady=5)

        self.close_button = Button(self.label_frame,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   width=13,
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0, padx=5, pady=5)

    def close_chart(self, partner):
        # put button back to normal
        partner.to_vocabulary.config(state=NORMAL)
        self.chart_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("XXXXXX_Quizpage")
    Quiz_Page()
    root.mainloop()
