def canProcessOrder(beef, chicken, salad, coffee, tea):
    if not (beef == chicken) and not (coffee == tea):
        return True
    return False
