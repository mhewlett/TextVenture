conv_kg = 0.453592
conv_m = 0.3048
loop = "Y"
while loop.upper() == "Y":
    name = input("Enter your name: ")
    print()
    print("Howdy " + name +". I hope you are having a good day.")
    print("I am going to request a couple of measurements to calculate your BMI.")
    print()
    weight = input("Enter your weight: ")
    if weight.replace(".","",1).isdigit():
        weight = float(weight)
        entry1 = input("Is that (K)g or (L)bs? ").upper()
        if entry1 != "K" and entry1 != "L":
            print("Please respond with the appropriate answer.")
            input("Press enter to start over.")
            print()
            continue
        elif entry1.upper() == "K":
            weight_k = weight
            print("Weight in kilograms: " + str(weight_k) + "Kg.")
        else:
            if entry1.upper() == "L":
                weight_k = float(round((weight * conv_kg),2))
                print("Weight converted to kilograms: " + str(weight_k) + "Kg.")
                print()
    else:
        print("Please enter your weight.")
        input("Press enter to start over.")
        continue

    height = input("Enter your height: ")
    if height.replace(".","",1).isdigit():
        height = float(height)
        entry2 = input("Is that in (M)eters or (F)eet? ").upper()
        if entry2 != "M" and entry2 != "F":
            print("Please respond with the appropriate answer.")
            input("Press enter to start over.")
            print()
            continue
        elif entry2.upper() == "M":
            height_m = height
            print("Height in meters: " + str(height_m) + "M.")
        else:
            if entry2.upper() == "F":
                height_m = float(round((height * conv_m),2))
                print("Height converted to meters: " + str(height_m) + "M.")
    else:
        print("Please enter your height.")
        input("Press enter to start over.")
        continue
    print()
    input("Press enter to calculate BMI.")
    bmi = weight_k / height_m ** 2
    round(bmi,2)
    print("*********************************************")
    print("BMI Result for " + name + ": ")
    print("Your weight in kilograms is " + str(round(weight_k,2)) + ". ")
    print("Your height in meters is " + str(round(height_m,2)) + ". ")
    print("Your calculated BMI is " + str(round(bmi,2)) + ". ")
    print("*********************************************")

    if bmi >= 25:
        print("Conclusion:")
        print("You are overweight.")
        print()
    else:
        print("Conclusion:")
        print("You are not overweight.")
        print()

    loop = input("Would you like to go again? Y or N ")

print("Have a great day! :)")
