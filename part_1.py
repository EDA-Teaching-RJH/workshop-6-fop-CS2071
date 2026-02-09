# Sample Bay
Sample_Bay = ["Basalt", "Silica", "Iron", "Dust"]

# Part 1.1
print("-------- Part 1.1 --------")
Upper = len(Sample_Bay) - 1
print("First", "Last", "Total")
print(Sample_Bay[0], Sample_Bay[Upper], Upper)
print("")

# Part 1.2
print("-------- Part 1.2 --------")
i = 0
for Sample_bay in Sample_Bay:
    print("Transmitting data for:", Sample_Bay[0+i])
    i = i + 1
print("")

# Part 1.3
print("-------- Part 1.3 --------")
New_Findings = []
a = 3
while a > 0:
    New_Findings.append(input("Input New Findings: ___ "))
    a = a - 1
else:
    print(New_Findings)
print("")

# Part 1.4
print("-------- Part 1.4 --------")
if "Dust" in Sample_Bay:
    print("Found Dust")
    Sample_Bay.remove("Dust")
    print("Removed Dust From Sample_Bay")
    print(Sample_Bay)
else:
    print("No Dust Found In Sample_Bay")