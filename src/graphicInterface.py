from tkinter import *
from tkinter import ttk
import networkx as nx


def createMainWindow():
    mainWindows = Tk()
    mainWindows.geometry("1000x500")
    return mainWindows

"""
The following function use the instance of Tk() class created on previous function. 
Therefore, the next functions both add Tk widgets and change the properties of this 
instancia returned for function previusly created.
"""
def implementingFrame(mw:Tk, options:dict):
    """
    :param mw: root window, where frame will be placed
    :param options: dict of diferent options to custom the frame
    :return: Custom frame placed on main window.
    """
    frameTmp = Frame(mw, bg = options["bgC"], height=options["h"], width=options["w"])
    return frameTmp
#...................................................................................................
def implementingLabel(f, options:dict):
    """
    :param f: object-type Frame of Tkinter library. Represent the secundary windows
            of aplication graphic application
    :return: a widget that is integrated in the main windows
    """
    labelTmp = Label(f, text="Nombre Ciudades" , height=options["h"] ,width=options["w"])
    return labelTmp
#...................................................................................................
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

def setObjectsOnGrid(w, r, c):
    """
    :param w: widget (object), which will be located on grid
    :param r: row of grid object inside of root windows
    :param c: column of grid object inside of root windows
    :return:
    """
    w.grid(row=r, column=c)






