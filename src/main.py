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

    #configurateGUI[0] --> frameTOP
    #configurateGUI[1] --> frameBOTTOM
    #configurateGUI[2] --> frameListCities
    #configurateGUI[3] --> frameListRoute
    #configurateGUI[4] --> labelSetRoute
    #configurateGUI[4] --> labelResult
    configurateGUI = [
        {"bgC":"#5dade2", "h":300, "w":950},
        {"bgC":"#5dade2", "h":100, "w":950},
        {"bgC": "#DAF7A6", "h": 300, "w": 300},
        {"bgC":"#FF5733", "h":300, "w":600},
        {"bgC": "#DAF7A6", "h": 100, "w": 300},
        {"bgC": "#FF5733", "h": 100, "w": 600}
    ]

    mainWindow = createMainWindow()

    citiesGraph = createGrahpCities(citiesList, distancesList)
    lc = listCities(citiesGraph)
    mr = matrixRoutes(citiesGraph)

    frameTOP = implementingFrame(mainWindow, configurateGUI[0])
    frameBOTTOM = implementingFrame(mainWindow, configurateGUI[1])
    frameListCities = implementingFrame(frameTOP, configurateGUI[2])
    frameListRoute = implementingFrame(frameTOP, configurateGUI[3])
    frameSetRoute = implementingFrame(frameBOTTOM, configurateGUI[4])
    frameResult = implementingFrame(frameBOTTOM, configurateGUI[5])
    deployAListAsTable(frameListCities, lc)
    deployAMatrixATable(frameListRoute, mr)

    #labelTitleCities = implementingLabel(frameListCities, configurateGUI[1])

    # Spacial Distribution.................................................................
    frameTOP.pack(side=TOP, pady=10)
    frameBOTTOM.pack(side=BOTTOM, pady=10)
    frameListCities.pack(side=LEFT)
    frameListRoute.pack(side=LEFT)
    frameSetRoute.pack(side=LEFT)
    frameResult.pack(side=RIGHT)

    #labelTitleCities.grid(row = 1, column = 1, padx=configurateGUI[0]["pdx"], pady=configurateGUI[0]["pdy"])

    mainWindow.mainloop()

    shRoute = getShortestPath(citiesGraph, 1, 6)
    print(shRoute)
