from abc import ABC, abstract method

class Game:
	def __init__(self):
		self.game = None

	@abstractmethod
	def create_game(self):
		self.game = ConnectFour()

class Grid():
	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self._grid = None
			
	
