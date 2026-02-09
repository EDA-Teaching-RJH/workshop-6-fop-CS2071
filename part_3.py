a = 0
b = 0
c = False

def main():
    Speed()
    Coordinates()

def Speed():
    try:
        a = int(input("Enter Motor Speed: ___"))
    except ValueError:
        print("Error: Corrupted Signal. Maintaining current speed.")

def Coordinates():
    while True:
        try:
            b = int(input("Input X Coordinate: ___"))
            c = str(b).isnumeric()
        except ValueError:
            print("Incorrect Value Type")
        if c is True:
            break

main()
print()