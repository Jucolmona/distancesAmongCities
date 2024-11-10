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
def deployAListAsTable(f, gc):
    """
    :param f: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :return: a view-table of cities, which is implemented the Shortest path algorithm
    """
    head = Label(f, text="Ciudades", width=10)
    head.pack(side=TOP)
    for i in range(1, 8):
        entryCity = Listbox(f, width=10)
        #entryCity.grid(row=i + 1, column=1)
        entryCity.insert(END, gc[i - 1])
        entryCity.pack()
#...................................................................................................
def deployAMatrixATable(f, m):
    """
    :param f: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :param m: matrix which be deployed as a table on the GUI
     :return: a view-table of cities, which is implemented the Shortest path algorithm
    """
    listHead = ["NODO 1", "NODO 2", "VALOR"]
    for i in range(len(listHead)):
        head = Entry(f, width=20)
        head.pack(side=TOP)
        head.insert(0, listHead[i])

    for r in range(len(m)):
        for c in range(len(m[r])):
            registryEntry = Listbox(f, width= 20)
            #registryEntry.grid(row=r+1, column=c+1)
            registryEntry.insert(END, m[r][c])
            registryEntry.pack()

def setObjectsOnGrid(w, r, c):
    """
    :param w: widget (object), which will be located on grid
    :param r: row of grid object inside of root windows
    :param c: column of grid object inside of root windows
    :return:
    """
    w.grid(row=r, column=c)






