class Weapon:
	def __init__(self, name, damage, attack_stat, dam_type, description):
		self.name = name
		self.damage = damage
		self.attack_stat = attack_stat
		self.dam_type = dam_type
		self.description = description

	def __str__(self):
		return f"{self.name.capitalize()} (Damage: {self.damage}) - {self.description}"

available_weapons = [
	Weapon("handgun", 4, "SPD", "normal", "9mm clip pistol"),
	Weapon("laser pistol", 3, "SPD", "energy", "A futuristic pistol that fires bolts of energy."),
	Weapon("machete", 4, "STR", "normal", "A sharp blade, great for slashing and slicing."),
	Weapon("laser hatchet", 3, "STR", "energy", "A one-handed axe with an energy blade."),
]


if __name__ == "__main__":
	for weapon in available_weapons:
		print(weapon)