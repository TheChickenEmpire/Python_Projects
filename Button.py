import PySimpleGUI as sg
sg.theme ('dark grey 13')
with open('Button important', 'r')as r:
    s = r.read()
with open('Button important', 'a') as a:
    if s == '':
        a.write('0')
with open('Button important', 'r')as r:
    output = float(r.read())
layout = [[sg.Text(output, size=(10), key='output', expand_x=True), sg.Text('times clicked', size=(10)), ],
           [sg.Button ('Button'),], ]
window = sg.Window('Button clicker', layout, resizable=True, )
while True:
    event, value = window.read()
    output = float(output)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Button':
        output = 1 + output
        window['output'].update(output)
        open('Button important', 'w').close()
        with open('Button important', 'a') as a:
            a.write(str(output))