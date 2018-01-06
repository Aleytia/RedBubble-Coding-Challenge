# 2017 RedBubble Software Intern Coding Test
### **Requirements**

------

- Python >= 3.0.  The latest release as of writing can be found [here](https://www.python.org/downloads/release/python-364/).
  - This will NOT work with installations of Python < 3.0.
- Python's NumPy package.  If you are using pip, you can install it with `pip3 install numpy`.
  - Other numpy installation methods can be found [here](https://www.scipy.org/scipylib/download.html). 

### **How To Run**

------

Clone this repository using:

```
git clone https://github.com/reverie-lu/RedBubble-Coding-Challenge
```

Navigate to the directory, call your Python interpreter on `main.py`.  For many Unix-based environments, this will be `python3`. (Warning: `python` and `python3` are different!)

```
python3 main.py cart.json base-prices.json
```

- `cart.json`: A path or URL to a json file that contains the user's cart.
- `base-prices.json`: A path or URL to a json file that contains the base prices.

To run test files, call the interpreter from the root directory with the -m flag:

```
python3 -m test.filename
```

Note that *filename* should **NOT** contain the .py extension. 

### Structure

------

- The main executable for this file can be found at the root level as `main.py`.  
- All other modules used can be found in `/src`.  
- Example JSON cart and base-price files can be found in `/ref`.  Notes on sp
- Specific submodules can be found in `/doc`. 
- Unit tests can be found in `/test`. 

### **License**

------

This project is licensed under the MIT license.  A copy of the license may be found in this repository as LICENSE.  More information on this license can be found [here](https://opensource.org/licenses/MIT).

------

reverie-lu | [github.com/reverie-lu](https://github.com/reverie-lu) | This repository was made public after the deadline for the challenge.
