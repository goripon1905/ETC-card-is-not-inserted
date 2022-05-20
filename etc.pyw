import tkinter
import tkinter as tk
import simpleaudio
import time
from subprocess import run
from tkinter import messagebox
from PIL import Image, ImageTk
try:
    import Tkinter as tk
except:
    import tkinter as tk

window = tkinter.Tk()
window.geometry("700x100")
window.title("ETCカードが挿入されていません")
window.attributes("-topmost", True)
window.overrideredirect(1)
window.update_idletasks()
w = window.winfo_width()
h = window.winfo_height()
scw = window.winfo_screenwidth()
sch = window.winfo_screenheight()
geometry = "+{:d}+{:d}".format(int((scw - w) / 2),
                               int((sch - h) / 2))
window.geometry(geometry)
img = Image.open('etc.png')
img = ImageTk.PhotoImage(img)
canvas = tkinter.Canvas(bg = "black", width=698, height=99)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
def run_after():
    wav_obj = simpleaudio.WaveObject.from_wave_file("etc.wav")
    play_obj = wav_obj.play()
    play_obj.wait_done()
    window.destroy()
window.after(1000, run_after)
window.mainloop()
