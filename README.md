# 🎧 Music Player Application

This README provides instructions for setting up and using the Music Player application built with Python and Tkinter.

## 🌐 Features
- 🔊 Play MP3 music files.
- ⏸️ Pause and resume playback.
- ⏹️ Stop playback.
- ⏭️ Skip to the next or previous track.
- 📚 User-friendly graphical interface.

## 🔧 Requirements
To run this application, ensure the following requirements are met:

### 🔄 Python Version
- Python 3.7 or higher.

### 📚 Python Libraries
- `tkinter` (Standard library; included with Python installation).
- `pygame` (For audio playback).

Install `pygame` using pip:
```bash
pip install pygame
```

### 🔒 Additional Files
Ensure the following files exist in the same directory as the script:
- `prev_img.png`: Image for the "Previous" button.
- `stop_img.png`: Image for the "Stop" button.
- `play_img.png`: Image for the "Play" button.
- `pause_img.png`: Image for the "Pause" button.
- `next_img.png`: Image for the "Next" button.

### 🎧 Music Directory
- Create a folder named `music` in the same directory as the script.
- Place your `.mp3` files in this `music` folder.

## 🚀 How to Use

1. **🔄 Run the Application**
   - Execute the script using Python:
     ```bash
     python music_player.py
     ```

2. **🔍 Interface Overview**
   - The application window displays a list of `.mp3` files in the `music` folder.
   - Buttons for "Play," "Pause," "Stop," "Next," and "Previous" are available at the bottom.

3. **🎧 Play a Song**
   - Select a song from the listbox by clicking on it.
   - Click the "Play" button to start playback.

4. **⏸️ Pause and Resume**
   - Click the "Pause" button to pause the playback.
   - Click the same button again (now labeled "Resume") to resume playback.

5. **⏹️ Stop Playback**
   - Click the "Stop" button to stop the currently playing track.

6. **⏭️ Navigate Tracks**
   - Use the "Next" button to skip to the next track.
   - Use the "Prev" button to return to the previous track.

## 🚪 Troubleshooting

### Common Issues
- **No Sound Output**:
  - Ensure `.mp3` files exist in the `music` folder.
  - Verify that the system audio is enabled and volume is up.
- **Button Images Not Displayed**:
  - Confirm that the button image files are in the same directory as the script.
  - Ensure the image file names match those specified in the script.
- **pygame Error**:
  - Ensure `pygame` is installed properly using pip.

### Logs and Errors
- Any errors will be displayed in the terminal or command prompt where the script is executed.



---
🎧 Enjoy your music!

