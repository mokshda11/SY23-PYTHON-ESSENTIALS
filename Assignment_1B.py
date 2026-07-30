#GRAVITATIONAL CONSTANTS
Earth_gravity = 9.8 
Moon_gravity = (1/6) * 9.8

#User defined function to compute weight
def compute_weight(m,g):
	return m*g

#Main program block
obj_mass = float(input("Please enter the mass of the object (kg): "))

#Perform Calculations
w_earth = compute_weight(obj_mass, Earth_gravity)
w_moon = compute_weight(obj_mass, Moon_gravity)

#Display Results
print(f"Objects weight on Earth: {w_earth}N")
print(f"Objects weight on Moon: {w_moon}N")