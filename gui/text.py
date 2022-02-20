
import tkinter as tk
from tkinter import *
import pyttsx3
from gtts import gTTS
import os

engine = pyttsx3.init()



def speaknow():
    text = e.get()

    if text == "kitap":
        engine.runAndWait()
        fh = open("kitap.txt", "r")
        myText = fh.read().replace("\n", " ")
        language = 'tr'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        fh.close()
        os.system("start output.mp3")
        engine.stop
    elif text == "book":
        engine.runAndWait()
        fh = open("book.txt", "r")
        myText = fh.read().replace("\n", " ")
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        fh.close()
        os.system("start output.mp3")
        engine.stop


root = Tk()
root.geometry("350x350")
obj = LabelFrame(root, text="Text to speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)


e = Entry(obj)



def click(event):
    e.config(state=NORMAL)
    e.delete(0,END)

def getBook(book,konum1,konum2):
    name = Label(obj, text=str(book), fg='blue', font=('arial', 16))
    name.place(x=konum1, y=konum2)


getBook("1-) KİTAP",100,50)
getBook("2-) BOOK",100,100)

e.insert(0,"lütfen kitap ismi girin")
e.configure(state=DISABLED)
e.bind("<Button-1>",click)


e.place(x=30, y=170)
name=Label(obj,text='KİTAP İSİMLERİ', fg='red',font=('arial',16))
name.place(x=100,y=10)


btn = Button(obj, text="Oku", font=20, bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)
btn.place(x=220, y=160)

root.title("Text to speech")


root.mainloop()