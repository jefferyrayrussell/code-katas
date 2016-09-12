"""Flight Paths Assignment for Code Fellows 401 Python."""

# -*- coding: utf-8 -*-
import math

"""
Pseudo Code:
*  Parse Json file for useable data.
*  Check to see if both airports are in the data.
*  Use breadth transversal of graph data structure to determine
    a route between the two cities.
*  Determine the distance of the route.



def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float. Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html.
    """

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def flight_paths_route(city1, city2):
    """Determine if a route exists between two cities."""


def flight_paths_cities(city1, city2):
    """Return a flight path between two cities."""


def flight_paths_distance(city1, city2):
    """Return the distance of a flight route."""
