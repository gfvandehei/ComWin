from tkinter import *
import socket
import threading
import sys
import os

class WinComGUI(Frame):
    '''
    responsible for holding the components of the GUI and the functions related
    to it
    '''
    def recieve_data(self):
        '''
        this function is designed to be run in a thread alongside the main loop
        -gets sent message from server prints and prints it to GUI
        '''
        while True:
            data=self.ClientSocket.recv(1024)
            if not data: 
                sys.exit(0)
            self.output_message=data.decode("utf-8")#self.output.insert(INSERT,data.decode("utf-8")+"/n")

    def connect_command(self):
        '''
        this function is in charge of connecting to the server
        socket of another computer also starts thread to recieve server message
        if sucessfully connected
        '''
        address=self.ip_entry.get()
        port=int(self.port_entry.get())
        self.output.insert(INSERT, "attempting to connect to {}:{} \n".format(address,port))
        try:
            self.ClientSocket.connect((address,port))
            self.RecvThread.start()
            self.output.insert(INSERT, "Connection Sucessful \n")
        except:
            self.output.insert(INSERT, "could not connect to {}:{}, please try again \n".format(address,port))

    def send_command(self):
        '''
        This sends a message to a connected client
        '''
        userinput=self.send_entry.get()
        if(self.c==0):
            self.output.insert(INSERT, "you are not yet connected \n")
        else:
            self.c.send(bytes(userinput,"utf-8"))
    
    def exit(self):
        '''
        takes care of safely exiting the program when exit button is pressed
        clicking x button may still not fully exit
        '''        
        self.ClientSocket.close()
        self.ServerSocket.close()        
        os._exit(0)        
        
    def createWidgets(self):
        '''
        populates the GUI
        '''
        self.connect_button=Button( text="Connect", bg="red", command=self.connect_command)
        self.connect_button.grid(row=0, sticky=W)
        self.send_button=Button( text="Send     ",bg="green", command=self.send_command)
        self.send_button.grid(row=1, sticky=W)
        self.exit_button=Button(text="Exit", command=self.exit)
        self.exit_button.grid(row=0,sticky=E)

        self.ip_entry=Entry()
        self.ip_entry.grid(row=0, column=0,sticky=W, padx=80)
        self.port_entry=Entry()
        self.port_entry.grid(row=0,column=0,sticky=E,padx=150)
        self.send_entry=Entry()
        self.send_entry.grid(row=1, column=0,sticky=W, padx=80)

        self.output=Text()
        self.output.grid(row=2)
        
    def pair(self):
        '''
        allows the server to take clients while still running other
        function, is made to be run in a thread
        '''
        while(True):
            self.c,self.addr=self.ServerSocket.accept()
            if(self.c!=0):
                self.connect_var=1
                break

    def __init__(self,master=None):
        self.exitflag=0
        self.connect_var=0
        self.master=master
        self.output_message=""
        Frame.__init__(self, master)
        host=socket.gethostname()#socket.gethostbyname(socket.gethostname())
        print(host)#used for debugging
        port=12345
        self.c,self.addr=0,0
        self.createWidgets()
        self.ClientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ServerSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ServerSocket.bind((host,12345))
        self.ServerSocket.listen(5)
        self.RecvThread=threading.Thread(target=self.recieve_data)
        self.PairThread=threading.Thread(target=self.pair)
        self.PairThread.start()
