#!/usr/bin/env python3

import json

#dictionary
types = set()
subtypes = set()
types_list = []

with open("/u/rbrooks/cs373/type_names.txt", "r") as f:
	for type_name_string in f :
		temp = type_name_string.rstrip(' \n').lstrip(' ')
		typeList = temp.split(" — ")

		card_type = typeList[0]
		card_subtype = ''
		if len(typeList) > 1 :
			card_subtype = typeList[1]
			subtypes.add(card_subtype)


		types.add((card_type, "DESCRIPTION"))
		types_list.append((card_type, card_subtype))
		
"""
for a in subtypes:
	print("('" + a , end = "'),\n")
print(str(len(subtypes)))
print("\n\n\n\n\n")
"""


for a in types:
	print(a, end = ",\n")



"""
print("\n\n\n\n\n")
for a in types_list:
	print(a, end = ",\n")
print(str(len(types_list)))
"""


#print(json.dumps(magic_list_new))
