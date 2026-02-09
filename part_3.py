def Speed():
    while True:
        try:
            return int(input("Enter Motor Speed: ___"))
        except ValueError:
            print("Error: Corrupted Signal. Maintaining current speed.")

def Coordinates():
    while True:
        try:
            c = int(input("Input X Coordinate: ___"))
            if c < 100 and c > -100:
                return c
            else:
                print("Coordinate out of range")
        except ValueError:
            print("Incorrect Value Type")

a = Speed()
b = Coordinates()


print(a, b)