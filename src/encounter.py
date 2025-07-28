import random
from enemy import Enemy, easy_enemies
from actions import Attack, TalkItOut, UseItem
from weapons import Weapon
from items import Item, BodyArmor, Medicine, Grenade, armor_loot, medicine_loot, grenade_loot


#Spawn enemies
def choose_enemies(level):
	num_enemies = level + 1
	enemies = []
	while num_enemies > 0:
		if level < 3:
			enemies.append(random.choice(easy_enemies)) #Add a random enemy to the encounter.
		elif 3 <= level < 8:
			enemies.append(random.choice(all_enemies)) #Could be hard, could be easy!
		elif 8 <= level < 10:
			enemies.append(random.choice(hard_enemies)) #Good luck, loser!
		num_enemies -= 1
	return enemies


#Choose player actions
def choose_action(player):
	attack_action = Attack("attack", player)
	talk_it_out = TalkItOut("talk it out", player.character_class.intelligence)
	use_item = UseItem("use item", player.inventory)

	available_actions = [
		attack_action, #D10 roll, <= accuracy
		talk_it_out,   #d10 roll <= (inteliigence - level)
		use_item,
	]
	
	print("\nWhat will you do?")
	for index, action in enumerate(available_actions, 1):
		print(f"{index}. {action.name.capitalize()}")

	while True:
		choice = input("Enter the number of the action you'd like to take.\n") #Number list to select an action.
		if choice.isdigit() and 1 <= int(choice) <= len(available_actions):
			selected_action = available_actions[int(choice) - 1]
			
		else:
			print("Invalid choice. Please choose a number from the list.")
		return selected_action




#Choose target
def choose_target(enemy_group):
	print(f"Which enemy will you target?")
	for index, target in enumerate(enemy_group, 1):
		print(f"{index}. {target.name}")
	while True:
		choice = input("Choose your target.\n")
		if choice.isdigit() and 1 <= int(choice) <= len(enemy_group):
			selected_target = enemy_group[int(choice) - 1]
			return selected_target
		else:
			print("Invalid choice. Please choose a number from the list.")
		



#Choose weapon
def choose_weapon(inventory):
	from weapons import Weapon

	carried_weapons = []
	for item in inventory:
		if isinstance(item, Weapon):
			carried_weapons.append(item)
	if not carried_weapons:
		print("You have no weapons!")
		return None
	print("Choose a weapon:")
	for index, weapon in enumerate(carried_weapons, 1):
		print(f"{index}. {weapon.name.capitalize()}")
	while True:
		choice = input("Enter the number of your weapon:\n")
		if choice.isdigit() and 1 <= int(choice) <= len(carried_weapons):
			return carried_weapons[int(choice) - 1]
		else:
			print("Invalid choice. Please enter a number form the list.")

#Choose item
def choose_item(inventory):
	usable_items = []
	print("Choose an item to use:")
	for item in inventory: 					#Item means item in inventory
		if isinstance(item, Item) and not isinstance(item, BodyArmor):
			usable_items.append(item)
	if not usable_items:
		print("You have no usable items!")
	for index, item in enumerate(usable_items, 1):		#Item means usable item
		print(f"{index}. {item.name}")
	while True:
		choice = input ("Enter the number of the item you wnat to use:\n")
		if choice.isdigit() and 1 <= int(choice) <= len(usable_items):
			return usable_items[int(choice) - 1]
		else:
			print("Invalid choice. Please enter a number form the list.")


#Combat
def run_combat(player, enemies, level):
	round_count = 1

	for enemy in enemies:
		print(f"\n{enemy.adjective} {enemy.name} appears!")
	input("Press Enter to continue....")
	
	while len(enemies) > 0 and player.character_class.current_HP > 0:
		print(f"\nRound {round_count}")

		#Player's turn
		print("\nYour turn")
		player_action = choose_action(player)					#Choose action
		if not player_action.name == "use item":
			player_target = choose_target(enemies)					#Choose target
		print(f"\nYou choose to {player_action.name}")
		if not player_action.name == "use item":
			print(f"and your target is: {player_target.name}.")

		if player_action.name == "attack":
			weapon = choose_weapon(player.inventory)			#Choose weapon
			if weapon == None:						#This came up in debugging
				print("You cannot attack!")
			else:
				accuracy = getattr(player.character_class, weapon.attack_stat)		#Get accuracy
				print(f"\nYou attack the {player_target.name} with your {weapon.name}!")
				if player_action.attack_roll(accuracy):
					print("You hit!")
					player_target.take_damage(weapon.damage, weapon.dam_type)
				else:
					print("You miss!")

		elif player_action.name == "talk it out":
			print(f"\nYou attempt to win over {player_target.name} with your words.")
			if player_action.talk_roll(player.character_class.intelligence, level):
				print("You persuade your enemy to choose peace!")
				print(f"The {player_target.name} lays down their weapons.")
				enemies.remove(player_target)
			else:
				print(f"The {player_target.name} is unconvinced!")

		elif player_action.name == "use item":
			used_item = choose_item(player.inventory)
			if isinstance(used_item, Medicine):
				used_item.heal(player)
			elif isinstance(used_item, Grenade):
				used_item.explode(enemies)

		for enemy in enemies:
			if enemy.HP <= 0:
				enemies.remove(enemy)
		if len(enemies) <= 0:
			print("Level cleared!")
			break

		input ("Press Enter to continue....")

		#Enemies' turn
		print("\nEnemy turn")
		for enemy in enemies:
			enemy_action = Attack("attack", enemy.weapon)
			print(f"\nThe {enemy.name} attacks you with its {enemy.weapon.name}!")
			if enemy_action.attack_roll(enemy.accuracy):
				player.take_damage(enemy.weapon.damage, enemy.weapon.dam_type)
			else:
				print(f"The {enemy.name} misses!")
			if player.character_class.current_HP <= 0:
				print("You have died!")
				print("Game over!")
				break
		print(f"You have {player.character_class.current_HP} HP.")
		input ("Press Enter to continue....")

		

		round_count += 1



						
		
		
		

#Each level will have a set number of enemies.
#The selection of enemies will be random, chosen from a list of Enemy instances.
#enemies will be the list of selected enemies