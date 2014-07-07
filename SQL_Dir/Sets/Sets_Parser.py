#!/usr/bin/env python3

import json

#dictionary
magic_list_old = []
magic_list_new = []

with open("/u/rbrooks/cs373/sets_old.json", "r") as f:
	magic_list_old = json.load(f)["sets"]

for magic_set in magic_list_old :
	set_ID = magic_set[1]
	set_name = magic_set [0]
	set_symbol =  "NULL"
	set_release = magic_set[3]
	parse_tuple = (set_ID, set_name, set_symbol, set_release)
	print(str(type(parse_tuple)))
	magic_list_new.append(parse_tuple)

print(magic_list_new)
#print(json.dumps(magic_list_new))
