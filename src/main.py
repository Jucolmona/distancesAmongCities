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


    citiesGraph = createGrahpCities(citiesList, distancesList)
    lc = listCities(citiesGraph)
    mr = matrixRoutes(citiesGraph)

    """----------- GUI Implementing -----------
                    General Layout             """

    configFrameTOP = {"bg":"#5dade2", "h":300, "w":950}
    frameTOP = implementingFrame(mainWindow, configFrameTOP)
    configFrameBOTTOM = {"bg":"#5dade2", "h":100, "w":950}
    frameBOTTOM = implementingFrame(mainWindow, configFrameBOTTOM)
    configFrameListCities = {"bg": "#DAF7A6", "h": 300, "w": 300}
    frameListCities = implementingFrame(frameTOP, configFrameListCities)
    configFrameListRoute = {"bg":"#FF5733", "h":300, "w":600}
    frameListRoute = implementingFrame(frameTOP, configFrameListRoute)
    configFrameSetRoute = {"bg": "#DAF7A6", "h": 100, "w": 300}
    frameSetRoute = implementingFrame(frameBOTTOM, configFrameSetRoute)
    configFrameResult = {"bg": "#FF5733", "h": 100, "w": 600}
    frameResult = implementingFrame(frameBOTTOM, configFrameResult)


    """--- Deploy a data ---"""
    deployAListAsTable(frameListCities, lc)
    deployAMatrixATable(frameListRoute, mr)

    implementingLabel(frameSetRoute,"Inicio", {"w":15, "h":1}).pack()
    dropDownListCities(frameSetRoute, lc)
    implementingLabel(frameSetRoute, "Destino", {"w": 15, "h": 1}).pack()
    dropDownListCities(frameSetRoute, lc)
    implementinButton(frameSetRoute, "Calcular ruta", {"w": 15, "h": 1}).pack()


    """--- Spacial Distribution ---"""
    frameTOP.pack(side=TOP, pady=10)
    frameBOTTOM.pack(side=BOTTOM, pady=10)
    frameListCities.pack(side=LEFT)
    frameListRoute.pack(side=LEFT)
    frameSetRoute.pack(side=LEFT)
    frameResult.pack(side=RIGHT)

    mainWindow.mainloop()

    shRoute = getShortestPath(citiesGraph, 1, 6)

    print(shRoute[1])
    for i in range(len(shRoute[1])):
        k = shRoute[1][i]
        print(citiesGraph.nodes[k]['name'], k)
        for e in citiesGraph.adjacency():
            if k in e[1]:
                print(e[1].get(k))
                print(e[0])
    print(f'Distancia total: {shRoute[0]}')

    for e in citiesGraph.adjacency():
        if 1 in e[1]:
            print(e[1])

