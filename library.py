class Library:
	def __init__(self):
		pass

class Computer:
	def __init__(self, books):
		self.books = books

	def get_book_genre(self, book_name):
		return self.books[book_name].genre
			

class Book:
	def __init__(self, title, author, genre):
		self.title = title
		self.author = author
		self.genre = genre

class BookPricing:
	def __init__(self, price):
		self.price = price
	
	def apply_discout(self, discount):
		self.price *= (1 - discount)
		return self.price

class Librarian:
	def __init__(self, name):
		self.name = name

import enum
class Genre(enum.Enum):
	Non-Fiction = 1
	Fiction = 1
