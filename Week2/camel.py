# Prompt for input, assign as camel
camel = input("camelCase: ")
# Print snake_case, remove end so it prints on same line
print("snake_case: ", end="")

# Use for loop for looping over character as str are iterable
for character in camel:
    if character.islower():
        print(character, end="")
    else:
        print("_" + character.lower(), end="")
# Print blank line as end=/n was removed
print()