"""
Unit test case for src/get_json.py.

Tests positive and negative inputs for both local files and URL-based loading.
"""

import unittest
from src import get_json as GJ

class TestGetJson(unittest.TestCase):
	"""
	TestCase class for src/get_json.py for easy test case running.

	Tests true positive, false positive, and true negative cases for local and
	URL-based json files.
	
	Note: We do not need to test for conformity: Guaranteed conforming input.
	"""	

	# Local-based tests

	def test_load_local_good_json(self):
		# Test a valid file: Note that Python loads jsons as "lists"	
		self.assertEqual(type(GJ.get_JSON('ref/cart/cart-4560.json')), type([]))

	def test_load_local_bad_json(self):
		# Test an invalid local file, not a URL:
		self.assertRaises(ValueError, lambda: GJ.get_JSON('nonexistent_path'))

	def test_load_local_not_json(self):
		# Test a local file that ISN'T a JSON file
		self.assertRaises(ValueError, lambda: GJ.get_JSON('main.py'))


	# URL-based tests

	def test_load_url_good_json(self):
		# Test a valid URL to a JSON
		self.assertEqual(
			type(GJ.get_JSON(
			'https://www.metaweather.com/api/location/search/?query=tokyo')
			), type([])) 

	def test_load_url_not_json(self):
		# Test loading a valid URL, but not a JSON url
		self.assertRaises(ValueError, lambda: GJ.get_JSON('https://google.com'))

	def test_load_nonexistent_url(self):
		# Test an invalid URL to a JSON: All bad URLs will throw ValueError
		self.assertRaises(ValueError, lambda: GJ.get_JSON('https://badurl.xyz'))

	def test_load_url_no_schema(self):
		# Test with an missing schema
		self.assertRaises(ValueError, lambda: GJ.get_JSON('badurl.xyz'))


# Make file executable as standalone
if __name__ == '__main__':
	unittest.main()
