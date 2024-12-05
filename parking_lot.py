# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum

class ParkingLot:

	def __init__(self, small_spaces, medium_spaces, large_spaces):
		self.parking_spaces = {CarType.SMALL: [],
							   CarType.MEDIUM: [],
							   CarType.LARGE: []}
		self.create_parking_lot(small_spaces, medium_spaces, large_spaces)


	def create_parking_lot(self, small_spaces, medium_spaces, large_spaces):

		space = 1

		for _ in range(small_spaces):
			self.parking_spaces[CarType.SMALL].append(ParkingSpace(CarType.SMALL))
			space += 1
		for _ in range(medium_spaces):
			self.parking_spaces[CarType.MEDIUM].append(ParkingSpace(CarType.MEDIUM))
			space += 1
		for _ in range(large_spaces):
			self.parking_spaces[CarType.LARGE].append(ParkingSpace(CarType.LARGE))
			space += 1


	def get_empty_parking_spaces(self):
		empty_spaces = []
		for space in self.parking_spaces:
			if space.is_empty:
				empty_spaces.append(space)
		return empty_spaces


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
