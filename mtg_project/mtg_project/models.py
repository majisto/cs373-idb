from django.db import models

class MagicCard(models.Model):
    """
    MagicCard is a class that models an actual magic card.
    Magic cards are used to make a deck and  play the Magic the gathering.

    fields inlcuded contain info that describe the card and its attributes
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

    def __str__(self):
        """
        returns a string representation of a MagicCard
        """
        return self.card_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('cards.views.details', args=[str(self.card_ID)])


class MagicSet(models.Model):
    """
    MagicSet is a class that models an  actual magic set.
    Magic sets are released every year containing 150-200 magic cards.
    Fields inlcuded contain info that describe the set and its attributes
    """
    set_ID = models.CharField(max_length =8,primary_key = True)
    set_name = models.CharField(max_length = 255)
    set_symbol =  models.CharField(max_length = 255)
    set_release_date = models.CharField('date released', max_length = 255) # mm/yyyy

    def __str__(self):
        """
        returns a string representation of a MagicSet
        """
        return self.set_name;

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('sets.views.details', args=[str(self.set_ID)])

    def _num_cards(self):
        """
        Calculates the total number of cards in the givenset on the fly
        return number of cards in the set
        """
        return self.magic_cards_set.all().count()

    set_num_cards = property(_num_cards)


class MagicType(models.Model):
    """
    MagicType is a class that models an magic type.
    a type in magic is a clasification of card.
    examples of types a card can be include: "Creature", "Land" , "Interrupt"
    magic types can but not necessarily have subtypes.
    all MagicCards MUST have a type.

    fields inlcuded contain info that describe the type and its attributes
    """
    type_name = models.CharField(max_length = 255,primary_key = True)
    type_description = models.TextField()
    type_subtypes = models.ManyToManyField('MagicSubtype', related_name = 'magic_subtype_set', null = True)

    def __str__(self):
        """
        returns a string representation of a MagicType
        """
        return self.type_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('type.views.details', args=[str(self.type_name)])

class MagicSubtype(models.Model):
    """
    MagicSubtypes is a class that models an actual magic subtype
    A subtype in magic is a specialized customization of a given type.

    subtypes can belong to multiple type
    not all cards have a subtype
    """
    subtype_name = models.CharField(max_length = 255,primary_key = True)

    def __str__(self):
        """
        returns a string representation of a MagicSubtype
        """
        return self.subtype_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('subtype.views.details', args=[str(self.subtype_name)])
