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
        self.large_spots_available = large_spots
        self.medium_spots_available = medium_spots
        self.small_spots_available = small_spots
        self.__create_lot(large_spots, medium_spots, small_spots)

    def __create_lot(self, large_spots, medium_spots, small_spots):
        spot_number = 0
        for _ in range(large_spots):
            self.spots[spot_number] = Space(spot_number, Size.LARGE)
            spot_number += 1
        for _ in range(medium_spots):
            self.spots[spot_number] = Space(spot_number, Size.MEDIUM)
            spot_number += 1
        for _ in range(small_spots):
            self.spots[spot_number] = Space(spot_number, Size.SMALL)
            spot_number += 1


class Ticket:
    def __init__(self, ticket_number, entry_time):
        self.ticket_number = ticket_number
        self.entry_time = entry_time

class TicketMachine:
    def __init__(self):
        self.ticket_number = 0

    def get_ticket(self):
        self.ticket_number += 1
        return Ticket(self.ticket_number)

from abc import ABC, abstractmethod
class TicketPricingStrategy(ABC):
    pass



