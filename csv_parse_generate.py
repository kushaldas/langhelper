import os
import csv
from gtts import gTTS

with open("swedish.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        word = row[0]
        filename = word.replace(" ", "_")
        fullname = f"{filename}.mp3"
        fullname = fullname.lower()
        if not os.path.exists(fullname):
            try:
                tts = gTTS(word, lang="sv")
                tts.save(fullname)
                print(f"Saved {word} voice.")
            except:
                print(f"Error on {word}")


