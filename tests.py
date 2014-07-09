from django.test import TestCase
from mtg_project.models import *

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
                 "set_symbol" : '',
                 "set_release_date" :'02/2014'}
        MagicSet.objects.create(**set_dict)

        set_dict = {"set_ID" : 'UNH',
            "set_name" : 'Unhinged',
            "set_symbol" : '',
            "set_release_date" : '11/2004'}

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
            "card_flavor_text" : '#_"If the hierarchies of nature were determined by ferocity alone, the badger would be lord of the beasts."_#£#_—Anthousa of Setessa_#',
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
            "card_text" : "+2: Exile the top three cards of target opponent''s library.£-X: Put a creature card with converted mana cost X exiled with Ashiok, Nightmare Weaver onto the battlefield under your control. That creature is a Nightmare in addition to its other types.£-10: Exile all cards from all opponents'' hands and graveyards.",
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
            "card_text" : "Tarmogoyf''s power is equal to the number of card types among cards in all graveyards and its toughness is equal to that number plus 1.",
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

        self.assertEqual(card_object.card_text, "Tarmogoyf''s power is equal to the number of card types among cards in all graveyards and its toughness is equal to that number plus 1.")
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
        self.assertEqual(set_object.set_symbol, '')

    def test_MagicSet_2(self) :
        self.db_setup()
        set_object = MagicSet.objects.get(set_ID = 'BNG')

        self.assertEqual(set_object.set_name, 'Born of the Gods')
        self.assertEqual(set_object.set_num_cards, 3)

    def test_MagicSet_3(self) :
        self.db_setup()
        set_object = MagicSet.objects.get(set_ID = 'UNH')

        self.assertEqual(set_object.set_name, 'Unhinged')
        self.assertEqual(set_object.set_release_date, '11/2004')

    """
    Tests for MagicType class
    """

    def test_MagicType_1(self) :
        self.db_setup()
        type_object = MagicType.objects.get(type_name = 'Enchant Creature')

        self.assertEqual(type_object.type_name, 'Enchant Creature')
        self.assertEqual(type_object.type_description, 'Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.')

        subtypes_names = [x.__str__() for x in type_object.type_subtypes.all()]

        self.assertEqual(subtypes_names[0], 'Angel')
        self.assertEqual(subtypes_names[1], 'Beast')
        self.assertEqual(subtypes_names[2], 'Hound Construct')

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


print("tests.py")
print("Done.")

