

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import PySimpleGUI as sg
import os
import csv

font1 = ("Courier", 10)

input_messages_frame1 = ['Choose a template file','Choose a parameter file']
input_messages_frame2 = ['Choose a json file']

pretty_print_size = len(max(input_messages_frame1, key=len))
pretty_print = "{:<"+ str(pretty_print_size) +"}"

pretty_print_size2 = len(max(input_messages_frame2, key=len))
pretty_print2 = "{:<"+ str(pretty_print_size2) +"}"


layout_instantiate = [[sg.T("")],
          [sg.Text(pretty_print.format(input_messages_frame1[0]) , font=font1) , sg.Input(key="-IN1-", change_submits=True), sg.FileBrowse(key="-IN11-")],
          [sg.Text(pretty_print.format(input_messages_frame1[1]) , font=font1) , sg.Input(key="-IN2-", change_submits=True), sg.FileBrowse(key="-IN22-")],
          [sg.Button("Submit", key="submit_instantiate")]]

layout_patternize = [[sg.T("")],
          [sg.Text(pretty_print2.format(input_messages_frame2[0]) , font=font1) , sg.Input(key="-IN1-", change_submits=True), sg.FileBrowse(key="-IN11-")],
          [sg.Button("Submit", key="submit_patternize")]]

tab_group = [[sg.TabGroup([[sg.Tab('Instantiate JSON', layout_instantiate, element_justification= 'center')], [sg.Tab('Patternize JSON', layout_patternize, element_justification= 'center')]], tab_location='centertop', border_width=5)]]


###Building Window
#window = sg.Window('JSON Flatter', layout, size=(600, 150))
sg.set_options(font=font1)
window =sg.Window("Tabs", tab_group)
#window = sg.Window('File creation from pattern & parameters', layout)




while True:
    event, values = window.read()
    print(values["-IN2-"])
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])
        with open(values["-IN-"], encoding='utf-8') as fh:
            data = js.load(fh)
       #data = js.load(open(values["-IN-"]))
        norm_data = pd.json_normalize(data)
        data_transposed = norm_data.transpose()
        outputname = os.path.splitext(values["-IN-"])[0] + '_output.csv'

        while True:
            try:
                data_transposed.to_csv(outputname, header=True, sep=";", index=True, encoding='utf-8')
                break
            except Exception as e:
                sg.popup(e)
                print(e)

        inputfile = csv.reader(open(outputname, 'r', encoding='utf-8'))
        outputfile = open(outputname + '_', 'w', encoding='utf-8')
        i = 0
        outputfile.write('PARAM;VALUE' + '\n')
        try:
                for row in inputfile:
                    place = row[0].replace('.', '_')
                    print(place)

                    while True:
                        try:
                            outputfile.write(place + '\n')
                            break
                        except Exception as e:
                            sg.popup(e)
                            print(e)
                    i += 1
        finally:
            outputfile.close()

        exit()
