import tkinter as tk
import fnmatch
import os
from pygame import mixer

# Initialize tkinter window
canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg='black')

# Get the directory of the script (current working directory)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the directory containing your music files (replace with your own path)
rootpath = os.path.join(script_directory, "music")
pattern = "*.mp3"

# Initialize pygame mixer
mixer.init()

# Load images for buttons (replace with your own image file paths)
prev_img = tk.PhotoImage(file=os.path.join(script_directory, "prev_img.png"))
stop_img = tk.PhotoImage(file=os.path.join(script_directory, "stop_img.png"))
play_img = tk.PhotoImage(file=os.path.join(script_directory, "play_img.png"))
pause_img = tk.PhotoImage(file=os.path.join(script_directory, "pause_img.png"))
next_img = tk.PhotoImage(file=os.path.join(script_directory, "next_img.png"))

# Create a listbox to display the available music files
listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)

# Create a label to display the selected song
label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('poppins', 18))
label.pack(pady=15)

# Create a frame for buttons
top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

# Create buttons for player controls
def play():
    selected_item = listBox.get("anchor")
    label.config(text=selected_item)
    file_path = os.path.join(rootpath, selected_item)
    mixer.music.load(file_path)
    mixer.music.play()

playButton = tk.Button(canvas, text="Play", image=play_img, bg='black', borderwidth=0, command=play)
playButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command=mixer.music.stop)
stopButton.pack(pady=15, in_=top, side='left')

paused = False  # Variable to track whether the music is paused

def pause_resume():
    global paused
    if paused:
        mixer.music.unpause()
        paused = False
        pauseButton.config(text="Pause", image=pause_img)
    else:
        mixer.music.pause()
        paused = True
        pauseButton.config(text="Resume", image=play_img)

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg='black', borderwidth=0, command=pause_resume)
pauseButton.pack(pady=15, in_=top, side='left')

def next_song():
    current_index = listBox.curselection()
    if current_index:
        next_index = int(current_index[0]) + 1
        if next_index < listBox.size():
            listBox.select_clear(current_index)
            listBox.select_set(next_index)
            selected_item = listBox.get(next_index)
            label.config(text=selected_item)
            file_path = os.path.join(rootpath, selected_item)
            mixer.music.load(file_path)
            mixer.music.play()

nextButton = tk.Button(canvas, text="Next", image=next_img, bg='black', borderwidth=0, command=next_song)
nextButton.pack(pady=15, in_=top, side='left')

def prev_song():
    current_index = listBox.curselection()
    if current_index:
        prev_index = int(current_index[0]) - 1
        if prev_index >= 0:
            listBox.select_clear(current_index)
            listBox.select_set(prev_index)
            selected_item = listBox.get(prev_index)
            label.config(text=selected_item)
            file_path = os.path.join(rootpath, selected_item)
            mixer.music.load(file_path)
            mixer.music.play()

preButton = tk.Button(canvas, text="Prev", image=prev_img, bg='black', borderwidth=0, command=prev_song)
preButton.pack(pady=15, in_=top, side='left')

# Populate the listbox with music files
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

# Start the tkinter main loop
canvas.mainloop()
