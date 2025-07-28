class Weapon:
	def __init__(self, name, description, damage, attack_stat, dam_type):
		self.name = name
		self.damage = damage
		self.attack_stat = attack_stat
		self.dam_type = dam_type
		self.description = description

	def __str__(self):
		return f"{self.name.capitalize()} (Damage: {self.damage}) - {self.description}"

available_weapons = [
	Weapon("handgun", "9mm clip pistol.", 4, "speed", "normal"),
	Weapon("laser pistol", "A futuristic pistol that fires bolts of energy.", 4, "speed", "energy",),
	Weapon("machete", "A sharp blade, great for slashing and slicing.", 4, "strength", "normal",),
	Weapon("laser hatchet", "A one-handed axe with an energy blade.", 4, "strength", "energy"),
	Weapon("toxic spike", "Long, sharp and venemous!", 4, "strength", "poison"),
	Weapon("gas gun", "A pistol that launches a gas canister.", 4, "speed", "poison"),
]


additional_weapons = [
	Weapon("assault rifle", "Semi-auto rifle with a stacked magazine.", 6, "speed", "normal"),
	Weapon("laser rifle", "High-tech rifle that fires a powerful beam.", 6, "speed", "energy"),
	Weapon("fire axe", "A two-handed axe for chopping through any obstacle.", 6, "strength", "normal"),
	Weapon("plasma sword", "No, it's not a lightsaber!", 6, "strength", "energy"),
	Weapon("snakebite", "Gauntlets with poisoned spikes on the knuckles.", 6, "strength", "poison"),
	Weapon("fume-o-tron", "Basically a hand-held water cannon that sprays poison.", 6, "speed", "poison"),
]


weapon_loot = available_weapons + additional_weapons

#at levels 1 and 2, only weaker weapons are available
#better weapons are available from level 3 onwards

def get_weapon_accuracy(player, weapon):
	return getattr(player, weapon.attack_stat)



if __name__ == "__main__":
	for weapon in available_weapons:
		print(weapon)