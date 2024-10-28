from tkinter import *



class Start:

    def __init__(self):
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # sets up GUI widget
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.main_page_heading = Label(self.start_frame,
                                       text="Japanese Helper",
                                       font=("Arial", "16", "bold"))
        self.main_page_heading.grid(row=0)

        instructions = ""

        self.quiz_instructions = Label(self.start_frame,
                                       text=instructions,
                                       wrap=250,
                                       width=40,
                                       justify="left")
        self.quiz_instructions.grid(row=1)

        self.questions_entry = Entry(self.start_frame,
                                     font=("Arial", "14"))
        self.questions_entry.grid(row=2, padx=10, pady=10)

        # BUTTONS BELOW

        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=4)

        self.to_hiragana_quiz = Button(self.button_frame,
                                       text="Hiragana",
                                       width=13,
                                       font=button_font,
                                       fg=button_fg,
                                       bg="#009900",
                                       command=display_quiz)

        self.to_hiragana_quiz.grid(row=1, column=0, padx=5, pady=5)

        self.to_vocabulary_quiz = Button(self.button_frame,
                                         text="Vocabulary",
                                         width=13,
                                         font=button_font,
                                         bg="green",
                                         fg="white",
                                         command=display_quiz)
        self.to_vocabulary_quiz.grid(row=1, column=1, padx=5, pady=5)

def display_quiz():
    pass



# main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Start")
    Start()
    root.mainloop()
