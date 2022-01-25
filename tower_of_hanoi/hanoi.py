def move_disk(from_pole, to_pole):
	print("Moving disk from pole {0} to pole {1}".format(from_pole, to_pole))
	

def solve_tower(height, from_pole, to_pole, helper_pole):
	if height >= 1:
		solve_tower(height-1, from_pole, helper_pole, to_pole)
		move_disk(from_pole, to_pole)
		solve_tower(height-1, helper_pole, to_pole, from_pole)
		
		
solve_tower(3, "A", "B", "C")
