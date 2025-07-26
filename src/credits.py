import choose_character

def roll_credits(player):
	print("\nThis has been a Hackathonic Games Production")
	print("for the Boot.dev 2025 Hackathon")
	print("\nCobbled together by CaveGuyJ")
	print("Copyright 2025")
	print("If you feel the need to steal this game, I pity you.")
	print("\nCaveGuyJ would like to thank Lane, Boots, and the whole boot.dev team! xoxo")
	print(f"\nThank you for playing, {player.name} the {player.character_class.name}!")

if __name__ == "__main__":
	roll_credits()