# Init item as list
items = []

# Loop only break when EOF
while True:
    try:
        items.append(input().upper())
    except EOFError:
        break

# run sort method on items list
items.sort()

# init prev as None, used to check if current item is same as prev
prev = None
for item in items:
    if item != prev:
        quantity = items.count(item)
        print(quantity, item)
    # save current item as prev before next iteration
    prev = item