from django.db import models

class MagicCard(models.Model):
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
        return self.card_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('cards.views.details', args=[str(self.card_ID)])

class MagicSet(models.Model):
    set_ID = models.CharField(max_length =8,primary_key = True)
    set_name = models.CharField(max_length = 255)
    set_symbol =  models.CharField(max_length = 255)
    set_release_date = models.CharField('date released', max_length = 255) # mm/yyyy

    def __str__(self):
        return self.set_name;

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('sets.views.details', args=[str(self.set_ID)])

    def _num_cards(self):
        return self.magic_cards_set.all().count()

    set_num_cards = property(_num_cards)



class MagicType(models.Model):
    type_name = models.CharField(max_length = 255,primary_key = True)
    type_description = models.TextField()
    type_subtypes = models.ManyToManyField('MagicSubtype', related_name = 'magic_subtype_set', null = True)

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('type.views.details', args=[str(self.type_name)])

class MagicSubtype(models.Model):
    subtype_name = models.CharField(max_length = 255,primary_key = True)

    def __str__(self):
        return self.subtype_name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('subtype.views.details', args=[str(self.subtype_name)])

