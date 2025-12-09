from linear_interpolation import linear_interpolation
import numpy as np

arrays_small = [
    linear_interpolation("./small_airplane_trajectories/small_airplane_trajectory_no1.txt"),
    linear_interpolation("./small_airplane_trajectories/small_airplane_trajectory_no2.txt"),
    linear_interpolation("./small_airplane_trajectories/small_airplane_trajectory_no3.txt"),
    linear_interpolation("./small_airplane_trajectories/small_airplane_trajectory_no4.txt"),
    linear_interpolation("./small_airplane_trajectories/small_airplane_trajectory_no5.txt")
]

min_len_small = min(len(a) for a in arrays_small)
arrays_trimmed_small = [a[:min_len_small] for a in arrays_small]

average_small = sum(arrays_trimmed_small) / len(arrays_trimmed_small)
print(average_small)

arrays_middle = [
    linear_interpolation("./middle_airplane_trajectories/middle_airplane_trajectory_no1.txt"),
    linear_interpolation("./middle_airplane_trajectories/middle_airplane_trajectory_no2.txt"),
    linear_interpolation("./middle_airplane_trajectories/middle_airplane_trajectory_no3.txt"),
    linear_interpolation("./middle_airplane_trajectories/middle_airplane_trajectory_no4.txt"),
    linear_interpolation("./middle_airplane_trajectories/middle_airplane_trajectory_no5.txt")
]

min_len_middle = min(len(a) for a in arrays_middle)
arrays_trimmed_middle = [a[:min_len_middle] for a in arrays_middle]

average_middle = sum(arrays_trimmed_middle) / len(arrays_trimmed_middle)
print(average_middle)