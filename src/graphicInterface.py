from tkinter import *
from tkinter import ttk
import networkx as nx


def createMainWindow():
    mainWindows = Tk()
    mainWindows.geometry("1000x500")
    mainWindowsFrame = Frame(mainWindows) #, bg='blue')
    #mainWindowsFrame.pack(fill= BOTH, expand= True, padx= 25, pady=25)
    return mainWindowsFrame

def implementingLabel(mw, r, c, data):
    """
    :param r: row of grid object inside of label
    :param c: column of grid object inside of label
    :param mw: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :return: a widget that is integrated in the main windows
    """
    #firtsLabel = Label(mainWindowsFrame,)
    firtsLabel = Label(mw, text=data , width=300,height=5).grid(row=r, column=c)
    return firtsLabel
def deployAListOfCities(mw, gc):
    """

    :param mw: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :return: a view-table of cities, which is implemented the Shortest path algorithm
    """
    head = Entry(mw, width=10)
    head.grid(row=1, column=1)
    head.insert(0, "Ciudades")
    for i in range(1, 8):
        entryCity = Entry(mw, width=10)
        entryCity.grid(row=i + 1, column=1)
        entryCity.insert(END, gc[i - 1])
    mw.mainloop()

#Label(mainWindowsFrame, text="Fila 1 Columna 2", width=15, height=5).grid(row=1, column=2)







