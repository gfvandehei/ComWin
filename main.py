from tkinter import *
from application import WinComGUI
import socket


if __name__=="__main__":
    root=Tk()
    #try to connect
    recsock=socket.socket()
    addr="192.168.1.181"
    try:
        recsock.connect((addr,12345))
        print(recsock.recv(1024))
    except:
        print("could not connect")
    
    
    #end of connection
    mainapp=WinComGUI(master=root)
    #mainapp.mainloop()
    while(True):
        mainapp.read_window.insert(INSERT, recsock.recv(1024))
        mainapp.update_idletasks()
        mainapp.update()
    root.destroy()
