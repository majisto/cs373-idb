from django.db import models

class MagicCard(models.Model):
    """
    MagicCard is a class that models an actual magic card.
    Magic cards are used to make a deck and  play the Magic the gathering.

    fields inlcuded contain info that describe the card and its attributes
    """
    card_ID = models.IntegerField()
    card_name = models.CharField(max_length = 255)
    card_setID = models.ForeignKey('MagicSet', related_name = 'magic_cards_set')  #'Model' in single quotes if not yet been defined
    card_type = models.ForeignKey('MagicType', related_name = 'magic_cards_set')
    card_subtype = models.ForeignKey('MagicSubtype', related_name = 'magic_cards_set', null = True)
    card_mana_cost = models.CharField(max_length = 255)
    card_converted_cost = models.IntegerField()
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

    def get_card_attr(self):
        result = []
        result.append(self.card_ID)
        result.append(self.card_name)
        result.append(self.card_setID)
        result.append(self.card_type)
        result.append(self.card_subtype)
        result.append(self.card_mana_cost)
        result.append(self.card_converted_cost)
        result.append(self.card_loyalty)
        result.append(self.card_rarity)
        result.append(self.card_text)
        result.append(self.card_flavor_text)
        result.append(self.card_power)
        result.append(self.card_toughness)
        result.append(self.card_price)
        return result



class MagicSet(models.Model):
    """
    MagicSet is a class that models an  actual magic set.
    Magic sets are released every year containing 150-200 magic cards.
    Fields inlcuded contain info that describe the set and its attributes
    """
    set_ID = models.CharField(max_length =8)
    set_name = models.CharField(max_length = 255)
    set_release_date = models.CharField('date released', max_length = 255) # mm/yyyy
    set_num_cards = models.IntegerField()

    def __str__(self):
        """
        returns a string representation of a MagicSet
        """
        return self.set_name;

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('sets.views.details', args=[str(self.set_ID)])

    def set_id(self):
        return self.set_ID



class MagicType(models.Model):
    """
    MagicType is a class that models an magic type.
    a type in magic is a clasification of card.
    examples of types a card can be include: "Creature", "Land" , "Interrupt"
    magic types can but not necessarily have subtypes.
    all MagicCards MUST have a type.

    fields inlcuded contain info that describe the type and its attributes
    """
    type_name = models.CharField(max_length = 255)
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
    subtype_name = models.CharField(max_length = 255)

    def __str__(self):
        """
        returns a string representation of a MagicSubtype
        """
        return self.subtype_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('subtype.views.details', args=[str(self.subtype_name)])
