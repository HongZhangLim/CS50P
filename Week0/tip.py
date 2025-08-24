def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Use method to remove $
    d = d.removeprefix("$")
    # Convert string into float
    d = float(d)
    # Return value
    return d

def percent_to_float(p):
    # Use method to remove %
    p = p.removesuffix("%")
    # Convert string into float, then into decimal multiplier
    p = float(p) / 100
    # Return value
    return p

main()
