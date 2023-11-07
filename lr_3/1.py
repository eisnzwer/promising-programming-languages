class SunSystem:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

class Planets:
    def __init__(self, name, diameter):
        self.name = name
        self.diameter = diameter
        self.satellites = []

    def add_satellite(self, satellite):
        self.satellites.append(satellite)

    def get_planet(self):
        print(f"Planet: {self.name}")
        print(f"Diameter: {self.diameter} km")
        if self.satellites:
            print("Satellites:")
            for satellite in self.satellites:
                print(f"- {satellite.name} (Diameter: {satellite.diameter} km)")
        else:
            print("No satellites.")

class Satellites:
    def __init__(self, name, diameter, planet):
        self.name = name
        self.diameter = diameter
        self.planet = planet

sun_system = SunSystem()

earth = Planets("Earth", 12742)
moon = Satellites("Moon", 3475, earth)
earth.add_satellite(moon)

mars = Planets("Mars", 6779)
phobos = Satellites("Phobos", 22, mars)
deimos = Satellites("Deimos", 12, mars)
mars.add_satellite(phobos)
mars.add_satellite(deimos)

sun_system.add_planet(earth)
sun_system.add_planet(mars)

for planet in sun_system.planets:
    planet.get_planet()
    print("=" * 30)
