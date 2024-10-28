from tkinter import *
import pandas as pd

jap_words = """Japanese

こんにちわ
バイバイ
ありがとう
おねがいします
ごめんなさい
やめて
はい
いいえ
なんですか？
どこですか？
どうですか？
いくらですか？
いますか？
だといいです
"""

eng_words = """English

hello
goodbye
thank you
please
sorry
stop
caution
yes
no
where is?
how?
how much is it?
is there?
I would like
"""


class Proof:

    def __init__(self):
        df = pd.read_csv("C00_japanese_vocab_backup.csv", encoding="UTF-8")
        jap_vocab = df.to_string(justify='left', index=False)

        # sets up GUI widget
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.japanese_words = Label(self.temp_frame,
                                    text=jap_vocab,
                                    font=("Arial", "16", "bold"),
                                    justify='left'
                                    )

        self.japanese_words.grid(row=0, column=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Proof()
    root.mainloop()
