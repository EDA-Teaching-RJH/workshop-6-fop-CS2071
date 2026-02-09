Travel_Log = []

while True:
    try:
        a = int(input("Sensor Reading (Slope Angle):"))
        if a > 45:
            print("CRITICAL TILT! HALTING.")
            print("Mission Terminated.")
            print("Total steps taken:", len(Travel_Log)+1)
            print(Travel_Log)
            break
        else:
            Travel_Log.append(a)
            print(Travel_Log)
    except ValueError:
        print("Sensor Glitch")