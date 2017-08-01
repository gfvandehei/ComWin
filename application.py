from tkinter import *

class WinComGUI(Frame):
    def connect_command(self):
        '''
        need a connect function
        '''
        print("conect")#placeholder

    def send_command(self):
        '''
        this works sort of, it wont print until the program is closed
        '''
        print("send")#placeholder
        
    def createWidgets(self):
        connect_Button=Button(self.master, text="Connect", bg="red", command=self.connect_command).grid(row=0, sticky=W)
        send_button=Button(self.master, text="Send     ",bg="green", command=self.send_command).grid(row=1, sticky=W)

        connect_entry=Entry(self.master).grid(row=0, column=0,sticky=W, padx=80)
        send_entry=Entry(self.master).grid(row=1, column=0,sticky=W, padx=80)

        Text(self.master).grid(row=2)
        
            

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.createWidgets()
