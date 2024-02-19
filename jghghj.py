import PySimpleGUI as sg
sg.theme("Lightbrown2")
#izveidot menu mainigo
menu_def=[["File",["Iziet"]],["Edit"]] #liek masivus masiva ar [x1,[x2]], neatvers vala logu ja nav pareizas iekavas, bet radis kluda pie read.90- nozime pirmā koda daļa kludaina
dalas = [
    [sg.Menu(menu_def)],
    [sg.T("")],# atstarpes no malinam
    [sg.T("     "), sg.Button("Sveiki!",size=(8,4)),sg.T("   "),sg.Button("Nekas", size=(8,4))],#var ari rakstit "T" nevis text
    [sg.T("")],
    [sg.T("   "), sg.Checkbox("Drukāt", default=False, key="IN")],# lai zinatu vai ievadits vai ne? kad rosas problema kad tu neatceries vai ievadiji
    [sg.T("   "), sg.Radio("Ir atļauja", 'Radio1', default=False, key='IN2')], # grupas indifikators- ja man ir divas radio pogas un adiopogam jabut ir vienadam lai mes grupetu, grupet- no divam radio pogam vares iekekset tikai vienu. 
    [sg.T("   "), sg.Radio("Nav atļauja", 'Radio1', default=False, key='IN3')],
    [sg.T("")],
    {sg.Multiline(size=(40,10), key="Multilains", disabled=True)}, # ja liek sito tas nevar neko ierakstit taja vairakrindu ievadee
    [sg.Button("Print"),sg.Button("Iziet")]


]
#loga definicija- definejam objektu logs
logs = sg.Window("Sanijas programma",dalas, size= (600,500))# ja screen size par mazu- visi elementi var neparadities


#galvenai notikumu cilks 
while True:
    event, values= logs.read()

    # ja spiez  Iziet tiek iziets
    if event== sg.WIN_CLOSED or event == "Iziet": # tas pats ar WINDOW_CLOSED
        break


    elif event=="Sveiki!":
    #keksim pie 'drukat' un radio pie 'ir atlauja'
        if values["IN"]==True and values["IN2"]:# parada ka pieskirtajai pogai IN- chckboks ir true
         logs["Multilains"].update("Labrit!")# ievavas updatam ieraksta ko atjaunos
    
    




    """ if event == "Print":

        #jasavac visi dati kur tie tika ievaditi
        vards=values["vards"]
        uzvards=values["uzvards"]"""
        #jaievieto teksts teksta lauka, lai neradas tikai terminalii- ar tikai [    print(f"Labdien, {vards},{uzvards}!")    ]

logs.close()
