# function convert accepts input and returns with converted emojis
def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

# function main that prompts input, calls convert then prints
def main():
    user_input = input()
    post = convert(user_input)
    print(post)

main()