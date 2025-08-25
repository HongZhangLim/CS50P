# Assign ans as variable, accept input
ans = input("What is  the Answer to the Great Question of Life, the Universe and Everything? ")

# Process ans
ans = ans.lower().strip()

# Use match-case as conditionals
match ans:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")