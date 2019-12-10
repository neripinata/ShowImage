from tkinter import *
from images import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master

        self.init_Window()

    def init_Window(self):
        self.master.title("Bands")
        self.pack(fill=BOTH, expand = 1)
        museButton = Button(self, text="Muse", command = muse)
        museButton.place(x=70,y=0)
        interpolButton = Button(self, text="Interpool", command = interpol)
        interpolButton.place(x=63,y=25)
        beachButton = Button(self, text="Beach House", command = beachHouse)
        beachButton.place(x=52,y=50)


def main():
    root = Tk()
    root.geometry("200x150")
    app = Window(root)
    root.mainloop()

