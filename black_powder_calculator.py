""" Calculates black powder amount in grams given shear pin 
and internal pressure volume"""

import numpy as np

# Force required to break 3 shear pins [lbf]
shear_force = 119.4

# Force required to overcome friction of nosecone [lbf]
friction_force = 40

# [User input] Internally pressurized chamber volume [in]
chamber_length = 13
# [User input] Internally pressurized chamber diameter [in]
chamber_diameter = 5.5

# Calculated chamber area [in^2]
chamber_area = chamber_diameter**2 * np.pi / 4
# Calculated chamber volume [in^3]
chamber_volume = chamber_area * chamber_length

# Calculate required chamber pressure [PSI]
chamber_pressure = (shear_force + friction_force) / chamber_area

# Constant R for FFFFg black powder [in/K]
R_c = 478.66
# Black powder combustion temperature [K]
T = 1739
# Gravitational constant [in/s^2]
g = 386.04

# Calculate black powder mass [lbf]
bp_mass = chamber_pressure * chamber_volume / (R_c * T)

# Convert black powder mass to gram units [g]
bp_gram_mass = np.round(bp_mass * 453.59, 2)
print(f"Black Powder [g]: {bp_gram_mass}")
