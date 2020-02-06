from Weather_Core_Func import *
while True:
    user_input = input('Say something')
    if sunny(user_input):
        print('Take your short')
    elif rainy(user_input) :
        print('Take your rain coat')
    elif stormy_rainy(user_input):
        print('stay home')
    elif rainy(user_input):
        print('Take your umbrella')
    else:
        print('sorry, I didn\'t quite catch that')
    if exit_(user_input):
        break