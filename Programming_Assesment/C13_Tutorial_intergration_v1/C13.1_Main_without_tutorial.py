from functools import partial
from tkinter import *
import tkinter as tk
import csv
import random


class Start:

    def __init__(self):

        # feedback and error message placeholder
        self.var_feedback = StringVar()
        self.var_has_error = StringVar()

        # the variable that dictates which mode of test is selected
        self.mode_selected = StringVar()

        # sets the default mode to "practice mode"
        self.mode_selected.set("practice")
        vocab_or_kana = ""

        # number of questions the user has decided to do
        self.questions_todo = IntVar()

        # general font for the buttons of the program
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # sets up GUI widget
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # heading for the main page
        self.main_page_heading = Label(self.start_frame,
                                       text="Japanese Helper",
                                       font=("Arial", "16", "bold"))
        self.main_page_heading.grid(row=0)

        instructions = "Please enter the number of questions you " \
                       "wish to go through below, and click the " \
                       "hiragana or vocabulary button, depending on which " \
                       "you want to practice."

        self.quiz_instructions = Label(self.start_frame,
                                       text=instructions,
                                       wrap=250,
                                       width=40,
                                       justify="left")
        self.quiz_instructions.grid(row=1)

        # set-up frame
        self.set_up_frame = Frame(self.start_frame)
        self.set_up_frame.grid(row=2)

        # entry box that determines the number of questions
        self.questions_entry = Entry(self.set_up_frame,
                                     font=("Arial", "14"))
        self.questions_entry.grid(row=0, column=0, pady=10)

        # button that changes which mode of test the user has selected
        self.mode_select = Button(self.set_up_frame,
                                  command=lambda: (self.change_mode(self.mode_selected.get())),
                                  text=self.mode_selected.get(),
                                  font=("Arial", "11", "bold"),
                                  bg="#0096C7",
                                  fg="white",
                                  width=6)
        self.mode_select.grid(row=0, column=1)

        # feedback frame
        self.feedback_frame = Frame(self.start_frame)
        self.feedback_frame.grid(row=3)

        self.feedback = Label(self.feedback_frame,
                              font=("Arial", "11"),
                              fg="red",
                              text=self.var_feedback.get())
        self.feedback.grid()

        # BUTTONS BELOW

        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=4)

        self.to_hiragana_quiz = Button(self.button_frame,
                                       text="Hiragana",
                                       width=13,
                                       font=button_font,
                                       fg=button_fg,
                                       bg="green",
                                       command=lambda: (self.input_questions("kana")))

        self.to_hiragana_quiz.grid(row=0, column=0, padx=15, pady=5)

        self.to_vocabulary_quiz = Button(self.button_frame,
                                         text="Vocabulary",
                                         width=13,
                                         font=button_font,
                                         bg="green",
                                         fg="white",
                                         command=lambda: (self.input_questions("vocab")))
        self.to_vocabulary_quiz.grid(row=0, column=2, padx=15, pady=5)

        self.to_tutorial = Button(self.start_frame,
                                  text="Tutorial",
                                  font=("Arial", "16", "bold"),
                                  bg="#D2B55B",
                                  fg="white",
                                  width=13,
                                  command=self.display_tutorial)
        self.to_tutorial.grid(row=5, padx=15, pady=5)

    def display_tutorial(self):
        pass

    def display_quiz(self, questions, mode, vocab_or_kana):
        Display_Quiz(self, questions, mode, vocab_or_kana)
        root.withdraw()

    def input_questions(self, vocab_or_kana):
        error = "Please enter a number that is more than 0"

        questions_number = self.questions_entry.get()
        min_questions = 1

        try:

            if int(questions_number) < min_questions:
                has_error = "yes"
            else:
                has_error = "no"

        # checks input is a integer
        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            self.feedback.config(text=error)
            return "invalid"

        else:
            self.feedback.config(text="")
            self.var_has_error.set("no")

        self.questions_todo.set(int(questions_number))
        self.display_quiz(self.questions_todo.get(), self.mode_selected.get(), vocab_or_kana)

        # when there is at least 1 valid calculation, display error message.
        # enables the history/export button

    def change_mode(self, selected_mode):

        if selected_mode == "practice":
            new_mode_selected = "test"
            new_bg = "#ff2c2c"

        elif selected_mode == "test":
            new_mode_selected = "practice"
            new_bg = "#0096C7"

        else:
            new_mode_selected = "practice"
            new_bg = "#0096C7"

        self.mode_selected.set(new_mode_selected)
        self.mode_select.config(text=new_mode_selected, bg=new_bg)


# prevent exit disables the corner [X] button,
# to prevent destroying the quiz box and leaving the cheat sheets
def prevent_exit():
    pass


