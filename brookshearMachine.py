#!/usr/bin/env python3

class BrookshearMachine():

	def __init__():
		pass

	def load(r, x, y):
		'''
		LOAD the register R with bit pattern XY
		'''
		pass

	def memLoad(r, x, y):
		'''
		LOAD the register R with bit pattern found in the memory cell at XY
		'''
		pass

	def store(r, x, y):
		'''
		STORE thebit pattern found in register R in the memory cell at XY
		'''
		pass

	def move(r, s):
		'''
		MOVE the bit pattern found in register R to register S
		'''
		pass

	def add(r, s, t):
		'''
		ADD the bit patterns in registers S & T as though they were two's
		complement representation & leave the result in register R
		'''
		pass

	def bmOr(r, s, t):
		'''
		OR the bit patternsin registers S and t and place the result in register R
		'''
		pass

	def bmAnd(r, s, t):
		'''
		AND the bit patterns in register S and T and place the result in register R
		'''
		pass

	def xor(r, s, t):
		'''
		XOR the bit patterns in register S and T and place theresult in register R
		'''
		pass

	def rotate(r, x):
		'''
		ROTATE the bit pattern in register R one bit to the right X times
		'''
		pass

	def jump(r, x, y):
		'''
		JUMP to the instruction located in the memory cell at address XY if
		the bit pattern in register R is equal to the bit pattern in register 0,
		otherwise, continue with the normal sequence of execution
		'''
		pass

	def halt(r, x, y):
		'''
		HALT execution
		'''
		pass

	def fetch():
		pass

	def increment():
		pass

	def decode():
		pass

	def execute():
		pass