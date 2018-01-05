"""
Unit test case for src/build_price_dict.py.

Because of guaranteed conformity and a limited testing scope, this test file
does NOT test ProductInfo's invidual methods directly. Instead, it affirms that
all the attributes are as expected. Should there be an error, the problem
can be immediately narrowed down to populate() and get_tuple().

In the event PriceDict's get_* methods fail, this test script will attempt 
to exit with code 1, as the integrity of all other tests cannot be guaranteed.
"""

import sys
import unittest
import numpy as np
import pprint as pp
from src import build_price_dict as BPD
from src import get_json as GJ

class TestBuildPriceDict(unittest.TestCase):
	"""
	TestCase class for src/build_price_dict.py for easy test case running.

	Tests various attributes of PriceDict and ProductInfo to affirm they load
	as we would like them to, and tests with multiple, singular, and no option 
	cases.

	Note: We don't need to test for specific methods, as conformity is 
	guaranteed, and in the case of an error, the size of the array will tell us
	what the error was immediately.
	"""

	def setUp(self):
		# Assume get_json works (see other testing file), use to get JSON
		self.pricejson = GJ.get_JSON('ref/base-prices/base-prices.json')
		# We can assume standard initialization works, as only variables are
		# assigned. Use it to create a PriceDict() instance, and no more.
		self.pricedict = BPD.PriceDict()

		"""
		For purposes of this coding test, we have been guaranteed that input 
		JSON files will conform to standards we want. Thus, we are not concerned
		about parsing the file, but rather getting the correct dimensions when
		given a base-prices file. 

		Each test will call build_lookup_dict() and build_lookup_array(); 
		ensure that their properties conform to expected values.

		Our scope of error if add_base_pries fails is limited to populate()
		and get_tuple().
		"""
		self.pricedict.add_base_price(self.pricejson)

	"""
	Test multiple options, singular option, and no option products.

	We do not need to check for exclusitivity - a size error guarantees that
	duplicate or missing elements occured.
	"""

	# Check hoodie option_dict and option_order. [Multiple Options]

	def test_lookup_dict_hoodie_option_dict_size(self):
		# Affrim option_dict has the correct number of elements 
		self.assertEqual(
			len(self.pricedict.lookup_dict['hoodie'].option_dict), 2
			)

	def test_lookup_dict_hoodie_option_category_dict_size_size(self):
		# Affirm hoodie's option-size option_dict has the correct size
		self.assertEqual(
			len(self.pricedict.lookup_dict['hoodie'].option_dict['size']), 6
			)

	def test_lookup_dict_hoodie_option_category_dict_colour_size(self):
		# Affirm hoodie's option-colour option_dict has the correct size
		self.assertEqual(
			len(self.pricedict.lookup_dict['hoodie'].option_dict['colour']), 2
			)

	def test_lookup_dict_hoodie_option_category_dict_size_size(self):
		# Affirm defaultdict creates an EMPTY lookup (defaultdict check)
		self.assertEqual(
			len(self.pricedict.lookup_dict['hoodie'].option_dict['NA']), 0
			)

	def test_lookup_dict_hoodie_option_order_size(self):
		# Affirm hoodie option_order has correct number of elements
		self.assertEqual(
			len(self.pricedict.lookup_dict['hoodie'].option_order), 2
			)


	# Test sticker option_dict and option_order. [One Option]
	def test_lookup_dict_sticker_option_dict_size(self):
		# Affrim option_dict has the correct number of elements 
		self.assertEqual(
			len(self.pricedict.lookup_dict['sticker'].option_dict), 1
			)

	def test_lookup_dict_sticker_option_category_dict_size_size(self):
		# Affirm stickers's option-size option_dict has the correct size
		self.assertEqual(
			len(self.pricedict.lookup_dict['sticker'].option_dict['size']), 4
			)

	def test_lookup_dict_sticker_option_category_dict_size_size(self):
		# Affirm defaultdict creates an EMPTY lookup
		self.assertEqual(
			len(self.pricedict.lookup_dict['sticker'].option_dict['NA']), 0
			)

	def test_lookup_dict_sticker_option_order_size(self):
		# Affirm sticker option_order has correct number of elements
		self.assertEqual(
			len(self.pricedict.lookup_dict['sticker'].option_order), 1
			)

	# Test legging option_dict and option_order. [No Options]

	def test_lookup_dict_leggings_option_dict_size(self):
		# Affrim option_dict has the correct number of elements 
		self.assertEqual(
			len(self.pricedict.lookup_dict['leggings'].option_dict), 0
			)

	def test_lookup_dict_leggings_option_category_dict_size_size(self):
		# Affirm defaultdict creates an EMPTY lookup
		self.assertEqual(
			len(self.pricedict.lookup_dict['leggings'].option_dict['NA']), 0
			)

	def test_lookup_dict_leggings_option_order_size(self):
		# Affirm leggings option_order has correct number of elements
		self.assertEqual(
			len(self.pricedict.lookup_dict['leggings'].option_order), 0
			)


	"""
	At this point, assume the lookup_dic has been constructed successfully.
	In this case, use the lookup_dict and confirm matching prices.

	Run two tests to affirm that get_price and get_index are true.
	"""

	def test_get_index(self):
		# Due to processing order, small will always be processed first.
		try:
			self.assertEqual(
				self.pricedict.get_index('hoodie', 'size', 'small'),
				0)
		except AssertionError:
			sys.exit("A critical test for BPD.get_index() has failed.")

	def test_get_price(self):
		# hoodie[0][0] will always be small / white/dark, which is 3800.
		# This is because build_price_dict scans in order.
		try:
			self.assertEqual(self.pricedict.get_price('hoodie', (0,0)), 3800)
			self.assertEqual(self.pricedict.get_price('leggings', ()), 5000)
		except AssertionError:
			sys.exit("A critical test for BPD.get_price() has failed.")


# Allow this script to be run directly as a module
if __name__ == '__main__':
	unittest.main()