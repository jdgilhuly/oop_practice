# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum

class ParkingLot:
	def __init__(self):

class ParkingSpace:
	def __init__(self):

class Car:
	def __init__(self, type):
		self.type = None
		self.size = None

class CarType(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3
