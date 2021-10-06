import random
diamonds = [ 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD' ]
hand = []
while len(diamonds) > 0:
    user_input = input('Press enter to pick a card, or Q then enter to quit: ')
    if user_input == 'Q':
        break
    else:
        length = len(diamonds) - 1
        rand_guess = random.randint(0, length )
        rm_val = diamonds[rand_guess]
        hand.append(rm_val)
        diamonds.remove(rm_val)
        print('Your hand:', hand)
        print('Remaining cards:', diamonds)
        continue
print('There are no more cards to pick')

