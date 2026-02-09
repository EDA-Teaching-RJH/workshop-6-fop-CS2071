command_batch = ["MOVE 10", "TURN LEFT", "MOVE 5", "MOVE five", "DIG","MOVE 20","XÆA-12", "RETURN", "MOVE 15"]
Set = ["MOVE", "DIG", "TURN"]
Rover_State = {"x": 0, "y": 0, "samples": 0}
Distance = int(0)
Count = int(0)
Dug = 0

while True:
    try:
        Filtered = str(command_batch[0+Count]).split()
    except:
        print("End Run")
        break
    if Filtered[0] == Set[0]:
        try:
            Distance = Distance + int(Filtered[1])
            Rover_State.update({"y": Distance})
            print(Rover_State)
        except:
            print("Error: Invalid distance ignored")
            pass
    if Filtered[0] == Set[2]:
        print("Turning...")
    if Filtered[0] == Set[1]:
        print("Digging...")
        Rover_State.update({"samples": Dug+1})
    if not Filtered[0] in Set:
        print("Error: Unknown command sequence")
        print(Filtered)

    Count = Count +1