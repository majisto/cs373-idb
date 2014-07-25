from django.test import TestCase
from mtg_project.models import *
from mtg_project.api    import *
from django.http import HttpResponse, HttpRequest
import json


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


def jsonLoadsFromResponse (resp) :
    resp_str = str(resp.content)
    resp_str = resp_str[resp_str.index("\'")+1:-1]
    return json.loads(resp_str)

print("tests.py")
print("Done.")


