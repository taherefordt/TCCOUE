import csv
import random


file = open("C00_japanese_vocab_backup.csv", "r", encoding="UTF-8")
all_translations = list(csv.reader(file, delimiter=","))
file.close()

all_translations.pop(0)

print(all_translations)

while True:
    print(all_translations[random.randint(0, 47)][1])
