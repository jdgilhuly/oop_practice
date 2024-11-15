from abc import ABC, abstract method

class Game(ABC):
	def __init__(self):
		self.game = None

	@abstractmethod
	def create_game(self):
		self.game = ConnectFour()
