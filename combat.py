import random
from attackhandler import AttackHandler

def hero_attack_assign():
    hero_attacks = [] # Initializes empty array
    counter = 0
    while True:
        if counter < 6: # Allows the hero to roll 6 random attacks
            category = random.randint(1,4)
            if category == 1:
                attack = random.choice(['Slash', 'Cleave', 'Body Slam'])
            elif category == 2:
                attack = random.choice(['Fire Ball', 'Fire Whip', 'Fire Storm', 'Fire Spark', 'Fire Blast'])
            elif category == 3:
                attack = random.choice(['Water Bolt', 'Water Surge', 'Water Shield', 'Water Tide', 'Water Crash'])
            elif category == 4:
                attack = random.choice(['Lightning Strike', 'Lightning Chain', 'Lightning Jolt', 'Lightning Clash', 'Lightning Overload'])
            if attack not in hero_attacks: # Prevents hero from rolling a duplicate attack
                hero_attacks.append(attack)
                counter += 1
        else:
            break
    return hero_attacks

def attack_categories(hero_attacks):
    # Different arrays for different spell types for submenus
    # Attacks > Fire Spells > Displays all fire spells etc
    general = []
    fire_spells = []
    water_spells = []
    lightning_spells = []
    for attack in hero_attacks: # Assumes that all spells will follow a standard naming convention (element + type)
        if 'Fire' in attack:
            fire_spells.append(attack)
        elif 'Water' in attack:
            water_spells.append(attack)
        elif 'Lightning' in attack:
            lightning_spells.append(attack)
        else:
            general.append(attack)
    return general, fire_spells, water_spells, lightning_spells

def speed_roll():
    speed_tie = True
    while speed_tie: # While loop that checks if the hero and monster rolled the same speed, in which case, both their speed is rolled again to prevent speed ties.
        hero_speed = random.randint(1, 20)
        monster_speed = random.randint(1, 20)
        print(f"Rolled speeds: \nHero: {hero_speed}, Monster: {monster_speed}")
        if hero_speed == monster_speed:
            print("Speed tie, rolling speed again!")
            hero_speed = random.randint(1, 20)
            monster_speed = random.randint(1, 20)
        else:
            speed_tie = False
            return hero_speed, monster_speed

def combat_pick(hero_attacks):
    general, fire, water, lightning = attack_categories(hero_attacks) # Calls the attack_categories function to separate spells into types
    available_categories = []
    # Checks if a category contains any spells/attacks and otherwise does not add to available categories if empty (No reason to print lightning spells if hero has none)
    if general: available_categories.append(("General Actions", general))
    if fire: available_categories.append(("Fire Spells", fire))
    if water: available_categories.append(("Water Spells", water))
    if lightning: available_categories.append(("Lightning Spells", lightning))

    input_valid = True
    while input_valid: # Input loop to ensure user picks valid option (Attacks, Defends, or Flees)
        print("\n=== Combat Options ===")
        print("1. Attacks")
        print("2. Defend")
        print("3. Flee")

        choice = input("Choose an action(1-3): ")
        if choice not in ['1', '2', '3']:
            print("Invalid choice, try again.")
            continue

        if choice == '1':
            while True: # Second input loop to ensure user picks valid spell categories (Fire Spells, Water Spells, etc)
                print("\n=== Attacks ===")
                for index, category in enumerate(available_categories, start=1): # Enumerate to pair categories with numbers for user input
                    print(f"{index}. {category[0]}")
                print(f"{len(available_categories)+1}. Back") # Ensures the back option dynamically scales with number of available categories and is always the last option

                category_choice = input("Choose an option: ")

                if category_choice.isdigit() and 1 <= int(category_choice) <= len(available_categories): # Checks if input is valid int and then checks if int falls within valid options
                    selected_category = available_categories[int(category_choice) - 1] # -1 to counterbalance options starting from one but arrays starting from 0
                    category_name, spells = selected_category # Currently the first thing in an array is the category name before being followed by the actual spells, this separates them.

                    while True: # Third input loop to ensure user picks valid spell (Fire Ball, Water Bolt, etc.)
                        print(f"=== {category_name} ===")
                        for index, option in enumerate(spells, start=1):
                            print(f"{index}. {option}")
                        print(f"{len(spells) + 1}. Back")  # Ensures the back option dynamically scales with number of available spells and is always the last option
                        input_choice = input("Choose an option: ")
                        if input_choice.isdigit() and 1 <= int(input_choice) <= len(spells):
                            selected_spell = spells[int(input_choice) - 1]
                            print(f"You have selected {selected_spell}!")
                            return selected_spell
                        elif input_choice == str(len(spells) + 1):
                            break
                        else:
                            print("Invalid choice, try again.")

                elif category_choice == str(len(available_categories)+1):
                    break
                else:
                    print("Invalid choice, try again.")
        elif choice == '2':
            return 'block'
        elif choice == '3':
            return 'flee'

