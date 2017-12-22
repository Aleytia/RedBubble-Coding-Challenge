"""
get_json.py attempts to take a directive to a JSON object and return a
JSON object from it. It first tries to load the directive as a local file,
and then attempts to load it as a URL. If both fail, it will raise an error.

!!  get_json does NOT make sure the json is malformed (for example, if the json
object is actually a completely unrelated json file). It only loads JSON
and returns a JSON object for the program to use.

This file uses Google's Python style guide:
https://google.github.io/styleguide/pyguide.html
"""

# TODO: REWRITE URL TO BE IN HTTPS FORM

import json
import os
import sys

from urllib.request import urlopen
from urllib.parse import urlparse


def get_JSON(jsonobject):
	"""
	get_JSON() attempts to load a reference to a JSON object and then return
	it as a json object. It will try to load as a local file, and then a URL,
	in that order. If both fail, then it raises a ValueError exception.

	Args:
		jsonobject: Reference to a json file or URL.

	Returns: Python-parseable JSON object from the passed in reference.

	Raises:
		ValueError: If jsonobject fails to load as a file or URL. 

	"""
	try:
		# Attempt to load jsonobject as a local file
		return json.load(open(os.path.abspath(jsonobject)))
	except:
		# attempt to load jsonobject as a URL
		with has_internet(jsonobject) as url:
			try:
				return json.loads(url.read().decode())
			except:
				# Either a bad file or URL, raise ValuError exception
				 raise ValueError("An invalid json file or URL was provided")



def has_internet(url):
	"""
	Verifies that the system this script is running on can access the provided
	URL. If it fails, then we raise an error.

	Args:
		url: The URL to check if a connection can be established with.
		jsontype: Either cart.json or base-prices.json

	Returns: A urlopen() object, to be read in validate_HTTP_JSON()

	Raises:
		ValueError: If provided URL is invalid. This may also be a bad file.
	"""

	# Add scheme to url if it is missing one
	if not urlparse(url).scheme:
		url = "http://" + url

	try:
		return urlopen(url, timeout=5)
	except:
		raise ValueError("An invalid json file or URL was provided")



# Define get_JSON to be entry point if this file is used sstandalone
if __name__ == "__main__":
	try:
		print(get_JSON('YOUR QUERY HERE'))
	except ValueError:
		print("Caught!")
