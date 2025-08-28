def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # check length 2~6 and return false if not
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # loop each character
    for i, c in enumerate(s):
        # check if first two char are alpha
        if i < 2 and not c.isalpha():
            return False
        # check symbols by char
        if not c.isalnum():
            return False
        # check digits by char
        if c.isdigit():
            # c = s[i]
            if s[i-1].isalpha() and s[i] == "0":
                return False
            # identify using index i inclusive, j exclusive
            if not s[i:].isdigit():
                return False
    return True

main()