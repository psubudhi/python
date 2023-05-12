import PySimpleGUI as sg
import zipmaker as zip

filechooser=sg.FilesBrowse("Choose files",key="files")
folderchooser=sg.FolderBrowse("Choose folder",key="folder")
outputlabel=sg.Text(key="output")
input1=sg.Input()
input2=sg.Input()
compressbutton=sg.Button("Compress")
label=sg.Text("Compress files into dest folder")
box=sg.InputText(tooltip="this is tool tip")
window = sg.Window('Zip Compressor',layout=[
    [label],
    [input1,filechooser],
    [input2,folderchooser],
    [compressbutton,outputlabel]])
while True:
    events, values=window.read()
    print(events)
    print(values)

    filepaths=values["files"].split(";")
    folder=values["folder"]

    zip.make_archive(filepaths,folder)

    window["output"].update(value="Compression Completed.")

window.close()
