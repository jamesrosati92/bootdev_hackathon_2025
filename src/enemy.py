from actions import Attack
from weapons import available_weapons, additional_weapons

import random

class Enemy:
	def __init__(self, name, adjective, weapon, HP, accuracy, armor, immune, resist, weak):
		self.name = name
		self.adjective = adjective
		self.weapon = weapon
		self.HP = HP
		self.accuracy = accuracy
		self.armor = armor
		self.immune = immune
		self.resist = resist
		self.weak = weak



	def take_damage(self, damage, dam_type):
		if dam_type in self.immune:
			damage = 0
			print(f"The {self.name} is immune to {dam_type.name}!")
		elif dam_type in self.resist:
			damage //= 2
			print(f"The {self.name} resists {dam_type} damage!")
		elif dam_type in self.weak:
			damage * 2
		else:
			damage -= self.armor
		self.HP -= damage
		print(f"The {self.name} takes {damage} damage!")
		if self.HP <= 0:
			print(f"You kill the {self.name}!")
		else:
			print(f"{self.name.capitalize()} is still alive with {self.HP} HP.")

easy_weapon = random.choice(available_weapons)
hard_weapon = random.choice(additional_weapons)

easy_enemies = [
	Enemy("scout robot", "A wandering", easy_weapon, 4, 4, 2, ["poison"], [], ["energy"]),
	Enemy("thug", "A viscious-looking", easy_weapon, 5, 5, 0, [], [], []),
	Enemy("blue mutant", "A heavyset", easy_weapon, 8, 6, 0, [], ["energy"], ["poison"]),
	Enemy("cyber guard", "A sleek", easy_weapon, 5, 5, 1, [], ["poison"], ["energy"]) 
]

hard_enemies = [
	Enemy("warbot", "A rumbling", hard_weapon, 8, 6, 4, ["poison"], [], ["energy"]),
	Enemy("trooper", "An angry", hard_weapon, 10, 7, 1, [], [], []),
	Enemy("green mutant", "A gigantic", hard_weapon, 15, 7, 1, [], ["energy"], ["poison"]),
	Enemy("cyber soldier", "A gleaming", hard_weapon, 10, 7, 2, [], ["poison"], ["energy"]),
]

all_enemies = easy_enemies + hard_enemies

		