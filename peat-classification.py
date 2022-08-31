print("Welcome to the program to classify peat based on ASTM standard!\n")

def peat_classification():

    # INPUTS

    fibers = float(input("% of fibers = "))
    ash = float(input("% of ash = "))
    pH = float(input("pH = "))

    # PROCESS

    if fibers < 33:
        print("Sapric")
    elif fibers >= 33 and fibers <= 67:
        print("Hemic")
    else:
        print("Fibric")

    if ash < 5:
        print("Low ash")
    elif ash >= 5 and ash <= 15:
        print("Medium ash")
    else:
        print("High ash")

    if pH < 4.5:
        print("Highly acidic")
    elif pH >= 4.5 and pH <= 5.5:
        print("Moderate acidic")
    elif pH > 5.5 and pH < 7:
        print("Slightly acidic")
    else:
        print("Basic")

peat_classification()
print()
decision = input("Classify again? (Y) / (N): ")
while decision != "N":
    print()
    peat_classification()
    print()
    decision = input("Classify again? (Y) / (N): ")
