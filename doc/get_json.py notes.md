### **get_json.py notes:**

---

Our get_json.py throws a general exception to keep the control flow clean, allowing only main.py to call sys.exit() commands. However, in actual usage, if we were to only load a local JSON file, we could do something like this instead:

```python
import json

def load_local_JSON(jsonfile, jsontype):
	'''
	jsonfile: Reference to a json object to load.
	jsontype: Either 'cart.json' or 'base-prices.json'
	'''
	try:
		json.load(open(jsonfile))
		return jsonfile 
	except ValueError as e:
		print('Invalid %s file "%s": %s.' % (jsontype, jsonfile, e))
		print('Please try again with a valid JSON file.')
	except FileNotFoundError:
		print('Invalid %s file "%s": No such file exists.' 
				% (jsontype, jsonfile))
```

Notice that local files use `json.load` , which differs from loading from URL, which we will see below.

There are two possible errors: 

- ValueError: A bad file was passed to the method (some 'bad value').
- FileNotFoundError: As the name implies, a file does not exist.

------

Loading from a URL is slightly different. We must first account that the running computer can establish a connection with the API server, and then load the JSON from the web.

```python
import json
from urllib.request import urlopen, URLError, HTTPError

def validate_HTTP_JSON(url, jsontype):
	with has_internet(url) as link:
		try:
			return json.loads(link.read().decode())
		except ValueError as e:
			print('Invalid %s url "%s".' % (jsontype, url))
			print('Please try again with a JSON URL.')
		except Exception:
			print('Error with your URL %s.' % url)
			print('Please check your input and try again.')

        
def has_internet(url):
  	try:
		return urlopen(url, timeout=5)
	except HTTPError as h:
		print('Invalid URL %s: HTTP Error %s thrown.' % (url, h.code)) 
		print('Please verify you have a working URL')
	except URLError as e:
		print('Bad URL "%s". (Error: %s)' % (url, e.reason))
		print('Please check your URL and try again!')
```

We define has_internet as a helper function that checks if a connection can be made, and if so, returns a urlopen object from that link, which will then be decoded in validate_HTTP_JSON. Otherwise, the methods are generally the same. Notice that from a URL, you should use `json.loads()` , which is different than `json.load()`.  



