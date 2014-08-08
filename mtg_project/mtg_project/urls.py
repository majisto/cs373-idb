from django.conf.urls import patterns, include, url

from mtg_project.views import home, set_splash, testing
from mtg_project.views import about, set_template, api_implement
from mtg_project.views import cards_splash, types_splash, how_to_play
from mtg_project.views import card_template, error, type_template
# from mtg_project.views import search
from mtg_project import views
from mtg_project.api import magic_cards_all, magic_sets_all, magic_types_all, magic_subtypes_all
from mtg_project.api import magic_card_id, magic_set_id, magic_type_name, magic_subtype_name
from haystack.forms import SearchForm






from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #Phase 2

    url(r'^about$', about),
    url(r'^how_to_play', how_to_play),
    url(r'^admin/', include(admin.site.urls)),

    # API URLs
    url(r'^cards.json$', magic_cards_all),
    url(r'^sets.json$', magic_sets_all),
    url(r'^types.json$', magic_types_all),
    url(r'^subtypes.json$', magic_subtypes_all),
    url(r'^cards/(?P<card_id>[0-9]+).json', magic_card_id),
    url(r'^sets/(?P<set_id>[A-Z]{2,3}).json', magic_set_id),
    url(r'^types/(?P<type_name>[a-zA-Z ]+).json', magic_type_name),
    url(r'^subtypes/(?P<subtype_name>[a-zA-Z ,]+).json', magic_subtype_name),

    # Content URLs
    url(r'^sets$', set_splash),
    url(r'^cards$', cards_splash),
    url(r'^types$', types_splash),
    url(r'^cards/id=(?P<card_id>[0-9]+)', card_template),
    url(r'^types/(?P<type_name>[a-zA-Z ]+)', type_template),
    url(r'^sets/(?P<set_id>[A-Z0-9]{2,3})', set_template),

    #Phase 3
    #url(r'^search/', search),
    url(r'^search/', views.MagicSearchView(my_form_class=SearchForm), name='haystack_search'),

    url(r'^testing$', testing),
    url(r'^api-implement$', api_implement),
    url(r'^$', home),
    url(r'$', error)


)

