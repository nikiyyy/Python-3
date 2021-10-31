import PySimpleGUI as sg     
import quotesForAPI
import HostsModify
import Tasks

def viewBW():
    list1=[]
    for i in HostsModify.listSites():
        if '#' not in i:
            list1.append(i)
    return list1

def viewT():
    list2=[]
    for i in Tasks.listTasks():
        list2.append(i)
    return list2


layout = [  [sg.Button('Generate Quote', size=(17, 1)),sg.Button('Show Blocked websites', size=(17, 1)),sg.Button('Show tasks', size=(17, 1))],     # Part 2 - The Layout
            [sg.Listbox(values=viewT(), size=(62, 6),key='-LBOX-')],
            [sg.Button('Block website', size=(12, 1)),sg.Button('Add Task', size=(12, 1)),sg.Button('Delete Task', size=(12, 1)),sg.Button('Unblock website', size=(12, 1))]
         ]

window = sg.Window('Thought Organiser desktop', layout)     

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    
    if event == 'Show tasks':
        window['-LBOX-'].update(values=viewT())
        
    if event == 'Show Blocked websites':
        window['-LBOX-'].update(values=viewBW())
        
    if event == 'Generate Quote':
        var = quotesForAPI.return_API_qoute()
        sg.popup(var[0] + var[1], title='Inspiring quote')
        
    if event == 'Block website':
        layout2 = [[sg.Text('Enter websote URL'), sg.InputText()],
                   [sg.Button('Block website', size=(13, 1))]]

        window2 = sg.Window('Block website', layout2) 
        event2, values = window2.read() 
        window2.close() 
        if event2 == sg.WIN_CLOSED or event2 == 'Cancel': 
            continue
        HostsModify.addSite(values[0])
        window['-LBOX-'].update(values=viewBW())
    
    if event == 'Add Task':
        layout2 = [[sg.Text('Task'), sg.InputText()],
                   [sg.Text('Type'), sg.InputText()],
                   [sg.Text('priority'), sg.InputText()],
                   [sg.Button('Add task', size=(13, 1))]]

        window2 = sg.Window('Add Task', layout2) 
        event2, values = window2.read() 
        window2.close() 
        if event2 == sg.WIN_CLOSED or event2 == 'Cancel': 
            continue
        Tasks.addTask(values[0], values[1], values[2])
        window['-LBOX-'].update(values=viewT())

    if event == 'Unblock website':
        layout2 = [[sg.Text('Enter website URL'), sg.InputText()],
                   [sg.Button('Unblock website', size=(13, 1))]]
        window2 = sg.Window('Unblock website', layout2) 
        event2, values = window2.read() 
        window2.close() 
        if event2 == sg.WIN_CLOSED or event2 == 'Cancel': 
            continue
        HostsModify.removeSite(values[0])
        window['-LBOX-'].update(values=viewBW())
        
    if event == 'Delete Task':
        layout2 = [[sg.Text('Enter Task ID'), sg.InputText()],
                   [sg.Button('Delete Task', size=(13, 1))]]
        window2 = sg.Window('Delete Task', layout2) 
        event2, values = window2.read() 
        window2.close() 
        if event2 == sg.WIN_CLOSED or event2 == 'Cancel': 
            continue
        Tasks.removeTask(values[0])
        window['-LBOX-'].update(values=viewT())
        
window.close()  