class Display_Quiz:

    def __init__(self, x, questions, mode, vocab_or_kana):

        self.quiz_box = Toplevel()

        print(mode)

        self.quiz_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_routine))

        if vocab_or_kana == "vocab":
            # opens and reads the csv file that holds the vocab quiz resources
            file = open("C00_japanese_vocab_backup.csv", "r", encoding="UTF-8")
            self.all_translations = list(csv.reader(file, delimiter=","))
            file.close()

        else:
            file = open("C00_hiragana_to_english.csv", "r", encoding="UTF-8")
            self.all_translations = list(csv.reader(file, delimiter=","))
            file.close()

        # self.answer_pair is a list that contains the selected word for the quiz's question including both translations
        self.answer_pair = []

        # self.answer_word
        self.answer_word = ""

        # answer_checked allows for the 'submit -> next' button change ,
        # this is done by telling the program whether the current answer has been assessed
        self.answer_checked = "no"

        # removes the top row of the csv file
        self.all_translations.pop(0)

        # no of questions completed (including in progress)
        self.questions_done = 0
        self.amount_correct = 0

        # INFO FRAME #
        # info frame contains the remaining questions and the no. of questions correct

        self.info_frame = Frame(self.quiz_box)
        self.info_frame.grid(row=0, padx=5, pady=20)

        self.completed_questions = Label(self.quiz_box,
                                         text=f"question\n {self.questions_done}/{questions}",
                                         font=("Arial", "7"))
        self.completed_questions.grid(row=0, column=0, sticky=NE)

        self.answers_correct = Label(self.quiz_box,
                                     text=f"{self.amount_correct}/{self.questions_done} correct",
                                     font=("Arial", "7"))
        self.answers_correct.grid(row=0, column=0, sticky=NW)

        # QUESTION FRAME #
        # question frame includes the question, the answer entry, the submit button, and feedback label

        self.question_frame = Frame(self.quiz_box)
        self.question_frame.grid(row=1, padx=5, pady=20)

        # displays the question
        self.question = Label(self.quiz_box,
                              text="",
                              font=("Arial", "11"))
        self.question.grid(row=0, pady=20, sticky=NS)

        # answer entry field
        self.submission = Entry(self.question_frame,
                                width=21,
                                font=("Arial", "16"))
        self.submission.grid(row=1, column=0)

        # submit button, which changes to a 'next' button upon use
        self.submit_button = Button(self.question_frame,
                                    text="submit",
                                    font=("Arial", "11", "bold"),
                                    bg="dark blue",
                                    fg="white",
                                    width=12,
                                    command=lambda: (self.next_question(questions, vocab_or_kana)))
        self.submit_button.grid(row=1, column=2)

        # FEEDBACK FRAME #

        self.feedback_frame = Frame(self.quiz_box)
        self.feedback_frame.grid(row=2, padx=5)

        # contains all feedback/responses from the program
        # this includes error messages, and incorrect/correct answer messages
        self.feedback_message = Label(self.feedback_frame,
                                      text="",
                                      font=("Arial", "11", "bold"))
        self.feedback_message.grid(row=0)

        # HELP FRAME #

        self.help_frame = Frame(self.quiz_box)
        self.help_frame.grid(row=3, padx=5, pady=20)

        # button that opens the hiragana chart page
        self.to_hiragana = Button(self.help_frame,
                                  text="Hiragana",
                                  font=("Arial", "16", "bold"),
                                  bg="#048c7f",
                                  fg="white",
                                  width=12,
                                  command=self.display_hiragana)
        self.to_hiragana.grid(row=0, column=0, padx=15, pady=5)

        # button that opens the vocabulary page
        self.to_vocabulary = Button(self.help_frame,
                                    text="Vocabulary",
                                    font=("Arial", "16", "bold"),
                                    bg="#048c7f",
                                    fg="white",
                                    width=13,
                                    command=self.display_vocab)
        self.to_vocabulary.grid(row=0, column=2, padx=15, pady=5)

        self.test_restrictions(mode)

        # generates the question
        self.generate_question(questions, vocab_or_kana)

    def test_restrictions(self, mode):
        if mode == "test":
            self.to_vocabulary.config(state=DISABLED)
            self.to_hiragana.config(state=DISABLED)
            print("hello")
        else:
            pass

    def generate_question(self, questions, vocab_or_kana):

        # changes the 'next' button back to a 'submit' button
        self.submit_button.config(text="submit")
        self.submission.config(bg="#FFFFFF")
        self.submission.delete(0, 'end')

        # because the two different quizzes have different amounts of total items in their csv's
        # the answer pairs are generated separately
        if vocab_or_kana == "vocab":
            # generates question/answer word pair
            self.answer_pair = self.all_translations[random.randint(0, 47)]
        else:
            self.answer_pair = self.all_translations[random.randint(0, 46)]

        # assigns the answer to be the english word of the pair
        question_word = self.answer_pair[1]
        self.answer_word = self.answer_pair[0]

        # generates question and figures out what question is being *answered*
        question_number = self.questions_done + 1
        self.question.config(text=f"what is '{question_word}' in english?")

        # adds 1 to the number of questions completed info text (from the question before being finished)
        self.completed_questions.config(text=f"question\n {question_number}/{questions}")

    def check_answer(self, questions):

        # adds 1 to the number of questions completed upon submission
        self.questions_done += 1

        # if the answer is correct the program tells the user and changes the score values
        if self.submission.get().lower() == self.answer_word:
            self.amount_correct += 1
            self.submission.config(bg="#D8FFB1")
            self.answers_correct.config(text=f"{self.amount_correct}/{self.questions_done} correct")
            self.feedback_message.config(text="correct")

        # otherwise the program tells the user it was wrong
        else:
            self.submission.config(bg="#FF9A98")
            self.feedback_message.config(text=f"incorrect, the right answer is '{self.answer_word}'")

        # if the user is on the final question, the "next" button becomes as a "finish" button
        if self.questions_done < questions:
            self.submit_button.config(text="next")
        else:
            self.submit_button.config(text="finish")

    def next_question(self, questions, vocab_or_kana):

        self.feedback_message.config(text="")

        # if the answer box is empty, the user must retry the question
        if self.submission.get() == "":
            self.feedback_message.config(text="please enter an answer")
            self.feedback_message.config(fg="red")

        else:

            # checks if the selected number of questions has been completed and if so, closes the quiz
            if self.questions_done < questions:

                # this chunk of code operates the pipeline of the submit button's function
                # from submitting an answer to advancing to the next question

                # if the answer has not been checked, check the answer and flip the answer_checked variable
                if self.answer_checked == "no":
                    self.check_answer(questions)
                    self.answer_checked = "yes"

                # otherwise, turn the submit button into a "next" button, and flip the variable again
                else:
                    self.generate_question(questions, vocab_or_kana)
                    self.answer_checked = "no"

            else:
                self.close_routine()

    def close_routine(self):
        # root.deiconify reveals the start page
        root.deiconify()
        # .destroy() removes the quiz box
        self.quiz_box.destroy()

    def display_vocab(self):
        # disables the corner [X] button while the chart is being displayed
        self.quiz_box.protocol('WM_DELETE_WINDOW', prevent_exit)
        # displays the table
        Display_Table(self)

    def display_hiragana(self):
        # disables the corner [X] button while the chart is being displayed
        self.quiz_box.protocol('WM_DELETE_WINDOW', prevent_exit)
        # displays the table
        Display_Chart(self)


