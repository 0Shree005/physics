import matplotlib.pyplot as plt
import numpy as np

def x_position(v0, theta, time, g):
    return v0 * np.cos(theta) * time

def y_position(v0, theta, time, g):
    return v0 * np.sin(theta) * time - 0.5 * g * time ** 2

#
v0 = 20 #m/s
theta = np.radians(45) #radians
g = 9.81 #m/s^2
time_step = 0.01 # seconds
total_time = 5 # seconds

#empty lists to store positions
x_positions = []
y_positions = []

# Calculating positions

for t in np.arange(0, total_time + time_step, time_step):
    x = x_position(v0, theta, t, g)
    y = y_position(v0, theta, t, g)
    x_positions.append(x)
    y_positions.append(y)


# plotting the positions
plt.plot(x_positions, y_positions)

plt.xlabel("Horizontal Position (X)")
plt.ylabel("Vertical Position (Y)")
plt.title("Projectile Motion with Initial Velocity" + str(v0) + "m/s and angle" + str(theta) + " degrees")

plt.grid(True) # grid lines

plt.show()