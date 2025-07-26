from weapons import available_weapons #The player character always starts with a weapon.

class CharacterClass:				#The classes are human, robot, mutant and cyborg.
	def __init__(
		self, name, description, accuracy, strength, speed, intelligence, luck, HP, SP, armor #SP = special points
		):
							#Accuracy is currently generic across all weapon types.
		self.name = name
		self.description = description
		self.accuracy = accuracy
		self.strength = strength
		self.speed = speed
		self.intelligence = intelligence
		self.luck = luck
		self.HP = HP
		self.SP = SP
		self.armor = armor
		

	def __str__(self):
		return f"{self.name.capitalize()}: {self.description}"

class PlayerCharacter:
	def __init__(self, name, character_class, weapon):
		self.name = name
		self.character_class = character_class
		self.inventory = [weapon] #The inventory starts with the player's chosen weapon.
	
	def __str__(self):
		return f"You are {self.name}, the {self.character_class.name}."

	def take_damage(self, damage, dam_type=None):
		if dam_type in self.character_class.immune:
			damage = 0
			print(f"You are immune to {dam_type} damage and are not hurt by the attack!")
		elif dam_type in self.character_class.resist:
			damage //= 2
			self.HP -= damage
		elif dam_type in self.character_class.weak:
			damage *= 2
			self.HP - damage
		else:
			self.HP -= damage
		print(f"You take {damage} damage!")


available_classes = [
	CharacterClass(
		"human", "Well-rounded and lucky", accuracy=6, strength=6, speed=6, intelligence=6, luck=6, HP=20, SP=3, armor=0
	),
	CharacterClass("robot", "Armored and immune to poison", accuracy=5, strength=7, speed=6, intelligence=4, luck=1, HP=25, SP=1, armor=2
	),
	CharacterClass("mutant", "Hardy and strong", accuracy=6, strength=8, speed=4, intelligence=5, luck=3, HP=30, SP=2, armor=0
	),
	CharacterClass("cyborg", "Fast and intelligent, with light armor and resistance to poison", accuracy=7, strength=5, speed=7, intelligence=7, luck=2, HP=20, SP=4, armor=1
	),
]



def choose_class():
	print("Choose your class:")
	for index, char_class in enumerate(available_classes, 1):
		print(f"{index}. {char_class}")
	while True:
		choice = input("\n Enter the number of your preferred class.\n")
		if choice.isdigit() and 1 <= int(choice) <= len(available_classes):
			selected_class = available_classes[int(choice) - 1] #Gets the character class from available_classes.
			print(f"You chose: {selected_class.name.capitalize()}") #.name is one property of selected_class
			return selected_class
		else:
			print("Invalid choice. Please enter a number from the list.")


def choose_weapon():
	print("Choose your weapon.")
	for index, weapon in enumerate(available_weapons, 1):
		print(f"{index}. {weapon}")
	while True:
		choice = input("\n Enter the number of your preferred weapon.\n")
		if choice.isdigit() and 1 <= int(choice) <= len(available_weapons):
			selected_weapon = available_weapons[int(choice) - 1]
			print(f"You chose: {selected_weapon.name.capitalize()}")
			return selected_weapon
		else:
			print("Invalid choice. Please enter a number from the list.")


def create_character():
	name = input("Enter your character's name: ")
	if len(name) > 20:
		raise Exception("Name must be 20 letters or less.")
	else:
		character_class = choose_class()
		weapon = choose_weapon()
		player = PlayerCharacter(name, character_class, weapon)
		print(player)
		return player

if __name__ == "__main__":
	create_character()