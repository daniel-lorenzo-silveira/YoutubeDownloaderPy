
from tkinter import *
import tkinter
from pytubefix import YouTube
from tkinter import filedialog, messagebox


def Download():
  folder = folder_path.get()
  video = YouTube(str(link.get()))
  stream = video.streams.get_highest_resolution()
  stream.download(folder)
  messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
  video = video.streams.get_highest_resolution()


def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

#Create main window
window = Tk()
window.title("Youtube Video Downloader")
window.geometry("500x200")
window.resizable(False,False)

text_instruction = Label(window,text="Insert Youtube URL",width=40, font=("Roboto UI",10, "bold")).pack(pady=8)
#Create a frame to insert label next to folder select button
frame = tkinter.Frame(window)
frame.pack(pady=5)

#Insert input value for the 'link' variable
link = tkinter.StringVar()
link_enter = tkinter.Entry(frame, textvariable=link,width=40)
link_enter.pack(side=tkinter.LEFT, padx=5)

#Select folder button and shows the selected path
tkinter.Button(frame, text="Selecionar Pasta", command=select_folder).pack(side=tkinter.RIGHT)
folder_path = tkinter.StringVar()
tkinter.Label(window, textvariable=folder_path).pack(pady=5)

#Download button with 'Download' function passed as a parameter
button_download = Button(window,text="Download", command=Download).pack(pady=5)

#Fecha a janela
window.mainloop() 

