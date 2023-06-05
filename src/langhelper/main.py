# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
import csv
import random
from playsound import playsound

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, QUrl, Signal, QThread

from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from PySide6 import QtQml as qml
import json
import sys

class WordsList(qtc.QObject):

    def __init__(self, parent=None):
        super(WordsList, self).__init__(parent)
        print(sys.argv)
        self.words = {}
        self.wlist = []
        self.session = []
        self.translations = {}
        csv_name = "swedish.csv"
        if len(sys.argv) > 1:
            csv_name = sys.argv[1]
        with open(csv_name) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                word = row[0]
                filename = word.replace(" ", "_")
                fullname = f"{filename}.mp3"
                self.words[word] = fullname
                self.translations[word] = row[1]
                self.wlist.append(word)

        self.currentword = ""

    @Slot()
    def next(self):
        number = random.randint(0, len(self.wlist))
        self.currentword = self.wlist.pop(number -1)
        self.session.append(self.currentword)
        with open("done.json", "w") as fobj:
            json.dump(self.session, fobj)

    @Slot(result=str)
    def len(self):
        return str(len(self.wlist))



    @Slot()
    def play(self):
        if self.currentword:
            filename = self.words[self.currentword]
            playsound(filename)

    @Slot(result=str)
    def show(self):
        if self.currentword:
            return f"{self.currentword} / {self.translations[self.currentword]}"



if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    ctxt = engine.rootContext()
    wlist = WordsList()
    ctxt.setContextProperty("wordslist", wlist)
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
