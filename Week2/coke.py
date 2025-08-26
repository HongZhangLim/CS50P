def main():
    print("Amount Due: 50")
    # Assign inserted to zero so that it uses same loop for <50
    inserted = 0

    # Repeat this loop for <50
    while inserted < 50:
        # Assign new coin as added to differentiate from previous value
        added = int(input("Insert Coin: "))
        # Calls check_valid func on added, then add it onto inserted
        inserted += check_valid(added)
        # Still within loop, only print amount due if inserted <50
        if inserted < 50:
            print("Amount Due:", 50 - inserted)
    if inserted == 50:
        print("Change Owed: 0")
    else:
        print("Change Owed:", inserted - 50)

# Func check valid to only accept 25, 10 ,5
def check_valid(inserted):
    if inserted in (25, 10, 5):
        return inserted
    else:
        return 0

main()