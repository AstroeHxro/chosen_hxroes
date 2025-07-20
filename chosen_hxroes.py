
#Introduction To Game
print('')
print('')
print('Welcome Adventurer! In this game, you will use your keyboard to choose')
print('between the various options provided!')
print('')
print('(ex: Typing 1 will choose option 1, typing 2 will choose')
print('option 2, and so on and so forth. Just like your adventure!)')
print('')
print('')
print('This world is cruel and unforgiving...')
print('Only the strong and cunning can possibly survive!')
print('Only YOU can choose the role that you play!')
print('There are four HEROES, but you may ONLY choose one!')
print('Who will you become in order to survive?...')
print("")
print('(1: Knight, 2: Mage, 3: Archer, 4: Berserker)')
print('')
print('')


#Heros' Journeys
def knight_advent():
    print('You chose The Knight!')
    print('')
    print('The Dark Forest is crawling with untold horrors...')
    print('Upon one morning, awoken a lone Knight. Tho this Knight knew not of fear, he remained wary of death.' \
    'His memories lost, blown away with the winds which carry life. Scattered across the lands like pollen in the spring. ' \
    'Waiting...Yearning... He longed to regain what felt like a piece...no the whole of his soul, stolen and sealed away far ' \
    'into the depths between love and madness. The only thing in this world to hold his trust was his sword and his sword alone.')

    #Choices: Knight
    print('')
    print('Now...Choose!')
    print('')
    sword_choice = int(input('1: Greatsword or 2: Broadsword? '))
    if sword_choice == 1:
        print('')
        print('You Chose the Greatsword!')
        print('')
        print('Some time passes...The Knight, partaking in his ealy afternoon meal, is interrupted by a sudden disturbance. Three towering orcs,' \
        'with skin the shade of grass and gripping clubs easily mistaken for young trees, barge into his humble abode. What was once considered'\
        'a safe haven, is now infested with those who find pleasure in dealing death. Armed with his Greatsword, the Knight' \
        ' ponders as to how he should deal with these lowly pests.')
        print('')
        print('Now...Choose!')
        print('')
        orc_choice = int(input('1: All three at once? or 2: One at a time? '))
        if orc_choice == 1 or 2:
            print('TO BE CONTINUED!')
            
    elif sword_choice == 2:
        print('')
        print('You chose the Broadsword!')
        print('')
        print('Some time passes...Heavy rain with thunder clapping as if the gods themselves jump for joy. A grin, piercing through the darkness, draws' \
        'attention like second nature. It appears to be effortless. The knight gazes upward at the dark force that disturbs his idle slumber. He has been here before.' \
        'There is nothing to fear, for he has conquered death far more times than he has gazed upon the sunset. His broadsword, gleaming with a shine similar to diamonds' \
        'which were submearged under the purist of holy waters.')
        print('Now...Choose!')
        print('')
        beast_choice = int(input('1: Charge the mysterious beast? or 2: Bring it into the light? '))
        if beast_choice == 1 or 2:
            print('TO BE CONTINUED!')



def mage_advent():
    print('You chose The Mage!')
    print('')
    print('The Dark Forest is crawling with untold horrors...')
    print('Ancient mostrosities have been know to plauge these foul lands.')
    print('Even the bravest of warriors fear death, but only a true Knight ')

def archer_advent():
    print('You chose The Archer!')
    print('')
    print('The Dark Forest is crawling with untold horrors...')

def berserker_advent():
    print('You chose The Berserker!')
    print('')
    print('The Dark Forest is crawling with untold horrors...')

def default():
    print('lo siento mami')


#Choose Your Hero
funcs_dict_heroes = {1: knight_advent, 2: mage_advent, 3: archer_advent, 4: berserker_advent}

choice = int(input('Now...Choose! '))

final = funcs_dict_heroes.get(choice)


if choice in funcs_dict_heroes:
    print('')
    final()
else: 
    print('Lo Siento Mami! But that is not an option!')






   

