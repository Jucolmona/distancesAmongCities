from programsModules import *
from graphicInterface import *

if __name__ == '__main__':
    citiesList = [(1, {"name":"Medellin"}), (2, {"name":"Puerto Berrio"}),
        (3, {"name": "Puerto Triunfo"}), (4, {"name": "Manizales"}),
        (5, {"name": "Honda"}), (6, {"name": "Ibague"}), (7, {"name": "Girardot"}),
        (8, {"name": "Bogota"})]
    distancesList = [(1, 2, 186), (1, 3, 190), (1, 4, 200), (2, 3, 129), (3, 5, 102),
                     (4, 5, 141), (4, 6, 174), (5, 6, 141), (5, 7, 138), (5, 8, 169),
                     (6, 7, 66), (7, 8, 133)
    ]

    """--- Creating main Windows (root windows) ---"""
    mainWindow = createMainWindow()

    """--- Creating Graph with networkx library
           and list cities and route matrix ---"""

    citiesGraph = createGrahpCities(citiesList, distancesList)
    lc = listCities(citiesGraph)
    mr = matrixRoutes(citiesGraph)

    """----------- GUI Implementing -----------
                    General Layout             """

    configFrameTOP = {"bg":"#657680", "h":350, "w":900}
    frameTOP = implementingFrame(mainWindow, {**configFrameTOP, "highlightbackground": "#444", "highlightthickness": 2})
    configFrameBOTTOM = {"bg":"#657680", "h":150, "w":900}
    frameBOTTOM = implementingFrame(mainWindow, {**configFrameBOTTOM, "highlightbackground": "#444", "highlightthickness": 2})
    configFrameListCities = {"bg": "#657680", "h": 350, "w": 450}
    frameListCities = implementingFrame(frameTOP, {**configFrameListCities, "highlightbackground": "#444", "highlightthickness": 2})
    configFrameListRoute = {"bg":"#657680", "h":350, "w":450}
    frameListRoute = implementingFrame(frameTOP, {**configFrameListRoute, "highlightbackground": "#444", "highlightthickness": 2})
    configFrameSetRoute = {"bg": "#657680", "h": 150, "w": 450}
    frameSetRoute = implementingFrame(frameBOTTOM, {**configFrameSetRoute, "highlightbackground": "#444", "highlightthickness": 2})
    configFrameResult = {"bg": "#657680", "h": 150, "w": 450}
    frameResult = implementingFrame(frameBOTTOM, {**configFrameResult, "highlightbackground": "#444", "highlightthickness": 2})

    """--- Deploy a data ---"""
    deployAListAsTable(frameListCities, lc)
    deployAMatrixATable(frameListRoute, mr)

    """--- Implementing I/O user ---"""
    implementingLabel(frameSetRoute,"Inicio", {"w":5, "h":1}).pack(side=TOP, fill=BOTH, expand=True, pady=5)  #
    source = dropDownListCities(frameSetRoute, lc)
    implementingLabel(frameSetRoute, "Destino", {"w":5, "h":1}).pack(side=TOP, fill=BOTH, expand=True, pady=5)
    target = dropDownListCities(frameSetRoute, lc)
    implementingButton(frameSetRoute, frameResult, "Calcular ruta", source, target, citiesGraph, {"w": 0, "h": 1}).pack()

    """--- Spacial Distribution ---"""
    """--- Main Windows ---"""
    frameTOP.grid(row = 0, column = 1, padx=10, pady=10)
    frameBOTTOM.grid(row = 1, column = 1, padx=10, pady=10)
    """--- Frames, Childrens ---"""
    frameListCities.grid(row = 0, column = 1, padx=10, pady=10)
    frameListRoute.grid(row = 0, column = 2, padx=10, pady=10)
    frameSetRoute.grid(row = 0, column = 1, padx=10, pady=10)
    frameResult.grid(row = 0, column = 2, padx=10, pady=10)

    """ --- Run GUI --- """
    mainWindow.mainloop()

    #print(shRoute)
    #print(getCities(citiesGraph, ("Medellin", "Bogota")))







