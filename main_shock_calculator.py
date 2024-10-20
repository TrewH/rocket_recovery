import numpy as np

# Drogue descent rate [m/s]
drogue_descent_velocity = 14.63
# Main + Drogue descent rate [m/s]
main_descent_velocity = 5.18
# Velocity at drogue deployment [m/s]
drogue_deployment_velocity = 0
# Velocity at main deployment [m/s]
main_deployment_velocity = 14.63

# Air density at 25,000 ft [kg/m^3]
air_density_drogue = 0.5494
# Air density at 1000ft [kg/m^3]
air_density_main = 1.185
# Area of main parachute [m^2]
main_area = 3**2 * np.pi / 4
# Parachute drag coefficient (both parachutes)
c_d = 2.2
# Rocket mass [kg]
m = 40
# Gravity [m/s^2]
g = 9.81
# Estimated time of parachute to open
deceleration_time = 0.25


"""METHOD ONE : DRAG EQUATION"""
main_force1 = 0.5 * air_density_main * main_deployment_velocity**2 * c_d * main_area
print(f"Snatch Force Method 1: {np.round(main_force1, 2)} N")

"""METHOD TWO: FORCE / DECELERATION"""
main_force2 = m * main_deployment_velocity / deceleration_time
print(f"Snatch Force Method 2: {np.round(main_force2, 2)} N")
