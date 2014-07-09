#!/usr/bin/env python3

import json
import re

#dictionary
card_list_new = []
set_type = []


def power_tough(blah) :
	value = 0
	try :
		value = float(blah)
	except ValueError:
		if "*" in blah :
			value = -1
			if len(blah) > 1 and "^" not in blah:
				value -= int(blah[0])
		elif len(blah):
			value = int(blah[0]) + int(blah[2]) / int(blah[4]) 
	return value

with open("/u/rbrooks/cs373/ass3_idb/cs373-idb/SQL_Dir/Cards/cards_old.txt", "r") as f:
	for magic_card_string in  f:
		temp = magic_card_string.rstrip(',\n')
		temp = temp.replace("NULL", "''")
		temp = temp[2:]
		magic_card = temp.split("','")

		card_ID = int(magic_card[0])
		card_name = magic_card[1]
		card_setID =  magic_card[2]
		    
		typeList =  magic_card[3].split(" — ")
		card_type = typeList[0]
		card_subtype = ''
		if len(typeList)  > 1 :
			card_subtype = typeList[1]

		card_mana_cost = magic_card[5]

		try:
			card_converted_cost = int(magic_card[6])
		except ValueError:
			continue

		card_loyalty = "<<_NULL_>>"
		try:
			card_loyalty = int(magic_card[9])
		except ValueError:
			pass

		card_rarity = magic_card[4]
		card_text = magic_card[10]
		card_flavor_text = magic_card[11]

		card_power = power_tough(magic_card[7])
		
		card_toughness = power_tough(magic_card[8])

		card_price = 0
		try: 
			card_price = float(magic_card[20])
		except ValueError:
			pass

		parse_tuple = (card_ID, card_name, card_setID, card_type, card_subtype, card_mana_cost, card_converted_cost, card_loyalty, card_rarity, card_text, card_flavor_text, card_power, card_toughness, card_price)

		card_list_new.append(parse_tuple)
		if card_setID == 'UNH' :
			set_type.append(card_ID)


for card in card_list_new :
	print(card, end = ",\n")

#print(set_type)
#print(str(len(set_type)))

