import PySimpleGUI as sg
sg.theme("LightGreen2")
dalas = [
    [sg.Text("ievadiet vārdu"), sg.InputText(key="vards")],
    [sg.Text("ievadiet uzvārdu"), sg.InputText(key="uzvards")],
    {sg.Multiline(size=(50,10), key="Multilains", disabled=True)}, # ja liek sito tas nevar neko ierakstit taja vairakrindu ievadee
    [sg.Button("Print"),sg.Button("Iziet")]

]
#loga definicija- definejam objektu logs
logs = sg.Window("Sanijas programma",dalas)
#galvenai notikumu cilks 
while True:
    event, values= logs.read()
    # ja spiez  Iziet tiek iziets
    if event== sg.WIN_CLOSED or event == "Iziet": # tas pats ar WINDOW_CLOSED
        break
    if event == "Print":
        #jasavac visi dati kur tie tika ievaditi
        vards=values["vards"]
        uzvards=values["uzvards"]
        #jaievieto teksts teksta lauka, lai neradas tikai terminalii- ar tikai [    print(f"Labdien, {vards},{uzvards}!")    ]
    logs["Multilains"].update(f"Labdien, tevi sauc {vards},{uzvards}!")
logs.close()

