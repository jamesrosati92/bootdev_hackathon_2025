import random

class Action:
	def __init__(self, name, AP_cost):
		self.name = name
		self.AP_cost = AP_cost
	
	def do_action(self):
		pass


class Attack(Action):
	def __init__(self, name, accuracy): #"name" is the string that will show when the player can choose an action.
		super().__init__(name, AP_cost=1)
		self.name = "attack"
		self.accuracy = accuracy

	def attack_roll(self, accuracy):
		roll = random.randint(1, 10)
		if roll <= accuracy:
			print("Hit!")
			return True
		else:
			print("Miss!")
			return False

class UseItem(Action):
	def __init__(self, name, AP_cost, available_items):
		super().__init__(name, AP_cost=1)
		self.available_items = inventory