# Part 2.1
print("-------- Part 2.1 --------")
Rover_Status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"}
print("Battery Status:", Rover_Status["Battery"])
print("")

# Part 2.2
print("-------- Part 2.2 --------")
Rover_Status.update({"Battery": 85})
Rover_Status.update({"Heater": "On"})
Rover_Status.update({"Speed": 5})
print(Rover_Status)
print("")

# Part 2.3
print("-------- Part 2.3 --------")
Site_A = {"Site": "Crater A", "Radiation": "Low", "Water": False} 
Site_B = {"Site": "Dune B", "Radiation": "High", "Water": True}
Mission_Log = [Site_A, Site_B]
for Mission_Log in Mission_Log:
    print(Mission_Log["Site"], "has", Mission_Log["Radiation"], "radiation.")