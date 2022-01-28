#cd gui
#python text.py
import tkinter as tk
from tkinter import *
import pyttsx3
from gtts import gTTS 
import os 
engine=pyttsx3.init()

def speaknow():
    engine.runAndWait()
    fh = open("kitap.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'tr'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    fh.close()
    os.system("start output.mp3")
    engine.stop
    #engine. yapman gerekebilir
   # engine.say(textv.get())
   #engine.runAndWait()
    #engine.stop

root= Tk()

#textv=StringVar()


obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)
#lbl=Label(obj,text="Text",font=30)
#lbl.pack(side=tk.LEFT,padx=5)

#text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
#text.pack(side=tk.LEFT,padx=10)


btn=Button(obj,text="Speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

root.title("Text to speech")
root.geometry("550x250")


root.mainloop()



#from gtts import gTTS 
  
# ses dosyası için kullanılacak kütüphane
#import os 

#fh = open("book.txt", "r")#r read
#myText = fh.read().replace("\n", " ")

# istenilen dile çevrilme
#language = 'tr'

#output = gTTS(text=myText, lang=language, slow=False)

#output.save("output.mp3")
#fh.close()

# başlatma 
#os.system("start output.mp3")