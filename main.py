# Python lib imports
import sys
import os

from argparse import ArgumentParser

# Self-defined imports
from src import calculate_price as CALC 
from src import get_json as GJ
from src import build_price_dict as BPD


def parse_args():
	"""
	Standard ArgumentParser module to accept command-line arguments 
	"""
	parser = ArgumentParser(description=__doc__)

	parser.add_argument('cart',
						help="""
						JSON file or URL containing the user's cart.
						""",
						type=str)

	parser.add_argument('base_prices',
						help="""
						JSON file or URL containing base prices.
						""",
						type=str)

	return parser.parse_args()


# Usage: calculate [flags] cart.json base-prices.json
def main():

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



	# This section does not need try/except, we need not test for conformity
	try:
		pricedict = BPD.PriceDict()
		pricedict.add_base_price(pricejson)
	except Exception as e:
		sys.exit("An error has occured while parsing the base-prices.")
	




# Define main() as our entrypoint
if __name__ == "__main__":
	main()