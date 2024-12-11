# parking lot

# car_sizes --> car --> spaces --> parking lot
# tickets --> tickets machine
# ticketpricingstrategy --> tickets machine

# tickets correspond with spaces

import enum
class CarSizes(enum.Enum):
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
        for _ in range(large_spots):
            pass
        for _ in range(medium_spots):
            pass
        for _ in range(small_spots):
            pass


class Ticket:
    pass

class TicketMachine:
    pass

from abc import ABC, abstractmethod
class TicketPricingStrategy(ABC):
    pass

