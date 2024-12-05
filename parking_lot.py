# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum
from collections import deque


class ParkingLot:

	def __init__(self, small_spaces, medium_spaces, large_spaces):
		self.parking_spaces = {}
		self.spaces_available = {
			CarType.SMALL.value: small_spaces,
			CarType.MEDIUM.value: medium_spaces,
			CarType.LARGE.value: large_spaces
		}

		self.__create_parking_lot(small_spaces, medium_spaces, large_spaces)

	def __create_parking_lot(self, small_spaces, medium_spaces, large_spaces):

		space_number = 0

		for _ in range(small_spaces):
			self.parking_spaces[space_number] = ParkingSpace(CarType.SMALL.value)
			space_number += 1

		for _ in range(medium_spaces):
			self.parking_spaces[space_number] = ParkingSpace(CarType.SMALL.value)
			space_number += 1

		for _ in range(large_spaces):
			self.parking_spaces[space_number] = ParkingSpace(CarType.SMALL.value)
			space_number += 1

	def __get_open_parking_spot(self, size):
		if not self.parking_spaces[size][0].is_empty:
			return None
		else:
			return self.parking_spaces[size].popleft()

	def __get_car_type_from_ticket(self, ticket_number):
		return self.spaces[ticket_number]

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

	def unpark(self, ticket_number):
		car_type = self.__get_car_type_from_ticket(ticket_number)
		parking_space = self.parking_spaces[car_type].popleft()
		parking_space.unpark_car()
		self.parking_spaces[car_type].append(parking_space)



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
		self.type = type.value
		self.color = color

	def get_car_details(self):
		return (self.type, self.color)

class CarType(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3


# Init Cars
small_car = Car(CarType.SMALL, "red")
print(small_car.get_car_details())

# Init Lot
parking_lot = ParkingLot(2, 2, 2)


# Test Parking
print(parking_lot.return_number_of_parking_spaces(CarType.SMALL.value))
parking_lot.park(small_car)
print(parking_lot.return_number_of_parking_spaces(CarType.SMALL.value))


