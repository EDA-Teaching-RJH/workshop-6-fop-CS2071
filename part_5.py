Status = {"Power": 100, "Samples": 0}
Inventory = []
Count = int(0)
Cost = int(100)

while True:
    # The Question
    a = str(input("Dig (D), Report (R), or Stop (S) ? ")).strip()

    # Dig, Report, or Stop commands
    if a is "D":
        b = input("Sample Name: ")
        Inventory.append(b)
        Count = Count +1
        Status.update({"Samples": Count})
        Cost = Cost -10
        Status.update({"Power": Cost})
    if a is "R":
        print(Status, Inventory)
    if a is "S":
        print(Status)
        break

    if Cost is 0:
        print("Rover Has Ran Out Of Power")
        print("Current Inventory", Inventory, "Amount of Samples", Status["Samples"])
        break
