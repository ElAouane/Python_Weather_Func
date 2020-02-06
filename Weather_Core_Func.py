def sunny(item):
    return item.lower() == 'sunny'
def stormy(item):
    return item.lower() == 'stormy'
def stormy_rainy(item):
    return 'rainy' in item.lower() and 'stormy' in item.lower()
def rainy(item):
    return item.lower() == 'rainy'
def exit_(item):
    return item == 'No more Magic'
