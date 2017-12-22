# Python lib imports
import sys
import os

from argparse import ArgumentParser

# Self-defined imports
from src import calculate_price as CALC 
from src import get_json as GJ



def get_JSON_path(jsonfile):
	"""
	Helper function to get the absolute path of a file
	"""
	#return os.path.abspath(jsonfile)
	try:
		return GJ.get_JSON(jsonfile)
	except:
		return "Caught!"



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


# TODO!
# Usage: calculate [flags] cart.json base-prices.json
def main():
	args = parse_args() # Get command line args




# Define main() as our entrypoint
if __name__ == "__main__":
	#main()