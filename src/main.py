from choose_character import create_character
from enemy import Enemy
from weapons import available_weapons
from actions import Attack
from credits import roll_credits


#Debugging

DEBUG = True  # Set to False for normal play

if DEBUG:
	# Create a default player and weapon for testing
	from choose_character import CharacterClass, PlayerCharacter
	from weapons import available_weapons

	test_class = CharacterClass(
		"robot", "Test robot", accuracy=5, strength=5, speed=5, intelligence=5, luck=5, HP=20, SP=1, armor=2
	)
	test_weapon = available_weapons[0]
	player = PlayerCharacter("TestPlayer", test_class, test_weapon)
else:
	player = create_character()

#Choose actions
def choose_action(weapon, accuracy): #For now, there's only "attack"
	attack_action = Attack("attack", accuracy)
	#Instantiate attack_action as an object.

	available_actions = [
		attack_action, 
		#Attack will use a d10 roll. The attack hits if the roll <= the stat. STR for melee, SPD for ranged
	]
	#I'll add more actions with more functionality later.
	#Other actions will be things like "use item", "defend", "inspect", "swap weapon", "special ability"
	
	print("\nWhat will you do?")
	for index, action in enumerate(available_actions, 1):
		print(f"{index}. {action.name.capitalize()}")

	while True:
		choice = input("Enter the number of the action you'd like to take.\n") #This shows the prompt to the user and accepts their input.
		if choice.isdigit() and 1 <= int(choice) <= len(available_actions):
			selected_action = available_actions[int(choice) - 1]
			print(f"You {selected_action.name}")
			return selected_action
		else:
			print("Invalid choice. Please choose a number from the list.")

def main():
#Step 1: character creation and stats
	
	if DEBUG == False:
		player = create_character()
		weapon = player.inventory[0] #Player's chosen weapon.
		inventory = player.inventory
		accuracy = player.character_class.accuracy
		#DEBUG skips character creation

	enemy_weapon = available_weapons[1]
	enemy = Enemy("mook", "fearsome", enemy_weapon, HP=5, accuracy=5) #I'll build proper enemies in their own encounter modules.

	
#Step 2: The enemy appears.
	print(f"\nA {enemy.adjective} {enemy.name} appears!")

#Step 3: combat turns	
	while enemy.HP > 0:
		action = choose_action(Attack, accuracy)
		action.attack_roll(accuracy) 
		#A matching function name across all actions might help. "execute_action" maybe.
		
		print(f"You attack the {enemy.name} with your {weapon.name} and deal {weapon.damage} damage!")

		enemy.take_damage(weapon.damage)
		enemy_action = choose_action(Attack, enemy.accuracy)
		action.attack_roll(action) #Enemy takes a turn after the player.
		print(f"The {enemy.name} attacks you with its {enemy_weapon.name} for {enemy_weapon.damage} damage!")

	#if player.HP <= 0:
		#print("You have died.")
		#print("Game over!")
		#exit()

#Step 4: credits
	roll_credits(player)
		


if __name__ == "__main__":
	main()