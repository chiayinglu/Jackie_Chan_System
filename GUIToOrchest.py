#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PySimpleGUI as sg
import requests
import json
import subprocess

initialString = "Hello, welcome to our Jackie Chan chatbot"

def gui2():
    layout = [
              [ sg.Multiline(size=(90,20),background_color='black',text_color='white',reroute_stdout=True,reroute_stderr=True,autoscroll = True)],
              [sg.Input(enable_events=True, key='-in-')],
              [sg.Button('Do things'), sg.Button('Exit')]
             ]
    
    window = sg.Window("Thrash fish go brrr", layout, finalize = True)
    
    #window.read()  #I need to press a button before the text will display
    #window.refresh() #doesn't refresh the output
    print(initialString)
    #window.refresh() #doesn't refresh the output
    
    while True:
        event, values = window.read() 
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if len(values['-in-']) > 480:
            window.Element('-in-').Update(values['-in-'][:-1])
        if event == 'Do things':
            print(values['-in-'])
            #### Saves input from interface to text file on local machine
            input = values["-in-"]                                      
            with open('input.txt','r+') as myfile:      
                data = myfile.read()                                                                                              
                myfile.seek(0)                                                                                                    
                myfile.write(input)                                                                                           
                myfile.truncate()                                                                                                 
            #### ####
            #subprocess.call("Orchest.py", shell= True)
            exec(open("Orchest.py").read())
            print("\n You pressed the button")
    window.close() 
gui2()

