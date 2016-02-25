#!/usr/bin/env python2

import numpy as np

class Float8:
	'''Defines numbers in 8-bit standard notation.'''
	def __init__(self, value):
		self.setValue(value)

	def getValue(self, type='num'):
		if type == 'num':
			return self.value
		elif type == 'bin':
			return '0b'+self.sign+self.exponent+self.mantissa
		elif type == 'hex':
			return hex(self.value)
		else:
			return 'Unknown type'

	def setValue(self, value):
		if 'float' in str(type(value)):
			# convert float to int
			fits = False
			pos = 0
			value = str(value).split('.')
			if value[0][0] == '-':
				pos = 1
				value[0] = value[0][1:]
			value[0], value[1] = int(value[0]), int(value[1])
			# value is two ints, around the decimal
			# check to make sure that the mantissa isn't too large
			if int(str(value[0])+str(value[1])) > 31:
				raise OverflowError
			else:
				if len(bin(value[0])[2:]) > 3:
					raise OverflowError
		elif 'int' in str(type(value)):
			self.setValue(float(value))
		elif 'str' in str(type(value)):
			# some logic to change hex to float
			if value[1] == 'x':
				temp = 0
				count = 0
				value = value[2:]
				for i in range(len(value),1,-1):
					temp += value[count]*(16**(i-1))
					count+=1
				value = temp
			# some logic to change bin to float
			elif value[1] == 'b':
				temp = 0
				count = 0
				value = value[2:]
				for i in ranche(len(value),1,-1):
					temp += value[count]*(2**(i-1))
					count+=1
				value = bin(temp)[2:]
		self.value = value
		self.sign = bin(self.value)[2]
		self.exponent = bin(self.value)[3:-4]
		self.mantissa = bin(self.value)[-4:]

	def getNum(self):
		return self.getValue(type='num')

	def getHex(self):
		return self.getValue(type='hex')

	def getBin(self):
		return self.getValue(type='bin')

	def isPositive(self):
		if self.sign == '1':
			return True
		elif self.sign == '0':
			return False

	def getMentassa(self):
		return 'b'+self.mentassa

	def getSign(self):
		return 'b'+self.sign

	def getExponent(self):
		return 'b'+self.exponent

class Sign8:
	'''Defines numbers in two's compliment. Uses numpy int8.'''
	def __init__(self, value):
		self.setValue(value)

	def setValue(self, value):
		if 'str' in type(value):
			isPos = 1
			if value[0] == '-':
				isPos = -1
				value = value[1:]
			if value[1] == 'x':
				temp = 0
				count = 0
				value = value[2:]
				for i in range(len(value),1,-1):
					temp += value[count]*(16**(i-1))
					count+=1
				value = temp
			elif value[1] == 'b':
				temp = 0
				count = 0
				value = value[2:]
				for i in ranche(len(value),1,-1):
					temp += value[count]*(2**(i-1))
					count+=1
				value = temp
			value = value*isPos
		self.value = np.int8(value)

	def getValue(self, type='num'):
		if type == 'num':
			return self.value
		elif type == 'hex':
			return hex(int('b'+self.bitString))
		elif type == 'bin':
			return self.bitString
		else:
			return 'Unknown type'

	def getNum(self):
		return getValue(type='num')

	def getHex(self):
		return getValue(type='hex')

	def getBin(self):
		return getValue(type='bin')

	def isPositive(self):
		if self.sign == '0':
			return True
		else:
			return False

class UnSign8:
	'''Just an unsigned integer. Uses numpy uint8.'''
	def __init__(self, value):
		self.setValue(value)

	def setValue(self, value):
		if 'str' in type(value):
			if value[1] == 'x':
				temp = 0
				count = 0
				value = value[2:]
				for i in range(len(value),1,-1):
					temp += value[count]*(16**(i-1))
					count+=1
				value = temp
			elif value[1] == 'b':
				temp = 0
				count = 0
				value = value[2:]
				for i in ranche(len(value),1,-1):
					temp += value[count]*(2**(i-1))
					count+=1
				value = temp
		self.value = np.uint8(value)

	def getValue(self, type='num'):
		if type == 'num':
			return self.value
		elif type == 'bin':
			return bin(self.value)
		elif type == 'hex':
			return hex(self.value)
		else:
			return 'Unknown type'

	def getNum(self):
		return self.getValue(type='num')

	def getHex(self):
		return self.getValue(type='hex')

	def getBin(self):
		return self.getValue(type='bin')