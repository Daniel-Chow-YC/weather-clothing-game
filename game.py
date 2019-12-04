# print('What is the weather like today?')
# weather = input("Is it sunny, rainy, stormy or rainy and stormy: ").lower()
#
# if weather == 'sunny':
#     print('Take your shorts!')
# elif weather == 'rainy':
#     print('Take your umbrella')
# elif weather == 'stormy':
#     print('Take your rain coat')
# elif weather == 'rainy and stormy':
#     print('Stay home.')
# else:
#     print("Sorry, I didn't quite catch that.")

print('What is the weather like today?')
weather = 'none'
while weather != 'no more magic':
    weather = input("Is it sunny, rainy, stormy or rainy and stormy: ").lower()
    if weather == 'no more magic':
        break
    elif weather == 'sunny':
        print('Take your shorts!')
    elif weather == 'rainy':
        print('Take your umbrella')
    elif weather == 'stormy':
        print('Take your rain coat')
    elif weather == 'rainy and stormy':
        print('Stay home.')
    else:
        print("Sorry, I didn't quite catch that.")