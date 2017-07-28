from Tkinter import *
from application import WinComGUI

if __name__=="__main__":
    root=Tk()
    mainapp=WinComGUI(master=root)
    mainapp.mainloop()
    root.destroy()
