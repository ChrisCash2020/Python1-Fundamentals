restart = 1
while restart <= 1:
    wizard, wizard_hp, wizard_damage = 'Wizard', 70, 150
    elf, elf_hp, elf_damage = 'Elf', 100, 100
    human, human_hp, human_damage = 'Human', 150, 20
    orc, orc_hp, orc_damage = 'Orc', 90, 100
    dragon_hp, dragon_damage = 300, 50
    print("1)   ", wizard )
    print("2)   ", elf )
    print("3)   ", human )
    print("4)   ", orc)
    print("5)   ", "Quit Game")
    choice = input("Choose your character ").lower()
    while True:
        if choice == '1' or choice == 'wizard':
            character, character_hp, character_damage = wizard, wizard_hp, wizard_damage
            print('You have chosen the character: ', character)
            print('Health: ', character_hp)
            print('Damage: ',character_damage )
            print()
            break
        elif choice == '2' or choice == 'elf': 
            character, character_hp, character_damage = elf, elf_hp, elf_damage
            print('You have chosen the character: ', character)
            print('Health: ', character_hp)
            print('Damage: ',character_damage )
            print()
            break
        elif choice == '3' or choice == 'human': 
            character, character_hp, character_damage = human, human_hp, human_damage
            print('You have chosen the character: ', character)
            print('Health: ', character_hp)
            print('Damage: ',character_damage )
            print()
            break
        elif choice == '4' or choice == 'orc': 
            character, character_hp, character_damage = orc, orc_hp, orc_damage
            print('You have chosen the character: ', character)
            print('Health: ', character_hp)
            print('Damage: ',character_damage )
            print()
            break
        elif choice == '5' or choice == 'quit game':
                print('Game Over')
                exit()
        else:
            print('Invalid choice')
            print("1)   ", wizard )
            print("2)   ", elf )
            print("3)   ", human )
            print("4)   ", orc)
            print("5)   ", "Quit Game")
            choice = input("Choose your character ").lower()
    while True :
        dragon_hp = dragon_hp - character_damage
        print('The', character, "Damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)
        print()
        if dragon_hp <= 0:
            print('The Dragon has lost the battle.')
            break
        character_hp = character_hp - dragon_damage
        print('The Dragon strikes back at the', character)
        print('The', character + "'s hitpoints are now: ", character_hp)
        print()
        if character_hp <= 0:
            print('The', character, "has lost the battle.")
            break
    restart_choice = input("restart? \nyes or no\n\n").lower()
    if restart_choice == 'yes':
        restart = restart
        print('\nNew Game')
    elif restart_choice == 'no':
        restart = restart + 1
        print('Game Over')