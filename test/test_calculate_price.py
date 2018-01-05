"""
Unit test case for src/calculate_price.py

Basic unit tests for the price calculation function of the program. Because 
JSON errors and conformity are guaranteed/caught before presented to this file,
the only tests needed are for the arithmetic behind it all.
"""

import sys
import unittest
import numpy as numpy
import pprint as pprint

from src import calculate_price as CALC
from src import build_price_dict as BPD 
from src import get_json as GJ

class TestCalculatePrice(unittest.TestCase):
	"""
	TestCase class for src/calculate_price.py for easy test case running.

	Calculates with a variety of potential carts: Carts with 0 items, 1 item,
	multiple items, and items that contain 0 options, which are represented 
	slightly specially by build_price.py. 
	"""
	def setUp(self):
		self.pricedict = BPD.PriceDict()
		self.pricedict.add_base_price(
			GJ.get_JSON('ref/base-prices/base-prices.json'))

		self.cart_9500 = GJ.get_JSON('ref/cart/cart-9500.json')
		self.cart_9363 = GJ.get_JSON('ref/cart/cart-9363.json')
		self.cart_4560 = GJ.get_JSON('ref/cart/cart-4560.json')
		self.cart_5500 = GJ.get_JSON('ref/cart/cart-5500.json')
		self.cart_0 = GJ.get_JSON('ref/cart/cart-0.json')

	"""
	Testing calculate is rather straightforward. Because get_json and
	build_price_dict are assumed to work perfectly before this, we only need
	to make sure we're calculating for prices correctly.

	To calculate prices correctly, we need to affirm it works properly for
	multiple items, one item, and zero items. Conformity and existence of 
	options is guaranteed otherwise.

	There is also one special case, where an item contains zero options. 
	Because the array is formatted slightly differently, run a test to make sure
	it still calculates correctly.
	"""

	def test_multiple_items(self):
		# Assert on two provided carts with 2 items
		self.assertEqual(CALC.calculate(self.cart_9500, self.pricedict), 9500)
		self.assertEqual(CALC.calculate(self.cart_9363, self.pricedict), 9363)

	def test_single_item(self):
		# Assert on a cart with a single item
		self.assertEqual(CALC.calculate(self.cart_4560, self.pricedict), 4560)

	def test_no_item(self):
		# Assert on a cart with no item
		self.assertEqual(CALC.calculate(self.cart_0, self.pricedict), 0)

	def test_no_options(self):
		# Assert on a cart with no item
		self.assertEqual(CALC.calculate(self.cart_5500, self.pricedict), 5500)


# Allow this module to be run directly
if __name__ == "__main__":
	unittest.main()