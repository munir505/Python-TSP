#This class is used for the Google Distance Matrix API
#Imports the module needed
import googlemaps
#Adds the API key needed
gmaps = googlemaps.Client(key='#API KEY GOES HERE')
#Function that gets the distance when two cities are given
def get_distance (city_one, city_two):
    #Gets the Python Dictionaries
    city_distance = gmaps.distance_matrix(city_one, city_two)
    #Gets the distance from the dictionary
    distance = city_distance['rows'][0]['elements'][0]['distance']['value']
    #Returns the distance
    return distance
