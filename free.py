# Canvas file at top level to record and test random notes

import json
import os
import numpy as np
import pprint
#import collections

from src import get_json as GJ
from collections import defaultdict


BASE = {};
OPTION = {};

A = [1, 2, 3, 4, 5]

OPTION['first'] = A

A = [5, 6, 7, 8, 9, 10]

OPTION['second'] = A

BASE['first'] = OPTION

#print(BASE['first']['first'][0])
#print(BASE['first']['second'])


##

#main = GJ.get_JSON('ref/base-prices/base-prices-hoodie.json')
#print(main[1]['options']['size'][0])
#print(list(main[1]['options']))
#print(list(main[1]['options']) == list(main[1]['options']))
#for products in main:
#	print('{} - {}'.format(products['product-type'], products['base-price']))

"""
print(main)

print()
print(main[0]['options']['colour'])

print(type('5'))
print(type(5))
"""

a = np.array([1,2,3,4,5,6,7,8],dtype=np.int8)
a.reshape((4,2))
print(a)
