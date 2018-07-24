#Import necessary libraries 
import Distances
import Directions
import csv

#Inputs for the population amount and travel type
population_check = int(input('Enter population amount: '))
type_travel = str(input('Enter Travel Type, Either, Transit, Drive or Walk: '))
#Initialize variables needed
matrix_list = []
data_size = 70
dataList = [['City', '0']]
city_list = []
travel_list = [['London', 0]]
travel_path = []
current_city = []
city_path = []
#Reading in and creating list with CSV file of cities
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        dataList.append(line)
#Cleaning the data by removing numbers from the names
def remove_numbers ():
    for x in range (data_size):
        result = ''.join(i for i in dataList[x][0] if not i.isdigit())
        remove_comma = dataList[x][1].replace(',','')
        dataList[x][0] = result
        dataList[x][1] = remove_comma
#Cleaning population numbers by removing commas and making ints
def make_number ():
    for x in range (data_size):
        to_number = int(dataList[x][1])
        dataList[x][1] = to_number
#Creating need to vist list
def sort_populated ():
    #Variable for cities over population numeber 
    check_number = 0
    #Checks what cities have a greater population
    for x in range (data_size):
        if(dataList[x][1] > population_check):
            check_number = check_number + 1
            #Adds the higher population cities to list
            city_list.append(dataList[x][0])
    for x in range (check_number):
        print(city_list[x])
    return check_number
#This creates the distance matrix
def create_matrix (matrix_size):
    for x in range (matrix_size):
        #Uses a small list for each line in the matrix with the distances
        add_to = []
        for y in range (matrix_size):
            #Uses distances class which uses Googles Distance Matrix to get distances
            distance = Distances.get_distance(city_list[x], city_list[y])
            add_to.append(distance)
        #Adds the Distances to the matrix
        matrix_list.append(add_to)
#Prints the matrix for debugging purposes
def print_matrix (matrix_size):
    for x in range (matrix_size):
        for y in range (matrix_size):
            print(matrix_list[x][y], end=" ")
        print('')
#This creates the list that holds the cities that need to be visited
def create_travelList (cityList_size):
    for x in range(1, cityList_size):
        travel_structure = [city_list[x], x]
        travel_list.append(travel_structure)
#Prints the travel list for debugging purposes
def print_struct (size):
    for x in range(size):
            print(travel_list[x])
#Initializes the path that is being created
def init_path ():
    #Add the first city to thee list
    current_city.append(travel_list[0])
    #Removes that city from the list that needs to be visited
    travel_list.remove(travel_list[0])
#Finds the closest city to the current city
def find_closest (current):
    #Making sure that the first value is the biggest
    smallest_distance = 100000000000
    #Holds the current closest city
    closest_city = []
    for x in range (len(travel_list)):
        #Checks the distance matrix for the closest city
        if matrix_list[current[0][1]][travel_list[x][1]] < smallest_distance:
            #Adds the smallest distance
            smallest_distance = matrix_list[current[0][1]][travel_list[x][1]]
            #Replaces the old closest to the list
            closest_city = travel_list[x]
    data_struct = [closest_city]
    #Returns the closest city
    return data_struct
#Starts the path building
def create_path (size, current):
    city_current = current
    #Goes through all cities to find the closest to each one 
    for x in range (size - 1):
        #Uses the function to fin dclosest to current
        return_data = find_closest(city_current)
        city_current = return_data
        #Adds the closest to the path list
        travel_path.append(city_current)
        #Removes from the need to visit cities
        travel_list.remove(city_current[0])
    #Adds the first and last travel path as the main city
    travel_path.insert(0,[['London', 0]])    
    travel_path.append([['London', 0]])
    #Prints out the path
    print('Suggested Route:')
    print(travel_path[0][0][0], end=" ")
    for x in range(1, size+1):
        print('->', end=" ")
        print(travel_path[x][0][0], end=" ")
#Changes the list size so that it is easier to use
def change_format (size):
    for x in range (size + 1):
        city_path.append(travel_path[x][0])
#Calculates the total distance using distance matrix
def total_distance (size):
    #Total Distance variable
    calculated_distance = 0
    for x in range (size):
        #Goes all cities in the travel path
        y = x + 1
        #Using the distance matrix
        current_distance = matrix_list[city_path[x][1]][city_path[y][1]]
        calculated_distance = calculated_distance + current_distance
    #returns total distance of all cities
    return calculated_distance
#Prints the directions for the user
def print_directions (size):
    for x in range (size):
        y = x + 1
        Directions.get_directions(city_path[x][0], city_path[y][0], type_travel)
#For debuggind purposes for the google directions API
def test_directions (size):
    for x in range (size):
        print(city_list[x])
        Directions.get_directions('London', city_list[x], 'walk')
#The main function that holds all the functions and runs in order
def main():
    print('Cities with over ', population_check, ' population:')
    print(' ')
    remove_numbers()
    make_number()
    city_amount = sort_populated()
    create_matrix(city_amount)
    create_travelList(city_amount)
    init_path()
    print(' ')
    create_path(city_amount, current_city)
    print(' ')
    change_format(city_amount)
    distance_meters = total_distance(city_amount)
    distance_KM = round(distance_meters * 0.001, 1)
    print('Total Distance: ', distance_KM, ' KM')
    print(' ')
    print_directions(city_amount)
main()
