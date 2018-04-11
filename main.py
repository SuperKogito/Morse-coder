from tkinter import *
from gui import Application


def main():
    root = Tk()
    app = Application(master=root)

    root.title("Morse Coder")
    root.minsize(950, 250)
    app.mainloop()


if __name__ == "__main__":
    main()
