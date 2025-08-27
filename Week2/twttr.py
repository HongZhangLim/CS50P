# Prompt for input, assign as text
text = input("Input: ")
# List out vowels, str are already iterable
vowels = "aeiouAEIOU"
# Print output, remove end so it prints on same line
print("Output: ", end="")

# Use for loop for looping over character as str are iterable
for character in text:
    if character not in vowels:
        print(character, end="")

# Print blank line as end=/n was removed
print()