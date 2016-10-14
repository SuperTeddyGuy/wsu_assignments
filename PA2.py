# -*- coding: utf-8 -*-
"""
Joao Victor "Teddy" Martins - 11537480
CptS 111-8108, Fall 2016
Programming Assignment #2
24/09/16
Lab Section 10

Program that uses Google Maps API to get distances between cities of the users choice,
and displaying the information in a presentable manner.
"""

import urllib.request #library for the google maps api use
import matplotlib.pyplot as plt #library for the grafh


def format_city_string(city_str):
    '''
    To prepare the city string for the query:
    1. remove comma (check)
    2. replace spaces with + (check)
    '''
    city_str = city_str.replace(",", "")
    city_str = city_str.replace(" ", "+")
    return city_str
  
def build_query(origin, dest):
    '''
    Builds the query string for the Google Distance Matrix API according to this website:
    https://developers.google.com/maps/documentation/distance-matrix/start
    '''
    query_base = "http://maps.googleapis.com/maps/api/distancematrix/json?origins="    
    query = query_base + origin
    query += "&destinations="
    query += dest
    query += "&mode=driving&sensor=false"
    return query
    
def extract_distance(results_str):
    '''
    Extracts the distance in meters from the JSON response.
    '''
    index = results_str.find("distance")
    results_str = results_str[index:]
    index = results_str.find("value")
    results_str = results_str[index:]
    index = results_str.find(":")
    results_str = results_str[index + 2:]
    index = results_str.find(r"\n")
    results_str = results_str[:index]
    dist = int(results_str)
    return dist
    
def get_distance(city1, city2):
    '''
    Accepts 2 strings representing cities in the U.S.
    Returns the integer distance in meters between city1 and city2
    '''
    city1 = format_city_string(city1)
    city2 = format_city_string(city2)
    
    query = build_query(city1, city2)

    web_obj = urllib.request.urlopen(query)
    # web_obj.read() returns an array of bytes, need to convert to a string
    results_str = str(web_obj.read())
    web_obj.close()
    
    dist = extract_distance(results_str)
    return dist
    
def display_instructions():
    '''
    Calls for the display if the instructions
    '''
    print("Welcome to the distance calculator program, utilizing Google Maps!\nYou will be prompted to enter 3 pairs of cities. \nPlease enter cities in the form (city, state abbreviation).\nFor example: New York, NY\nThe program will tell you the distances between each pair of cities. Enjoy!")

def get_city_string(pair_num, city_ordering):
    '''
    Prompts the user for entering the cities which the distance will be calculated
    '''
    city_string = str(input("Please enter the %s city of pair #%d: " % (pair_num, city_ordering)))
    return city_string
    
def meters_to_miles(meters):
    '''
    Converts the distance provided by google in meters to miles
    '''
    miles = meters * 0.000621371
    return miles

def display_city_distance(city1, city2, distance):
    '''
    Calls for the display if the distances of the cities the user selected
    '''
    print("The distance between %s and %s is %.2f miles" % (city1, city2, distance))

def plot_city_distances(city1, dist1, city2, dist2, city3, dist3, city4, dist4, city5, dist5, city6, dist6):
    '''
    111 STUDENTS: THIS IS THE FUNCTION YOU WILL CALL FOR THE **BONUS** TASK
    Accepts 6 strings representing cities in the U.S. and 6 distances in meters representing 
    the distance between the city and Pullman, WA
    Ordering of the parameters is 6 pairs of city string, distance value
    
    Uses matplotlib functions to plot a bar graph of the city distances. 
    Save the plot by clicking on the save button on the toolbar of the plot window.
    Press the X to close the window when you are done.
    
    This function does not return anything.
    '''
    x = [0, 1, 2, 3, 4, 5]    
    x_labels = [city1, city2, city3, city4, city5, city6]
    y = [meters_to_miles(dist1), meters_to_miles(dist2), meters_to_miles(dist3), meters_to_miles(dist4), \
         meters_to_miles(dist5), meters_to_miles(dist6)]
    plt.bar(x, y)
    plt.xticks(x, x_labels, rotation=45, ha='left')
    plt.xlabel("City")
    plt.ylabel("Distance in Miles from Pullman")
    plt.tight_layout()
    # show the window
    plt.show()
    
def main():
    display_instructions()
    
    #cityx_y stores the string of the cities name, where x is the pair, and y is the order
    city1_1 = get_city_string("first", 1)
    city1_2 = get_city_string("second", 1)    
    city2_1 = get_city_string("first", 2)
    city2_2 = get_city_string("second", 2)
    city3_1 = get_city_string("first", 3)
    city3_2 = get_city_string("second", 3)
    
    #dist_x stores the distance given by google in meters
    dist_1 = get_distance(city1_1, city1_2)
    dist_2 = get_distance(city2_1, city2_2)
    dist_3 = get_distance(city3_1, city3_2)

    #dist_milesx stores the distance after the convertion to miles
    dist_miles1 = meters_to_miles(dist_1)
    dist_miles2 = meters_to_miles(dist_2)
    dist_miles3 = meters_to_miles(dist_3)
    
    display_city_distance(city1_1, city1_2, dist_miles1)
    display_city_distance(city2_1, city2_2, dist_miles2)
    display_city_distance(city3_1, city3_2, dist_miles3)
    
    #distX_away stores the distance between Pullman, WA and the other cities entered by the user
    dist1_away = get_distance("Pullman, WA", city1_1)
    dist2_away = get_distance("Pullman, WA", city1_2)
    dist3_away = get_distance("Pullman, WA", city2_1)
    dist4_away = get_distance("Pullman, WA", city2_2)
    dist5_away = get_distance("Pullman, WA", city3_1)
    dist6_away = get_distance("Pullman, WA", city3_2)
    
    plot_city_distances(city1_1, dist1_away, city1_2, dist2_away, city2_1, dist3_away, city2_2, dist4_away, city3_1, dist5_away, city3_2, dist6_away)

main()
