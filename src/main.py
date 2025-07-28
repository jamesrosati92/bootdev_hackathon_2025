from choose_character import create_character
from enemy import Enemy
from enemy import easy_enemies
from weapons import available_weapons, additional_weapons, weapon_loot, get_weapon_accuracy
from actions import Attack
from credits import roll_credits
from encounter import choose_enemies
from encounter import run_combat
from items import BodyArmor, Medicine, Grenade, armor_loot, medicine_loot, grenade_loot
from experience_points import award_experience

import random


#Debugging

DEBUG = False  #Set to False for normal play

if DEBUG:
	# Create a default player and weapon for testing
	from choose_character import CharacterClass, PlayerCharacter
	from weapons import available_weapons

	test_class = CharacterClass(
		"mutant", "Test mutant", 8, 8, 8, 5, 20, 1, [], ["energy"], []
	)
	inventory =[available_weapons[0], available_weapons[2], available_weapons[4], medicine_loot[0], grenade_loot[0]]
	player = PlayerCharacter("TestPlayer", test_class, inventory)

else:
	player = create_character()

def main():

#Step 1: Spawn level
	player_base_armor = player.character_class.armor
	level = 1
	while player.character_class.current_HP > 0:

#Step 2: spawn level
		
		enemies = choose_enemies(level)
		print(f"\nLevel {level}")

#Step 3: combat turns
		run_combat(player, enemies, level)
		input("Press Enter to continue....")

#Step 4: Level rewards
		loot = []
		if level == 1:
			loot = [medicine_loot[0],
				medicine_loot[0],
				random.choice(available_weapons)
			]
			
		else:
			loot = [random.choice(medicine_loot),
			random.choice(medicine_loot),
			random.choice(armor_loot),
			random.choice(grenade_loot),
			random.choice(weapon_loot),
			]
		print("Searching for loot, you found:")
		for item in loot:		#Here, item means loot item.
			print(f"{item.name}\n")
		player.inventory += loot
		player.character_class.armor = player_base_armor
		unique_armor_names = set()
		for item in player.inventory:	#Here, item means inventory item.
			if isinstance(item, BodyArmor) and item.name not in unique_armor_names:
				player.character_class.armor += item.armor_bonus
				unique_armor_names.add(item.name)

		input("Press Enter to continue....")

		for stat in player.character_profile:
			print(stat)
		award_experience(player, level)

		level += 1
		input("Press Enter to continue....")

#The Boss
	if level == 10:
		from enemy_mechastoob import mecha_stoob_weapons, stoob_weapon, mecha_stoob
		print("The ground shudders and shakes from mighty footfalls.")
		input("Press Enter to continue....")
		print("Before you, standing as tall as something much bigger than you expected,")
		input("Press Enter to continue....")
		print("It's the terrifying, horrifying, stupefying:")
		input("Press Enter to continue....")
		print("Mecha Stoob!!")
		print("The evil step-cousin of the regular second cousin of boot.dev's very own Boots!")
		input("Press Enter to continue...")
		print("The cyber bear is out for your blood! Good luck to you....")
		run_combat(player, mecha_stoob, level=10)
		print("Congratulations! You have defeated the One and Only Mecha Stoob!")
		print("You win!")
		input("Press Enter to continue....")

#Credits
	roll_credits(player)
		


if __name__ == "__main__":
	main()