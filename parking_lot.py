# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum

class ParkingLot:
	def __init__(self):
		pass
	def get_empty_parking_spaces(self):
		pass
	def park_car(self, car):
		pass

class ParkingSpace:

	def __init__(self, size):
		self.size = size
		self.is_empty = True

	def get_parking_space_details(self):
		return self.size

	def park_car(self):
		self.is_empty = False

	def unpark_car(self):
		self.is_empty = True

class Car:
	def __init__(self, type):
		self.type = None

	def get_car_details(self):
		return self.type

class CarType(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3

x = Car(CarType.SMALL)
print(x.get_car_details())
