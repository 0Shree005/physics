# Projectile Motion Simulation

## Introduction
This project simulates the motion of a projectile launched with an initial velocity (v0) at an angle (θ) under the influence of gravity (g) and air resistance (b). Euler's method is used to numerically solve the equations of motion.

## Objective
To compare the trajectory of the projectile with and without air resistance, and to analyze the effect of air resistance on the projectile’s motion.

## Methodology

### Equations of Motion

#### Equations without air resistance
x(t) = v0 cos(θ) t 
y(t) = v0 sin(θ) t - 1/2gt^2

#### Equations with air resistance
ax = -b * v * vx
 ay = -g - b * v * vy
{ where v = sqrt( (vx^2) + (vy^2) ) }

### Updating Velocities and Positions Using Euler's Method

#### Updating Velocities
vx (i + 1) = vx(i) + ax(i)Δt
vy (i + 1) = vy(i) + ay(i)Δt

#### Updating Positions
x (i + 1) = x(i) + vx(i)Δt
y (i + 1) = y(i) + vy(i)Δt

### Implementation
1. Code initializes the projectile’s velocity (20 m/s) and position (0,0).
2. A ```for``` loop iterates through the total time, updating velocities and positions using the calculated accelerations.
3. The positions are stored on each iteration, which are then used by Matplotlib to plot the trajectory.

## Results
The generated plot shows the trajectory of the projectile under the influence of gravity and air resistance. The curve represents the parabolic path of the projectile, and it can be observed that the presence of air resistance affects both the range and the height of the projectile.

### Path without Air Resistance
- The projectile follows a standard parabolic trajectory; it is a symmetric path.
- The maximum height reached is approximately 10.3 m.
- The distance traveled is approximately 40.5 m.

### Path with Air Resistance
- The projectile’s range and maximum height are reduced due to the opposing force of air resistance. The trajectory is less symmetric, and the descent is steeper compared to the ascent.
- The maximum height reached is approximately 1.18 m.
- The distance traveled is approximately 2.45 m.

