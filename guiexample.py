import PySimpleGUI as sg

BUTTON_QUIT = 'Quit'

# All the stuff inside your window.
layout = [  [sg.Text("What's your name?",key="Question")],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button(BUTTON_QUIT,key="QUIT_KEY")] ]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == "QUIT_KEY":
        break

    window['Question'].update('Hello ' + values[0] + '!', text_color='red')

window.close()
