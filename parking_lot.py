# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum
import datetime


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
		if self.spaces_available[size] == 0:
			return None, None
		else:
			for space_number, space in self.parking_spaces.items():
				if space.is_empty:
					return space_number, space
			return None, None

	def return_number_of_parking_spaces(self, size):
		return self.spaces_available[size]

	def park(self, car):
		space_number, parking_space = self.__get_open_parking_spot(car.type)
		if parking_space:
			parking_space.park_car(car.type)
			self.spaces_available[car.type] -= 1
			return space_number
		return None

	def unpark(self, space_number):
		parking_space = self.parking_spaces[space_number]
		parking_space.unpark_car()
		self.spaces_available[parking_space.size] += 1


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

class Ticket:
	def __init__(self, ticket_number, entry_time):
		self.ticket_number = ticket_number
		self.entry_time = entry_time
		self.is_paid = False


class TicketMachine:
	def __init__(self):
		self.ticket_number = 0
		self.tickets = {}

	def get_ticket(self):
		self.ticket_number += 1
		self.tickets[self.ticket_number] = Ticket(self.ticket_number, datetime.datetime.now())
		return self.ticket_number

	def pay_ticket(self, ticket_number):
		self.tickets[ticket_number].is_paid = True
		return self.calculate_parking_fee(self.tickets[ticket_number].entry_time)

	def calculate_parking_fee(self, entry_time):
		exit_time = datetime.datetime.now()
		time_difference = exit_time - entry_time
		return time_difference.total_minutes() * 0.05

def test_parking_lot():

	# Init Parking Lot
	parking_lot = ParkingLot(2, 2, 2)


	ticket_machine = TicketMachine()


	# Init Cars
	small_car = Car(CarType.SMALL, "red")
	small_car_2 = Car(CarType.SMALL, "blue")
	small_car_3 = Car(CarType.SMALL, "green")
	medium_car = Car(CarType.MEDIUM, "blue")
	large_car = Car(CarType.LARGE, "green")


	# Test Parking

test_parking_lot()