#!/usr/bin/env python3

class Numbers:
	'''Just a wrapper class for my datatypes.'''

	class float8:
		'''Defines numbers in 8-bit standard notation.'''
		def __init__(self, bitString=''):
			self.bitString = bitString
			self.sign = self.bitString[0]
			self.exponent = self.bitString[1:4]
			self.mentassa = self.bitString[5:]

		def getValue(self, type='num'):
			if type == 'num':
				return self.value
			elif type == 'bin':
				return 'b'+self.bitString
			elif type == 'hex':
				return hex(int('b'+self.bitString))
			else:
				return 'Unknown type'

		def setValue(self, value):
			if 'float' in type(value):
				# some logic to change into useful datatype
				pass
			elif 'int' in type(value):
				# some logic to change into float
				pass
			elif 'str' in type(value):
				# some logic to change bin to float
				# some logic to change hex to float
				pass

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

	class sign8:
		'''Defines numbers in two's compliment.'''
		def __init__(self, bitString=''):
			self.bitString = bitString
			self.sign = self.bitString[0]
			self.bitValue = self.bitString[1:]
			self.value = int('b'+self.bitValue) * (-1)

		def setValue(self, value):
			if 'int' in type(value):
				# run some logic to convert the given value into 2's compilment
				pass

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
			if self.sign == '1':
				return True
			else:
				return False

	class unsign8:
		'''Just an unsigned integer.'''
		def __init__(self, bitString=''):
			self.bitString = bitString
			self.value = self.bitString

		def setValue(self, value):
			if 'int' in type(value):
				# some logic to keep the value
			elif 'str' in type(value):
				# some logic to convert bin to int
				# some logic to convert hex to int
				pass

		def getValue(self, type='num'):
			if type == 'num':
				return int('b'+self.bitString)
			elif type == 'bin':
				return 'b'+self.bitString
			elif type == 'hex':
				return hex(int('b'+self.bitString))
			else:
				return 'Unknown type'

		def getNum(self):
			return self.getValue(type='num')

		def getHex(self):
			return self.getValue(type='hex')

		def getBin(self):
			return self.getValue(type='bin')