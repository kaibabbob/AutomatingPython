#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import re
import yaml
import json
from pprint import pprint as pp

print("its a start")

liste = [{"key1" : "value1" , "key2" : "value2"}, "cars", "planes", ["red", "blue", "green"]]

print(type(liste))

with open("config.yml","w") as f:
    f.write("---\n")
    f.write(yaml.dump(liste,default_flow_style=False))

with open("config.json", "w") as f:
    json.dump(liste,f)

with open("config.yml") as f:
    new_list = yaml.load(f)

pp(new_list)

print("-"*20)

with open("config.json") as f:
    new_list = json.load(f)

pp(new_list)
