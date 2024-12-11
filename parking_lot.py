# parking lot

# car_sizes --> car --> spaces --> parking lot
# tickets --> tickets machine
# ticketpricingstrategy --> tickets machine

# tickets correspond with spaces

from enum import Enum
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3

class Car:
    def __init__(self, type):
        self.type = type

    def print_car_type(self):
        print(self.type)

class Space:
    def __init__(self, space_number, size):
        self.space_number = space_number
        self.size = size

class ParkingLot:
    def __init__(self, large_spots, medium_spots, small_spots):
        self.spots = {}


    def __create_lot(self, large_spots, medium_spots, small_spots)
        spot_number = 0
        for _ in range(large_spots):
            self.spots[spot_number] = Space(spot_number, CarSize.LARGE)
            spot_number += 1
        for _ in range(medium_spots):
            self.spots[spot_number] = Space(spot_number, CarSize.MEDIUM)
            spot_number += 1
        for _ in range(small_spots):
            self.spots[spot_number] = Space(spot_number, CarSize.SMALL)
            spot_number += 1



class Ticket:
    pass

class TicketMachine:
    pass

from abc import ABC, abstractmethod
class TicketPricingStrategy(ABC):
    pass

