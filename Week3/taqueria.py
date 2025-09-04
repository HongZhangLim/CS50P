price_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# init total as 0
total = 0
# infinite loop
while True:
    # try might error
    try:
        item = input("Item: ").title()
        if item in price_dict:
            # return price from dict
            price = (price_dict[item])
            total += price
            # total:.2f = format(total, '.2f')
            print(f"Total: ${total:.2f}")
    # except ctrl d to end input, break loop
    except EOFError:
        break