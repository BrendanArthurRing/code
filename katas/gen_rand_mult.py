# Random Number Pair Generator - Test for Deep Dream


import random

arr = [[1, 20], [2, 40], [3, 50]]

def gen_rand_mult_dd(mult, arr):
	m = []
	for i in range(mult):
		r = random.choice(arr)
		x = r[0]
		y = random.randint(0, r[1])
		m.append([x, y]) # this part does not work
		return m

gen_rand_mult_dd(6, arr)



deep_dream_sequence = ["render_deepdream(T(", 
layer
")[:,:,:,"
channel
"]+T("

layer_a
")[:,:,:,"
channel_a

"], img0)"