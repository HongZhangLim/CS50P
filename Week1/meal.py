def main():
    time = input("What time is it? ")
    # Pass computed outcome value of func
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# function converts time, a str to float
def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m)
    # Return value at the end of func to generate outcome
    return h + (m / 60)


if __name__ == "__main__":
    main()