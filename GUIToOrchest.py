#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PySimpleGUI as sg
import requests
import json
import subprocess


def gui2():
    #Sets up Interface
    layout = [
              [ sg.Multiline(size=(90,20),background_color='black',text_color='white',reroute_stdout=True,reroute_stderr=True,autoscroll = True)], #Output text grid
              [sg.Input(enable_events=True, key='-in-')], #enables input to be saved in input field
              [sg.Button('Do things'), sg.Button('Exit')] #start button and exit button
             ]
    
    window = sg.Window("Jackie Chan System", layout, finalize = True) #sets up application window
    
    initialString = "Hello, welcome to our Jackie Chan chatbot"
    print(initialString)
    
    #While the interface is running:
    while True:
        event, values = window.read()
        #If Exit button is clicked, break the loop and close interface.
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        #Maximises amount of characters within input field
        if len(values['-in-']) > 480:
            window.Element('-in-').Update(values['-in-'][:-1])
        #If the start button is pressed (Do things) run this code:
        if event == 'Do things':
            #Saves values stored in input field to variable input
            input = values["-in-"]
            #Save the input values in the input.txt file
            with open('input.txt','r+') as myfile:      
                data = myfile.read()                                                                                              
                myfile.seek(0)                                                                                                    
                myfile.write(input)                                                                                           
                myfile.truncate()                                                                                                 
            print("User: ", input)
            #Calls the Orchestrator
            exec(open("Orchest.py").read())
    window.close() 
gui2()

