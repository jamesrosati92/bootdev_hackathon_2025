from actions import Attack
import weapons

class Enemy:
	def __init__(self, name, adjective, weapon, HP, accuracy):
		self.name = name
		self.adjective = adjective
		self.HP = HP
		self.accuracy = accuracy
		self.weapon = weapon



	def take_damage(self, damage, dam_type=None):
		self.HP -= damage
		if self.HP <= 0:
			print(f"You killed the {self.name}!")
		else:
			print(f"{self.name.capitalize()} is still alive with {self.HP} HP.")
		