import PySimpleGUI as sg

label=sg.Text("My Text")
box=sg.InputText(tooltip="this is tool tip")
window = sg.Window('MY First GUI',layout=[[label],[box]])
window.read()
window.close()