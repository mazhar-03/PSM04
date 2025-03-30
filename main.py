import math
import numpy as np
import matplotlib.pyplot as plt

# OBJECT 1 (Sphere)
mass_obj1 = 1
radius_obj1 = 2
inertia_obj1 = 2 / 3 * mass_obj1 * radius_obj1 ** 2
angular_velocity_obj1 = 0
rotation_angle_obj1 = 0

# OBJECT 2 (Ball)
mass_obj2 = 1
radius_obj2 = 2
inertia_obj2 = 2 / 5 * mass_obj2 * radius_obj2 ** 2
angular_velocity_obj2 = 0
rotation_angle_obj2 = 0

# SHARED VARIABLES
inclination_angle = np.deg2rad(45)
gravitational_acceleration = 10
position_obj1 = 0
velocity_obj1 = 0
position_obj2 = 0
velocity_obj2 = 0
height = 2
time = 0
time_step = 0.1
simulation_duration = 5
num_steps = int(simulation_duration / time_step)

initial_angle_obj1 = 0
initial_angle_obj2 = 0

# RESULT STORAGE
time_values = np.zeros(num_steps)
position_obj1_values = np.zeros(num_steps)
position_obj2_values = np.zeros(num_steps)
height_obj1_values = np.zeros(num_steps)
height_obj2_values = np.zeros(num_steps)
rotation_obj1_values = np.zeros(num_steps)
rotation_obj2_values = np.zeros(num_steps)


def calculate_linear_motion(inertia, mass, radius, velocity, position):
    acceleration = gravitational_acceleration * np.sin(inclination_angle) / (1 + inertia / (mass * radius ** 2))
    velocity_delta = acceleration * time_step / 2
    position_change = (velocity + velocity_delta) * time_step
    velocity_change = acceleration * time_step
    position += position_change
    velocity += velocity_change
    height = radius
    return position, velocity, height, acceleration


def calculate_rotational_motion(radius, angular_velocity, acceleration, initial_angle):
    angular_acceleration = acceleration / radius
    angular_velocity_change = angular_acceleration * time_step
    angle_change = (angular_velocity + angular_velocity_change / 2) * time_step
    angle = initial_angle + angle_change
    rotation_angle = math.pi / 2 - angle
    angular_velocity += angular_velocity_change
    return rotation_angle, angular_velocity, angle_change, angle


# Simulation Loop
for step in range(num_steps):
    position_obj1, velocity_obj1, height_obj1, acceleration_obj1 = calculate_linear_motion(inertia_obj1, mass_obj1,
                                                                                           radius_obj1, velocity_obj1,
                                                                                           position_obj1)
    rotation_obj1, angular_velocity_obj1, angle_change_obj1, initial_angle_obj1 = calculate_rotational_motion(
        radius_obj1, angular_velocity_obj1, acceleration_obj1, initial_angle_obj1)

    position_obj2, velocity_obj2, height_obj2, acceleration_obj2 = calculate_linear_motion(inertia_obj2, mass_obj2,
                                                                                           radius_obj2, velocity_obj2,
                                                                                           position_obj2)
    rotation_obj2, angular_velocity_obj2, angle_change_obj2, initial_angle_obj2 = calculate_rotational_motion(
        radius_obj2, angular_velocity_obj2, acceleration_obj2, initial_angle_obj2)

    time_values[step] = time
    position_obj1_values[step] = position_obj1
    position_obj2_values[step] = position_obj2
    height_obj1_values[step] = height_obj1
    height_obj2_values[step] = height_obj2
    rotation_obj1_values[step] = rotation_obj1
    rotation_obj2_values[step] = rotation_obj2
    time += time_step

# PLOTTING RESULTS
fig, axs = plt.subplots(2, 2)

# Object 1 (Sphere) Linear Motion
axs[0, 0].plot(time_values, position_obj1_values)
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Position Object 1 (m)')
axs[0, 0].set_title('Linear Motion of Object 1 (Position)')

axs[1, 0].plot(time_values, height_obj1_values)
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Height Object 1 (m)')
axs[1, 0].set_title('Height of Object 1')

# Object 2 (Ball) Linear Motion
axs[0, 1].plot(time_values, position_obj2_values)
axs[0, 1].set_xlabel('Time (s)')
axs[0, 1].set_ylabel('Position Object 2 (m)')
axs[0, 1].set_title('Linear Motion of Object 2 (Position)')

axs[1, 1].plot(time_values, height_obj2_values)
axs[1, 1].set_xlabel('Time (s)')
axs[1, 1].set_ylabel('Height Object 2 (m)')
axs[1, 1].set_title('Height of Object 2')

fig.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
