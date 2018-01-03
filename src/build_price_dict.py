import numpy as np 
import pprint

from collections import defaultdict

"""
Constant strings used in the base-prices JSON files.
"""
PTYPE = 'product-type'
OPT = 'options'
BP = 'base-price'


class ProductInfo:
	""" 
	Stores array index information about each individual product.

	Attributes:
		option_dict: A defaultdict of dict that contains the array index of each option.
			Structure is dict['option-category']['option'] = (index, as int)
		optino_order: Dict using integers as keys (from 0, consecutive) that keeps track
			of the dimension order of each option for item.
			(For example, colour may be the array's 1st dimension, and size the second:
			order: access_array[colour_option][size_option]).
	"""

	def __init__(self):
		"""
		Initialize instance variables to default or empty values.
		"""
		self.option_dict = defaultdict(dict)
		self.option_order = {}


	def populate(self, product):
		"""
		Takes a product from the base-prices.json file and adds options not already
		in option_dict and/or option_order to the dict and/or order, assigning new 
		options index values in the process. (This does not overwrite already existing
		values).

		len() is used to get the next available index.

		Args:
			product: An indexed entry from the base-prices json file, containng
				new options to be added to this ProductInfo's attributes.
		"""

		# Iterate through all option_categories
		for option_category, options in product[OPT].items():
			# Iterate through all possible options
			for option in options:
				# Check to see if we need to add the current option (i.e,. 'white') 
				option_info = self.option_dict[option_category]
				if option in option_info:
					continue
				option_info[option] = len(option_info)

			# Check if the current option_category (i.e., 'size') is in the order dict.
			if option_category in self.option_order.values():
				continue
			self.option_order[len(self.option_order)] = option_category

	
	def get_tuple(self): 
		"""
		Constructs a tuple containing the number of each option, in option_category
		order. This tuple is used to specify the dimensions of a numpy array which will
		store all the individual price values of this Product.

		Returns:
			A tuple containing the number of options in their appearance order.	
		"""
		option_tuple = ()
		# Iterate through each option category and add the number of elements in it
		for index in range(len(self.option_order)): 
			curr_option = self.option_order[index]
			option_tuple += (len(self.option_dict[curr_option]),)
		return option_tuple


	"""
	def __repr__(self):
		return str(self.option_dict)

	def __str__(self):
		return str(self.option_dict)
	"""


class PriceDict:
	"""
	Class to store and lookup (in amortized constant time) prices from base-prices.

	Note: This class can accept multiple base-prices JSON objects, but build_lookup_array()
		must be called each time a new price JSON is added.

	Note: PriceDict currently accepts prices up to unsigned-int 32 (A maximum price of 4294967295).
		There is no support for negative prices.

	Attribute:
		price_array: numpy array storing prices for each price based on its option combinations.
		lookup_dict: dict of ProductInfo to store option access indices in price_array.
	"""

	def __init__(self):
		"""
		Initialize instance variables to default values.
		"""
		self.price_array = {} # Dict of numpy arrays containng the prices
		self.lookup_dict = defaultdict(ProductInfo) # Dict that contains info on each invvidual product


	def build_lookup_dict(self, pricejson):
		"""
		From the passed in base-prices JSON object, get all options, and then through populate(),
		assign them all array index values to be used in assignment and lookup in the price_array.

		Note: 
			Always call this before build_lookup_array!

		Params:
			pricejson: Base-prices json to pull options to assign array indices.
		"""
		for product in pricejson:
			product_info = self.lookup_dict[product[PTYPE]]
			product_info.populate(product)


	def build_lookup_array(self, pricejson):
		"""
		After calling build_lookup_dict, this function runs through the base-prices json and 
		generates numpy n-d arrays. A single array is assigned to each product-type, and the
		number of dimensions and their sizes are equal to the number of option-categories and 
		options themselves (i.e., category = size, option(s) = S, M, L.). This method then
		populates each combination provided in pricejson with the provided price.

		Note:
			This can be called multiple times, each time a new price JSON is added to the current
			PriceDict.

		Params:
			pricejson: JSON object to get all prices and options from.
		"""

		# Create a numpy-zero array for each product, assume prices can't be negative.
		for product, product_info in self.lookup_dict.items():
			# get_tuple provides array dimensions, initalize to 0 to prevent strange prices.
			product_tuple = self.lookup_dict[product].get_tuple()
			self.price_array[product] = np.zeros(product_tuple, dtype=np.uint32)

		# Update the price for every item in base-prices.json
		for product in pricejson:
			product_name = product[PTYPE]			
			product_options = self.lookup_dict[product_name].option_order
			product_dict = self.lookup_dict[product_name].option_dict

			# List to keep track of all indices we will be setting a price
			update_indices = []

			# We must iterate with both to ensure the option_order is respected
			for key, option_category in product_options.items():
				# Keep track of the indices of all presented options
				curr_indices = []
				# Go through each invidual option, and add its price_array index
				for option in product[OPT][option_category]:
					curr_indices.append(product_dict[option_category][option])
				# Append this list to the update_indices, for use by np.ix_
				update_indices.append(curr_indices)

			# Actual assignment done here: Assigns all combinations using ix_ to price
			self.price_array[product_name][np.ix_(*update_indices)] = product[BP]


	def add_base_price(self, pricejson):
		"""
		Helper function to take care of all PriceDict initialization; creates a lookup_dict
		and the lookup_array.

		Params:
			pricejson: A base-prices JSON object to build this PriceDict from.

		Note: This method, as implied by the name, can be used to add an additional 
			base-prices JSON object.
		"""
		self.build_lookup_dict(pricejson)
		self.build_lookup_array(pricejson)
