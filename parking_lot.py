# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum

class ParkingLot:

	def __init__(self):
		pass

	def create_parking_lot(self, size):
		self.parking_spaces = [ParkingSpace(size) for _ in range(size)]

	def get_empty_parking_spaces(self):
		pass


class ParkingSpace:

	def __init__(self, size):
		self.size = size
		self.is_empty = True

	def get_parking_space_details(self):
		return self.size

	def park_car(self, car_size):
		if self.is_empty:
			if self.size >= car_size:
				self.is_empty = False
				return True
			else:
				return False
		else:
			return False

	def unpark_car(self):
		self.is_empty = True

class Car:
	def __init__(self, type, color):
		self.type = type
		self.color = color

	def get_car_details(self):
		return (self.type, self.color)

class CarType(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3

x = Car(CarType.SMALL, "red")
print(x.get_car_details())
