from random import randint
#generate lists and dictionaries of n size

def gen_list(n):
	r = []
	for f in range(n):
		r.append(randint(0,f))
	return(r)

print(gen_list(10))

def gen_dict(n):
	r = {}
	for f in range(n):
		r[f] = randint(0,f)
	return(r)

print(gen_dict(5))
