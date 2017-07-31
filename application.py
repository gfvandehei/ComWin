from tkinter import *

class WinComGUI(Frame):

    def printInput(self):
        '''
        this works sort of, it wont print until the program is closed
        '''
        input_string=self.user_input.get()
        self.read_window.insert(INSERT, input_string)#this outputs text to the text box
        print(input_string)
        
    def createWidgets(self):
        #area for initializing components of GUI
        self.quit_button=Button(self)
        self.quit_button["text"]="Exit"
        self.quit_button["command"]=self.quit
        self.quit_button.pack()
        #this part has to do with user input
        self.user_input=Entry() #makes user input window area
        self.user_input.pack()
        self.input_button=Button(self)
        self.input_button["text"]="Read Text"
        self.input_button['command']=self.printInput
        self.input_button.pack()
        #end of user input
        #start of readfromserver
        self.read_window=Text()
        self.read_window.pack()
        #end of readfromserver

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
