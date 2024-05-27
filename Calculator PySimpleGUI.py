import PySimpleGUI as sg

sg.theme('Dark Gray 13')

output = ''

layout = [[sg.Text('Calculator')],
          [sg.Text('', size=(10), key='output', expand_x=True)],
          [sg.Button ('7'), sg.Button ('8'), sg.Button ('9')],
          [sg.Button ('4'), sg.Button ('5'), sg.Button ('6')],
          [sg.Button ('1'), sg.Button ('2'), sg.Button ('3')],
          [sg.Button ('0'), sg.Button ('+'), sg.Button ('-')],
          [sg.Button ('*'), sg.Button ('/'), sg.Button ('=')],
          [sg.Button ('.'), sg.Button ('π'),sg.Button ('del'), sg.Button ('Clear')],]

window = sg.Window('Calculator', layout, resizable=True,)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    inputs = list (range(0,10))
    inputs.append('+')
    inputs.append('-')
    inputs.append('*')
    inputs.append('/')
    inputs.append('.')
    for x in inputs:
        if event == str(x):
            output = output + str(x)
            window['output'].update(output)

    if event == 'Clear':
        output = ''
        window['output'].update(output)

    if event == 'π':
        output = output + str(3.14159265359)
        window['output'].update(output)

    if event == 'del':
        output = output[:len(output) -1]
        window['output'].update(output)
    
    if event == '=':
        if output != "":
            try:
                output = str(eval(output))
                window['output'].update(output)
            except:
                output = ''
                window['output'].update("ERROR")

    if event == '.':
        output = output
        window['output'].update(output)