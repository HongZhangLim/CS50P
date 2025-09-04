# list month, index + 1 will return month in numeric
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:  # keep looping until a valid date
        date_str = input("Date: ").strip()  
        # ask user to input a date
        # .strip() removes spaces

        # Case 1: numeric format with /
        if "/" in date_str:  
            # check if input contains "/" like MM/DD/YYYY
            try:
                m, d, y = date_str.split("/")  
                # split string into 3 parts: month, day, year

                if not (m.isdigit() and d.isdigit() and y.isdigit()):
                    continue  
                # make sure all str parts are digits
                # if not, restart while True loop

                m = int(m)  # convert month string to integer
                d = int(d)  # convert day string to integer
                y = int(y)  # convert year string to integer

                if int(m) <= 12 and int(d) <= 31:
                    # validate: month ≤ 12 and day ≤ 31

                    print(y, "{:02}".format(m), "{:02}".format(d), sep = "-")  
                    # print in YYYY-MM-DD format
                    # {:02} → zero-pad
                    break  # stop loop after valid date found

            except ValueError:  
                # if non-numeric str enter int(), ignore and restart loop
                continue

        # Case 2: word month format with ,
        elif "," in date_str:  
            # check if input contains ","
            try:
                m, d, y = date_str.split(" ")  
                # split by spaces

                d = d.removesuffix(",")  
                # remove , from day str

                if not (m in months and d.isdigit() and y.isdigit()):
                    continue  
                # validate
                # if not, restart loop

                m = get_month(m)  # convert month name to number
                d = int(d)        # convert day to integer
                y = int(y)        # convert year to integer

                if m <= 12 and d <= 31:
                    # validate month, day range
                    print(y, "{:02}".format(m), "{:02}".format(d), sep = "-")
                    # printing rule: YYYY-MM-DD
                    break

            except ValueError:
                # if non-numeric enter int(), restart loop
                continue

# function: convert month name → month number
def get_month(month):
    return months.index(month) + 1  

main()