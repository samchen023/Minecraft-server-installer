import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

bar = ttk.Progressbar(root,length=150,mode='indeterminate',orient='horizontal')
bar.pack(pady=20)
bar.start(20)

root.mainloop()