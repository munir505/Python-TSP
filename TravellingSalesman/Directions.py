#This class is used to get the direction, either by walk, transit or drive
#Using the Google Direction API
#url lib needed to make API request
import urllib.request
#JSON used to send request
import json
import re
#Endpoint used to make the request, provided by Google
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
#API key that is needed to use the API
api_key = #API KEY GOES HERE
#Function that gets the directions, requires three variables
def get_directions (location_one, location_two, travel_type):
    #Origin is the first city
    origin = location_one.replace(' ', '+')
    #destination is the ending city that is being travel to
    destination = location_two.replace(' ', '+')
    #Either walk, transit or drive
    travel_type = travel_type
    #Part of the request, used to add the varibales and key to the endpoint
    directions_request = 'origin={}&destination={}&mode={}&key={}'.format(origin, destination, travel_type, api_key)
    #Adds all to endpoint 
    request = endpoint + directions_request
    #Reciving and reading the request
    responce = urllib.request.urlopen(request).read()
    #Format as python dictionary
    directions = json.loads(responce)
    #Gets data from dictionary 
    routes = directions['routes'][0]
    legs = routes['legs'][0]
    #Print the first and last location
    print('From ', location_one, ' to ', location_two,' going by ', travel_type)
    #Prints all steps from the two locations
    for x in range (0, len (legs['steps'])):
        #Cleans and prints the output
        print(clean_string(legs['steps'][x]['html_instructions']))
    print('You have reached ', location_two)
    print(' ')
#This function is used to clean the output, which contains some HTML code 
def clean_string(string_HTML):
    clean = re.compile('<.*?>')
    clean_text = re.sub(clean, '', string_HTML)
    return clean_text
