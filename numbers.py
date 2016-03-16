#!/usr/bin/env python2

import numpy as np

class Float8:
	'''Defines numbers in 8-bit standard notation.
	   Numbers are input as integers, added and subtracted,
	   then returned as integers.'''
	lookup = [dict(), dict()]

	# generate the lookup table
	@staticmethod
	def generate():
		for i in range(8,255):
			bitString = bin(i)[2:]
			sign = int(bitString[0])
			exponent = bitString[1:4]
			mantissa = bitString[4:]
			preRad = []
			postRad = []
			for j in mantissa:
				postRad.append
			# set numbers for the exponent
			# one is negative, 0 is positive
			if exponent == '111':
				exponent = [0, 3]
			elif exponent == '110':
				exponent = [0, 2]
			elif exponent == '101':
				exponent = [0, 1]
			elif exponent == '100':
				exponent = [0, 0]
			elif exponent == '011':
				exponent = [1, 1]
			elif exponent == '010':
				exponent = [1, 2]
			elif exponent == '001':
				exponent = [1, 3]
			elif exponent == '000':
				exponent = [1, 4]
			# set the postRad values
			for i in mantissa:
				postRad.append(int(i))
			# set the decimal values
			if exponent[0] == 1:
				for i in range(1,exponent[1]):
					tempPostRad = [0]
					for j in postRad:
						tempPostRad.append(j)
					postRad = tempPostRad
			elif exponent[0] == 0:
				for i in range(1,exponent[1]):
					if postRad == []:
						preRad.append(0)
					else:
						preRad.append(postRad.pop(0))
			# calculate whole numbers
			if preRad == []:
				preRad = 0
			else:
				tempVal = 0
				for i in range(len(preRad)):
					tempVal += preRad[i]*(2**(3-i))
				preRad = tempVal
			# calculate decimal values
			if postRad == []:
				postRad = 0
			else:
				tempVal = 0
				for i in range(len(postRad)):
					tempVal += postRad[i]*(1/(2**(i+1)))
				postRad = tempVal
			## add 'em up and find the negative
			value = (-1)*sign*(preRad + postRad)
			## add the value to the lookup tables
			Float8.lookup[0][str(i)] = value
			Float8.lookup[1][str(value)] = i

	@staticmethod
	def add(self, x, y):
		z = self.lookup[0][str(x)] + self.lookup[0][str(y)]
		return Float8.lookup[1][str(z)]

	@staticmethod
	def sub(self, x, y):
		z = self.lookup[0][str(x)] - self.lookup[0][str(y)]
		return Float8.lookup[1][str(z)]

Float8.generate()

class Sign8:
	'''Defines numbers in two's compliment.
	Takes in integers, makes sure that they are 8-bit integers
	through out the transaction, then returns as an integer.
	uses numpy int8.'''
	@staticmethod
	def add(self, x, y):
		z = np.int8(np.int(x) + np.int(y))
		return z

	@staticmethod
	def sub(self, x, y):
		z = np.int(np.int(x) + np.int(y))
		return z

class UnSign8:
	'''Just an unsigned integer. Uses numpy uint8.'''
	@staticmethod
	def add(self, x, y):
		z = np.uint8(np.uint8(x) + np.uint8(y))
		return z

	@staticmethod
	def sub(self, x, y):
		z = np.uint8(np.uint8(x) - np.uint8(y))
		return z