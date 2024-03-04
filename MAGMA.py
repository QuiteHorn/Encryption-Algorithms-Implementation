import datetime

S0 = [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
S1 = [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15]
S2 = [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0]
S3 = [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11]
S4 = [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12]
S5 = [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0]
S6 = [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7]
S7 = [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]

S = [S0, S1, S2, S3, S4, S5, S6, S7]

MASK32 = 2 ** 32 - 1

from general import *

def t(x):
	y = 0
	for i in reversed(range(8)):
		j = (x >> 4 * i) & 0xf
		y <<= 4
		y ^= S[i][j]
	return y

def rot11(x):
	return x << 11

class MAGMA():
	def __init__(self, key):
		key = str_to_bit_array(key)
		self.keys = self.gen_keys(key)

	def gen_keys(self, k):
			keys = []
			while len(k) < 256:
				k += [0]
			for i in range(0, 256, 32):
				keys.append(bits_to_int(k[i:i+32]))
			for i in range(8):
				keys.append(keys[i])
			for i in range(8):
				keys.append(keys[i])
			for i in reversed(range(8)):
				keys.append(keys[i])
			return keys

	def f(self, x, k):
		x = bits_to_int(x)
		return int_to_bits(rot11(t((x + k) % 2 ** 32)))

	def encrypt(self, text):
		if len(str_to_bit_array(text)) % 64 != 0:
			pad_len = 8 - (len(text) % 8)
			text += pad_len * chr(pad_len)

		text = str_to_bit_array(text)
		blocks = split_blocks(text, 64)

		result = list()

		for block in blocks:
			result += self.encrypt_block(block)
		final_res = bit_array_to_str(result)
		return final_res

	def encrypt_block(self, block):
		l, r = split_blocks(block, 32)

		keys = self.keys

		for i in range(31):
			tmp = r
			r = xor(l, self.f(r, keys[i]))
			l = tmp

		return xor(l, self.f(r, keys[-1])) + r

	def decrypt(self, text):
		text = str_to_bit_array(text)
		blocks = split_blocks(text, 64)

		result = list()

		for block in blocks:
			result += self.decrypt_block(block)
		final_res = bit_array_to_str(result)

		pad_len = ord(final_res[-1])
		return final_res[:-pad_len]

	def decrypt_block(self, block):
		l, r = split_blocks(block, 32)

		keys = self.keys

		for i in range(31):
			tmp = r
			r = xor(l, self.f(r, keys[i]))
			l = tmp
		return xor(l, self.f(r, keys[-1])) + r
