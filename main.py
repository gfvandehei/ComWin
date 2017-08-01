from tkinter import *
from application import WinComGUI
import socket


if __name__=="__main__":
    root=Tk()
    #try to connect
    recsock=socket.socket()
    try:
        recsock.connect((socket.gethostname(),12345))
        print(recsock.recv(1024))
    except:
        print("could not connect")
    
    
    #end of connection
    mainapp=WinComGUI(master=root)
    #mainapp.mainloop()
    while(True):
        mainapp.update_idletasks()
        mainapp.update()
        mainapp.read_window.insert(INSERT, recsock.recv(1024))
    root.destroy()
