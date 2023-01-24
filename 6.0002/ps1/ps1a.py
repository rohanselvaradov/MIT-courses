###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

COWLIST_FILENAME = "ps1_cow_data.csv"

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cowdict = {} # Create empty dictionary to store cow pairs
    with open(filename) as cowlist: # Open file
        for line in cowlist: # Iterate through each line of file
            line = line.split(",") # Split each line with a ,
            cowdict[line[0]] = line[1].strip("\n") # Set name key as corresponding weight removing \n
        return cowdict # Returns complete dictionary
    
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = [] # Create empty list to contain list of each trip list
    cows_copy = sorted(cows, key = cows.get, reverse = True) # Sorts and copies input cows dictionary
    while cows_copy: # Continue until all cows have been allocated a trip and been deleted
        current_trip = [] # Set current trip to be empty
        current_weight = 0 # Set starting weight as 0
        for item in cows_copy[:]: # Iterates through cowlist
            if current_weight + int(cows[item]) <= limit: # Checks if the next cow can be added within limit
                current_trip.append(item) # Adds cow to current trip
                current_weight += int(cows[item]) # Adds cow's weight to current weight
                cows_copy.remove(item) # Removes cow from list that are yet to be transported
        trips.append(current_trip) # When no more cows can fit, add current trip to list of all trips
    return trips # When all cows are allocated a trip, return trips
            

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = sorted(cows, key = cows.get, reverse = True) # Sort and copy input cow dictionary
    for partition in get_partitions(cows_copy): # Iterate through every possible partition of inputs
        possible = True # Set possible to True
        while possible: # Continue until possible is False
            for trip in partition: # Iterate through each individual trip within partition
                trip_weight = 0 # Set starting weight to 0
                for cow in trip: # Iterate through each individual cow within trip
                    trip_weight += int(cows[cow]) # Add the cow's weight to the trip weight
                    if trip_weight > limit: # If the trip weight exceeds the limit
                        possible = False # Set possible to False
            if possible: # If possible is still true
                return partition # Return the current partition
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    greedy_start = time.time()
    greedy_result = greedy_cow_transport(load_cows(COWLIST_FILENAME))
    greedy_end = time.time()
    print("Greedy took a time of",greedy_end - greedy_start,"seconds and had a result of",greedy_result)
    
    brute_force_start = time.time()
    brute_force_result = brute_force_cow_transport(load_cows(COWLIST_FILENAME))
    brute_force_end = time.time()
    print("Brute force took a time of",brute_force_end - brute_force_start,"seconds and had a result of",brute_force_result)
    
