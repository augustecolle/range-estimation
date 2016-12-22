from parameters import *
import numpy as np
import matplotlib.pyplot as plt
import geopy
from geopy.distance import vincenty

def get_slope_of_gps_data(filename, deltax = 0.1, s = 10, deltax_avg_slope = 100):



