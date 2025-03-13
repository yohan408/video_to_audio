import moviepy.editor
from tkinter import filedialog


file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])

video=moviepy.editor.VideoFileClip(file_path)

audio=video.audio

audio.write_audiofile("C:/Users/CodeWithShani/Desktop/Extracted_audio.mp3")