class Display_Chart:

    def __init__(self, partner):
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        self.chart_box = Toplevel()

        # disables the hiragana button on the quiz page to prevent more being created
        partner.to_hiragana.config(state=DISABLED)

        self.chart_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_chart, partner))

        # frame that contains the image
        self.image_frame = Frame(self.chart_box, padx=5, pady=5)
        self.image_frame.grid()

        # grabs the image file from the program folder
        image = tk.PhotoImage(file="hiragana_chart.png")
        smaller_image = image.subsample(2, 2)

        # displays the hiragana chart
        self.chart_image = Label(self.image_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0)

        # allows the chart to be closed easier
        self.close_button = Button(self.image_frame,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0)

    def close_chart(self, partner):
        # puts the chart button back to normal
        partner.to_hiragana.config(state=NORMAL)
        partner.quiz_box.protocol('WM_DELETE_WINDOW',
                                  partial(Display_Quiz.close_routine, partner))
        self.chart_box.destroy()


class Display_Table:

    def __init__(self, partner):
        self.vocab_box = Toplevel()

        # closes the vocabulary button
        partner.to_vocabulary.config(state=DISABLED)

        self.vocab_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_vocab, partner))

        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        self.image_frame = Frame(self.vocab_box, padx=5, pady=5)
        self.image_frame.grid()

        image = tk.PhotoImage(file="jap_eng_vocab.png")
        smaller_image = image.subsample(1, 1)

        self.chart_image = Label(self.image_frame,
                                 image=smaller_image)

        self.chart_image.image = smaller_image
        self.chart_image.grid(row=0, column=0)

        self.close_button = Button(self.image_frame,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   command=partial(self.close_vocab, partner))
        self.close_button.grid(row=1, column=0)

    def close_vocab(self, partner):
        # puts the vocabulary button back to normal
        partner.to_vocabulary.config(state=NORMAL)
        partner.quiz_box.protocol('WM_DELETE_WINDOW',
                                  partial(Display_Quiz.close_routine, partner))
        self.vocab_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Japanese Quiz")
    Start()
    root.mainloop()
