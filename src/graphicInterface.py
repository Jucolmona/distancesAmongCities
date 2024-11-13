from tkinter import *
from tkinter import ttk
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
def implementingFrame(mw:Tk, options:dict):
    """
    :param mw: root window, where frame will be placed
    :param options: dict of diferent options to custom the frame
    :return: Custom frame placed on main window.
    """
    frameTmp = Frame(mw, bg = options["bgC"], height=options["h"], width=options["w"])
    return frameTmp
#.................................................................................
#.................................................................................
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
    head = Label(f, text="Ciudades", width="20")
    head.pack(side=TOP, expand=True)
    for i in range(1, 8):
        entryCity = Listbox(f)
        #entryCity.grid(row=i + 1, column=1)
        entryCity.insert(END, gc[i - 1])
        entryCity.pack()
        entryCity.config(width="15", height="1")
#...................................................................................................
def deployAMatrixATable(f, m):
    """
    :param f: object-type Frame of Tkinter library. Represent the main windows of aplication graphic application
    :param m: matrix which be deployed as a table on the GUI
     :return: a view-table of cities, which is implemented the Shortest path algorithm
    """
    frameTableHead = Frame(f)
    frameTableHead.pack(side=TOP)
    listHead = ["INICIO", "DESTINO", "DISTANCIA"]
    for i in range(len(listHead)):
        Label(frameTableHead, text=listHead[i], height= "1", width="15").pack(side=LEFT, expand=True)

    scrollbar = Scrollbar(f, orient=VERTICAL)
                          #, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas = Canvas(f, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)


    frameTableBody = Frame(canvas)
    canvas.create_window((3, 3), window=frameTableBody, anchor="nw")

    for r in range(len(m)):
        for c in range(len(m[r])):
            if r%2==0:
                Label(frameTableBody, text=m[r][c], height="1", bg="#e7e9eb", width="15").grid(row=r, column=c)
            else:
                Label(frameTableBody, text=m[r][c], height="1", bg="#c7c8c8", width="15").grid(row=r, column=c)

    #frameTableBody.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

#.......................................................................................................
def setObjectsOnGrid(w, r, c):
    """
    :param w: widget (object), which will be located on grid
    :param r: row of grid object inside of root windows
    :param c: column of grid object inside of root windows
    :return:
    """
    w.grid(row=r, column=c)






