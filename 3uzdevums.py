import PySimpleGUI as sg
sg.theme("DarkBrown6")
menu_def=[["Help",["About"]]]
dalas=[
    [sg.Menu(menu_def)],
    [sg.T("Izvētlies jaukāko gadalaiku")],# atstarpes no malinam
    [sg.Combo(["Pavasaris", "Vasara", "Rudens","Ziema"], key="COMBO", enable_events=True, size=(40,10))],
    [sg.Button("Tava izvēle ir:")],
    [sg.T("", key="vieta")]


]
#loga definicija- definejam objektu logs
logs = sg.Window("Sanijas programma",dalas, size= (600,500))


#galvenai notikumu cilks 
while True:
    event, values= logs.read()

    # ja spiez  Iziet tiek iziets
    if event== sg.WIN_CLOSED or event == "Iziet": # tas pats ar WINDOW_CLOSED
        break

# kada veida varam noteikt kas ir izvelets
   
    elif event=="Tava izvēle ir:":
        mana_izvele=values["COMBO"]
        logs["vieta"].update(f"Tu izvēlējies:{mana_izvele}")
    
    elif event== "About...":
        sg.popup("Sanija Sokirka")
logs.close()


