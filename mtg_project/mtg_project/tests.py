from mtg_project.models import *
from mtg_project.api    import *
from mtg_project.views  import MagicSearchView

from django.test import TestCase
from django.http import HttpRequest
from django.core.management import call_command
from django.test.utils import override_settings

import os
import json
import shlex

from haystack.backends import SQ

from json import loads

try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

import haystack
from haystack.query import SearchQuerySet, AutoQuery

class MTG_TEST(TestCase) :

    """
    Manually setup a database
    """
    def db_setup(self) :
        subtype_dict = {"subtype_name" : 'Beast'}
        subtype_object1 = MagicSubtype.objects.create(**subtype_dict)

        subtype_dict = {"subtype_name" : 'Hound Construct'}
        subtype_object2 = MagicSubtype.objects.create(**subtype_dict)
        subtype_dict = {"subtype_name" : 'Angel'}
        subtype_object3 = MagicSubtype.objects.create(**subtype_dict)

        type_dict = {"type_name" : 'Enchant Creature',
            "type_description" : 'Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.'}
        type_object = MagicType.objects.create(**type_dict)

        type_object.type_subtypes.add(subtype_object1)
        type_object.type_subtypes.add(subtype_object2)
        type_object.type_subtypes.add(subtype_object3)

        type_dict = {"type_name" : 'Interrupts',
            "type_description" : 'Interrupt is an obsolete card type. It has not been supported by the game since Sixth Edition. Under the original rules, an interrupt was a spell that would resolve before the rest of the Batch. Some examples of interrupts include Counterspell, Red Elemental Blast and Dark Ritual. All Interrupt cards have received errata to make them instants, and all references to Interrupts have been given errata to reference instants.'}
        MagicType.objects.create(**type_dict)

        type_dict = {"type_name" : 'Basic Land',
            "type_description" : 'These lands are unlike nonbasic lands in that any number may be included in a deck. There are basic lands for each color — Plains, Island, Swamp, Mountain, and Forest for white, blue, black, red, and green, respectively. Each basic land has the basic land type of the same name; e.g., Plains have the Plains land type. Basic lands are thought of as the cornerstones of Magic design, and no lands should be printed if they are strictly better than basic lands, with the sole exception to this rule being the dual lands from Alpha/Beta/Unlimited/Revised. Consequently, other, nonbasic lands feature drawbacks, in addition to the fact that no more than four copies of nonbasic lands may be played in a deck.'}
        MagicType.objects.create(**type_dict)

        set_dict = {"set_ID" : 'BNG',
                 "set_name" : 'Born of the Gods',
                 "set_release_date" :'2014-02-07',
                 "set_num_cards" : 165}
        MagicSet.objects.create(**set_dict)

        set_dict = {"set_ID" : 'UNH',
            "set_name" : 'Unhinged',
            "set_release_date" : '2004-11-20',
            "set_num_cards" : 140}

        MagicSet.objects.create(**set_dict)

        set_object = MagicSet.objects.get(set_ID = 'BNG')
        type_object = MagicType.objects.get(type_name = 'Enchant Creature')
        subtype_object = MagicSubtype.objects.get(subtype_name = 'Beast')


        card_dict = {"card_ID" : 378490,
            "card_name" : 'Charging Badger',
            "card_setID" : set_object,
            "card_type" : type_object,
            "card_subtype" : subtype_object,
            "card_mana_cost" : '{G}',
            "card_converted_cost" : 1,
            "card_loyalty" : None,
            "card_rarity" : 'C',
            "card_text" : 'Trample',
            "card_flavor_text" : "If the hierarchies of nature were determined by ferocity alone, the badger would be lord of the beasts. --Anthousa of Setessa",
            "card_power" : 1.0,
            "card_toughness" : 1.0,
            "card_price" : 0.14}

        MagicCard.objects.create(**card_dict)

        card_dict = {"card_ID" : 373500,
            "card_name" : 'Ashiok, Nightmare Weaver',
            "card_setID" : set_object,
            "card_type" : type_object,
            "card_subtype" : subtype_object,
            "card_mana_cost" : '{1}{U}{B}',
            "card_converted_cost" : 3,
            "card_loyalty" : 3,
            "card_rarity" : 'M',
            "card_text" : "+2: Exile the top three cards of target opponents library. -X: Put a creature card with converted mana cost X exiled with Ashiok, Nightmare Weaver onto the battlefield under your control. That creature is a Nightmare in addition to its other types. -10: Exile all cards from all opponents hands and graveyards.",
            "card_flavor_text" : '',
            "card_power" : 0,
            "card_toughness" : 0,
            "card_price" : 8.14}

        MagicCard.objects.create(**card_dict)

        card_dict = {"card_ID" : 136142,
            "card_name" : 'Tarmogoyf',
            "card_setID" : set_object,
            "card_type" : type_object,
            "card_subtype" : subtype_object,
            "card_mana_cost" : '{1}{G}',
            "card_converted_cost" : 2,
            "card_loyalty" : None,
            "card_rarity" : 'R',
            "card_text" : "Tarmogoyfs power is equal to the number of card types among cards in all graveyards and its toughness is equal to that number plus 1.",
            "card_flavor_text" : '',
            "card_power" : -1,
            "card_toughness" : -2,
            "card_price" : 190.38}

        MagicCard.objects.create(**card_dict)

    """
    Tests for MagicCard class
    """

    def test_MagicCard_1(self) :

        self.db_setup()
        card_object = MagicCard.objects.get(card_ID = 378490)

        self.assertEqual(card_object.card_ID, 378490)
        self.assertEqual(card_object.card_name, 'Charging Badger')
        self.assertEqual(card_object.card_setID.__str__(), 'Born of the Gods')
        self.assertEqual(card_object.card_type.__str__(), 'Enchant Creature')

    def test_MagicCard_2(self) :
        self.db_setup()
        card_object = MagicCard.objects.get(card_ID = 373500)

        self.assertEqual(card_object.card_ID, 373500)
        self.assertEqual(card_object.card_mana_cost, '{1}{U}{B}')
        self.assertEqual(card_object.card_flavor_text, '')
        self.assertEqual(card_object.card_loyalty, 3)

    def test_MagicCard_3(self) :
        self.db_setup()
        card_object = MagicCard.objects.get(card_ID = 136142)

        self.assertEqual(card_object.card_text, "Tarmogoyfs power is equal to the number of card types among cards in all graveyards and its toughness is equal to that number plus 1.")
        self.assertEqual(card_object.card_power, -1)
        self.assertEqual(card_object.card_toughness, -2)
        self.assertEqual(card_object.card_price, 190.38)

    """
    Tests for MagicSet class
    """

    def test_MagicSet_1(self) :
        self.db_setup()
        set_object = MagicSet.objects.get(set_ID = 'BNG')

        self.assertEqual(set_object.set_ID, 'BNG')

    def test_MagicSet_2(self) :
        self.db_setup()
        set_object = MagicSet.objects.get(set_ID = 'BNG')

        self.assertEqual(set_object.set_name, 'Born of the Gods')
        self.assertEqual(set_object.set_num_cards, 165)

    def test_MagicSet_3(self) :
        self.db_setup()
        set_object = MagicSet.objects.get(set_ID = 'UNH')

        self.assertEqual(set_object.set_name, 'Unhinged')
        self.assertEqual(set_object.set_release_date, '2004-11-20')

    """
    Tests for MagicType class
    """

    def test_MagicType_1(self) :
        self.db_setup()
        type_object = MagicType.objects.get(type_name = 'Enchant Creature')

        self.assertEqual(type_object.type_name, 'Enchant Creature')
        self.assertEqual(type_object.type_description, 'Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.')

        subtypes_names = [x.__str__() for x in type_object.type_subtypes.all()]

        self.assertEqual(set(subtypes_names), {'Beast', 'Hound Construct', 'Angel'})


    def test_MagicType_2(self) :
        self.db_setup()
        type_object = MagicType.objects.get(type_name = 'Interrupts')

        self.assertEqual(type_object.type_name, 'Interrupts')
        self.assertEqual(type_object.type_description, 'Interrupt is an obsolete card type. It has not been supported by the game since Sixth Edition. Under the original rules, an interrupt was a spell that would resolve before the rest of the Batch. Some examples of interrupts include Counterspell, Red Elemental Blast and Dark Ritual. All Interrupt cards have received errata to make them instants, and all references to Interrupts have been given errata to reference instants.')


    def test_MagicType_3(self) :
        self.db_setup()
        type_object = MagicType.objects.get(type_name = "Basic Land")

        self.assertEqual(type_object.type_name, 'Basic Land')
        self.assertEqual(type_object.type_description, 'These lands are unlike nonbasic lands in that any number may be included in a deck. There are basic lands for each color — Plains, Island, Swamp, Mountain, and Forest for white, blue, black, red, and green, respectively. Each basic land has the basic land type of the same name; e.g., Plains have the Plains land type. Basic lands are thought of as the cornerstones of Magic design, and no lands should be printed if they are strictly better than basic lands, with the sole exception to this rule being the dual lands from Alpha/Beta/Unlimited/Revised. Consequently, other, nonbasic lands feature drawbacks, in addition to the fact that no more than four copies of nonbasic lands may be played in a deck.')

    """
    Tests for MagicSubtype class
    """

    def test_MagicSubtype_1(self) :
        self.db_setup()
        subtype_object = MagicSubtype.objects.get(subtype_name = "Beast")

        self.assertEqual(subtype_object.subtype_name, 'Beast')

    def test_MagicSubtype_2(self) :
        self.db_setup()
        subtype_object = MagicSubtype.objects.get(subtype_name = "Hound Construct")

        self.assertEqual(subtype_object.subtype_name, 'Hound Construct')

    def test_MagicSubtype_3(self) :
        self.db_setup()
        subtype_object = MagicSubtype.objects.get(subtype_name = "Angel")

        self.assertEqual(subtype_object.subtype_name, 'Angel')


    """
    Tests for magic_sets_all
    """
    def test_magic_sets_all_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        sets_response = magic_sets_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(sets_response)

        self.assertTrue("objects" in r_dict)

    def test_magic_sets_all_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        sets_response = magic_sets_all(r, indent = None)
        objs = jsonLoadsFromResponse(sets_response)["objects"]

        self.assertTrue(len(objs))
        f_obj = objs[0]

        self.assertTrue("set_ID" in f_obj)
        self.assertTrue("set_name" in f_obj)
        self.assertTrue("set_release_date" in f_obj)

    def test_magic_sets_all_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        sets_response = magic_sets_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(sets_response)

        self.assertTrue("meta" in r_dict)


    """
    Tests for magic_set_id
    """
    def test_magic_set_id_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        set_response = magic_set_id(r,"UNH", indent = None)

        r_dict = jsonLoadsFromResponse(set_response)

        self.assertTrue("set_ID" in r_dict)
        self.assertTrue("set_name" in r_dict)
        self.assertTrue("set_release_date" in r_dict)
        self.assertTrue("set_num_cards" in r_dict)
        self.assertTrue("set_cards" in r_dict)

    def test_magic_set_id_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        set_response = magic_set_id(r,"UNH", indent = None)

        r_dict = jsonLoadsFromResponse(set_response)

        self.assertEqual(r_dict["set_ID"], "UNH")
        self.assertEqual(r_dict["set_name"], "Unhinged")
        self.assertEqual(r_dict["set_num_cards"],  140)

    def test_magic_set_id_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        set_response = magic_set_id(r,"BNG", indent = None)

        r_dict = jsonLoadsFromResponse(set_response)

        self.assertEqual(r_dict["set_release_date"], "2014-02-07")
        self.assertEqual(r_dict["set_cards"], [378490, 373500, 136142])

    """
    Tests for magic_types_all
    """

    def test_magic_types_all_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        types_response = magic_types_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(types_response)

        self.assertTrue("objects" in r_dict)

    def test_magic_types_all_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        types_response = magic_types_all(r, indent = None)
        objs = jsonLoadsFromResponse(types_response)["objects"]

        self.assertTrue(len(objs))
        f_obj = objs[0]

        self.assertTrue("type_description" in f_obj)
        self.assertTrue("type_name" in f_obj)

    def test_magic_types_all_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        types_response = magic_types_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(types_response)

        self.assertTrue("meta" in r_dict)


    """
    Tests for magic_type_name
    """
    def test_magic_type_name_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        type_response = magic_type_name(r,"Enchant Creature", indent = None)

        r_dict = jsonLoadsFromResponse(type_response)

        self.assertTrue("type_name" in r_dict)
        self.assertTrue("type_description" in r_dict)
        self.assertTrue("type_subtypes" in r_dict)

    def test_magic_type_name_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        type_response = magic_type_name(r,"Enchant Creature", indent = None)

        r_dict = jsonLoadsFromResponse(type_response)

        self.assertEqual(r_dict["type_name"], "Enchant Creature")
        self.assertEqual(r_dict["type_description"], "Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.")
        self.assertEqual(r_dict["type_subtypes"],  ['Beast', 'Hound Construct', 'Angel'])

    def test_magic_type_name_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        type_response = magic_type_name(r,"Interrupts", indent = None)

        r_dict = jsonLoadsFromResponse(type_response)

        self.assertEqual(r_dict["type_name"], "Interrupts")
        self.assertEqual(r_dict["type_description"], "Interrupt is an obsolete card type. It has not been supported by the game since Sixth Edition. Under the original rules, an interrupt was a spell that would resolve before the rest of the Batch. Some examples of interrupts include Counterspell, Red Elemental Blast and Dark Ritual. All Interrupt cards have received errata to make them instants, and all references to Interrupts have been given errata to reference instants.")
        self.assertEqual(r_dict["type_subtypes"],  [])


    """
    Tests for magic_subtypes_all
    """

    def test_magic_subtypes_all_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        subtypes_response = magic_subtypes_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(subtypes_response)

        self.assertTrue("objects" in r_dict)

    def test_magic_subtypes_all_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        subtypes_response = magic_subtypes_all(r, indent = None)
        objs = jsonLoadsFromResponse(subtypes_response)["objects"]

        self.assertTrue(len(objs))
        f_obj = objs[0]

        self.assertTrue("subtype_name" in f_obj)

    def test_magic_subtypes_all_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        subtypes_response = magic_subtypes_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(subtypes_response)

        self.assertTrue("meta" in r_dict)


    """
    Tests for magic_subtypes_name
    """
    def test_magic_subtype_name_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        subtype_response = magic_subtype_name(r,"Beast", indent = None)

        r_dict = jsonLoadsFromResponse(subtype_response)

        self.assertTrue("subtype_name" in r_dict)
        self.assertTrue("subtype_supertypes" in r_dict)

    def test_magic_subtype_name_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        subtype_response = magic_subtype_name(r,"Beast", indent = None)

        r_dict = jsonLoadsFromResponse(subtype_response)

        self.assertEqual(r_dict["subtype_name"], "Beast")
        self.assertEqual(r_dict["subtype_supertypes"], ["Enchant Creature"])

    def test_magic_subtype_name_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        subtype_response = magic_subtype_name(r,"Angel", indent = None)

        r_dict = jsonLoadsFromResponse(subtype_response)

        self.assertEqual(r_dict["subtype_name"], "Angel")
        self.assertEqual(r_dict["subtype_supertypes"],  ["Enchant Creature"])



    """
    Tests for magic_cards_all
    """

    def test_magic_cards_all_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        cards_response = magic_cards_all(r, indent = None)

        r_dict = jsonLoadsFromResponse(cards_response)

        self.assertTrue("objects" in r_dict)

    def test_magic_cards_all_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        cards_response = magic_cards_all(r, indent = None)
        objs = jsonLoadsFromResponse(cards_response)["objects"]

        self.assertTrue(len(objs))
        f_obj = objs[0]

        self.assertTrue("card_name" in f_obj)
        self.assertTrue("card_setID" in f_obj)
        self.assertTrue("card_type" in f_obj)
        self.assertTrue("card_subtype" in f_obj)
        self.assertTrue("card_mana_cost" in f_obj)
        self.assertTrue("card_converted_cost" in f_obj)
        self.assertTrue("card_loyalty" in f_obj)
        self.assertTrue("card_rarity" in f_obj)
        self.assertTrue("card_text" in f_obj)
        self.assertTrue("card_flavor_text" in f_obj)
        self.assertTrue("card_power" in f_obj)
        self.assertTrue("card_toughness" in f_obj)
        self.assertTrue("card_price" in f_obj)

    def test_magic_cards_all_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        cards_response = magic_cards_all(r, indent = None)
        r_dict = jsonLoadsFromResponse(cards_response)

        self.assertTrue("meta" in r_dict)


    """
    Tests for magic_card_id
    """
    def test_magic_card_id_1(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        card_response = magic_card_id(r,378490, indent = None)

        r_dict = jsonLoadsFromResponse(card_response)

        self.assertTrue("card_name" in r_dict)
        self.assertTrue("card_setID" in r_dict)
        self.assertTrue("card_type" in r_dict)
        self.assertTrue("card_subtype" in r_dict)
        self.assertTrue("card_mana_cost" in r_dict)
        self.assertTrue("card_converted_cost" in r_dict)
        self.assertTrue("card_loyalty" in r_dict)
        self.assertTrue("card_rarity" in r_dict)
        self.assertTrue("card_text" in r_dict)
        self.assertTrue("card_flavor_text" in r_dict)
        self.assertTrue("card_power" in r_dict)
        self.assertTrue("card_toughness" in r_dict)
        self.assertTrue("card_price" in r_dict)

    def test_magic_card_id_2(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        card_response = magic_card_id(r,378490, indent = None)

        r_dict = jsonLoadsFromResponse(card_response)

        self.assertEqual(r_dict["card_name"], "Charging Badger")
        self.assertEqual(r_dict["card_setID"], 'BNG')
        self.assertEqual(r_dict["card_type"], 'Enchant Creature')
        self.assertEqual(r_dict["card_subtype"], 'Beast')
        self.assertEqual(r_dict["card_mana_cost"], '{G}')
        self.assertEqual(r_dict["card_converted_cost"], 1)

    def test_magic_card_id_3(self):
        self.db_setup()
        r = HttpRequest()
        r.method = 'GET'
        card_response = magic_card_id(r,378490, indent = None)

        r_dict = jsonLoadsFromResponse(card_response)

        self.assertEqual(r_dict["card_loyalty"] , None)
        self.assertEqual(r_dict["card_rarity"] , "C")
        self.assertEqual(r_dict["card_text"] , "Trample")
        self.assertEqual(r_dict["card_flavor_text"] , "If the hierarchies of nature were determined by ferocity alone, the badger would be lord of the beasts. --Anthousa of Setessa")
        self.assertEqual(r_dict["card_power"] , 1.0)
        self.assertEqual(r_dict["card_toughness"] , 1.0)
        self.assertEqual(r_dict["card_price"] , 0.14)

"""
API self Test
"""

class APItests (TestCase) :
    url = "http://ni42.pythonanywhere.com/"

    def test_get_all_cards(self) :
        request = Request(self.url+"cards.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        with open("mtg_project/all_card.json") as data_file :
            expected_response = json.load(data_file)

        for obj in response_objects:
            self.assertTrue(obj in expected_response)

    def test_get_card_1(self) :
        expected_response = {
            "card_ID": 378516,
            "card_converted_cost": 5,
            "card_flavor_text": "",
            "card_loyalty": None,
            "card_mana_cost": "{W}{U}{B}{R}{G}",
            "card_name": "Chromanticore",
            "card_power": 4.0,
            "card_price": 1.69,
            "card_rarity": "M",
            "card_setID": "BNG",
            "card_setID_id": 1,
            "card_subtype": "Manticore",
            "card_subtype_id": 199,
            "card_text": "Bestow {2}{W}{U}{B}{R}{G} (If you cast this card for its bestow cost, its an Aura spell with enchant creature. It becomes a creature again if its not attached to a creature.) Flying, first strike, vigilance, trample, lifelink Enchanted creature gets +4/+4 and has flying, first strike, vigilance, trample, and lifelink.",
            "card_toughness": 4.0,
            "card_type": "Enchantment Creature",
            "card_type_id": 4
            }

        request = Request(self.url+"cards/378516.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        self.assertEqual(expected_response, response_data)

    def test_get_card_2(self) :
        expected_response = {
            "card_ID": 378515,
            "card_converted_cost": 2,
            "card_flavor_text": "Thaumaturges of Theros have learned to weave their magic into the world around them, but it can be pulled apart strand by strand.",
            "card_loyalty": None,
            "card_mana_cost": "{1}{G}",
            "card_name": "Unravel the Aether",
            "card_power": 0.0,
            "card_price": 0.26,
            "card_rarity": "U",
            "card_setID": "BNG",
            "card_setID_id": 1,
            "card_subtype": None,
            "card_subtype_id": None,
            "card_text": "Choose target artifact or enchantment. Its owner shuffles it into his or her library.",
            "card_toughness": 0.0,
            "card_type": "Instant",
            "card_type_id": 6
            }

        request = Request(self.url+"cards/378515.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        self.assertEqual(expected_response, response_data)

    def test_get_card_3(self) :
        expected_response = {
            "card_ID": 378525,
            "card_converted_cost": 3,
            "card_flavor_text": "",
            "card_loyalty": None,
            "card_mana_cost": "{1}{B}{R}",
            "card_name": "Ragemonger",
            "card_power": 2.0,
            "card_price": 0.37,
            "card_rarity": "U",
            "card_setID": "BNG",
            "card_setID_id": 1,
            "card_subtype": "Minotaur Shaman",
            "card_subtype_id": 87,
            "card_text": "Minotaur spells you cast cost {B}{R} less to cast. This effect reduces only the amount of colored mana you pay. (For example, if you cast a Minotaur spell with mana cost {2}{R}, it costs {2} to cast.)",
            "card_toughness": 3.0,
            "card_type": "Creature",
            "card_type_id": 13
            }

        request = Request(self.url+"cards/378525.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        self.assertEqual(expected_response, response_data)

    def test_get_all_sets(self) :
        request = Request(self.url+"sets.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        expected_response = [
            {
                "set_ID": "BNG",
                "set_details": "Born of the Gods is a small set with 165 cards. It was released on 2014-02-07.",
                "set_name": "Born of the Gods",
                "set_num_cards": 165,
                "set_release_date": "2014-02-07",
                "set_story": "No longer content to walk the planes of the Multiverse seeking pleasure, the planeswalker Xenagos returns to Theros to become the god of revels. The boundaries that separate everyday existence from Nyx are growing dangerously thin. Strange creatures of enchantment, called Nyxborn or Born of the Gods, are pouring into the mortal world as Xenagos threatens to disrupt the very nature of the plane. Mogis, the god of slaughter sends hordes of mortal and Nyxborn minotaurs against the human cities Akros, Meletis and Setessa. Elspeth Tirel leads an army of heroes to break the minotaur siege at Akros. The humans were victorious, but the victory celebration after the battle becomes the ultimate ritual to launch Xenagos into Nyx as a god. Elspeth is blamed for his ascension and driven away in disgrace."
            },
            {
                "set_ID": "DGM",
                "set_details": "Dragon's Maze is a small set with 142 cards. It was released on 2013-05-03.",
                "set_name": "Dragon''s Maze",
                "set_num_cards": 142,
                "set_release_date": "2013-05-03",
                "set_story": "The Implicit Maze is a system of mana paths or leylines through the guildgates and districts of Plane that has manifested after the Guildpact was destroyed. On instruction of Niv-Mizzet and using Jace Beleren's notes, it was discovered by Ral Zarek. The maze was created by Azor I to be revealed in case the Guildpact dissolved. In this way, the founder of the Azorius Senate tried to foster an atmosphere of peaceful collaboration. At the end of the maze in the Forum of Azor lies great power. In order for it to be solved, all the guilds of Ravnica must participate at once. Niv-Mizzet has announced that each guild will has send one champion as its delegate in the running of the maze. At an appointed time, the champions meet at the Transguild Promenade, and embark on a race through the twists and turns of the maze. The one who triumphs, gains the power behind it for his or her guild. Others fall to its dangers."
            },
            {
                "set_ID": "FUT",
                "set_details": "The set features 180 cards, 81 of which are timeshifted pre-prints, i.e. cards that have not been printed before but may appear in a future set, also known as futureshifted. Each of the cards features some quality that has never appeared in the game before, such as a new keyword ability (Fleshwrither), the application of a new keyword for an old ability (Thornweald Archer), or even referencing cards and card types that do not exist yet (Goldmeadow Lookout, Steamflogger Boss). Each of these unique aspects appear on only a small number of cards, indicating that they may be more properly explored in later sets. Additionally, most of the cards in some way reference unexplored planes, hinting at potential themes and locations for upcoming sets. The cards also feature a new futuristic card frame to hint at potential changes to the layout of Magic cards and to denote which cards are actually timeshifted. However, it has been confirmed that the Future Sight frame will not become the norm for subsequent sets. The new card frame sports specific symbols for different card types. As with Planar Chaos, the cards have the standard colored rarity symbols. It was released on 2007-05-03.",
                "set_name": "Future Sight",
                "set_num_cards": 180,
                "set_release_date": "2007-05-04",
                "set_story": "The quest to mend Dominaria\u2019s temporal and planar damage continues. A temporal rift connected to an alternate Dominaria has enabled Phyrexian horrors to cross over into the present day. Freyalise is gone, having given her planeswalker's spark and her life to close that rift, thereby protecting her sanctum of Skyshroud one last time.But time fractures still plague Dominaria. The damage to the planar fabric at Tolaria was so severe that it couldn't be healed \u2014 not in the present day. The heroes seek out the planeswalker Karn, the only being ever to travel through time. To heal Tolaria\u2019s rift, Karn uses the full extent of his planeswalking power to enter the rift and return to the past, to the moment before the archwizard Barrin cast a spell that obliterated countless Phyrexians and himself. Karn succeeds and seals the planar rift before Barrin\u2019s actions can rip it open. In the next moment, Karn is lost. Even as Venser begins to realize his full potential, the planeswalker Jeska returns to Dominaria for the first time since Karona fell. Her friend and ally Karn is gone, and someone will pay. An ancient, evil intelligence drives Jeska\u2019s wrath and threatens to undermine Teferi and Jhoira\u2019s efforts to complete Dominaria\u2019s healing: Leshrac has returned."
            },
            {
                "set_ID": "GTC",
                "set_details": "Gatecrash contains 249 cards (101 commons, 80 uncommons, 53 rares, 15 mythic rares), including randomly inserted premium versions of all cards in the set. Like Return to Ravnica, the preceding expansion set, Gatecrash focuses on the guild system and multicolor cards. The five guilds returning in Gatecrash are the Boros Legion, House Dimir, Gruul Clans, Orzhov Syndicate, and Simic Combine. Despite being a large expansion, Gatecrash does not contain any basic lands (Return to Ravnica has some extra). The set features two planeswalkers; one, Gideon, Champion of Justice, is an established planeswalker, whilst the other, Domri Rade is a new. The expansion symbol is a pointed arch of a gate. It was released on 2013-02-01.",
                "set_name": "Gatecrash",
                "set_num_cards": 249,
                "set_release_date": "2013-02-01",
                "set_story": "Jace begins to piece together the greater mystery of the Implicit Maze. It's now a race to see who will unlock its secrets."
            },
            {
                "set_ID": "JOU",
                "set_details": "Like its predecessors, Journey into Nyx has a ancient Greek themed top-down design, making use of many mythological tropes. The set contains 165 cards (60 Common, 60 Uncommon, 35 Rare, 10 Mythic) and includes randomly inserted premium versions of all cards. Fitting in with the enchantment matters theme, 59 of the set's 165 cards carry the enchantment type. The set introduces the Lamia creature type. It was released on 2014-05-02.",
                "set_name": "Journey into Nyx",
                "set_num_cards": 165,
                "set_release_date": "2014-05-02",
                "set_story": "The plane of Theros is in chaos. Gods and mortals are pitted against each other, and terrifying monsters stalk the land. Heroes strive for glory while new and terrifying constellations take shape in the night sky. Supported by Ajani, Elspeth travels to Nyx and kills Xenagos. Afraid of her power, Heliod kils Elspeth."
            },
            {
                "set_ID": "M14",
                "set_details": "Magic 2014 contains 249 cards (101 Common, 60 Uncommon, 53 Rare, 15 Mythic, 20 Basic Lands), including randomly inserted premium versions of all cards. The returning mechanic for this Core Set was Slivers. Even more than the previous set, Magic 2014 is strongly integrated with its digital counterpart, Duels of the Planeswalkers. In celebration of Magic 's 20th anniversary, the logo of the set has the mythic orange / bronze color instead of the usual yellow or blue. The set puts the spotlight on Chandra. This meant a new Planeswalker card aimed at making a splash in Constructed, many Chandra-themed support cards, and flavor throughout the set attached to her persona. It was released on 2013-07-19.",
                "set_name": "Magic 2014 Core Set",
                "set_num_cards": 249,
                "set_release_date": "2013-07-19",
                "set_story": ""
            },
            {
                "set_ID": "CNS",
                "set_details": "Conspiracy is a special large set with 197 cards. It was released on 2014-06-06.",
                "set_name": "Magic: The Gathering - Conspiracy",
                "set_num_cards": 197,
                "set_release_date": "2014-06-06",
                "set_story": "All new cards in Conspiracy depict the environment of the Paliano, the High City on the plane of Fiora, which is the home of Dack Fayden and the setting of the Magic comic book published by IDW"
            },
            {
                "set_ID": "MMA",
                "set_details": "Modern Masters is a 229 card set consisting of reprints of cards originally printed between Eighth Edition and Alara Reborn. Thus every card is legal in the Modern format and other formats in which the sets are legal from which the cards originate. It was designed to fill the need of reprinting certain cards to make them more easily available to current or prospective Modern players, without re-introducing those cards into Standard. The set also does not contain any cards which are on the banned list of the Modern format at the time of its design. Modern Masters is exclusively booster-based, thus no satellite products such as Preconstructed decks are branded with the set. Each booster contains 15 playable cards: 10 commons, 3 uncommons and one rare or mythic rare, and one foil card of any rarity replacing the basic land which would normally be found in a booster as Modern Masters does not contain a run of basic lands. Due to the higher expected average value of the cards contained in a booster and the lower print run, the MSRP of one booster of Modern Masters is set to $6.99 (with the MSRP of a booster of the current draft set being $3.49). Due to the higher MSRP booster displays only contain 24 packs, which is also the number required for a regular draft (three boosters for each of eight players), as the set was designed specifically for draft. A number of cards also change rarity from their original printing as mythic rare wasn't introduced until the Alara block, and/or receive new artwork. It was released on 2013-06-07.",
                "set_name": "Modern Masters",
                "set_num_cards": 229,
                "set_release_date": "2013-06-07",
                "set_story": ""
            },
            {
                "set_ID": "RTR",
                "set_details": "Return to Ravnica contains 274 cards (25 basic lands, 101 commons, 80 uncommons, 53 rares, 15 mythic rares), including randomly inserted premium versions of all cards in the set. As was the case with the original Ravnica block, Return to Ravnica focuses on the guild system and multicolor cards. Five guilds \u2014 the Azorius Senate, Golgari Swarm, Izzet League, Cult of Rakdos, and Selesnya Conclave \u2014 are featured in Return to Ravnica; the other five guilds appear in the following expansion, Gatecrash. Because R&D had to fit in five guilds, rather than four, the set contained more uncommon cards than usual. It it is unknown what the expansion symbol of this is set is meant to represent, though some people think it is a stylized Orzhov Mitre. It was released on 2012-10-05.",
                "set_name": "Return to Ravnica",
                "set_num_cards": 274,
                "set_release_date": "2012-10-05",
                "set_story": "As the name of the expansion implies, Return to Ravnica is set in Ravnica, a plane comprising a singular megalopolis or ecumenopolis, in which a vast and diverse variety of inhabitants co-exist. Once, the law of city and plane of Ravnica was dictated by the Guildpact and was controlled in relative harmony by the ten guilds, each of which representing a color pairing of the five colors of Magic. In Dissension, however, the Guildpact had been broken. Faced with a magical code that is built into the very foundations of the city-world itself, Jace Beleren marches into the numinous depths of Ravnica\u2019s underbelly in search of the promise of powerful magic. Once buried in past, the code resurfaces as Ravnica\u2019s power-hungry mage guilds, unbound by the Guildpact that had once maintained order, struggle for control of the plane."
            },
            {
                "set_ID": "THS",
                "set_details": "Theros contains 249 cards (20 basic lands, 121 commons, 60 uncommons, 53 rares, 15 mythic rares), and includes randomly inserted premium versions of all cards. The set has an ancient Greek themed top-down design, making use of many mythological tropes (Heroes, Monsters and Gods). It is the first set to thematically take place on the plane of Theros. It is mostly monocolored with a handful of gold cards. Theros block is an enchantment block that plays off building blocks in M14 and Return to Ravnica block. The mood and tone are those of Greek myth: adventure, achievement, accomplishment, a hero's journey. Many existing creature types are reworked to match the Greek flavor. Apart from Minotaurs, it's not a tribal set. There are three Planeswalkers in the set, namely Elspeth and two new ones: Ashiok and Xenagos. There is an above average amount of legendary permanents. The expansion symbol depicts an stylized temple and altar. It was released on 2013-09-27.",
                "set_name": "Theros",
                "set_num_cards": 249,
                "set_release_date": "2013-09-27",
                "set_story": "Theros is watched over by a pantheon of 15 powerful gods. The gods, though residing in Nyx, are able to take on many forms and often walk among mortals. Each also has a unique color identity. The five core gods are mono-coloured and make up the central pillars of the Theran belief system. The colour identities of these five are: Heliod (white), Thassa (blue), Erebos (black), Purphoros (red), and Nylea (green). The ten minor gods represent the two colour pairings and will be introduced in Born of the Gods and Journey into Nyx."
            },
            {
                "set_ID": "UG",
                "set_details": "The set included 86 silver-border cards, 5 black-border cards (lands) and 6 Token creatures. The lands are special full art lands which have extended artwork inside an oval frame stretching from the top to bottom of the card. On top of that oval frame is a round gem of the appropriate color with the at the time current tap symbol. At the bottom is a slightly larger featuring the appropriate mana symbol. The top left corner has the name of the basic land while the bottom left corner simply reads Land with Artist and copyright information as well as collectors number running along the bottom. Unlike other sets which feature up to four distinct arts per basic land, Unglued only has one art per basic land. The rest of Unglued are silver-bordered joke cards which are still functional. Names, flavor texts, types and mechanics as well as the art featured on the card parody the game, individual cards, concepts, the history or players of the game. Unglued and its followup Unhinged are also the only sets in which the artwork of non-Planeswalker cards of extend outside the artframe. The card B.F.M. (Big Furry Monster) even extends over two cards. Some cards have specialized frames allowing for other jokes. Unglued also makes special mention of Chickens and Clamfolks as creature types. A follow up set, tentatively called Unglued 2: The Obligatory Sequel, never got made. This was another set than Unhinged. It was released on 1998-08-11.",
                "set_name": "Unglued",
                "set_num_cards": 86,
                "set_release_date": "1998-08-11",
                "set_story": "All 94 cards in the Unglued set each had a single word printed on the bottom of the card. When combined in proper numerical order with other cards in the series spell out the following secret message: Here are some cards that didn't make it to print: Socks of Garfield, Hot Monkey Love, Colonel's Secret Recipe, Squee's Play, Banned in France, Spoon, Disrobing Scepter, Butt Wolf, Lotus Roach, Sesame Efreet, Needless Reminder Text, Chicken Choker, Clockwork Doppelganger, Henway, HELP I'M TRAPPED IN CARTA MUNDI, Mad Cow, Poke, Lord of Wombats, Gratuitous Babe Art, Brothers' War Bonds, Dwarven Kickboxer, Mickey's Drunk, Pact with the Wastes, CoP:BO, Urza's Chia Pet, Thallid Shooter, Shoelace, When Chihuahuas Attack, Wall of Cookies, Kobold Ninja, Mucusaur, Kjeldoran Outhouse, Bear in the Woods, Dental Thrull, Flavatog, Cereal Killer."
            },
            {
                "set_ID": "UNH",
                "set_details": "Unhinged included 140 silver-bordered cards and 5 black-bordered cards (the basic lands), all of which had foil versions which occur in a similar rate to normal Magic Sets. The set boasts many jokes, and has even set a precedent or two of its own for tournament-worthy Magic. Many cards are references to previous cards. The set is only available in English due to the difficulty to translate. Unhinged features a sixth color: pink. Water Gun Balloon Game can create a pink permanent and for abilities that let you produce mana of any color, you can choose {P} pink. However, there is no Unhinged (Basic) Land card that can produce pink mana. In addition, Avatar of Me can be whatever the color of your eyes are, allowing brown and hazel mana. One card, called Super Secret Tech, only exists as a foil rare card and technically affects the foil card concept as a whole. Its rarity is supposedly ten times more common than that of other Unhinged foil rare cards. It was released on 2004-11-20.",
                "set_name": "Unhinged",
                "set_num_cards": 140,
                "set_release_date": "2004-11-20",
                "set_story": "Much like Unglued before it, each card in the Unhinged set -including Super Secret Tech- has a single word printed on the bottom of the card after the artist's name and card number. When all cards are placed in the proper order with other cards in the series they spell out a secret message detailing cards that allegedly did not make it into the set. Placing all the Unhinged cards in reverse alphabetical order will cause the following message to appear: Here are some more cards that didn't make it: Moronic Tutor; Lint Golem; Wave of Incontinence; I'm Quitting Magic; Bob from Accounting; Castrate; Mishra's Bling Bling; Dead Bunny Isle; Circle of Protection: Pants; Time Fart; Sliver and Onions; Kobold Ass Master; Thanks, Barn; Mild Mongrel; Robo-Samurai; Obligatory Angel; Chump-Blocking Orphan; Wrath of Dog; Celery Stalker; Hugs-a-lot Demon; Assticore; Codpiece of the Chosen; Hurl; What the Cluck?!; Nachomancer; Scrubotomy; Arcbound Noah; Darksteel Spork; Look at Me, I'm Accounts Receivable; Hydro Djinn; Bad Stone Rain Variant; S.O.B.F.M.; Pinko Kami; Purple Nurple; Form of Uncle Istvan; Them's Fightin' Wards; Spleen of Ramos; Fifteenth Pick; Squizzle, Goblin Nabizzle; Zombie Cheerleading Squad; Two-Way Myr; Bone Flute 2: Electric Boogaloo; Magic Offline; Nutclamp; Bwahahahaaa!; Dragon Ass; Phyrexian Sno-Cone Machine; Chimney Pimp; R.T.F.C.; Greased Weasel; Flame War; We Don't Need No Stinkin' Merfolk; Ting!; and Disrobing Scepter (again!)."
            }
        ]

        for obj in response_objects:
            self.assertTrue(obj in expected_response)

    def test_get_set_1 (self) :
        request = Request(self.url+"sets/FUT.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        expected_response = {
            "set_ID": "FUT",
            "set_cards": [
                136150,
                130345,
                126193,
                136055,
                132212,
                132224,
                132225,
                136204,
                136048,
                136155,
                136049,
                130676,
                126143,
                130686,
                126161,
                130672,
                132229,
                130334,
                136054,
                130684,
                130582,
                126204,
                136156,
                130309,
                125878,
                126141,
                126177,
                126169,
                136053,
                126211,
                130635,
                136043,
                132226,
                132228,
                136196,
                136207,
                126132,
                132214,
                136215,
                136143,
                136192,
                130699,
                126131,
                132220,
                132227,
                126149,
                130713,
                130669,
                126187,
                130707,
                136044,
                130690,
                136200,
                136157,
                130311,
                126159,
                132211,
                130581,
                136040,
                130595,
                130328,
                132216,
                130695,
                126162,
                130574,
                130683,
                136201,
                130634,
                130694,
                130680,
                136194,
                126164,
                132218,
                136046,
                130698,
                136208,
                126139,
                136198,
                132213,
                126147,
                126166,
                136035,
                126151,
                126146,
                130332,
                130691,
                126186,
                126165,
                136195,
                136033,
                136051,
                136148,
                136152,
                136159,
                130689,
                126158,
                136202,
                130316,
                130346,
                136154,
                130614,
                126156,
                130588,
                136140,
                136138,
                126198,
                136206,
                136045,
                130564,
                132219,
                136210,
                130701,
                130638,
                136213,
                132223,
                126160,
                136211,
                126148,
                136216,
                136153,
                132217,
                136145,
                130339,
                126153,
                126199,
                130591,
                130353,
                130670,
                126210,
                130320,
                130327,
                136212,
                136161,
                126200,
                136158,
                130347,
                136137,
                136214,
                126134,
                126201,
                130314,
                136160,
                130704,
                136146,
                130329,
                130708,
                126213,
                130341,
                136032,
                130659,
                130344,
                132221,
                130323,
                136042,
                136151,
                130675,
                136205,
                136056,
                130706,
                126215,
                136199,
                136142,
                136139,
                130630,
                130338,
                136047,
                136041,
                130342,
                130616,
                130325,
                136149,
                136209,
                136197,
                130644,
                136141,
                126178,
                132222,
                130331,
                130702,
                132215
            ],
            "set_details": "The set features 180 cards, 81 of which are timeshifted pre-prints, i.e. cards that have not been printed before but may appear in a future set, also known as futureshifted. Each of the cards features some quality that has never appeared in the game before, such as a new keyword ability (Fleshwrither), the application of a new keyword for an old ability (Thornweald Archer), or even referencing cards and card types that do not exist yet (Goldmeadow Lookout, Steamflogger Boss). Each of these unique aspects appear on only a small number of cards, indicating that they may be more properly explored in later sets. Additionally, most of the cards in some way reference unexplored planes, hinting at potential themes and locations for upcoming sets. The cards also feature a new futuristic card frame to hint at potential changes to the layout of Magic cards and to denote which cards are actually timeshifted. However, it has been confirmed that the Future Sight frame will not become the norm for subsequent sets. The new card frame sports specific symbols for different card types. As with Planar Chaos, the cards have the standard colored rarity symbols. It was released on 2007-05-03.",
            "set_name": "Future Sight",
            "set_num_cards": 180,
            "set_release_date": "2007-05-04",
            "set_story": "The quest to mend Dominaria\u2019s temporal and planar damage continues. A temporal rift connected to an alternate Dominaria has enabled Phyrexian horrors to cross over into the present day. Freyalise is gone, having given her planeswalker's spark and her life to close that rift, thereby protecting her sanctum of Skyshroud one last time.But time fractures still plague Dominaria. The damage to the planar fabric at Tolaria was so severe that it couldn't be healed \u2014 not in the present day. The heroes seek out the planeswalker Karn, the only being ever to travel through time. To heal Tolaria\u2019s rift, Karn uses the full extent of his planeswalking power to enter the rift and return to the past, to the moment before the archwizard Barrin cast a spell that obliterated countless Phyrexians and himself. Karn succeeds and seals the planar rift before Barrin\u2019s actions can rip it open. In the next moment, Karn is lost. Even as Venser begins to realize his full potential, the planeswalker Jeska returns to Dominaria for the first time since Karona fell. Her friend and ally Karn is gone, and someone will pay. An ancient, evil intelligence drives Jeska\u2019s wrath and threatens to undermine Teferi and Jhoira\u2019s efforts to complete Dominaria\u2019s healing: Leshrac has returned."
        }

        self.assertEqual(expected_response, response_data)


    def test_get_set_2 (self) :
        request = Request(self.url+"sets/BNG.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        expected_response = {
            "set_ID": "BNG",
            "set_cards": [
                378373,
                378402,
                378459,
                378374,
                378375,
                378403,
                378460,
                378376,
                378488,
                378430,
                378404,
                378431,
                378489,
                378432,
                378529,
                378433,
                378434,
                378461,
                378377,
                378435,
                378490,
                378405,
                378516,
                378436,
                378491,
                378406,
                378492,
                378462,
                378378,
                378407,
                378408,
                378437,
                378438,
                378379,
                378380,
                378517,
                378518,
                378381,
                378463,
                378409,
                378410,
                378464,
                378382,
                378439,
                378465,
                378519,
                378440,
                378466,
                378411,
                378493,
                378383,
                378441,
                378467,
                378442,
                378468,
                378469,
                378412,
                378413,
                378470,
                378443,
                378444,
                378384,
                378445,
                378385,
                378386,
                378530,
                378494,
                378387,
                378388,
                378446,
                378447,
                378389,
                378495,
                378531,
                378390,
                378496,
                378471,
                378520,
                378497,
                378521,
                378522,
                378472,
                378414,
                378473,
                378391,
                378448,
                378415,
                378416,
                378498,
                378523,
                378392,
                378499,
                378449,
                378500,
                378501,
                378502,
                378417,
                378450,
                378474,
                378393,
                378418,
                378503,
                378451,
                378475,
                378419,
                378394,
                378395,
                378452,
                378504,
                378420,
                378476,
                378524,
                378505,
                378506,
                378532,
                378477,
                378396,
                378525,
                378507,
                378526,
                378478,
                378421,
                378397,
                378479,
                378453,
                378480,
                378481,
                378508,
                378509,
                378482,
                378483,
                378454,
                378510,
                378511,
                378455,
                378398,
                378422,
                378527,
                378533,
                378512,
                378513,
                378423,
                378399,
                378456,
                378534,
                378484,
                378424,
                378425,
                378400,
                378514,
                378535,
                378536,
                378537,
                378426,
                378485,
                378486,
                378427,
                378515,
                378401,
                378428,
                378457,
                378458,
                378429,
                378487,
                378528
            ],
            "set_details": "Born of the Gods is a small set with 165 cards. It was released on 2014-02-07.",
            "set_name": "Born of the Gods",
            "set_num_cards": 165,
            "set_release_date": "2014-02-07",
            "set_story": "No longer content to walk the planes of the Multiverse seeking pleasure, the planeswalker Xenagos returns to Theros to become the god of revels. The boundaries that separate everyday existence from Nyx are growing dangerously thin. Strange creatures of enchantment, called Nyxborn or Born of the Gods, are pouring into the mortal world as Xenagos threatens to disrupt the very nature of the plane. Mogis, the god of slaughter sends hordes of mortal and Nyxborn minotaurs against the human cities Akros, Meletis and Setessa. Elspeth Tirel leads an army of heroes to break the minotaur siege at Akros. The humans were victorious, but the victory celebration after the battle becomes the ultimate ritual to launch Xenagos into Nyx as a god. Elspeth is blamed for his ascension and driven away in disgrace."
        }

        self.assertEqual(expected_response, response_data)

    def test_get_set_3 (self) :
        request = Request(self.url+"sets/DGM.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        expected_response = {
            "set_ID": "DGM",
            "set_cards": [
                369036,
                368961,
                369082,
                369016,
                369053,
                369017,
                368974,
                369044,
                368984,
                369000,
                368985,
                369047,
                368954,
                369030,
                369051,
                368997,
                369008,
                369028,
                368953,
                368971,
                369057,
                369029,
                368999,
                369056,
                369003,
                369039,
                369084,
                369096,
                369058,
                369089,
                369061,
                369086,
                368944,
                369055,
                368962,
                368969,
                368955,
                369095,
                368987,
                368964,
                369023,
                368960,
                369035,
                369040,
                368956,
                369077,
                369087,
                369021,
                369048,
                368948,
                368995,
                368947,
                369064,
                369052,
                369059,
                368983,
                369066,
                368965,
                368981,
                368994,
                369050,
                369091,
                369014,
                369076,
                368976,
                369038,
                369062,
                368957,
                368980,
                369026,
                369049,
                369007,
                368988,
                369093,
                368973,
                369002,
                368996,
                369078,
                369079,
                369054,
                369099,
                369069,
                369006,
                369013,
                369001,
                369090,
                369073,
                368946,
                368975,
                369085,
                368990,
                369031,
                368958,
                369022,
                369033,
                368993,
                368978,
                368979,
                368998,
                368986,
                369075,
                368966,
                369025,
                369088,
                368952,
                369005,
                369092,
                369060,
                369018,
                368945,
                368963,
                368959,
                368968,
                369043,
                369068,
                369083,
                369067,
                369015,
                368972,
                368992,
                368949,
                369098,
                369011,
                369020,
                368970,
                369034,
                369072,
                369046,
                369010,
                369074,
                368977,
                369070,
                368951,
                369045,
                369012,
                369081,
                369094,
                369004,
                369037,
                369027,
                369019,
                369065
            ],
            "set_details": "Dragon's Maze is a small set with 142 cards. It was released on 2013-05-03.",
            "set_name": "Dragon''s Maze",
            "set_num_cards": 142,
            "set_release_date": "2013-05-03",
            "set_story": "The Implicit Maze is a system of mana paths or leylines through the guildgates and districts of Plane that has manifested after the Guildpact was destroyed. On instruction of Niv-Mizzet and using Jace Beleren's notes, it was discovered by Ral Zarek. The maze was created by Azor I to be revealed in case the Guildpact dissolved. In this way, the founder of the Azorius Senate tried to foster an atmosphere of peaceful collaboration. At the end of the maze in the Forum of Azor lies great power. In order for it to be solved, all the guilds of Ravnica must participate at once. Niv-Mizzet has announced that each guild will has send one champion as its delegate in the running of the maze. At an appointed time, the champions meet at the Transguild Promenade, and embark on a race through the twists and turns of the maze. The one who triumphs, gains the power behind it for his or her guild. Others fall to its dangers."
        }

        self.assertEqual(expected_response, response_data)

    def test_get_all_types (self) :
        request = Request(self.url+"types.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        expected_response = [
            {
                "type_description": "Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.",
                "type_name": "Enchant Creature"
            },
            {
                "type_description": "Land creature has the properties of both a land and a creature.  It can be tapped for mana as a land, but has power and toughness like a creature.  It has no casting cost to play like a land, but like a creature it has summoning sickness, thus its abilities cannot be used on the first turn it comes into play.",
                "type_name": "Land Creature"
            },
            {
                "type_description": "Gods are indestructable legendary enchantment creatures (living enchantments). For this reason, all enchantments are thought to be gifts from the gods, a unique form of magic enabled by divinities. The gods of Theros grant their favors to those whose devotion is great enough. Gamewise, they don''t manifest as creatures on the battlefield until a player''s devotion to their color is high enough. If a God enters the battlefield while the player''s devotion to its color is less than the required number, abilities that trigger when a creature enters the battlefield won''t trigger. If a God on the battlefield is a creature and the player''s devotion to its color drops below the required number, it immediately stops being a creature. A God can''t attack the turn it enters the battlefield unless it has haste, even if it wasn''t a creature as it entered the battlefield. They are always legendary enchantments, and their abilities work whether they''re creatures or not.",
                "type_name": "Legendary Enchantment Creature"
            },
            {
                "type_description": "Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow).  The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods.  These had all global enchantment effects.",
                "type_name": "Enchantment Creature"
            },
            {
                "type_description": "Artifacts are permanents that represent magical items, animated constructs, pieces of equipment, or other objects and devices. Up until the introduction of the colorless, non-artifact Eldrazi cards in the Rise of the Eldrazi set, artifacts were distinct from other card types in that they were the only existing cards that had wholly generic mana costs (meaning they can be cast using any type of mana), excluding certain cards which cost 0 Mana.",
                "type_name": "Artifact"
            },
            {
                "type_description": "Instants, like sorceries, represent one-shot or short-term magical spells.  They are never put into the in-play zone; instead, they take effect when their mana cost is paid and the spell resolves, and then are immediately put into the player''s graveyard.  Sorceries and instants differ only in when they can be played.  Sorceries can only be played during the player''s main phase, and only when nothing else is on the stack. Instants, on the other hand, can be played at any time, including during other player''s turns and while another spell or ability is waiting to resolve.",
                "type_name": "Instant"
            },
            {
                "type_description": "Enchantment artifacts represent the weaponry of the gods. Enchantment creatures and enchantment artifacts in the Theros block all have a unique card frame that shows the starfield of Nyx.",
                "type_name": "Legendary Enchantment Artifact"
            },
            {
                "type_description": "Interrupt is an obsolete card type. It has not been supported by the game since Sixth Edition. Under the original rules, an interrupt was a spell that would resolve before the rest of the Batch. Some examples of interrupts include Counterspell, Red Elemental Blast and Dark Ritual. All Interrupt cards have received errata to make them instants, and all references to Interrupts have been given errata to reference instants.",
                "type_name": "Interrupt"
            },
            {
                "type_description": "Legendary is a supertype that can be found on artifacts, creatures, enchantments and lands.  The \"legend rule\" is the name for a rule that prevents a single player from having two or more of the same legendary permanent in play at the same time. This latest version of the rule has been in effect since the release of Magic 2014.",
                "type_name": "Legendary Artifact"
            },
            {
                "type_description": "Lands may be tapped to produce mana of one color in Magic.  They cost nothing to play, can only be played once per turn and are immune to the usual 4 or less rule per card type in a deck.",
                "type_name": "Land"
            },
            {
                "type_description": "There may be only one of any legendary permanent with the same name under a player''s control at any one time. If two or more legendary permanents with the same name are in play under one player''s control at the same time, the player chooses and sacrifices one.",
                "type_name": "Legendary Land"
            },
            {
                "type_description": "Artifact creatures are both Artifacts and Creatures. This means that anything that affects either artifacts or creatures affects them. Artifact creatures can be anything from robots, Animated objects, to living creatures infused with metal",
                "type_name": "Artifact Creature"
            },
            {
                "type_description": "Creature is used for the further classification of creatures, both cards and tokens. Historically, creature type was simply for purposes relating to flavor; however, as distant as Fallen Empires, creature types have had thematic and mechanistic purposes too.",
                "type_name": "Creature"
            },
            {
                "type_description": "Sorcery is a card type, and, along with instants, is the only spell type that is not a permanent. A player who has priority may play a sorcery card from his or her hand during a main phase of his or her turn when the stack is empty.",
                "type_name": "Sorcery"
            },
            {
                "type_description": "Planeswalker card types were introduced in Lorwyn. [2] [3] [4] Like the player him or herself, a planeswalker card represents a powerful being that is able to move from plane to plane.",
                "type_name": "Planeswalker"
            },
            {
                "type_description": "Enchantments represent persistent magical effects, usually remaining in play indefinitely. Most have continuous or triggered abilities, but some have abilities that can be activated by their controllers. ",
                "type_name": "Enchantment"
            },
            {
                "type_description": "A Summon spell, Summon Creature or Summon is an obsolete spell type which had the form of \"Summon <creature>\" in the type line of a card (where <creature> would be the current creature subtype).",
                "type_name": "Summon"
            },
            {
                "type_description": "In addition to snow lands there were a lot of other snow permanents with the release of Coldsnap. Again, this type did nothing of its own but it would matter in the interaction with other cards such as Chill to the Bone.",
                "type_name": "Snow Creature"
            },
            {
                "type_description": "Similar in type to creature with the restriction that only instance of this card can be allowed in play at one time.  If a controller has two of the same name, he must choose to sacrifice one.",
                "type_name": "Legendary Creature"
            },
            {
                "type_description": "Type created in unhinged set.  Done entirely in Pig Latin.  The card reads Double Strike, whenever the controller of this card speaks a non pig-latin word, sacrifice it. This piece of flavor text doesn''t really say anything",
                "type_name": "Eaturecray"
            },
            {
                "type_description": "Similar to Land in that they can be tapped to gain one mana of the color the land represents.  Can be as many of this type in your deck as you prefer and can only be played once per turn.  These are Island/Mountain/Swamp/Forest/Plain only.",
                "type_name": "Basic Land"
            }
        ]

        for obj in response_objects:
            self.assertTrue(obj in expected_response)

    def test_get_type_1 (self) :
        request = Request(self.url+"types/Enchant Creature.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        expected_response = {
            "type_description": "Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.",
            "type_name": "Enchant Creature",
            "type_subtypes": []
        }

        self.assertEqual(expected_response, response_data)

    def test_get_type_2 (self) :
        request = Request(self.url+"types/Artifact.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        expected_response = {
            "type_description": "Artifacts are permanents that represent magical items, animated constructs, pieces of equipment, or other objects and devices. Up until the introduction of the colorless, non-artifact Eldrazi cards in the Rise of the Eldrazi set, artifacts were distinct from other card types in that they were the only existing cards that had wholly generic mana costs (meaning they can be cast using any type of mana), excluding certain cards which cost 0 Mana.",
            "type_name": "Artifact",
            "type_subtypes": [
                "Equipment",
                "Fortification"
            ]
        }

        self.assertEqual(expected_response, response_data)

    def test_get_type_3 (self) :
        request = Request(self.url+"types/Land.json")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        expected_response = {
            "type_description": "Lands may be tapped to produce mana of one color in Magic.  They cost nothing to play, can only be played once per turn and are immune to the usual 4 or less rule per card type in a deck.",
            "type_name": "Land",
            "type_subtypes": [
                "Forest Plains",
                "Swamp Mountain",
                "Forest Island",
                "Plains Swamp",
                "Island Swamp",
                "Plains Island",
                "Gate",
                "Island Mountain",
                "Swamp Forest",
                "Mountain Plains",
                "Mountain Forest"
            ]
        }

        self.assertEqual(expected_response, response_data)

"""
Search Test
"""

TEST_INDEX = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_test_index'),
    },
}

def search_or (q) :
    sq = None
    for phrase in shlex.split(q):
        if not sq:
            sq = SQ(content=phrase)
        else:
            sq |= SQ(content=phrase)
    return sq

def search_and (q) :
    sq = None
    for phrase in shlex.split(q):
        if not sq:
            sq = SQ(content=phrase)
        else:
            sq &= SQ(content=phrase)
    return sq

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class SearchTest (TestCase) :

    fixtures = ['test_data.json']

    def setUp (self) :
        super(SearchTest, self).setUp()
        haystack.connections.reload('default')
        call_command('rebuild_index', verbosity=0, interactive=False, noinput =True)

    def tearDown (self) :
        call_command('clear_index', interactive=False, verbosity=1)

    def testSingleWordOr(self):
        search = search_or('Chromanticore')
        query = SearchQuerySet().filter(search)
        actual_results = [q.object for q in query]
        expected_results = []
        expected_results += [MagicCard.objects.get(pk = 1)]
        self.assertEqual(expected_results, actual_results)

    def testSingleWordAnd(self):
        search = search_and('Chromanticore')
        query = SearchQuerySet().filter(search)
        actual_results = [q.object for q in query]
        expected_results = []
        expected_results += [MagicCard.objects.get(pk = 1)]
        self.assertEqual(expected_results, actual_results)

    def testMultiWordOr(self):
        search = search_or('Chromanticore Gods')
        query = SearchQuerySet().filter(search)
        actual_results = [q.object for q in query]
        expected_results = []
        expected_results += [MagicCard.objects.get(pk = 1)]
        expected_results += [MagicSet.objects.get(pk = 1)]
        expected_results += [MagicType.objects.get(pk = 1)]
        self.assertEqual(expected_results, actual_results)

    def testMultiWordAnd(self):
        search = search_and('Chromanticore Gods')
        query = SearchQuerySet().filter(search)
        actual_results = [q.object for q in query]
        expected_results = []
        expected_results += [MagicCard.objects.get(pk = 1)]
        self.assertEqual(expected_results, actual_results)



def jsonLoadsFromResponse (resp) :
    resp_str = str(resp.content)
    resp_str = resp_str[resp_str.index("\'")+1:-1]
    return json.loads(resp_str)

print("tests.py")
print("Done.")


