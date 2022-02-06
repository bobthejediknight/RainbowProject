from colormap import rgb2hex
import PIL.Image
from graph import *
from datetime import datetime
from geopy.geocoders import Nominatim
#This file is complete

def extractFileInformation(input):
    # Extract the addresses from the input File
    inputFile = open(input, "r")
    fileLines = inputFile.read()
    listOfAddrs = fileLines.split("\n")[:-1]
    inputFile.close()
    return listOfAddrs

def getCoordData(Address):
    geolocator = Nominatim(user_agent="RainbowProject")
    location = geolocator.geocode(Address.split(":")[0])
    Coords = [location.latitude, location.longitude, Address.split(":")[0],
                       Address.split(":")[1]]
    return geolocator, location, Coords

def turnAddressesToCoordinates(listOfAddrs):
    # Turn the Addresses that you can into Coordinates and
    # replace coordinates with string "ManuallyFill" for
    # the addresses of which you can't access the coordinates
    listOfCoords = [[None, None]] * len(listOfAddrs)
    for i in range(len(listOfCoords)):
        try:
            geolocator, location, listOfCoords[i] = getCoordData(listOfAddrs[i])

        except:
            listOfCoords[i] = ["ManuallyFill", "ManuallyFill", listOfAddrs[i].split(":")[0],
                               listOfAddrs[i].split(":")[1]]

    return listOfCoords

def writeCoordinatesToOutputFile(output, listOfCoords):
    # Write the Coordinates into the output file
    outputFile = open(output, "w")
    outputFile = open(output, "w")
    for i in range(len(listOfCoords)):
        outputFile.write(str(listOfCoords[i][0]) + ", " + str(listOfCoords[i][1]) + ":" + str(listOfCoords[i][2]) + ":" + str(listOfCoords[i][3]) + "\n")
    outputFile.close()
    return

def addrToCoords(input, output):
    listOfAddrs = extractFileInformation(input)
    listOfCoords = turnAddressesToCoordinates(listOfAddrs)
    writeCoordinatesToOutputFile(output, listOfCoords)
    return


def main():
    addrToCoords("addresses.txt", "coordinates.txt")
    return


if __name__ == '__main__':
    main()
