#!/usr/bin/env python2

import operator
from numbers import Sign8, Float8

class BentonMachine():

	def __init__(self, memDict=dict()):
		self.pc= 0
		self.ir='0000'
		self.setMemory(memDict)
		self.registers={'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
						'6':0, '7':0, '8':0, '9':0, 'A':0, 'B':0,
						'C':0, 'D':0, 'E':0, 'F':0}

	def setMemory(self, memDict):
		self.memory = memDict

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
		STORE the bit pattern found in register R
		in the memory cell at XY
		'''
		try:
			x = int(x)
		except:
			if x == 'a' or x == 'A':
				x = 10
			elif x == 'b' or x == 'B':
				x = 11
			elif x == 'c' or x == 'C':
				x = 12
			elif x == 'd' or x == 'D':
				x = 13
			elif x == 'e' or x == 'E':
				x = 14
			elif x == 'f' or x == 'F':
				x = 15
		try:
			y = int(y)
		except:
			if y == 'a' or y == 'A':
				y = 10
			elif y == 'b' or y == 'B':
				y = 11
			elif y == 'c' or y == 'C':
				y = 12
			elif y == 'd' or y == 'D':
				y = 13
			elif y == 'e' or y == 'E':
				y = 14
			elif y == 'f' or y == 'F':
				y = 15
		val = (x*(16**2))+(y*(16**1))
		self.memory[str(val)] = self.registers[str(r)]

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
		self.registers[str(r)] = Sign8.add(self.registers[s], self.registers[t])

	def addFloat(self, r, s, t):
		self.registers[str(r)] = Float8.add(self.registers[s], self.registers[t])

	def bmOr(self, r, s, t):
		'''
		OR the bit patterns in registers S and t and place the result in register R
		'''
		val = [bin(self.registers[str(s).upper()])[2:], bin(self.registers[str(t).upper()])[2:]]
		while True:
			if len(val[0]) < 8:
				val[0] = '0'+val[0]
			else:
				break
		while True:
			if len(val[1]) < 8:
				val[1] = '0'+val[1]
			else:
				break
		tempVal = ''
		for i in range(8):
			if val[0] == '1' or val[1] == '1':
				tempVal = tempVal + '1'
			else:
				tempVal = tempVal + '0'
		val = tempVal
		tempVal = 0
		for i in range(len(val)):
			tempVal += int(val[i])*(2**(3-i))
		val = tempVal
		self.registers[str(r)] = val

	def bmAnd(self, r, s, t):
		'''
		AND the bit patterns in register S and T and place the result in register R
		'''
		val = [bin(self.registers[str(s)])[2:], bin(self.registers[str(t)])[2:]]
		while True:
			if len(val[0]) < 8:
				val[0] = '0'+val[0]
			else:
				break
		while True:
			if len(val[1]) < 8:
				val[1] = '0'+val[1]
			else:
				break
		tempVal = ''
		for i in range(8):
			if val[0] == '1' and val[1] == '1':
				tempVal = tempVal + '1'
			else:
				tempVal = tempVal + '0'
		val = tempVal
		for i in range(len(val)):
			tempVal += int(val[i])*(2**(3-i))
		val = tempVal
		self.registers[str(r)] = val

	def xor(self, r, s, t):
		'''
		XOR the bit patterns in register S and T and place theresult in register R
		'''
		val = [bin(self.registers[str(s)])[2:], bin(self.registers[str(t)])[2:]]
		while True:
			if len(val[0]) < 8:
				val[0] = '0'+val[0]
			else:
				break
		while True:
			if len(val[1]) < 8:
				val[1] = '0'+val[1]
			else:
				break
		tempVal = ''
		for i in range(8):
			if val[0] == '1' and val[1] == '1':
				tempVal = tempVal + '0'
			elif val[0] == '1' or val[1] == '1':
				tempVal = tempVal + '1'
			else:
				tempVal = tempVal + '0'
		val = tempVal
		for i in range(len(val)):
			tempVal += int(val[i])*(2**(3-i))
		val = tempVal
		self.registers[str(r)] = val

	def rotate(self, r, x):
		'''
		ROTATE the bit pattern in register R one bit to the right X times
		'''
		value = bin(self.registers[str(r)])[2:]
		while True:
			length = len(value)
			if length < 8:
				value = '0'+value
			else:
				break
		for c in range(1,x):
			value = value[-1]+value[0:-1]
		tempVal = 0
		for i in range(len(value)):
			tempVal += value[i]*(2**(3-i))
		value = tempVal
		self.registers[str(r)] = value

	def jump(self, r, x, y):
		'''
		JUMP to the instruction located in the memory cell at address XY if
		the bit pattern in register R is equal to the bit pattern in register 0,
		otherwise, continue with the normal sequence of execution
		'''
		value = [str(x), str(y)]
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
		value = (value[0]*(16)) + (value[1]*(16**2))
		if self.registers[str(r)] == self.registers['0']:
			self.pc=value

	def fetch(self):
		self.ir = hex(self.memory[str(self.pc)])[2]+\
		hex(self.memory[str(self.pc+1)])[2]+\
		hex(self.memory[str(self.pc+2)])[2]+\
		hex(self.memory[str(self.pc+3)])[2]

	def increment(self):
		self.pc += 4

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
		elif self.ir[0] == 'C' or self.ir[0] == '0':
			return
		elif self.ir[0] == 'D':
			pass
		elif self.ir[0] == 'E':
			pass
		elif self.ir[0] == 'F':
			pass
		pass

	def run(self):
		try:
			self.fetch()
			self.increment()
			self.execute()
			print "IR: " + self.ir.upper() + " PC: " + hex(self.pc).upper()[2:]
			print "MEMORY:"
			print sorted(self.memory.items(), key=operator.itemgetter(0))
			print "REGISTERS:"
			print sorted(self.registers.items())
			print "\n"
			return True
		except:
			print "DONE"
			return False