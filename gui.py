import tkinter as tk
from tkinter import *
from PIL import ImageTk
from pygame import mixer
from logic import morse_logic

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")
        self.pause_state = 0

        import tkinter as Tk
        import tkinter.ttk as ttk
        import tkinter.font as font
        # tkFont.BOLD == 'bold'
        font.nametofont('TkDefaultFont').configure(size=12) # tiny


        for r in range(6): self.master.rowconfigure(r, weight=1)
        for c in range(6): self.master.columnconfigure(c, weight=1)

        Frame1 = self.make_frame(0, 0, 3, 2)
        Frame2 = self.make_frame(3, 0, 3, 1)
        Frame3 = self.make_frame(0, 2, 3, 4)
        Frame4 = self.make_frame(3, 2, 3, 4)
        Frame5 = self.make_frame(3, 1, 3, 1)

        self.make_button(Frame1, "icons/play.png", 0)
        self.make_button(Frame2, "icons/stop.png", 1)
        self.make_button(Frame5, "icons/pause.png", 2)

        self.input = tk.LabelFrame(Frame3, text=" Input text ")
        self.textvar = tk.StringVar()
        self.textbox = tk.Text(self.input, height=4, width=50, font=("TkDefaultFont", 14), wrap='word', undo=True)
        self.textbox.pack(expand=1, fill="both", padx=5, pady=5)
        self.input.pack(expand=1, fill="both", padx=5, pady=5)

        button2 = tk.Button(self.input, text="Generate morse code", command=lambda: self.generate_morse())
        button2.pack(side=tk.LEFT, expand=1, fill="both", padx=5, pady=5)

        self.output = tk.LabelFrame(master, text=" Morse code ")
        self.status_message = tk.StringVar()
        self.status_message.set('\n Your Morse code will be displayed here \n')

        self.textwidget = tk.Label(self.output, textvariable=self.status_message, wraplength=590)
        self.textwidget.configure(relief='flat', state="normal")
        self.textwidget.pack(expand=1, fill="both", padx=5, pady=5)
        self.output.grid(row = 3, column = 2, rowspan = 3, columnspan = 4, sticky = W+E+N+S)


    def make_frame(self, r, c, rs, cs):
        frame = tk.Frame()
        frame.grid(row = r, column = c, rowspan = rs, columnspan = cs, sticky = W+E+N+S)
        return frame

    def make_button(self, Frame, img_name, i):
        b = tk.Button(Frame)
        image = ImageTk.PhotoImage(file=img_name)
        if i==0: b.config(image=image, command=lambda: self.play())
        elif i==1: b.config(image=image, command=lambda: self.stop())
        else: b.config(image=image, command=lambda: self.pause())
        b.image = image
        b.pack(side="top", fill="both", expand=True)


    def play(self):
        print("play")
        if self.pause_state == 0:
            mixer.init()
            mixer.music.load('file.mp3')
            mixer.music.play()
        else:
            mixer.music.unpause()

    def stop(self):
        print("stop")
        mixer.music.stop()
        self.pause_state = 0

    def pause(self):
        print("pause")
        mixer.music.pause()
        self.pause_state = 1

    def generate_morse(self):
        print("morse")
        self.morse_coder = morse_logic()
        msg = self.textbox.get("1.0", tk.END)
        morse_code = self.morse_coder.process(msg)
        self.status_message.set(morse_code)
