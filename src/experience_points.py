def award_experience(player, level):
	XP_reward = level
	print(f"You gain {XP_reward} experience points!")

	all_stats = list(player.character_profile.keys()) #Convert the character profile to a list of keys.
	improvable_stats = all_stats[3:-4] 	#Make a list without name, description, class, armor, immune, resist, weak.


	while XP_reward > 0:
		print("Which stat would you like to improve?")
		for index, stat in enumerate(improvable_stats, 1):
			print(f"{index}. {stat}")
		choice = input("Choose a stat.\n")
		if choice.isdigit() and 1 <= int(choice) <= len(improvable_stats):
			selected_stat = improvable_stats[int(choice) - 1]
		else:
			print("Invalid choice. Please enter a number form the list.")
			
		if selected_stat == "HP":
			player.character_class.max_HP += 5
			player.character_class.current_HP += 5
		else:
			player.character_profile[selected_stat] += 1
		print(f"You have raised your {selected_stat}!")
		XP_reward -= 1

	return player.character_profile