import matplotlib.pyplot as plt
from get_average_error import get_average_error
from linear_interpolation import linear_interpolation_x

simulation_small, simulation_middle, average_small, average_middle, error_small, error_middle = get_average_error()

def make_graph():
    small_x = linear_interpolation_x("./small_airplane_trajectories/small_airplane_trajectory_no4.txt")
    middle_x = linear_interpolation_x("./middle_airplane_trajectories/middle_airplane_trajectory_no2.txt")

    plt.figure(figsize=(10, 6))

    """plt.plot(small_x, average_small, label="The experimentally obtained trajectory of the small airplane")
    plt.plot(small_x, simulation_small, label="The simulated trajectory of the small airplane")
    plt.xlabel("Horizontal position[m]")
    plt.ylabel("Height[m]") 
    plt.xlim(0, 3.0)
    plt.ylim(-1.75, 0.25)
    plt.grid(True)
    plt.legend()"""
    
    """plt.plot(middle_x, average_middle, label="The experimentally obtained trajectory of the middle-sized airplane")
    plt.plot(middle_x, simulation_middle, label="The simulated trajectory of the middle-sized airplane")
    plt.xlabel("Horizontal position[m]")
    plt.ylabel("Height[m]")
    plt.grid(True)
    plt.legend()"""

    plt.plot(small_x, error_small, label="The simulation error of small airplane trajectory")
    plt.xlabel("Horizontal position[m]")
    plt.ylabel("Vertical position error (Exp. - Sim.)[m]")
    plt.xlim(0, 3.0)
    plt.grid(True)
    plt.legend()

    plt.plot(middle_x, error_middle, label="The simulation error of middle-sized airplane trajectory")
    plt.xlabel("Horizontal position[m]")
    plt.ylabel("Vertical position error (Exp. - Sim.)[m]")
    plt.grid(True)
    plt.legend()

    plt.show()

make_graph()