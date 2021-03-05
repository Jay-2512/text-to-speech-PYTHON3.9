from tkinter import *
from gtts import gTTS as gt
from playsound import playsound as ps
import os.path, time
from os import path


root = Tk()

# functions
def play_audio():
    file_name = 'outputData.mp3'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path+'/outputData.mp3'
    msg = text_box.get();
    output = gt(text = msg, lang = 'en', slow = False)
    output.save(dir_path + "/outputData.mp3")
    ps(dir_path + '/outputData.mp3')
    time.sleep(0.5)

    if path.exists(file_path):
        os.remove(file_path)


def reset_all():    
    text_box.delete(first=0, last=1000)


def exit():
    root.destroy()

# main window config

root.geometry('500x200')
root.resizable(False, False)
root.configure(bg='#FFFFFF')
root.title('Text-To-Speech')


#Label

label_1 = Label(root, text = "TEXT TO SPEECH")
label_1.config(font='courier 20 bold', bg = "#FFFFFF", pady = 10)
label_1.pack()

#text box

text_box = Entry(root, width = 50, bd = 5)
text_box.pack(pady = 10)
text_box.insert(0, "Enter the text here!")

#buttons

button_accept_entry = Button(root, text = "PLAY", width = 13, font = 'Arial 15 bold', bg = '#64d9b4', fg = "#000000", command = play_audio)
button_accept_entry.pack(side = LEFT, fill=BOTH, expand=FALSE, pady = 20)

button_accept_entry = Button(root, text = "RESET", font = 'Arial 15 bold', bg = '#034473', fg = '#FFFFFF', command = reset_all)
button_accept_entry.pack(side = LEFT, fill=BOTH, expand=TRUE, pady = 20)

button_accept_entry = Button(root, text = "EXIT", width = 12, font = 'Arial 15 bold', bg = '#e64635', fg = '#FFFFFF', command = exit)
button_accept_entry.pack(side = RIGHT, fill=BOTH, expand=FALSE, pady = 20)


root.mainloop()