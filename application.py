from tkinter import *
import socket

class WinComGUI(Frame):
    def connect_command(self):
        #connects socket to server
        address=self.ip_entry.get()
        port=self.port_entry.get()
        self.output.insert(INSERT, "attempting to connect to {}:{} \n".format(address,port))

    def send_command(self):
        '''
        this works sort of, it wont print until the program is closed
        '''
        print("send")#placeholder
        
    def createWidgets(self):
        self.connect_button=Button( text="Connect", bg="red", command=self.connect_command)
        self.connect_button.grid(row=0, sticky=W)
        self.send_button=Button( text="Send     ",bg="green", command=self.send_command)
        self.send_button.grid(row=1, sticky=W)

        self.ip_entry=Entry()
        self.ip_entry.grid(row=0, column=0,sticky=W, padx=80)
        self.port_entry=Entry()
        self.port_entry.grid(row=0,column=0,sticky=E,padx=150)
        self.send_entry=Entry()
        self.send_entry.grid(row=1, column=0,sticky=W, padx=80)

        self.output=Text()
        self.output.grid(row=2)
        
            

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.createWidgets()
        ClientSocket=socket.socket()
