# parking lot

# car_sizes --> car --> spaces --> parking lot
# tickets --> tickets machine
# ticketpricingstrategy --> tickets machine

# tickets correspond with spaces

class Car:
    def __init__(self, type):
        self.type =
    pass

import enum
class CarSizes(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3



class Space:
    pass

class ParkingLot:
    pass

class Ticket:
    pass

class TicketMachine:
    pass

from abc import ABC, abstractmethod
class TicketPricingStrategy(ABC):
    pass

