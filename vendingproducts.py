names = [" crisps", "Chocolate", "Water"]
prices = [100, 120, 80]


def show_products():
    print("\nVENDING MACHINE")

    for number in range(len(names)):
        print(number + 1, "-", names[number], "-", prices[number],"p")
