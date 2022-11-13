print("Welcome to the program to classify peat based on ASTM standard and the Von Post scale!\n")

def peat_classification():

    # INPUTS

    fibers = float(input("% of fibers = "))
    organic = float(input("% of organic content = "))
    ash = 100 - organic
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

def peat_visual_classification():
    vonPost = input("Von Post scale: ")
    fibers = float(input("% of fibers = "))
    if (vonPost == "H1" or vonPost == "H2" or vonPost == "H3") and fibers > 67:
        print("Ptf")
    elif (vonPost == "H4" or vonPost == "H5" or vonPost == "H6") and (fibers >=33 and fibers <= 67):
        print("Pth")
    elif (vonPost == "H7" or vonPost == "H8" or vonPost == "H9" or vonPost == "H10") and fibers < 33:
        print("Pta")
    else:
        print("Non-symbol")

def decision_classification():
    choice = input("(l)ab or (v)isual?: ") 
    if choice == "l":
        peat_classification()
    elif choice == "v":
        peat_visual_classification()

decision_classification()
print()
decision = input("Classify again? (Y) / (N): ")
while decision != "N":
    print()
    decision_classification()
    print()
    decision = input("Classify again? (Y) / (N): ")
