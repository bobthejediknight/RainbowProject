"""
https://www.youtube.com/watch?v=f28_tfmuVts
"""
#pip install geopy
# import module
from geopy.geocoders import Nominatim
from geopy import distance



def initializeNominatimAPI():
    #Initialize Nominatim API
    geolocator = Nominatim(user_agent = "GoogleV3")
    return geolocator

def getLocation(dict, Input_place1, Input_place2):
    # Get location of the input strings
    place1 = dict[Input_place1]
    place2 = dict[Input_place2]
    return place1, place2

def getLatAndLong(dict, Input_place1, Input_place2):
    # Get latitude and longitude
    Loc1_lat, Loc1_lon = dict[Input_place1][0], dict[Input_place1][1]
    Loc2_lat, Loc2_lon = dict[Input_place2][0], dict[Input_place2][1]
    return Loc1_lat, Loc1_lon, Loc2_lat, Loc2_lon

def genLocationTuples(Loc1_lat, Loc1_lon, Loc2_lat, Loc2_lon):
    #create location tuples
    location1 = (Loc1_lat, Loc1_lon)
    location2 = (Loc2_lat, Loc2_lon)
    return location1, location2

def distanceBetween(Input_place1, Input_place2, dict):
    geolocator = initializeNominatimAPI()

    place1, place2 = getLocation(dict, Input_place1, Input_place2)

    Loc1_lat, Loc1_lon, Loc2_lat, Loc2_lon = getLatAndLong(dict, Input_place1, Input_place2)

    location1, location2 = genLocationTuples(Loc1_lat, Loc1_lon, Loc2_lat, Loc2_lon)

    return distance.distance(location1, location2).km
