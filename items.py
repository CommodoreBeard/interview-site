from random import randint, choice

def random_title():
    descriptors = [
        "AMAZING",
        "CHEAP",
        "SHINNY",
        "GENUINE",
        "REAL",
        "PERFECT",
        "NOT STOLEN"
    ]
    return "{}, {} iPhone".format(choice(descriptors), choice(descriptors))

def random_price():
    return '£{}.{}{}'.format(randint(0, 100), randint(0, 9), randint(0, 9))

def new_item():
    return {
        'title': random_title(),
        'price' : random_price()
    }

def items():
    items = []
    for i in range(15):
        items.append(new_item())
    return items