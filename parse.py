#!/usr/bin/env python

from __future__ import unicode_literals, print_function
import re
import yaml
import json
from pprint import pprint as pp
from ciscoconfparse import CiscoConfParse


# Excercise 8
print("\n\n ** Excercise 8 print crypto maps **")
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

for my_map in cisco_cfg.find_objects(r"^crypto map CRYPTO") :
    map_entries = my_map.all_children

    print("\n")
    pp(my_map.text)
    for statement in map_entries :
        pp(statement.text)

# Excercise 9
print("\n\n ** Excercise 9: show crypto Maps using PFS group2 **")

for my_map in cisco_cfg.find_objects_w_child(parentspec = r"^crypto map CRYPTO", childspec = r"pfs group2") :
    pp(my_map.text)

# Excercise 10
print("\n\n ** Excercise 10: show crypto maps not using AES based transform sets")

for transform in cisco_cfg.find_objects(r"set transform-set") :
	if not "AES" in transform.text :
		my_map = transform.parent
		print(my_map.text)
		print(transform.text)
        
