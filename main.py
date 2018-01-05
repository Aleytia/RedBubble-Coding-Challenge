"""
main.py runs the entire price calculator. It accepts the json files or URL,
converts them into readable JSON objects, creates a PriceDict to get prices
in amortized constant time, then calculates the price. main.py also handles
command-line argument processing and error handling.

This file uses Google's Python style guide:
https://google.github.io/styleguide/pyguide.html
"""

import sys
import os

from argparse import ArgumentParser

from src import calculate_price as CALC 
from src import get_json as GJ
from src import build_price_dict as BPD


def parse_args():
	"""
	Standard ArgumentParser module to accept command-line arguments.

	Returns an ArgumentParser, read in main(). 
	"""
	parser = ArgumentParser(description=__doc__)

	# Path to the cart
	parser.add_argument('cart',
						help="""
						JSON file or URL containing the user's cart.
						""",
						type=str)

	# Path to the base-prices
	parser.add_argument('base_prices',
						help="""
						JSON file or URL containing base prices.
						""",
						type=str)

	return parser.parse_args()


def main():
	"""
	Main function. Gets JSON objects from args, creates a PriceDict, and then
	calculates the price.

	ArgumentParser Usage:
		python3 main.py cart.json base-prices.json

	Args:
		cart.json - Directive to a JSON-formatted cart file/URL
		base-prices.json - Directive to a JSON-formatted base-prices file/URL

	Returns: 
		Exit code 0 on successful completion.
		Exit code 1 on error handling.

	"""
	# 1: Parse command-line arguments
	args = parse_args() # Get command line args


	# 2: Get JSOn files/urls into JSON objects
	# Get cart into a JSON object
	try:
		cartjson = GJ.get_JSON(args.cart)
	except Exception as e:
		# If an exception is thrown, let's also check prices so the user will
		# know if only the cart or both cart and prices are malformed
		try:
			GJ.get_JSON(args.base_prices)
		except Exception as e:
			print()
			print(str(e) % 'cart')
			sys.exit(str(e) % 'base prices')

		print()
		sys.exit(str(e) % 'cart')

	# Get base-prices into a JSON object
	try:
		pricejson = GJ.get_JSON(args.base_prices)
	except Exception as e:
		print()
		sys.exit(str(e) % 'base prices')


	"""
	Instantiate a PriceDict object, and load the prices into it.

	Note: We are guaranteed that the files will work here, so there is no
	need to do error checking. We only need to catch any error and exit.
	"""
	try:
		pricedict = BPD.PriceDict()
		pricedict.add_base_price(pricejson)
	except Exception as e:
		sys.exit("An error has occured while parsing the base-prices.")
	

	"""
	We are also guaranteed here that all provided cart files conform and won't
	have errors we must catch. As a precaution, we will catch any Exception
	and exit in that case.
	"""
	try:
		total_cost = CALC.calculate(cartjson, pricedict)
	except Exception as e:
		sys.exit("An error has occured while calculating the total price.")

	# Print the total cost
	print(total_cost)

	sys.exit(0)


# Define main() as our entrypoint
if __name__ == "__main__":
	main()