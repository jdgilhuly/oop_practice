# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum
from collections import deque

class ParkingLot:

	def __init__(self, small_spaces, medium_spaces, large_spaces):
		self.parking_spaces = {CarType.SMALL: deque(),
							   CarType.MEDIUM: deque(),
							   CarType.LARGE: deque()}
		self.__create_parking_lot(small_spaces, medium_spaces, large_spaces)


	def __create_parking_lot(self, small_spaces, medium_spaces, large_spaces):

		for _ in range(small_spaces):
			self.parking_spaces[CarType.SMALL].append(ParkingSpace(CarType.SMALL))
		for _ in range(medium_spaces):
			self.parking_spaces[CarType.MEDIUM].append(ParkingSpace(CarType.MEDIUM))
		for _ in range(large_spaces):
			self.parking_spaces[CarType.LARGE].append(ParkingSpace(CarType.LARGE))

	def __get_open_parking_spot(self, size):
		if not self.parking_spaces[size][0].is_empty:
			return None
		else:
			return self.parking_spaces[size].popleft()

	def return_number_of_parking_spaces(self, size):
		return len(self.parking_spaces[size])

	def park(self, car):
		parking_space = self.__get_open_parking_spot(car.type)
		if parking_space:
			if parking_space.park_car(car.type):
				self.parking_spaces[car.type].append(parking_space)
				return True
			else:
				self.parking_spaces[car.type].appendleft(parking_space)
				return False
		return False


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

small_car = Car(CarType.SMALL, "red")
print(small_car.get_car_details())


parking_lot = ParkingLot(2, 2, 2)

print(parking_lot.return_number_of_parking_spaces(CarType.SMALL))
parking_lot.park(small_car)
print(parking_lot.return_number_of_parking_spaces(CarType.SMALL))


