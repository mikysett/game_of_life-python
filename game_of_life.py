"""Conway's Game of Life,
Inspired by Al Sweigart book The Big Book of Small Python Projects,
Really helpful and appreciated.
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
View Al Sweigart code at https://nostarch.com/big-book-small-python-projects"""

import copy, random, sys, time

# Set up the constants:
DEFAULT_WIDTH = 80	# The width of the cell grid.
DEFAULT_HEIGHT = 20 # The height of the cell grid.

ALIVE = 'O'	# The character representing a living cell.
DEAD = ' '	# The character representing a dead cell.

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.

def run_game_of_life():
	cells, width, height = create_map()

	while True: # Main program loop.
		# Each iteration of this loop is a step of the simulation.
		print_board(cells, width, height)
		cells = calculate_next_step_cells(cells, width, height)
		try:
			time.sleep(1) # Add a 1 second pause to reduce flickering.
		except KeyboardInterrupt: # When Ctrl-C is pressed, end the program.
			print("Conway's Game of Life")
			sys.exit()

def create_map():
	cells = {}
	# Put random dead and alive cells into cells
	# if no map file is passed:
	if len(sys.argv) <= 1:
		width = DEFAULT_WIDTH
		height = DEFAULT_HEIGHT
		for x in range(width): # Loop over every possible column.
			for y in range(height): # Loop over every possible row.
				# 50/50 chance for starting cells being alive or dead.
				if random.randint(0, 1) == 0:
					cells[(x, y)] = ALIVE # Add a living cell.
				else:
					cells[(x, y)] = DEAD # Add a dead cell.
	# Take map and cell info from a file if passed as a parameter
	else:
		try:
			with open(sys.argv[1]) as map_file:
				map_lines = map_file.readlines()
				width = len(map_lines[0]) - 1
				height = 0
				for line in map_lines:
					for x in range(len(line)):
						if line[x] == ALIVE:
							cells[(x, height)] = ALIVE
						elif line[x] == DEAD:
							cells[(x, height)] = DEAD
					height += 1
		except FileNotFoundError:
			print("Map file not found!")
			sys.exit()
	return (cells, width, height)

def print_board(cells, width, height):
	print('\n' * 50) # Separate each step with newlines.
	# Print cells on the screen:
	print('-' * width + '|')
	for y in range(height):
		for x in range(width):
			print(cells[(x, y)], end='') # Print the # or space.
		print("|") # Print a newline at the end of the row.
	print('-' * width + '|')
	print('Press Ctrl-C to quit.')

def calculate_next_step_cells(prev_cells, width, height):
	cells = copy.deepcopy(prev_cells)
	# Calculate the next step's cells based on current step's cells:
	for x in range(width):
		for y in range(height):
			# Get the neighboring coordinates of (x, y), even if they
			# wrap around the edge:
			left = (x - 1) % width
			right = (x + 1) % width
			above = (y - 1) % height
			below = (y + 1) % height
			# Count the number of living neighbors:
			numNeighbors = 0
			if prev_cells[(left, above)] == ALIVE:
				numNeighbors += 1 # Top-left neighbor is alive.
			if prev_cells[(x, above)] == ALIVE:
				numNeighbors += 1 # Top neighbor is alive.
			if prev_cells[(right, above)] == ALIVE:
				numNeighbors += 1 # Top-right neighbor is alive.
			if prev_cells[(left, y)] == ALIVE:
				numNeighbors += 1 # Left neighbor is alive.
			if prev_cells[(right, y)] == ALIVE:
				numNeighbors += 1 # Right neighbor is alive.
			if prev_cells[(left, below)] == ALIVE:
				numNeighbors += 1 # Bottom-left neighbor is alive.
			if prev_cells[(x, below)] == ALIVE:
				numNeighbors += 1 # Bottom neighbor is alive.
			if prev_cells[(right, below)] == ALIVE:
				numNeighbors += 1 # Bottom-right neighbor is alive.

			# Set cell based on Conway's Game of Life rules:
			# Living cells with 2 or 3 neighbors stay alive:
			if prev_cells[(x, y)] == ALIVE and (numNeighbors == 2
												or numNeighbors == 3):
				cells[(x, y)] = ALIVE
			# Dead cells with 3 neighbors become alive:
			elif prev_cells[(x, y)] == DEAD and numNeighbors == 3:
				cells[(x, y)] = ALIVE
			# Everything else dies or stays dead:
			else:
				cells[(x, y)] = DEAD
	return cells

run_game_of_life()
