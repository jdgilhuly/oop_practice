from abc import ABC, abstract method

class Game:
	def __init__(self):
		self.game = None

	@abstractmethod
	def create_game(self):
		self.game = ConnectFour()

class Grid():
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
	
	
