import tkinter as tk
from tkinter import ttk
from tkinter.tix import WINDOW
from tkinter import *
from tkinter.filedialog import askdirectory
import wget
import webbrowser
import os
import subprocess

APP_VERSION = "v0.0.1"

def selectPath():
    path_ = askdirectory()
    if path_:
        path.set(path_)
    return path_

def download():
    with open('download.txt') as f:
        links = f.read().splitlines()

    versions = [link.split('/n')[0] for link in links]

    for i, version in enumerate(versions):
        print(f"{i}: {version}")

    selected_index = box.current()
    if selected_index >= 0 and selected_index < len(links):
        selected_link = links[selected_index]
        selected_link_parts = selected_link.split(' ')
        selected_link = ' '.join(selected_link_parts[1:])
        selected_path = path.get()

        if os.path.isdir(selected_path):
            wget.download(selected_link, out=os.path.join(selected_path, selected_link.split('/')[-1]))
        else:
            print("Invalid path or directory does not exist.")

    else:
        error = "没有找到所选链接！"
        print(error)
    

##infowindow
def createinfoWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("400x200")
    newWindow.title("Info")
    label = ttk.Label(newWindow, text="Made by Samchen023")
    label.pack(side="top")
    version_label = ttk.Label(newWindow, text=f"App Version: {APP_VERSION}")
    version_label.pack()
    link1 = Label(newWindow, text="Github", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind(
        "<Button-1>", lambda e: callback("https://github.com/samchen023/control-center")
    )

def callback(url):
    webbrowser.open_new(url)

def javacheck():
    subprocess.run('python','javacheck.py')

root=tk.Tk()
root.title("Minecraft架設器")
root.geometry("600x350")

menu=tk.Menu(root)
root.config(menu=menu)

submenu1=tk.Menu(activebackground="gray",tearoff=0)
menu.add_cascade(label="File", menu=submenu1)

submenu1.add_command(label="INFO", command=createinfoWindow)
submenu1.add_command(label="EXIT", command=root.destroy)


serverversion=tk.Label(root,text="版本選擇")
serverversion.pack()
box = ttk.Combobox(root,
                    width=15,
                    values=['1.19.4','1.19.3','1.19.2','1.19.1','1.19','1.18.2','1.18.1','1.18','1.17.1','1.17','1.16.5','1.16.4','1.16.3','1.16.2','1.16.1','1.16','1.15.2','1.15.1','1.15','1.14.4','1.14.3','1.14.2','1.14.1','1.14','1.13.2','1.13.1','1.13','1.12.2','1.12.1','1.12','1.11.2','1.11.1','1.11','1.10.2','1.10.1','1.10','1.9.4','1.9.3','1.9.2','1.9.1','1.9',])
version=box.get()
box.pack(pady=5)

path= StringVar()

frame = tk.Frame(root)
frame.pack()

pathlable=tk.Label(frame,text="目標路徑")
pathlable.grid(column=0,row=0,padx=5) 

pathentry=tk.Entry(frame,textvariable=path,width=40)
pathentry.grid(column=1,row=0,pady=5) 

pathbutton=tk.Button(frame,text="路徑選擇",command=selectPath)
pathbutton.grid(column=2,row=0,pady=5,padx=5) 

btn = tk.Button(root, text='下載',command=lambda: download())
btn.pack(pady=5,ipady=5,ipadx=60)     

java17check=tk.Checkbutton(root, text='java 17 (版本1.17以後)')
java17check.pack()
java8check=tk.Checkbutton(root, text='java 8 (版本1.16.4以前)')
java8check.pack()


root.mainloop()