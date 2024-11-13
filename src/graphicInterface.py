from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

import networkx as nx


def createMainWindow():
    """
    This function create a main windows of GUI of aplications
    """
    mainWindows = Tk()
    mainWindows.geometry("1000x500")
    return mainWindows

"""
The following function use the instance of Tk() class created on previous function. 
Therefore, the next functions both add Tk widgets and change the properties of this 
instancia returned for function previusly created.
"""
#.................................................................................
def implementingFrame(mw, dictConf={}):
    """
    Implement the Frame widget of Tkinter Library along with basic options for its configuration
    :param mw: root window, where frame will be placed
    :param dictConf: dict of diferent options to custom the frame
    :return: Custom frame placed on main window.
    """
    frameTmp = Frame(mw)
    frameTmp.config(bg=dictConf.get("bg", "#c2c2c2"),
                    height=dictConf.get("h", 5),
                    width=dictConf.get("w", 5))
    return frameTmp
#.................................................................................
def implementingLabel(f, t, dictConf={}):
    """
    :param f: object-type Frame of Tkinter library. Represent the secundary windows
            of aplication graphic application
    :param t: text, that will be show for label widget
    :return: a widget that is integrated in the main windows
    """
    labelTmp = Label(f, text=t)
    labelTmp.config(bg=dictConf.get("bg", "#c2c2c2"),
                    height=dictConf.get("h", 5),
                    width=dictConf.get("w", 5))
    return labelTmp
#.................................................................................
#...................................................................................................
def deployAListAsTable(f, l):
    """
    :param: l list-type object that contains the entries of a table
    :param f: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :return: a view-table of cities, which is implemented the Shortest path algorithm
    """
    dictConfigHead = {"h":1, "w":20}
    head = implementingLabel(f, "Ciudades", dictConfigHead)
    head.pack(side=TOP, expand=True)
    for i in range(len(l)):
        entryCity = implementingLabel(f, l[i])
        entryCity.pack(side=TOP, fill=BOTH)
        entryCity.config(width="15", height="1")
#...................................................................................................
def deployAMatrixATable(f, m):
    """
    :param f: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :param m: matrix which be deployed as a table on the GUI
     :return: a view-table of cities, which is implemented the Shortest path algorithm
    """
    frameTableHead = implementingFrame(f) #Frame(f)
    frameTableHead.pack(side=TOP)
    listHead = ["INICIO", "DESTINO", "DISTANCIA"]
    for i in range(len(listHead)):
        Label(frameTableHead, text=listHead[i], height= "1", width="15").pack(side=LEFT, expand=True)

    canvas = Canvas(f, scrollregion=(0,100,0,100))
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(f, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    frameTableBody = implementingFrame(canvas)
    canvas.create_window((0, 0), window=frameTableBody, anchor="nw")

    canvas['yscrollcommand'] = scrollbar.set

    for r in range(len(m)):
        for c in range(len(m[r])):
            if r%2==0:
                Label(frameTableBody, text=m[r][c], height="1", bg="#e7e9eb", width="15").grid(row=r, column=c)
            else:
                Label(frameTableBody, text=m[r][c], height="1", bg="#c7c8c8", width="15").grid(row=r, column=c)

    #frameTableBody.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))
#.......................................................................................................
def dropDownListCities(f, l):
    """
    :param: l list-type object that contains the entries of a drop-Down List
    :param f: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :return: a drop-Down List of cities, which is set as source and target in the Shortest path algorithm
    """
    menuTmp = Combobox(f, state="readonly", values=l)
    menuTmp.pack()
#.......................................................................................................
def setObjectsOnGrid(w, r, c):
    """
    :param w: widget (object), which will be located on grid
    :param r: row of grid object inside of root windows
    :param c: column of grid object inside of root windows
    :return:
    """
    w.grid(row=r, column=c)






