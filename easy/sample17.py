def canProcessOrder(beef,chicken,salad,coffee,tea):
    if (beef ^ chicken) and (coffee ^ tea):
        return True
    else:
        return False