#!/usr/bin/env python2

from bentonMachine import BentonMachine as BM

def main(args):
	memory = dict()
	state = False
	if args[0] == '--hex' or args[0] == '-h':
		state = True
		for i in range(0,len(args[1])):
			value = args[1][i]
			try:
				value = int(value)
			except:
				if value == 'a' or value == 'A':
					value = 10
				elif value == 'b' or value == 'B':
					value = 11
				elif value == 'c' or value == 'C':
					value = 12
				elif value == 'd' or value == 'D':
					value = 13
				elif value == 'e' or value == 'E':
					value = 14
				elif value == 'f' or value == 'F':
					value = 15
			memory[str(i)] = value*(16)
	elif args[0] == '--bin' or args[0] == 'b':
		state = True
		for i in range(0,len(args[1],2)):
			memory.append(int(args[1][i]*(2)))
	elif args[0] == '--help' or args[0] == '-H':
		print "Benton Machine"
		print "An implementation of the Brookshear Macheine"
		print "As described in 'Computer Science: An Overview'"
		print "\n"
		print "Usage:"
		print "  -h, --hex\tInput memory values as hexadecimal"
		print "  -b, --bin\tInput memory values as binary"
		print "  -H, --help\tPrint this help message"

	if state:
		# initialize machine
		machine = BM(memory)
		while True:
			if not machine.run():
				break

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])