"""
calculate_price.py goes through the provided cart file, and with a PriceDict, 
gets the total price of all items in the cart. Accounts for markup and quantity.

This file uses Google's Python style guide:
https://google.github.io/styleguide/pyguide.html
"""

# No imports are needed

# Constants used in JSON files.
PTYPE = 'product-type' 
OPT = 'options'
MKUP = 'artist-markup'
QT = 'quantity'

def calculate(cartjson, pricedict):
	"""
	Calculate takes a cart JSON object and a pricedict and returns
	the total price, accounting for markup and quantity.

	Args:
		cartjson: A JSON object containing a user's cart.
		pricedict: A pridedict object. Contains price retrieval information.

	Note: Make sure pricedict's add_base_price() is called at least once
		before calling calculate()

	Returns: Total price of all items in the cart.
	"""

	total_price = 0

	price_lookup = pricedict.lookup_dict 
	price_array = pricedict.price_array	

	# Iterate through each item present in the cart
	for item in cartjson:

		item_name = item[PTYPE]

		# Use a tuple to generate in-order indices of options, from the dict.
		lookup_indices = ()

		option_order = price_lookup[item_name].option_order
		option_lookup = price_lookup[item_name].option_dict

		# Iterate through each option in order
		for option_category in option_order.values():
			item_option = item[OPT][option_category]
			# Get the index of said option and append it to the tuple
			lookup_indices += (pricedict.get_index( item_name, 
													option_category, 
													item_option), )

		# Formula: base_price + round(base_price * markup) * quantity 
		# Round down the prices in cents after markup percentage calculation.
		item_base_price = pricedict.get_price(item_name, lookup_indices)
		item_markup = int((item_base_price * item[MKUP])/100)
		item_price = (item_base_price + item_markup) * item[QT]

		total_price += item_price

	return total_price