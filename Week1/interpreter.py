# Prompt for input and split into xyz variables
# Format x, z as float
x, y, z = input("Expression: ").split()
x, z = float(x), float(z)

# Arithmetic operation funtion for +, -, *, or /
def opr():
    match y:
        case "+":
            result = x + z
        case "-":
            result = x - z
        case "*":
            result = x * z
        case "/":
            result = x / z
    return result

# Calls opr func, print returned result
print(opr())