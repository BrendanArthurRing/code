# Define Fighter Selection
fighters = [
["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

# Define Initial Position of Selector
initial_position = (0,0)

# Define the Moves
moves = ['up', 'left', 'right', 'left', 'left']

# 
def street_fighter_selection(fighters, initial_position, moves):
	solution = []
	def rotate(l, n):
		return l[-n:] + l[:-n]
	x = initial_position[0]
	y = initial_position[1]
	up = 'up' ; down = 'down' ; left = 'left' ; right = 'right'
	for direction in moves:
		# Move selector up.
		if direction is up:
			x = 0
			# Append to solution list.
			solution.append(fighters[x][y])
		# Move selector down.
		elif direction is down:
			x = 1
			# Append to solution list.
			solution.append(fighters[x][y])
		# Rotate selector left
		elif direction is left:
			# Rotate top in left direction.
			top = rotate(fighters[0], 1)
			# Rotate bottom in left direction.
			bottom = rotate(fighters[1], 1)
			# Save rotation changes to fighters.
			fighters = [top, bottom]
			# Append to solution list.
			solution.append(fighters[x][y])
		elif direction is right:
			# Rotate top in right direction.
			top = rotate(fighters[0], -1)
			# Rotate bottom in left direction.
			bottom = rotate(fighters[1], -1)
			# Save rotation changes to fighters list.
			fighters = [top, bottom]
			# Append to solution list.
			solution.append(fighters[x][y])
	print(solution)
	return solution

street_fighter_selection(fighters, initial_position, moves)


# Visualization
'''
["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]

Starting Position
fighters[0][0]

Right
fighters[0][1]

Down
fighters[1][1]


Down
if fighters[x] == 0:
	x = 1
else:
	x = 1

Up
if fighters[x] == 0:
	x = 0
else:
	x = 0



'''


'''
fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up","down","right","left"]

test.describe("Character selection")
test.it("should work with no selection cursor moves")
moves =  []
solution = []
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should go left 8 times")
moves =  ["left"]*8
solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should go right 8 times")
moves =  ["right"]*8
solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should go up 4 times, always the same")
moves =  ["up"]*4
solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should go down 4 times, always the same")
moves =  ["down"]*4
solution = ['Ken', 'Ken', 'Ken', 'Ken']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should use all 4 directions counter-clockwise twice")
moves =  ["down","right","up","left"]*2
solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should use all 4 directions clockwise twice")
moves =  ["up","left","down","right"]*2
solution = ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

test.it("should cover all characters")
moves =  ["up"]+["left"]*6+["down"]+["right"]*6
solution = ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Ken']
test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
'''




# Instructions
'''
Short Intro

Some of you might remember spending afternoons playing Street Fighter 2 in some Arcade back in the 90s or emulating it nowadays with the numerous emulators for retro consoles.

Can you solve this kata? Suuure-You-Can!

UPDATE: a new kata's harder version is available here.

The Kata

You'll have to simulate the video game's character selection screen behaviour, more specifically the selection grid. Such screen looks like this:

alt text

Selection Grid Layout in text:

| Ryu  | E.Honda | Blanka  | Guile   | Balrog | Vega    |
| Ken  | Chun Li | Zangief | Dhalsim | Sagat  | M.Bison |

Input

    the list of game characters in a 2x6 grid;
    the initial position of the selection cursor (top-left is (0,0));
    a list of moves of the selection cursor (which are up, down, left, right);

Output

    the list of characters who have been hovered by the selection cursor after all the moves (ordered and with repetition, all the ones after a move, wether successful or not, see tests);

Rules

Selection cursor is circular horizontally but not vertically!

As you might remember from the game, the selection cursor rotates horizontally but not vertically; that means that if I'm in the leftmost and I try to go left again I'll get to the rightmost (examples: from Ryu to Vega, from Ken to M.Bison) and vice versa from rightmost to leftmost.

Instead, if I try to go further up from the upmost or further down from the downmost, I'll just stay where I am located (examples: you can't go lower than lowest row: Ken, Chun Li, Zangief, Dhalsim, Sagat and M.Bison in the above image; you can't go upper than highest row: Ryu, E.Honda, Blanka, Guile, Balrog and Vega in the above image).

Test

For this easy version the fighters grid layout and the initial position will always be the same in all tests, only the list of moves change.

Notice : changing some of the input data might not help you.

Examples

1.

fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
initial_position = (0,0)
moves = ['up', 'left', 'right', 'left', 'left']

then I should get:

['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']

as the characters I've been hovering with the selection cursor during my moves. Notice: Ryu is the first just because it "fails" the first up See test cases for more examples.

2.

fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
initial_position = (0,0)
moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']

Result:

['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']

OFF-TOPIC

Some music to get in the mood for this kata :

Street Fighter 2 - selection theme
https://www.youtube.com/watch?v=GR3d9FMBkC8
'''

# Link to Kata
# https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
