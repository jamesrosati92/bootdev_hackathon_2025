mecha_stoob = Enemy("one and only Mecha Stoob", 100) #This is the end-game boss. He's really mean!
							#He'll have high armor
							#Instead of attacking directly himself, he will use the Hacker Smacker
							#and the Coder Cracker; these have their own HP and armor. The player
							#can target these instead of Mecha Stoob and reduce his offensive powers

hacker_smacker = Enemy("Hacker Smacker", 20)
	if mecha-stoob.HP <= 0:
		self.HP = 0

coder_cracker = Enemy("Coder Cracker", 20)
	if mecha-stoob.HP <= 0:
		self.HP = 0

#Mecha Stoob will have a different taunt during each of the first five rounds.
#Add a round counter to main.py