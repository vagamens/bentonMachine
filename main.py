#!/usr/bin/env python2

from bentonMachine import BentonMachine as BM

def main(args):
	memory = []
	if args[0] == '--hex' or args[0] == '-h':
		for i in range(0,len(args[1],2)):
			value = [args[1][i], args[1][i+1]]
			try:
				value[0] = int(value[0])
			except:
				if value[0] == 'a' or value[0] == 'A':
					value[0] = 10
				elif value[0] == 'b' or value[0] == 'B':
					value[0] = 11
				elif value[0] == 'c' or value[0] == 'C':
					value[0] = 12
				elif value[0] == 'd' or value[0] == 'D':
					value[0] = 13
				elif value[0] == 'e' or value[0] == 'E':
					value[0] = 14
				elif value[0] == 'f' or value[0] == 'F':
					value[0] = 15
			try:
				value[1] = int(value[1])
			except:
				if value[1] == 'a' or value[1] == 'A':
					value[1] = 10
				elif value[1] == 'b' or value[1] == 'B':
					value[1] = 11
				elif value[1] == 'c' or value[1] == 'C':
					value[1] = 12
				elif value[1] == 'd' or value[1] == 'D':
					value[1] = 13
				elif value[1] == 'e' or value[1] == 'E':
					value[1] = 14
				elif value[1] == 'f' or value[1] == 'F':
					value[1] = 15
			memory.append(value[0]*(16**2)+value[1]*(16**1))
	elif args[0] == '--bin' or args[0] == 'b':
		for i in range(0,len(args[1],2)):
			memory.append((int(args[1][i])*(2**2))+(int(args[1][i])*(16**1)))

	# initialize machine
	machine = BM(memory)
	while True:
		if machine.run():
			pass
		else:
			break

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])