import os
import csv
import time
from playsound import playsound
with open("demo.csv") as csvfile:
    reader = csv.reader(csvfile)
    words = []
    result = {}
    for row in reader:
        word = row[0]
        words.append(word)
        tran = row[1]
        result[word] = tran

    words.sort()
    for word in words:
        filename = word.replace(" ", "_")
        fullname = f"{filename}.mp3"
        tran = result[word]
        try:
            playsound(fullname)
            print(f"{word} | {tran}")
            input("Press a key to continue.")
            for i in range(2):
                playsound(fullname)
                print(f"{word} | {tran}")
                time.sleep(3)
        except: 
            print("wrong word going next")


