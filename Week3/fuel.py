# infinite loop
while True:
    # try code might error
    try:
        frac = input("Fraction: ").split("/")
        percent = (int(frac[0]) / int(frac[1])) * 100
        # validate percent in range, if not restart loop
        if not 0 <= percent <= 100:
            continue
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break

percent = round(percent)
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(percent, "%", sep = "")