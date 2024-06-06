import matplotlib.pyplot as plt
import numpy as np

# Constants
v0 = 20 #initial velocity (m/s)
theta = np.radians(45) # angle converted to radians
g = 9.81 # acc. due to gravity m/s^2
b = 0 # air resistance coefficient
time_step = 0.01 # seconds
total_time = 5 # seconds


# Conditions
vx = v0 * np.cos(theta) # initial velocity in x direction 
vy = v0 * np.sin(theta) # initial velocity in y direction 
x = 0 # initial position in x direction 
y = 0 # initial position in y direction 

# Lists to store positions
x_positions = [x]

y_positions = [y]


# Euler's Method
for _ in np.arange(0, total_time, time_step):
    # calculating speed
    speed = np.sqrt(vx**2 + vy**2)

    # calculating accelerations
    ax = -b * speed * vx
    ay = -g - b * speed * vy

    # Updating velocities
    vx += ax * time_step 
    vy += ay * time_step

    # Updating positions
    x += vx * time_step
    y += vy * time_step

    # storing positions
    x_positions.append(x)
    y_positions.append(y)

    # break out of the loop if projectile hits the ground
    if y < 0:
        break



# def x_position(v0, theta, time, g):
#     return v0 * np.cos(theta) * time

# def y_position(v0, theta, time, g):
#     return v0 * np.sin(theta) * time - 0.5 * g * time ** 2



# # Calculating positions

# for t in np.arange(0, total_time + time_step, time_step):
#     x = x_position(v0, theta, t, g)
#     y = y_position(v0, theta, t, g)
#     x_positions.append(x)
#     y_positions.append(y)


# plotting the positions
plt.plot(x_positions, y_positions)

plt.xlabel("Horizontal Position (X)")
plt.ylabel("Vertical Position (Y)")
plt.title(f"Projectile Motion with Initial Velocity {v0} m/s and angle {np.degrees(theta)} degrees")
plt.legend()

plt.grid(True) # grid lines

plt.show()