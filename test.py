import tkinter as tk
root = tk.Tk()
root.title('my window')
root.geometry('200x150')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

mycheckbutton1 = tk.Checkbutton(root, text='apple',
                                var=var1)
mycheckbutton1.pack()
mycheckbutton2 = tk.Checkbutton(root, text='banana',
                                var=var2)
mycheckbutton2.pack()
mycheckbutton3 = tk.Checkbutton(root, text='orange',
                                var=var3)
mycheckbutton3.pack()

var1.set(True)

root.mainloop()
