from weapons import Weapon
import random

mecha_stoob_weapons = [
	Weapon("hacker smacker", "A hydraulic data hammer.", 10, "strength", "normal")
	Weapon("coder cracker", "Looks like a humungous death-ray cannon.", 10, "speed", "energy")
	Weapon("focus f***er", "His jaws are dripping with mind-numbing poison.", 10, "strength", "poison")
]



stoob_weapon = random.choice(mecha_stood_weapons)



mecha_stoob = Enemy("Mecha Stoob", "The one and only", stoob_weapon, 100, 8, 5, [], [], []) #This is the end-game boss. He's really mean!
							#He'll have high armor
							#Instead of attacking directly himself, he will use the Hacker Smacker
							#and the Coder Cracker; these have their own HP and armor. The player
							#can target these instead of Mecha Stoob and reduce his offensive powers


