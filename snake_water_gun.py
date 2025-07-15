import random

def swg(comp, mine):
    if comp == mine:
        return None
    if comp == 's' and mine == 'g':
        return True
    elif comp == 'g' and mine == 'w':
        return True
    elif comp == 'w' and mine == 's':
        return True
    else:
        return False

choice = ('s', 'w', 'g')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input('Choose either of s (snake), w (water), g (gun): ')

win = swg(comp, mine)
print(f'You chose {mine} and computer chose {comp}')
if win == None:
    print('Match draw buddy')
elif win:
    print('You win buddy')
else:
    print('You lose buddy')
    
   