"""
MicroPython driver for MLX90614 IR temperature sensor
"""

import ustruct

_REGISTER_TA = const(0x06)     # ambient
_REGISTER_TOBJ1 = const(0x07)  # object

class MLX90614:
	def __init__(self, i2c, address=0x5a):
		self.i2c = i2c
		self.address = address

	def read16(self, register):
		data = self.i2c.readfrom_mem(self.address, register, 2)
		return ustruct.unpack('<H', data)[0]

	def read_temp(self, register):
		temp = self.read16(register);
		# apply measurement resolution (0.02 degrees per LSB)
		temp *= .02;
		# Kelvin to Celcius
		temp -= 273.15;
		return temp;

	def read_ambient_temp(self):
		return self.read_temp(_REGISTER_TA)

	def read_object_temp(self):
		return self.read_temp(_REGISTER_TOBJ1)
