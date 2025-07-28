class Item:
	def __init__(self, name):
		self.name = name

	def pick_up_item(self):
		return player.inventory.append(self)

	def item_effect(self, name):
		pass



class BodyArmor(Item):
	def __init__(self, name, armor_bonus):
		super().__init__(name)
		self.armor_bonus = armor_bonus


armor_loot = [BodyArmor("helmet", 1),
	BodyArmor("chest plate", 2),
	BodyArmor("leg armor", 1),
	BodyArmor("bracers", 1)
]



class Medicine(Item):
	def __init__(self, name, healing):
		super().__init__(name)
		self.healing = healing

	def heal(self, player):
		if player.character_class.current_HP == player.character_class.max_HP:
			print("You are already at full health.")
		else:
			player.character_class.current_HP += self.healing
			if player.character_class.current_HP > player.character_class.max_HP:
				player.character_class.current_HP = player.character_class.max_HP
			print("You restore some HP.")
		return player.character_class.current_HP
			

medicine_loot = [Medicine("pain killers", 5),
	Medicine("bandages", 10),
	Medicine("first aid kit", 20),
]



class Grenade(Item):
	def __init__(self, name, damage, dam_type):
		super().__init__(name)
		self.damage = damage
		self.dam_type = dam_type

	def explode(self, enemies):
		for enemy in enemies:
			enemy.take_damage(self.damage, self.dam_type)


grenade_loot = [Grenade("frag grenade", 4, "normal"),
	Grenade("plasma detonator", 4, "energy"),
	Grenade("acid bomb", 4, "poison"),
]
		