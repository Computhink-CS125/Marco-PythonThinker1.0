# ============================================================
# Q2. List Operations
# ============================================================
# You are working with a list of planets.
# The program must perform several operations on this list.

# Program Requirements:
# - Use the list:
#   planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
# - Print the 3rd item using index
# - Append "neptune" to the list
# - Rename "mars" to "muskworld"
# - Remove "uranus" from the list
# - Using a for loop, print all the planets one by one

# ============================================================

planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
print(planets[2])
planets.append("neptune")
index_to_change = planets.index("mars")
planets[index_to_change] = "muskworld"
planets.remove("uranus")
for planet in planets:
    print(planet)