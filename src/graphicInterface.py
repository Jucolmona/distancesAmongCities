from tkinter import *
from tkinter import ttk

mainWindows = Tk()
mainWindows.geometry("1000x500")
mainWindowsFrame = Frame(mainWindows, bg='blue')
mainWindowsFrame.pack(fill= BOTH, expand= True, padx= 25, pady=25)

#firtsLabel = Label(mainWindowsFrame,)
firtsLabel = Label(mainWindowsFrame,
                   text="Fila 1 Columna 1",
                   width=300,
                   height=5).grid(row=1, column=1)

#Label(mainWindowsFrame, text="Fila 1 Columna 2", width=15, height=5).grid(row=1, column=2)


mainWindows.mainloop()

