import tkinter as tk
import fnmatch
import os
from pygame import mixer
from playsound import playsound

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg = 'black')

rootpath = "C:\\Users\\ASUS\\Desktop\\Internship\\music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

def select():
    label.config(text= listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))

listBox = tk.Listbox(canvas, fg="cyan" , bg = "black" , width = 100 , font=('poppins',14))
listBox.pack(padx=15, pady= 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx=10 , pady= 5, anchor= 'center')


preButton = tk.Button(canvas, text = "Prev", image=prev_img, bg='black', borderwidth=0)
preButton.pack(pady=15, in_ =top, side = 'left')

stopButton = tk.Button(canvas, text = "stop", image=stop_img, bg='black', borderwidth=0)
stopButton.pack(pady=15 ,in_ =top, side = 'left')

playButton = tk.Button(canvas, text = "play", image=play_img, bg='black', borderwidth=0 , command = select )
playButton.pack(pady=15 ,in_ =top, side = 'left')

pauseButton = tk.Button(canvas, text = "pause", image=pause_img, bg='black', borderwidth=0)
pauseButton.pack(pady=15 ,in_ =top, side = 'left')

nextButton = tk.Button(canvas, text = "next", image=next_img, bg='black', borderwidth=0)
nextButton.pack(pady=15 ,in_ =top, side = 'left')



for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)




canvas.mainloop()