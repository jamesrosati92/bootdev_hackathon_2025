class Human:
	description = "Well-rounded, with higher luck than any other class. No immunities, weaknesses or resistances."
	STR = 6
	SPD = 6
	INT = 6
	LCK = 6
	HP = 20
	PP = 4
	Armor = 0
	immune = []
	resist = []
	weak = []

class Robot:
	description = "Armored, immune to poison and quite strong. Weak to energy and with only moderate intelligence and very low luck."
	STR = 7
	SPD = 6
	INT = 5
	LCK = 1
	HP = 25
	PP = 1
	Armor = 2
	immune = [poison]
	resist = []
	weak = []

class Mutant:
	description = "High HP and strength. Moderate speed and luck. Resists energy damage, but weak to poison."
	STR = 8
	SPD = 4
	INT = 6
	LCK = 4
	HP = 30
	PP = 3
	Armor = 0
	immune = []
	resist = [energy]
	weak = [poison]	

class Cyborg:
	description = "High speed and intelligence. Resistant to poison. Light natural armor."
	STR = 5
	SPD = 7
	INT = 7
	LCK = 2
	HP = 20
	PP = 2
	Armor = 1
	immune = []
	resist = [poison]
	weak = []