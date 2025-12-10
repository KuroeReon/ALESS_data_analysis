from linear_interpolation import linear_interpolation
from get_average import get_average
import numpy as np

average_small, average_middle = get_average()
simulation_middle = linear_interpolation("simulation_trajectory_middle.txt")
error_middle = average_middle - simulation_middle
print(error_middle)