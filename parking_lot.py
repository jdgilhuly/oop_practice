# parking_lot.py
from abc import ABC, abstractmethod
from enum import Enum
import datetime

# 1. Create interfaces/abstract classes
class ParkingStrategy(ABC):
    @abstractmethod
    def find_available_space(self, parking_spaces, vehicle_type):
        pass

class FeeCalculator(ABC):
    @abstractmethod
    def calculate_fee(self, entry_time, exit_time):
        pass

# 2. Split ParkingLot responsibilities
class ParkingSpaceManager:
    def __init__(self, space_configuration):
        self.parking_spaces = {}
        self.spaces_available = space_configuration
        self.__create_parking_lot(space_configuration)

    def __create_parking_lot(self, space_configuration):
        space_number = 0

        for _ in range(space_configuration[CarType.SMALL.value]):
            self.parking_spaces[space_number] = ParkingSpace(CarType.SMALL.value)
            space_number += 1

        for _ in range(space_configuration[CarType.MEDIUM.value]):
            self.parking_spaces[space_number] = ParkingSpace(CarType.SMALL.value)
            space_number += 1

        for _ in range(space_configuration[CarType.LARGE.value]):
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

class ParkingLot:
    def __init__(self, space_manager, parking_strategy, fee_calculator):
        self.space_manager = space_manager
        self.parking_strategy = parking_strategy
        self.fee_calculator = fee_calculator

    def park(self, vehicle):
        space_number = self.parking_strategy.find_available_space(
            self.space_manager.parking_spaces,
            vehicle.type
        )
        if space_number:
            self.space_manager.parking_spaces[space_number].park_car(vehicle.type)
            self.space_manager.spaces_available[vehicle.type] -= 1
            return space_number
        return None

    def unpark(self, space_number):
        parking_space = self.space_manager.parking_spaces[space_number]
        parking_space.unpark_car()
        self.space_manager.spaces_available[parking_space.size] += 1

# 3. Implement concrete strategies
class DefaultParkingStrategy(ParkingStrategy):
    def find_available_space(self, parking_spaces, vehicle_type):
        if self.spaces_available[vehicle_type] == 0:
            return None, None
        else:
            for space_number, space in self.parking_spaces.items():
                if space.is_empty:
                    return space_number, space
            return None, None

class HourlyFeeCalculator(FeeCalculator):
    def calculate_fee(self, entry_time, exit_time):
        time_difference = exit_time - entry_time
        return time_difference.total_seconds() / 3600 * 0.05

# 4. Make vehicle types extensible
class VehicleType(ABC):
    @abstractmethod
    def get_size_requirement(self) -> int:
        pass

class Car(VehicleType):
    def __init__(self, car_type, color):
        self.type = car_type.value
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


class FeeCalulator:
    def __init__(self) -> None:
        pass

    def calculate_parking_fee(self, entry_time):
        exit_time = datetime.datetime.now()
        time_difference = exit_time - entry_time
        return time_difference.total_minutes() * 0.05



def test_parking_lot():

    # Init Parking Lot
    parking_lot = ParkingLot(ParkingSpaceManager({CarType.SMALL.value: 2, CarType.MEDIUM.value: 2, CarType.LARGE.value: 2}), DefaultParkingStrategy(), HourlyFeeCalculator())


    ticket_machine = TicketMachine()


    # Init Cars
    small_car = Car(CarType.SMALL, "red")
    small_car_2 = Car(CarType.SMALL, "blue")
    small_car_3 = Car(CarType.SMALL, "green")
    medium_car = Car(CarType.MEDIUM, "blue")
    large_car = Car(CarType.LARGE, "green")


    # Test Parking

test_parking_lot()