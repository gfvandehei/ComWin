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
            #this connects the thread to a varaible
            mainapp.output.insert(INSERT,mainapp.output_message+"\n")
            mainapp.output_message=""
        if(mainapp.connect_var==1):
            mainapp.output.insert(INSERT, "paired successfully with {}".format(mainapp.addr))
            mainapp.connect_var=0

        
    root.destroy()
