from pydub import AudioSegment
from pygame import mixer # Load the required library

class morse_logic():
    def __init__(self):
        self.CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
                    'D': '-..',    'E': '.',      'F': '..-.',
                    'G': '--.',    'H': '....',   'I': '..',
                    'J': '.---',   'K': '-.-',    'L': '.-..',
                    'M': '--',     'N': '-.',     'O': '---',
                    'P': '.--.',   'Q': '--.-',   'R': '.-.',
                    'S': '...',    'T': '-',      'U': '..-',
                    'V': '...-',   'W': '.--',    'X': '-..-',
                    'Y': '-.--',   'Z': '--..'   }
    
    def process(self, msg):
        	
        morse_msg = ''
        pause = AudioSegment.silent(duration=500)
        morse_sound = pause
        
        for word in msg.split():
            for char in word:
                morse_msg += self.CODE[char.upper()] + '  '
                sound_name = char.lower() + ".mp3" 
                print(sound_name)
                sound = AudioSegment.from_mp3(sound_name)
                
                # Concatenation is just adding
                morse_sound += sound
                
                # writing mp3 files is a one liner
                morse_sound.export("file.mp3", format="mp3")
                    
            morse_msg += '    ' 
            morse_sound += pause            
        return morse_msg
    
        
from tkinter import *
from PIL import ImageTk
import tkinter as tk

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


        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(6):
            self.master.columnconfigure(c, weight=1)
        
        Frame1 = self.make_frame(0, 0, 3, 2)
        Frame2 = self.make_frame(3, 0, 3, 1)
        Frame3 = self.make_frame(0, 2, 3, 4)
        Frame4 = self.make_frame(3, 2, 3, 4)
        Frame5 = self.make_frame(3, 1, 3, 1)
     
        self.make_button(Frame1, "play.png", 0)
        self.make_button(Frame2, "stop.png", 1)
        self.make_button(Frame5, "pause.png", 2)
        
        
        self.input = tk.LabelFrame(Frame3, text=" Input text ")
        self.textvar = tk.StringVar()
        self.textbox = tk.Text(self.input, height=4, width=50, font=("TkDefaultFont", 14), wrap='word', undo=True)
        self.textbox.pack(expand=1, fill="both", padx=5, pady=5)
        self.input.pack(expand=1, fill="both", padx=5, pady=5)
        
        button2 = tk.Button(self.input, text="Generate morse code", command=lambda: self.generate_morse())
        button2.pack(side=tk.LEFT, expand=1, fill="both", padx=5, pady=5)
        
        
        self.output = tk.LabelFrame(master, text=" Hide text status ")
        self.status_message = tk.StringVar()
        self.status_message.set('\n No text is hidden yet\n')
        
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
        if i==0: 
            b.config(image=image, command=lambda: self.play(self.pause_state))
        elif i==1: 
            b.config(image=image, command=lambda: self.stop())
        else: 
            b.config(image=image, command=lambda: self.pause(self.pause_state))
        
        b.image = image
        b.pack(side="top", fill="both", expand=True)
        
        
    def play(self, pause):
        print("play")
        if pause == 0:
            mixer.init()
            mixer.music.load('file.mp3')
            mixer.music.play()
        else:
            mixer.music.unpause()


        
    def stop(self):
        print("stop")
        mixer.music.stop()
        self.pause_state = 0

        
    def pause(self, pause):
        print("pause")
        mixer.music.pause()
        pause = 1
                
    def generate_morse(self):
        print("morse")
        self.morse_coder = morse_logic()
        msg = self.textbox.get("1.0", tk.END)
        morse_code = self.morse_coder.process(msg)
        self.status_message.set(morse_code)



def main():
    root = Tk()
    app = Application(master=root)
    
    xyla = [0, 0, 950, 250]
    root.title("Morse Coder")
    root.minsize(xyla[2], xyla[3])
    #root.resizable(0, 0)
    root.configure(background='black')
    #root.geometry("%dx%d+%d+%d" % (xyla[0], xyla[1], 400, 100))
    
    app.mainloop()


if __name__ == "__main__":
    main()
