from linear_interpolation import linear_interpolation_y
import numpy as np

def get_average_error():
    arrays_small = [
        linear_interpolation_y("./small_airplane_trajectories/small_airplane_trajectory_no1.txt"),
        linear_interpolation_y("./small_airplane_trajectories/small_airplane_trajectory_no2.txt"),
        linear_interpolation_y("./small_airplane_trajectories/small_airplane_trajectory_no3.txt"),
        linear_interpolation_y("./small_airplane_trajectories/small_airplane_trajectory_no4.txt"),
        linear_interpolation_y("./small_airplane_trajectories/small_airplane_trajectory_no5.txt")
    ]

    min_len_small = min(len(a) for a in arrays_small)
    arrays_trimmed_small = [a[:min_len_small] for a in arrays_small]
    simulation_small = linear_interpolation_y("simulation_trajectory_small.txt")[:min_len_small]
    average_small = sum(arrays_trimmed_small) / len(arrays_trimmed_small)
    error_small = average_small - simulation_small

    sum_of_squares_error_small = np.sum(error_small**2)
    RMSE_small = np.sqrt(sum_of_squares_error_small / min_len_small)
    print(RMSE_small)

    arrays_middle = [
        linear_interpolation_y("./middle_airplane_trajectories/middle_airplane_trajectory_no1.txt"),
        linear_interpolation_y("./middle_airplane_trajectories/middle_airplane_trajectory_no2.txt"),
        linear_interpolation_y("./middle_airplane_trajectories/middle_airplane_trajectory_no3.txt"),
        linear_interpolation_y("./middle_airplane_trajectories/middle_airplane_trajectory_no4.txt"),
        linear_interpolation_y("./middle_airplane_trajectories/middle_airplane_trajectory_no5.txt")
    ]

    min_len_middle = min(len(a) for a in arrays_middle)
    arrays_trimmed_middle = [a[:min_len_middle] for a in arrays_middle]
    simulation_middle = linear_interpolation_y("simulation_trajectory_middle.txt")[:min_len_middle]
    average_middle = sum(arrays_trimmed_middle) / len(arrays_trimmed_middle)
    error_middle = average_middle - simulation_middle

    sum_of_squares_error_middle = np.sum(error_middle**2)
    RMSE_middle = np.sqrt(sum_of_squares_error_middle / min_len_middle)
    print(RMSE_middle)

    return simulation_small, simulation_middle, average_small, average_middle, error_small, error_middle

