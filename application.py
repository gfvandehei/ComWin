from Tkinter import *

class WinComGUI(Frame):
    def createWidgets(self):
        #area for initializing components of GUI
        self.quit_button=Button(self)
        self.quit_button["text"]="Exit"
        self.quit_button["command"]=self.quit
        self.quit_button.pack()

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
