# Canvas file at top level to record and test random notes

import json
import os


BASE = {};
OPTION = {};

A = [1, 2, 3, 4, 5]

OPTION['first'] = A

A = [5, 6, 7, 8, 9, 10]

OPTION['second'] = A

BASE['first'] = OPTION

print(BASE['first']['first'][0])
print(BASE['first']['second'])


##

# How ew open JSON files
data =json.load(open('ref/base-prices/base-prices.json'))
print(os.path.abspath('ref/base-prices/base-prices.json'))