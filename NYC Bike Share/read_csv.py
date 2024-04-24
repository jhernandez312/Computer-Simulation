import numpy as np
import simpy
import csv
from collections import defaultdict


def station_data(csv_input_path):
    """
    Load station data from a CSV file into a dictionary where each key is a start station
    and the value is a list of tuples. Each tuple contains the end station name and the probability
    of transitioning to that end station.

    Structure of the returned dictionary:
    {
        'Start Station A': [('End Station X', probability), ('End Station Y', probability), ...],
        'Start Station B': [('End Station Z', probability), ...],
        ...
    }
    """
    station_data = defaultdict(list)

    with open(csv_input_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                start_station = row[0]
                end_station = row[1]
                probability = float(row[2]) if row[2] else None

                station_data[start_station].append((end_station, probability))

    return dict(station_data)



def start_station(csv_filepath):
    """
    Reads a CSV file and creates a list of tuples where each tuple contains a station name and its probability.

    Parameters:
    - csv_filepath: The path to the CSV file to be read.

    Returns:
    - A list of tuples, where each tuple is (station_name, probability).
    """
    station_probabilities = []
    with open(csv_filepath, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            if row:
                station_name, probability = row[0], float(row[1])
                station_probabilities.append((station_name, probability))
    return station_probabilities

stations_with_bikes = {
    "South Waterfront Walkway - Sinatra Dr & 1 St": 1,
    "Grove St PATH": 1,
    "Hoboken Terminal - Hudson St & Hudson Pl": 1,
    "Hoboken Terminal - River St & Hudson Pl": 1,
    "Newport Pkwy": 1,
    "City Hall - Washington St & 1 St": 1,
    "Newport PATH": 1,
    "12 St & Sinatra Dr N": 1,
    "Hoboken Ave at Monmouth St": 1,
    "Marin Light Rail": 1,
    "Hamilton Park": 1,
    "14 St Ferry - 14 St & Shipyard Ln": 1,
    "Liberty Light Rail": 1,
    "Columbus Dr at Exchange Pl": 1,
    "Harborside": 1,
    "11 St & Washington St": 1,
    "Washington St": 1,
    "Sip Ave": 1,
    "Hudson St & 4 St": 1,
    "8 St & Washington St": 1,
    "Madison St & 1 St": 1,
    "City Hall": 1,
    "Warren St": 1,
    "Newark Ave": 1,
    "Columbus Park - Clinton St & 9 St": 1,
    "Grand St & 14 St": 1,
    "Church Sq Park - 5 St & Park Ave": 1,
    "Columbus Drive": 1,
    "Van Vorst Park": 1,
    "Clinton St & Newark St": 1,
    "Grand St": 1,
    "Paulus Hook": 1,
    "Manila & 1st": 1,
    "9 St HBLR - Jackson St & 8 St": 1,
    "Bloomfield St & 15 St": 1,
    "4 St & Grand St": 1,
    "7 St & Monroe St": 1,
    "JC Medical Center": 1,
    "Clinton St & 7 St": 1,
    "Willow Ave & 12 St": 1,
    "Morris Canal": 1,
    "McGinley Square": 1,
    "Brunswick & 6th": 1,
    "Jersey & 3rd": 1,
    "Brunswick St": 1,
    "Baldwin at Montgomery": 1,
    "Adams St & 2 St": 1,
    "Southwest Park - Jackson St & Observer Hwy": 1,
    "Marshall St & 2 St": 1,
    "Journal Square": 1,
    "Madison St & 10 St": 1,
    "6 St & Grand St": 1,
    "Dixon Mills": 1,
    "Lafayette Park": 1,
    "Riverview Park": 1,
    "Stevens - River Ter & 6 St": 1,
    "Mama Johnson Field - 4 St & Jackson St": 1,
    "Pershing Field": 1,
    "Hilltop": 1,
    "Jersey & 6th St": 1,
    "Essex Light Rail": 1,
    "Monmouth and 6th": 1,
    "Oakland Ave": 1,
    "Adams St & 11 St": 1,
    "Bergen Ave": 1,
    "Fairmount Ave": 1,
    "Montgomery St": 1,
    "Christ Hospital": 1,
    "Astor Place": 1,
    "Heights Elevator": 1,
    "Lincoln Park": 1,
    "Leonard Gordon Park": 1,
    "Communipaw & Berry Lane": 1,
    "5 Corners Library": 1,
    "Glenwood Ave": 1,
    "Union St": 1,
    "Dey St": 1,
    "Jackson Square": 1,
    "Bergen Ave & Stegman St": 1,
    "Grant Ave & MLK Dr": 1,
    "JCBS Depot": 1
}
