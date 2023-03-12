def part_1(choose):
    if choose == 'left':
        choose_2 = input('Do you swim of wait? Type swim or wait: ')
        part_2(choose_2)
    else:
        print('Fall into a hole. Game Over')


def part_2(choose):
    if choose == 'wait':
        choose_3 = input('Which door do you choose? Type red, blue or yellow: ')
        part_3(choose_3)
    else:
        print('Attacket by trout. Game Over')


def part_3(choose):
    if choose == 'red':
        print('Burned by fire. Game Over.')
    elif choose == 'blue':
        print('Eaten by beasts. Game Over.')
    elif choose == 'yellow':
        print('''
    8b        d8                                                                               88              
    Y8,    ,8P                                                                                ""              
    Y8,  ,8P                                                                                                 
    "8aa8" ,adPPYba,  88       88    ,adPPYYba, 8b,dPPYba,  ,adPPYba,    8b      db      d8 88 8b,dPPYba,   
    `88' a8"     "8a 88       88    ""     `Y8 88P'   "Y8 a8P_____88    `8b    d88b    d8' 88 88P'   `"8a  
    88  8b       d8 88       88    ,adPPPPP88 88         8PP"""""""     `8b  d8'`8b  d8'  88 88       88  
    88  "8a,   ,a8" "8a,   ,a88    88,    ,88 88         "8b,   ,aa      `8bd8'  `8bd8'   88 88       88  
    88   `"YbbdP"'   `"YbbdP'Y8    `"8bbdP"Y8 88          `"Ybbd8"'        YP      YP     88 88       88  
                                                                                                            
                ''')
    else:
        print('Game Over')

def treasury_island():
    print('Welcome to Treasure Island. Your mission is to find the treasure.')
    choose_1 = input('You are at the cross road. Where do you want to go? Type left of right: ')
    part_1(choose_1)

treasury_island()