# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:29:26 2016

@author: Teddy
"""
import webbrowser
import urllib.request

def open_input_file(name):
    infile = open(name + ".txt", "r")
    return infile
    
def open_output_file(name):
    outfile = open(name + "_stats.txt", "w")
    return outfile
    
def close_files(file):
    file.close()
    
def format_search_term(search_term):
    '''
    To prepare the search term string for the query:
    1. remove comma (check)
    2. replace spaces with + (check)
    '''
    search_term = search_term.replace(",", "")
    search_term = search_term.replace(" ", "+")
    return search_term
  
def build_query(query):
    '''
    Builds the query string for the Spotify Search API according to this website:
    https://developer.spotify.com/web-api/console/get-search-item/
    '''
    query_base = "https://api.spotify.com/v1/search?q="    
    query = query_base + query
    # perform a track search and only return the top result
    query += "&type=track&limit=1"
    return query
    
def extract_numeric_value(results_str, label):
    '''
    Extracts an integer value represented by the label parameter from the JSON response.
    '''
    index = results_str.find(label)
    results_str = results_str[index:]
    index = results_str.find(":")
    results_str = results_str[index + 2:]
    index = results_str.find(",")
    results_str = results_str[:index]
    value = int(results_str)
    return value
    
def extract_preview_url(results_str):
    '''
    Extracts the preview url from the JSON response.
    '''
    index = results_str.find("preview_url")
    results_str = results_str[index:]
    index = results_str.find(":")
    results_str = results_str[index:]
    index = results_str.find("\"")
    results_str = results_str[index + 1:]
    index = results_str.find("\"")
    results_str = results_str[:index]
    return results_str
    
def get_track_information(track, artist, info_type):
    '''
    111 STUDENTS: THIS IS THE FUNCTION YOU WILL CALL
    Accepts 3 strings representing a track and its artist, and the name of the information to retrieve (info_type).
    info_type can be:
        "duration_ms": returns an integer representing the duration of the song in MILLISECONDS        
        "popularity": returns an integer representing the popularity of the song
        "preview_url": returns a string representing a url hosting a short clip of the song
    Returns the requested information for track and artist
    '''
    track = format_search_term(track)
    artist = format_search_term(artist)
    
    # search the spotify database for a track by artist
    search_terms = track + "+" + artist
    
    query = build_query(search_terms)

    web_obj = urllib.request.urlopen(query)
    # web_obj.read() returns an array of bytes, need to convert to a string
    results_str = str(web_obj.read())
    web_obj.close()
    
    info = ""
    if info_type == "popularity" or info_type == "duration_ms":
        info = extract_numeric_value(results_str, info_type)
    elif info_type == "preview_url":
        info = extract_preview_url(results_str)
    else:
        print("Unknown information type")
    return info
    
def get_song_name(infile, outfile):
    '''
    This function gets the song name from the input file and writes it to the output.
    If there is no more names, this function will    
    '''
    name = str(infile.readline().strip())
    if name != '':
        outfile.write("Track: " + name + "\n")
        return name

def get_song_artist(infile, outfile):
    '''
    Same as get_song_name, but for the artist.
    '''
    artist = str(infile.readline().strip())
    if artist != '':
        outfile.write("Artist: " + artist + "\n")
        return artist
    
def calc_song_duration(duration_ms):
    '''
    This function will calculate the time of the song in minutes and seconds.
    Is also calculates the average time, after the value is calculated in miliseconds
    '''
    secs = duration_ms / 1000
    mins = 0
    while secs > 60:
        mins += 1
        secs -= 60
    total = str("%d mins and %d seconds\n" % (mins,secs))
    
    return total
    
def display_console_message(name, artist):
    '''
    Display on the console what song and artist that is being analyzed through the Spotify API.
    '''
    print("Querying Spotify for information regarding %s by %s..." % (name, artist))
    

def main():
    #infile represents the file of the playlist
    name_of_file = str(input("Please enter the name of the file to open (no '.txt' needed): "))
    infile = open_input_file(name_of_file)
    outfile = open_output_file(name_of_file)
    print("Reading in playlist information from " + name_of_file + ".txt...")
    count = 0  #'count' counts how many songs there are in the playlist. If count == 0, user shall enter another file that has at least one song.
    total_ms = 0 #stores the total in miliseconds returned by spotify API
    most_pop = -1 #stores the pop. value of the most pop. song
    most_pop_name = '' #stores the name of the most pop. song
    total_popularity = 0 #stores the total added value of popularity to divide by the number of songs to get the average
    duration_temp = -1 #stores the duration of the longest song in ms
    longest = '' #stores the name of the longest song
    pop_url = '' #stores the most populars song's url
    #this loop gets the track, artist, duration, popularity and the url for each song; It does for each song, writing each one on the output and restarting the loop.
    while True:    
        name = get_song_name(infile, outfile) 
        artist = get_song_artist(infile, outfile) 
        display_console_message(name, artist)
        line = infile.readline()
        duration_ms = get_track_information(name, artist, "duration_ms")
        #str_duration is the string that says how long the song is in minutes and seconds.
        str_duration = calc_song_duration(duration_ms)
        outfile.write("Duration: " + str_duration)
        popularity = get_track_information(name, artist, "popularity")
        outfile.write("Popularity: " + str(popularity) + "\n")        
        url = get_track_information(name, artist, "preview_url")
        outfile.write("Preview URL: " + url + "\n\n")
        #this if checks if the song is the longest one.
        if duration_ms > duration_temp:
            longest = name
            duration_temp = duration_ms
        #this if checks if the song is the most popular one.
        if popularity > most_pop:
            most_pop_name = name
            most_pop = popularity
            pop_url = url
        count += 1
        total_popularity += popularity
        total_ms += duration_ms
        if line == '': 
            break
    outfile.write("Number of tracks in playlist: " + str(count) + "\n")
    outfile.write("Average track duration: " + str(calc_song_duration(total_ms / count)))
    outfile.write("Longest track in playlist: " + longest + " at " + str(calc_song_duration(duration_temp)))
    outfile.write("Average playlist track popularity: " + str(total_popularity / count) + "\n")
    outfile.write("Most popular track in playlist: " + str(most_pop_name) + " at " + str(most_pop) + "\n")
    
    print("Opening preview for most popular song...")
    webbrowser.open(pop_url)    
    
    close_files(infile)
    close_files(outfile)
    print("Closing files...")
        
main()