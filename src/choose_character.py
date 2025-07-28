from weapons import available_weapons #The player character always starts with a weapon.

class CharacterClass:				#The classes are human, robot, mutant and cyborg.
	def __init__(
		self, name, description, strength, speed, intelligence, luck, max_HP, armor, immune, resist, weak
		):
		#Accuracy is currently generic across all weapon types.
		self.name = name
		self.description = description
		self.strength = strength
		self.speed = speed
		self.intelligence = intelligence
		self.luck = luck
		self.max_HP = max_HP				#HP cap for healing
		self.current_HP = max_HP			#Takes damage
		self.armor = armor #Each point of armor reduces damage from dam_type "normal" by 1.
		self.immune = immune
		self.resist = resist
		self.weak = weak
		

	def __str__(self):
		return f"{self.name.capitalize()}: {self.description}"

class PlayerCharacter:
	def __init__(self, name, character_class, inventory):
		self.name = name
		self.character_class = character_class
		self.inventory = inventory #The inventory starts with the player's chosen weapon.
		self.character_profile = {
			"Name": self.name,
			"Class": self.character_class,
			"Description": self.character_class.description,
			"Strength": self.character_class.strength,
			"Speed": self.character_class.speed,
			"Intelligence": self.character_class.intelligence,
			"Luck": self.character_class.luck,
			"HP": f"{self.character_class.current_HP}/{self.character_class.max_HP}",
			"Armor": self.character_class.armor,
			"Immunities": self.character_class.immune,
			"Resistances": self.character_class.resist,
			"Weaknesses": self.character_class.weak,
		}
	
	def __str__(self):
		return f"You are {self.name}, the {self.character_class.name}."

	def take_damage(self, damage, dam_type):
		if dam_type in self.character_class.immune:
			damage = 0
			print(f"You are immune to {dam_type} damage and are not hurt by the attack!")
		elif dam_type in self.character_class.resist:
			damage //= 2

		elif dam_type in self.character_class.weak:
			damage *= 2
		else:
			damage -= self.character_class.armor
			if self.character_class.armor > 0:
				print("Your armor protects you from some of the damage!")
		self.character_class.current_HP -= damage
		print(f"You take {damage} damage!")


available_classes = [
	CharacterClass(
		"human", "Well-rounded and lucky", 6, 6, 6, 6, 20, 0, [], [], []
	),
	CharacterClass(
		"robot", "Armored and immune to poison", 7, 6, 4, 1, 25, 2, ["poison"], [], ["energy"]
	),
	CharacterClass(
		"mutant", "Hardy and strong, resists energy damage but weak to poison.", 8, 4, 5, 3, 30, 0, [], ["energy"], ["poison"]
	),
	CharacterClass(
		"cyborg", "Fast and intelligent, with light armor and resistance to poison", 5, 7, 7, 2, 20, 1, [], ["poison"], []
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
		inventory = [choose_weapon()]
		player = PlayerCharacter(name, character_class, inventory)
		print(player)
		return player

if __name__ == "__main__":
	create_character()