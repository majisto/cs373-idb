from django.conf.urls import patterns, include, url

from mtg_project.views import home, set_splash, ug, unh, ths, rtr, mma, m14, jou
from mtg_project.views import gtc, fut, dgm, cns, bng, about, sets_template
# from mtg_project.views import guru_id_380442, guru_id_373603, guru_id_382303
# from mtg_project.views import guru_id_136196, guru_id_370728, guru_id_9771
# from mtg_project.views import guru_id_366450, guru_id_370404, guru_id_378516
# from mtg_project.views import guru_id_369096, guru_id_270359, guru_id_73947
from mtg_project.views import cards_splash, types_splash, enchantment_creature, legendary_creature, artifact, how_to_play
from mtg_project.views import card_template, error, type_template

card_id = 9771

#Phase 2

from mtg_project.api import magic_cards_all, magic_sets_all, magic_types_all, magic_subtypes_all
from mtg_project.api import magic_card_id, magic_set_id, magic_type_name, magic_subtype_name





from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtg_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^sets$', set_splash),
    #url(r'^cards$', cards_splash),
    #url(r'^types$', types_splash),
    url(r'^template$', sets_template),
    url(r'^sets/UNH$', unh),
    url(r'^sets/UG', ug),
    url(r'^sets/THS', ths),
    url(r'^sets/RTR', rtr),
    url(r'^sets/MMA', mma),
    url(r'^sets/M14', m14),
    url(r'^sets/JOU', jou),
    url(r'^sets/GTC', gtc),
    url(r'^sets/FUT', fut),
    url(r'^sets/DGM', dgm),
    url(r'^sets/CNS', cns),
    url(r'^sets/BNG', bng),
    url(r'^types/enchantment_creature', enchantment_creature),
    url(r'^types/legendary_creature', legendary_creature),
    url(r'^types/artifact', artifact),

    #url(r'^about$', about),
    #url(r'^how_to_play', how_to_play),
    #url(r'$', home)



    #Phase 2
    url(r'^cards.json$', magic_cards_all),
    url(r'^sets.json$', magic_sets_all),
    url(r'^types.json$', magic_types_all),
    url(r'^subtypes.json$', magic_subtypes_all),
    url(r'^cards/(?P<card_id>[0-9]+).json', magic_card_id),
    url(r'^sets/(?P<set_id>[A-Z]{2,3}).json', magic_set_id),
    url(r'^types/(?P<type_name>[a-zA-Z ]+).json', magic_type_name),
    url(r'^subtypes/(?P<subtype_name>[a-zA-Z ,]+).json', magic_subtype_name),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^sets$', set_splash),
    url(r'^cards$', cards_splash),
    url(r'^types$', types_splash),

    url(r'^about$', about),
    url(r'^how_to_play', how_to_play),
    url(r'^card-template', card_template, {"card_id":card_id}),
    url(r'^cards/id=(?P<card_id>[0-9]+)', card_template),
    url(r'^types/(?P<type_id>[0-9]+)', type_template),
    url(r'^$', home),
    url(r'$', error)

)

