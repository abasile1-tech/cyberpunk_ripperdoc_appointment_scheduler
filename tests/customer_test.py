import unittest
from app import db
from models.Customer import Customer

class TestCustomer(unittest.TestCase):
	def setUp(self):
		self.jackie = Customer()
		self.jackie.id = 100
		self.jackie.name = "Jackie Welles"

	def test_repr(self):
		self.assertEqual("<Customer: 100: Jackie Welles>", self.jackie.__repr__())

	