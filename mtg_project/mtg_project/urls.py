from django.conf.urls import patterns, include, url
from mtg_project.views import home, set_splash, ug, unh, ths, rtr, mma, m14, jou
from mtg_project.views import gtc, fut, dgm, cns, bng, about, sets_template
from mtg_project.views import guru_id_380422, guru_id_373603, guru_id_382303
from mtg_project.views import guru_id_136196, guru_id_370728, guru_id_9771
from mtg_project.views import guru_id_366450, guru_id_370404, guru_id_378516
from mtg_project.views import guru_id_369096, guru_id_270539, guru_id_73947
from mtg_project.views import cards_splash



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtg_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sets$', set_splash),
    url(r'^cards$', cards_splash),
    url(r'^template$', sets_template),
    url(r'^sets/UNH', unh),
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
    url(r'^cards/guru_id_380422$', guru_id_380422),
    url(r'^cards/guru_id_373603$', guru_id_373603),
    url(r'^cards/guru_id_382303$', guru_id_382303),
    url(r'^cards/guru_id_136196$', guru_id_136196),
    url(r'^cards/guru_id_370728$', guru_id_370728),
    url(r'^cards/guru_id_9771$', guru_id_9771),
    url(r'^cards/guru_id_366450$', guru_id_366450),
    url(r'^cards/guru_id_370404$', guru_id_370404),
    url(r'^cards/guru_id_378516$', guru_id_378516),
    url(r'^cards/guru_id_369096$', guru_id_369096),
    url(r'^cards/guru_id_270539$', guru_id_270539),
    url(r'^cards/guru_id_73947$', guru_id_73947),
    url(r'^about$', about),
    url(r'$', home)
)
