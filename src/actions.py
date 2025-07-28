import random

class Action:
	def __init__(self, name):
		self.name = name
	
	def do_action(self):
		pass


class Attack(Action):
	def __init__(self, name, accuracy): #"name" is the string that will show in the "choose action" prompt.
		super().__init__(name)
		self.name = "attack"
		self.accuracy = accuracy

	def attack_roll(self, accuracy):
		roll = random.randint(1, 10)
		if roll <= accuracy:
			return True
		else:
			return False

class UseItem(Action):
	def __init__(self, name, inventory):
		super().__init__(name)
		self.available_items = inventory

	def use_item(item, inventory):
		item.item_effect()
		inventory.remove(item)
		return


class TalkItOut(Action):
	def __init__(self, name, intelligence):
		super().__init__(name)
		self.name = "talk it out"
		self.intelligence = intelligence

	def talk_roll(self, intelligence, level):
		roll = random.randint(1, 10)
		success_chance = intelligence - level
		if roll <= success_chance:
			print(f"Success!")
			return True
		else:
			print("Failure!")
			return False
		