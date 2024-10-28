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

        self.image_list = ["hiragana_chart.png", "jap_eng_vocab.png", "hiragana_chart.png"]
        self.image_index = 0
        self.selected_image = StringVar()
        self.selected_image.set(self.image_list[self.image_index])

        self.tutorial_box = Toplevel()

        partner.to_tutorial.config(state=DISABLED)

        self.tutorial_box.protocol('WM_DELETE_WINDOW',
                                   partial(self.close_chart, partner))

        image = PhotoImage(file=f"{self.image_list[0]}")
        smaller_image = image.subsample(2, 2)

        self.tutorial_image = Label(self.tutorial_box,
                                    image=smaller_image)

        self.tutorial_image.image = smaller_image
        self.tutorial_image.grid(row=2, column=0)

        self.next = Button(self.tutorial_box,
                           text="next",
                           font=button_font,
                           fg=button_fg,
                           bg="#D2B55B",
                           command=lambda: self.next_image())
        self.next.grid(row=1, column=1)

        self.close_button = Button(self.tutorial_box,
                                   text="dismiss",
                                   font=button_font,
                                   fg=button_fg,
                                   bg="dark red",
                                   command=partial(self.close_chart, partner))
        self.close_button.grid(row=1, column=0)

    def next_image(self):

        # if the index from the list, of the image shown is less than that of the lists maximum,
        # the program switches the image with the next one in line
        if self.image_index < (len(self.image_list) - 1):

            # adds one to the index no. to keep track of slide no.
            self.image_index += 1
            # grabs the image from the file
            next_image = PhotoImage(file=f"{self.image_list[self.image_index]}")
            # switches out the images
            self.tutorial_image.config(image=next_image)
            self.tutorial_image.image = next_image

        else:
            pass

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
