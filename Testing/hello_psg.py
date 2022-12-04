# hello_psg.py

import PySimpleGUI as sg

layout = [
    [sg.Text("Hellow From PySimpeleGUI")],
    [sg.Button("OK")]
]
margins =  (100,50)
#creat the window
window = sg.Window(title="My Calendar", layout, margins)
#sg.Window(title="Hello World", layout = [[]], margins = (100,50)).read()
#create an event loop 
while True: 
    event, values = window.read()
    # End program is user closes window or 
    # pressed the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    
window.close()
    