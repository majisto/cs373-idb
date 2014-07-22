#!usr/bin/env python3

from mtg_project.models import MagicCard, MagicSet, MagicType, MagicSubtype
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


cards_json =    BASE_DIR + "/mtg_project/cards_json.json"
sets_json =     BASE_DIR + "/mtg_project/sets_json.json"
type_json =     BASE_DIR + "/mtg_project/types_json.json"
subtype_json =  BASE_DIR + "/mtg_project/subtypes_json.json"
type_pairs =    BASE_DIR + "/mtg_project/types_subtypes.json"


def import_subtypes () :
    subtype_array = []
    with open(subtype_json, "r") as h :
        subtype_array = json.load(h)["Subtypes"]
    for subtype in subtype_array :
        s, created = MagicSubtype.objects.get_or_create(subtype_name = subtype)
        if created :
            s.save()


""" SUBTYPES MODEL

   subtype_name = models.CharField(max_length = 255,primary_key = True)
"""

def import_types () :
    types_array = []
    with open(type_json, "r") as h :
        types_array = json.load(h)["Types"]
    m_type_subtypes = {}
    with open(type_pairs, "r") as h :
        m_type_subtypes = json.load(h)

    for m_type in types_array :
        t, created = MagicType.objects.get_or_create(type_name = m_type[0], type_description = m_type[1])

        if created:
            t.save()

        if not t:
            print(m_type)

        if m_type[0] in m_type_subtypes and t is not None and t.type_subtypes.all().count():
            #t = MagicType.objects.get(type_name = m_type[0])
            for subtype in m_type_subtypes[m_type[0]] :
                t.type_subtypes.add(MagicSubtype.objects.get(subtype_name = subtype))
                t.save()


""" TYPES MODEL

	type_name = models.CharField(max_length = 255,primary_key = True)
    type_description = models.TextField()
    type_subtypes = models.ManyToManyField('MagicSubtype', related_name = 'magic_subtype_set', null = True)

"""


def import_sets () :
	sets_array = []
	with open(sets_json, "r") as h :
		sets_array = json.load(h)["Sets"]

	for m_set in sets_array :
		s, created = MagicSet.objects.get_or_create(set_ID = m_set[0],
		                            set_name = m_set[1],
		                            set_symbol = m_set[2],
		                            set_release_date = m_set[3])
		if created:
		    s.save()


"""  SETS MODEL

	set_ID = models.CharField(max_length =8,primary_key = True)
    set_name = models.CharField(max_length = 255)
    set_symbol =  models.CharField(max_length = 255)
    set_release_date = models.CharField('date released', max_length = 255) # mm/yyyy
    """



def import_cards () :

    cards_array = []
    with open(cards_json, "r") as h :
        cards_array = json.load(h)["Cards"]

    for card in cards_array:

        s = MagicSet.objects.get(set_ID = card[2])
        t = MagicType.objects.get(type_name = card[3])


        su = None
        if len(card[4]):
            su = MagicSubtype.objects.get(subtype_name = card[4])

        loy = None
        if len(str(card[7])):
            loy = card[7]

        c, created = MagicCard.objects.get_or_create(card_ID = card[0],
                                    card_name = card[1],
                                    card_setID = s,
                                    card_type = t,
                                    card_subtype = su,
                                    card_mana_cost = card[5],
                                    card_converted_cost = card[6],
                                    card_loyalty = loy,
                                    card_rarity = card[8],
                                    card_text = card[9],
                                    card_flavor_text = card[10],
                                    card_power = card[11],
                                    card_toughness = card[12],
                                    card_price = card[13]
                                    )
        if created:
            c.save()

		# I saved at the end

    """
    card_ID = models.IntegerField(primary_key = True)
    card_name = models.CharField(max_length = 255)
    card_setID = models.ForeignKey('MagicSet', related_name = 'magic_cards_set')  #'Model' in single quotes if not yet been defined
    card_type = models.ForeignKey('MagicType', related_name = 'magic_cards_set')
    card_subtype = models.ForeignKey('MagicSubtype', related_name = 'magic_cards_set')
    card_mana_cost = models.CharField(max_length = 255)
    card_converted_cost = models.SmallIntegerField()
    card_loyalty = models.SmallIntegerField(null = True)
    card_rarity = models.CharField(max_length = 255)
    card_text = models.TextField()
    card_flavor_text = models.TextField()
    card_power = models.FloatField()
    card_toughness = models.FloatField()
    card_price = models.FloatField()
    """


def run_imports () :
    #order is important
    #subtype before type
    #sets before cards
    #everything before cards

	import_subtypes()
	import_types()
	import_sets()
	import_cards()

	print("Done")

"""
MagicCard.objects.all().delete()
MagicSet.objects.all().delete()
MagicType.objects.all().delete()
MagicSubtype.objects.all().delete()
"""

run_imports()
