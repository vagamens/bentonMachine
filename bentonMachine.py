#!/usr/bin/env python2

import operator
import numpy as n
from numbers import sign8, unsign8

class BrookshearMachine():

	def __init__(self):
		self.pc= ''
		self.ir=''
		self.memory=dict()
		self.registers={'0'=0, '1'=0, '2'=0, '3'=0, '4'=0, '5'=0,
						'6'=0, '7'=0, '8'=0, '9'=0, 'A'=0, 'B'=0,
						'C'=0, 'D'=0, 'E'=0, 'F'=0}

	def setPC(self, value):
		if value[0] == ['A'-'F'] or value[0] == ['0'-'9']:
			if value[1] == ['A'-'F'] or value[1] == ['0'-'9']:
				self.pc=value

	def setIR(self, value):
		if 'int' in type(value):
			if value <= 15:
				self.ir = value

	def load(self, r, x, y):
		'''
		LOAD the register R with bit pattern XY
		'''
		self.registers[str(r)] == str(x)+str(y)

	def memLoad(self, r, x, y):
		'''
		LOAD the register R with bit pattern found in the memory cell at XY
		'''
		self.registers[str(r)] = self.memory[str(x+y)]

	def store(self, r, x, y):
		'''
		STORE the bit pattern found in register R in the memory cell at XY
		'''
		self.memory[str(x+y)] = self.registers[str(r)]

	def move(self, r, s):
		'''
		MOVE the bit pattern found in register R to register S
		'''
		self.registers[str(r)] = self.registers[str(s)]
		self.registers[str(s)] = 0

	def add2s(self, r, s, t):
		'''
		ADD the bit patterns in registers S & T as though they were two's
		complement representation & leave the result in register R
		'''
		self.registers[str(r)] = s * t

	def addFloat(self, r, s, t):
		pass

	def bmOr(self, r, s, t):
		'''
		OR the bit patterns in registers S and t and place the result in register R
		'''
		self.registers[str(r)] = n.bitwise_or(s, t)

	def bmAnd(self, r, s, t):
		'''
		AND the bit patterns in register S and T and place the result in register R
		'''
		self.registers[str(r)] = n.bitwise_and(s, t)

	def xor(self, r, s, t):
		'''
		XOR the bit patterns in register S and T and place theresult in register R
		'''
		self.registers[str(r)] = n.bitwise_xor(s, t)

	def rotate(self, r, x):
		'''
		ROTATE the bit pattern in register R one bit to the right X times
		'''
		c = 1
		while c <= x:
			self.registers[str(r)] = n.right_shift(self.registers[str(r)]

	def jump(self, r, x, y):
		'''
		JUMP to the instruction located in the memory cell at address XY if
		the bit pattern in register R is equal to the bit pattern in register 0,
		otherwise, continue with the normal sequence of execution
		'''
		if self.registers[str(r)] == self.registers['0']:
			self.pc=str(x)+str(y)

	def fetch(self):
		self.ir = self.registers[str(self.pc)]+self.registers[str(self.pc+1)]

	def increment(self):
		self.pc += 2

	def execute(self):
		## load from memory
		if self.ir[0] == '1':
			self.memLoad(self.ir[1], int(str(self.ir[2])+ str(self.ir[3])))
		## load
		elif self.ir[0] == '2':
			self.load(self.ir[1], self.ir[2], self.ir[3])
		## store
		elif self.ir[0] == '3':
			self.store(self.ir[1], self.ir[2], self.ir[3])
		## move
		elif self.ir[0] == '4':
			self.move(self.ir[2], self.ir[3])
		## add
		elif self.ir[0] == '5':
			self.add2s(self.ir[1], self.ir[2], self.ir[3])
		## add
		elif self.ir[0] == '6':
			## not yet implemented
			self.addFloat(self.ir[1], self.ir[2], self.ir[3])
		## or
		elif self.ir[0] == '7':
			self.bmOr(self.ir[1], self.ir[2], self.ir[3])
		## and
		elif self.ir[0] == '8':
			self.bmAnd(self.ir[1], self.ir[2], self.ir[3])
		## exclusive or
		elif self.ir[0] == '9':
			self.xor(self.ir[1], self.ir[2], self.ir[3])
		## rotate
		elif self.ir[0] == 'A':
			pass
		## jump
		elif self.ir[0] == 'B':
			pass
		## halt
		elif self.ir[0] == 'C':
			return
		elif self.ir[0] == 'D':
			pass
		elif self.ir[0] == 'E':
			pass
		elif self.ir[0] == 'F':
			pass
		pass

	def run(self):
		self.fetch()
		self.increment()
		self.decode()
		self.execute()