def monster_pick(behavior, m_health_points, max_health):
    health_percentage = m_health_points / max_health

    if behavior == 1:  # Aggressive behavior
        if health_percentage > 0.5:
            # Healthy - Weak Attack
            return random.choice(['Strike', 'Double Slash'])
        elif health_percentage > 0.25:
            # Wounded - Powerful Attacks
                return random.choice(['Power Strike', 'Desperate Lunge'])
        else:
            # Critical - Very Powerful Attacks
            return random.choice(['Death Blow', 'Last Stand'])

    elif behavior == 2:  #  behavior
        if health_percentage > 0.6:
            # Healthy - Powerful Attacks
            return random.choice(['Power Strike', 'Desperate Lunge', 'Death Blow'])
        elif health_percentage > 0.3:
            # Wounded - Weaker Attack
            return 'Double Slash'
        else:
            # Critical - Weak Attack
            return 'Strike'

def combat_turn(hero_hp, combat_strength, monster_hp, m_combat_strength):
    hero_attacks = hero_attack_assign() # Initializes heroes attacks
    print(f"You rolled these attacks: {hero_attacks}")
    hero_speed, monster_speed = speed_roll()
    monster_behavior = random.randint(1,2) # There are two monster behaviors, 1 is similar to a berserker that gets stronger as it gets lower on health. The other is the opposite and opens with strong attacks but weakens as its hp gets lower
    max_health = monster_hp # Takes however much health the monster has as the max health, but this max_health will not change. It is used as a reference point for monster behavior
    # Initialize hero and monster health
    m_health_points = monster_hp
    health_points = hero_hp

    while health_points > 0 and m_health_points > 0: # Battle happens as long as nobody is at 0 hp.
        attack = combat_pick(hero_attacks) # We use this instead of feeding the combat_pick() into the handle() function to catch if user blocks or flees which are not coded into the handler
        monster_attack = monster_pick(monster_behavior, m_health_points, max_health)
        if attack == 'flee': # Run away option, results in monster winning technically
            health_points *= 0.85
            print("You've fled the battle, not unscathed though")
            return 'Monster'
        else:
            damage = AttackHandler.handle(attack, combat_strength)
            monster_damage = AttackHandler.handle(monster_attack, m_combat_strength)
            blocking = False

        if hero_speed > monster_speed:
            if attack != 'block' and attack != 'Water Shield': # If hero goes first and didnt pick a defensive move, they do damage first
                m_health_points -= damage
                print(f"You've dealt {damage} damage! Monster has {max(0, m_health_points)} health left.")
                if m_health_points > 0: # If monster lived heroes attack, takes it's turn. The max(0) makes it so it doesnt print out negative health amounts, it just stops at 0 which is dead.
                    health_points -= monster_damage
                    print(f"Monster used: {monster_attack}\nMonster dealt {monster_damage} damage back to you! You have {max(0, health_points)} health left.")
                    if health_points < 1:
                        print("Monster has killed you!")
                        return 'Monster'
                else:
                    print("You've killed the monster!")
                    return 'Hero'
            elif attack == 'block':
                health_points -= (monster_damage * 0.5)
                print(f"You blocked! Monster dealt {monster_damage * 0.5} instead!")
                if health_points < 1:
                    print("Monster has killed you!")
                    return 'Monster'
            elif attack == 'Water Shield':
                health_points -= ((monster_damage * 0.5) + damage)
                print(f"You blocked! Monster dealt {(monster_damage * 0.5) + damage} instead!")
                if health_points < 1:
                    print("Monster has killed you!")

        elif hero_speed < monster_speed:
            if attack == 'block':
                health_points -= (monster_damage * 0.5)
                print(f"You blocked! Monster dealt {monster_damage * 0.5} instead!")
                if health_points < 1:
                    print("Monster has killed you!")
                    return 'Monster'
            elif attack == 'Water Shield':
                health_points -= ((monster_damage * 0.5) + damage)
                print(f"You blocked! Monster dealt {(monster_damage * 0.5) + damage} instead!")
                if health_points < 1:
                    print("Monster has killed you!")
                    return 'Monster'
            else:
                health_points -= monster_damage
                print(f"Monster dealt {monster_damage} damage! You have {max(0, health_points)} health left.")
                if health_points > 0:
                    m_health_points -= damage
                    print(f"You've dealt {damage} damage back! Monster has {max(0, m_health_points)} health left.")
                    if m_health_points < 1:
                        print("You've killed the monster!")
                        return 'Hero'
                else:
                    print("Monster has killed you!")
                    return 'Monster'