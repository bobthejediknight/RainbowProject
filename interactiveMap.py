"""
author: Antonio Marino

Description:
This file creates an interactive map that displays where job sites are
on a map as well as what equipment is stored there.
"""
from graph import *


def GraphWinTwinCities():
    '''Creates the GraphWin object with a map of the twin cities as a background'''
    Win = GraphWin("Rainbow International Interactive Map", 850, 669)
    Win.setCoords(-93603, 44746, -92753, 45222)
    twinCitiesMap = Image(Point((-92753 - 425), (44746 + 238)), 'Road-map-of-the-Twin-Cities-network.png')
    twinCitiesMap.draw(Win)
    return Win

def makeListOfAddresses():
    '''Creates an in order list of all of the addresses of job sites'''
    Addresses = open("OptimalRoute.txt", "r")
    listOfAddrs = Addresses.readlines()
    for i in range(len(listOfAddrs)):
        listOfAddrs[i] = listOfAddrs[i].split(":")[1]

    return listOfAddrs[:-1]

def makeListOfPoints():
    '''Creates an ordered list of all of the points that correspond to job sites on the map'''
    f = open("OptimalRoute.txt", "r")
    fileLines = f.read().split("\n")[:-1]
    listOfPoints = []
    for i in range(len(fileLines)):
        listOfPoints.append(fileLines[i].split(":")[0])
        Coordinates = listOfPoints[i].split(", ")
        listOfPoints[i] = Point(int(float(Coordinates[1]) * 1000), int(float(Coordinates[0]) * 1000))

    listOfPoints.append(listOfPoints[0])
    f.close()
    return listOfPoints

def makeListOfEquipment():
    '''Creates an ordered list of all of the equipment at all of the job site'''
    f = open("OptimalRoute.txt", "r")
    fileLines = f.read().split("\n")[:-1]
    listOfEquipment = []

    for i in range(len(fileLines)):
        listOfEquipment.append(fileLines[i].split(":"))
        Equipment = listOfEquipment[i][2]
        listOfEquipment[i] = Equipment

    f.close()
    return listOfEquipment

def listInfo():
    '''extracts address, point/coordinate, and equipment data for use on map'''
    listOfAddresses = makeListOfAddresses()
    listOfPoints = makeListOfPoints()
    listOfEquipment = makeListOfEquipment()

    return [listOfAddresses, listOfPoints, listOfEquipment]

def drawRedDots(Point, Win):
    '''draws red dots that correspond to job sites on the map'''
    Address1 = Circle(Point, 5)
    Address1.setFill("red")
    Address1.draw(Win)
    return Address1

def drawLines(Point1, Point2, Win):
    '''draws lines between job sites that represent semi-optimal route on the map'''
    route1 = Line(Point1, Point2)
    route1.setFill("blue")
    route1.draw(Win)
    return route1

def drawInfoBoxes(point, Equipment, Address, Win):
    '''draws information boxes with address and equipment data for each job site on the map'''
    InfoBox1 = Rectangle(Point(point.getX() - 50, point.getY() - 50),
                         Point(point.getX() + 50, point.getY() + 50))
    InfoBox1.setFill("white")
    Text1 = Text(point, "Address: " + Address + "\n" + "Equipment:" + Equipment)
    return InfoBox1, Text1

def setShownAndHiddenObjects(Address1, InfoBox1, Text1, point):
    '''initializes which objects are currently being shown or hidden on the map'''
    CurrentlyDrawnItem = [[Address1], [Point(point.getX() - 5, point.getY() - 5),
                                       Point(point.getX() + 5, point.getY() + 5)]]
    NotCurrentlyDrawnItem = [[InfoBox1, Text1], [Point(point.getX() - 50, point.getY() - 50),
                                                 Point(point.getX() + 50, point.getY() + 50)]]
    return [CurrentlyDrawnItem, NotCurrentlyDrawnItem]


def populateWindow(listOfInfo, Win):
    '''draws red dots, info boxes, and initilizes the shown and hidden objects on the map'''
    listOfAddresses, listOfPoints, listOfEquipment = listOfInfo[0], listOfInfo[1], listOfInfo[2]
    ListOfObjects = []
    for i in range(len(listOfAddresses)):
        Address1 = drawRedDots(listOfPoints[i], Win)
        route1 = drawLines(listOfPoints[i], listOfPoints[i + 1], Win)
        InfoBox1, Text1 = drawInfoBoxes(listOfPoints[i], listOfEquipment[i], listOfAddresses[i], Win)
        pair = setShownAndHiddenObjects(Address1, InfoBox1, Text1, listOfPoints[i])
        ListOfObjects.append(pair)

    return ListOfObjects

def clickedObject(ListOfObjects, clicked, index):
    # If we have clicked on an object, switch the order
    # in which they appear in the ListOfObjects list at that element
    switch = ((clicked.getX() >= ListOfObjects[index][0][1][0].getX()) and (clicked.getX() <= ListOfObjects[index][0][1][1].getX())) and ((clicked.getY() >= ListOfObjects[index][0][1][0].getY()) and (clicked.getY() <= ListOfObjects[index][0][1][1].getY()))
    return switch

def switchHiddenAndShownObjects(Win, ListOfObjects, index):
    #undraw and draw the appropriate items
    tempObject = ListOfObjects[index][0]
    ListOfObjects[index][0] = ListOfObjects[index][1]
    ListOfObjects[index][1] = tempObject
    Found = True

    for objectToUndraw in ListOfObjects[index][1][0]:
        objectToUndraw.undraw()

    for objectToDraw in ListOfObjects[index][0][0]:
        objectToDraw.draw(Win)
    return

def iterateOverClicks(Win, ListOfObjects):
    # iterate through the set of possible clicked objects
    # and check to see if the user clicked on an individual
    # object
    clicked = Win.getMouse()
    index = 0
    Found = False
    while (index < len(ListOfObjects)) and (Found == False):
        if (clickedObject(ListOfObjects, clicked, index)):
            switchHiddenAndShownObjects(Win, ListOfObjects, index)
        index += 1
    return

def keepWindowOpen(Win, ListOfObjects):
    while True:
        iterateOverClicks(Win, ListOfObjects)
    Win.close()

def keepWindowOpenWithoutError(Win, ListOfObjects):
    '''keeps the window up'''
    #try:
    keepWindowOpen(Win, ListOfObjects)
    #except:
    #    pass
    return

def main():
    #Create a graph window of the twin cities
    #Then, create and plot address data
    Win = GraphWinTwinCities()
    listOfInfo = listInfo()
    ListOfObjects = populateWindow(listOfInfo, Win)
    #Keeps the window open indefinitely
    keepWindowOpenWithoutError(Win, ListOfObjects)

if __name__ == "__main__":
    main()
