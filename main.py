from tkinter import *
from application import WinComGUI
import socket

if __name__=="__main__":
    root=Tk()    
    mainapp=WinComGUI(master=root)

    while(True):
        mainapp.update_idletasks()
        mainapp.update()
        if(mainapp.output_message!=""):
            mainapp.output.insert(INSERT,mainapp.output_message+"\n")
            mainapp.output_message=""
        
    root.destroy()
