"""Flight Path Between Two Airports Assignment for Code Fellows 401 Python."""

# -*- coding: utf-8 -*-

import json
import urllib

AIRPORTS_URL = 'https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json'


def fetch_data(url):
    """Fetch airports json data using provided url."""
    with urllib.request.urlopen('https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json') as response:
        html = response.read()
    return html.decode('utf-8')


def convert_json_data(data):
    """Convert the fetched json airport data into usable python data."""
    airports_data = json.loads(data)
    return airports_data


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.

    Point1 and point2 must have the format [latitude, longitude].
    The return value is a float.  Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html.
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def airport_present(airports_data, airport):
    """Check if an airport found in airport data."""
    try:
        return next((item for item in airport_data if item["airport"] == airport))
    except StopIteration:
        raise NameError("{} not present in airport data.".format(airport))


def airports_present(airports_data, departure_airport, arrival_airport):
    """Check that selected airports are in airport data."""
    airport_present(airports_data, departure_airport)
    airport_present(airports_data, arrival_airport)
    return True


def determine_route_between_airports(airports_data, departure_airport, arrival_airport):
    """Determine list of airports in complete flight route."""
    # Pseudo Code
    # Use the graph data structure to model airports_data
    # Traverse through airports_data using "destination airports" as edges
    # Use the neighbors method on graph class to create a list.
    return flight_route_list


def flight_route_mileage(airports_data, flight_route_list):
    """Determine total mileage of route between airports."""
    # Pseudo Code
    # Use the provided calculate distance function
    # Use the lat lon data to determine distance between each airport
    # Provide cumulative mileage total
    return cumulative_mileage


def main_flight_route_function(departure_airport, arrival_airport):
    """Return the flight path and mileage between two airports."""
    airports_data = convert_json_data(fetch_data(AIRPORTS_URL))
    airports_present(airports_data, departure_airport, arrival_airport)
    flight_route_list = determine_route_between_airports(airports_data, departure_airport, arrival_airport)
    cumulative_mileage = flight_route_mileage(airports_data, flight_route_list)
    print(flight_route_list, cumulative_mileage)


if __name__ == '__main__':
    main()
