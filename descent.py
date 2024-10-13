from rocketpy import Environment, Rocket, Flight

env = Environment(
    railLength=5,
    latitude=32.990254,
    longitude=-106.974998,
)

rocket = Rocket(
    # Replace with custom motor
    motor="Cesaroni_M1670",
    # Rocket radius in meters
    radius=127 / 1000,
    # Rocket dry mass in kg
    mass=19,
)

rocket.add_parachute(
    "Drogue",
    CdS=1.2,
    trigger="apogee",
    lag=1,
    noise=(0, 0, 0),
    terminalVelocity=70,
    lineLength=5,
)

rocket.add_parachute(
    "Main",
    CdS=10.0,
    trigger="altitude",
    lag=1,
    noise=(0, 0, 0),
    terminalVelocity=5,
    lineLength=10,
    openingHeight=500,
)

flight = Flight(rocket, environment=env)

flight.allInfo()
