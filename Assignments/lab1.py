#    A programme that that calculates a person's BMI and prints a message telling whether
#    they are above, within or below the healthy range
# by: Caleb Otchi


def BMI():
    print(
        "This programme calculates your BMI and lets you know\nwhether it's above, within or below the healthy range.\n")

    # Now the user inputs their weight and height
    # w is the weight in pounds
    w = eval(input("Enter the weight(in pounds) of person: "))
    # h is the height in inches
    h = eval(input("Enter the height(in inches) of person: "))
    print("\n")

    # The formula below is to calculate the BMI
    BMI = (w * 720) / (h ** 2)
    print("The person's BMI is {0:0.2f}".format(BMI))

    # Below is a decision structure to determine if the person is
    # above, within or below the healthy range
    if BMI < 19:
        print("This means that the person is below the healthy range.")
    elif BMI >= 19 and BMI <= 25:
        print("This means that the person is within the healthy range.")
    else:
        print("This means that the person is above the healthy range.")


BMI()
