from django.shortcuts import render, get_object_or_404, render_to_response
from mtg_project.models import MagicCard, MagicSet, MagicType
from django.http import HttpResponse
import random
import urllib
import json
from haystack.views import SearchView
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery
import haystack.constants as constants
import shlex
from haystack.backends import SQ
from haystack.forms import SearchForm

nav_template = "navbar_template.html"


set_list = []
set_list.append('BNG')
set_list.append('CNS')
set_list.append('DGM')
set_list.append('FUT')
set_list.append('GTC')
set_list.append('JOU')
set_list.append('M14')
set_list.append('MMA')
set_list.append('RTR')
set_list.append('THS')
set_list.append('UG')
set_list.append('UNH')


#HOME PAGE
def home(request):
    return render(request, "ext_home_splash.html", {"navbar_template":nav_template})

#SPLASH PAGE FOR SETS
def set_splash(request):
    global set_list
    html_dict = {"navbar_template":nav_template}
    sets = []

    for st in set_list:
        try:
            s = MagicSet.objects.get(set_ID=st)
        except:
            render(request, "ext_404.html")
        else:
            s = s.__dict__
            set_id = s['set_ID']
            set_name = s['set_name']
            lower_set_id = set_id.lower()
            set_dict = {"id":set_id, "lower_id":lower_set_id, "name":set_name}
            sets.append(set_dict)
    html_dict.update({"set_list":sets})

    return render(request, "ext_sets_splash.html", html_dict)

#SPLASH PAGE FOR CARDS
def cards_splash(request):
    html_dict = {"navbar_template":nav_template}
    try:
        sets = list(MagicSet.objects.all())
    except:
        render(request, "ext_404.html")
    else:
        num_sets = len(sets)
        num_cards = 2
        set_index = 0
        set_num = 0
        cards_to_render = []
        set_ids = []
        while set_num < num_sets:
            try:
                cards = list(MagicCard.objects.all().filter(card_setID=sets[set_num].id))
            except:
                render(request, "ext_404.html")

            for x in range(num_cards):
                set_ids.append(sets[set_index].set_ID)
            set_index += 1

            sample_cards = set()
            while len(sample_cards) < num_cards:
                r = random.randint(0,len(cards))
                if r not in sample_cards: sample_cards.add(r)

            for x in list(sample_cards):
                try:
                    cards_to_render.append(cards[x].card_ID)
                except:
                    render(request, "ext_404.html")

            set_num += 1

        all_the_cards = zip(cards_to_render, set_ids)
        html_dict.update({"cards_and_sets":all_the_cards})

    return render(request, "ext_cards_splash.html", html_dict)


#SPLASH PAGE FOR TYPES
def types_splash(request):
    html_dict = {"navbar_template":nav_template}
    types = []
    type_ids = []

    try:
        t = list(MagicType.objects.all())
    except:
        render(request, "ext_404.html")
    else:
        for v in t:
            types.append(v.type_name)
            type_ids.append(v.id)

    result = zip(type_ids, types)
    html_dict.update({"types":result})
    return render(request, "ext_types_splash.html", html_dict)

#ABOUT PAGE
def about(request):
    return render(request, "ext_about.html")

#A TESTING PAGE
# def sets_template(request):
#     return render(request, "sets_template.html")


#THE HOW TO PLAY PAGE
def how_to_play(request):
    return render(request, "ext_how_to_play.html", {"navbar_template":nav_template})


#THE 404 PAGE
def error(request):
    return render(request, "ext_404.html")

#THE TEMPLATED PAGE THAT EVERY CARD USES
def card_template(request, card_id):
    html_dict = {"navbar_template":nav_template}
    try:
        attr_list = MagicCard.objects.get(card_ID = card_id)
    except:
        return render(request, "ext_404.html")
    else:
        attr_list = attr_list.get_card_attr()

    try:
        s = MagicSet.objects.get(set_name=str(attr_list[2]))
    except:
        return render(request, "ext_404.html")


    html_dict.update({"card_id":attr_list[0]})
    html_dict.update({"card_name":attr_list[1]})
    html_dict.update({"card_setName":attr_list[2]})
    html_dict.update({"card_setID":s.set_id()})
    html_dict.update({"card_type":attr_list[3]})
    html_dict.update({"card_subtype":attr_list[4]})
    html_dict.update({"card_mana_cost":attr_list[5]})
    html_dict.update({"card_converted_cost":attr_list[6]})
    html_dict.update({"card_loyalty":attr_list[7]})
    html_dict.update({"card_rarity":attr_list[8]})
    html_dict.update({"card_text":attr_list[9]})
    html_dict.update({"card_flavor_text":attr_list[10]})
    html_dict.update({"card_power":attr_list[11]})
    html_dict.update({"card_toughness":attr_list[12]})
    html_dict.update({"card_price":attr_list[13]})

    return render(request, "ext_cards_template.html", html_dict)



def set_template(request, set_id):

    html_dict = {"navbar_template":nav_template}
    html_dict.update({"card_setID": set_id})
    html_dict.update({"lower_set_id": set_id.lower()})

    m_set = get_object_or_404(MagicSet, set_ID=set_id)

    html_dict.update({"set_name" : m_set.set_name})
    html_dict.update({"num_cards" : m_set.set_num_cards})
    html_dict.update({"release_date" : m_set.set_release_date})
    html_dict.update({"story_text" : m_set.set_story})
    html_dict.update({"details_text" : m_set.set_details.replace("{{num_cards}}",str(m_set.set_num_cards)).replace("{{release_date}}", str(m_set.set_release_date))})
    set_num_id =m_set.id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "ext_404.html")

    cards = []
    index = 0
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})
    return render(request,"ext_sets_template.html", html_dict)



def type_template(request, type_name): # changed from type_id
    html_dict = {"navbar_template":nav_template}
    #try:
     #   typeName = MagicType.objects.all().filter(id=type_id)[0].type_name
    #except:
    #    render(request, "ext_404.html")

    html_dict.update({"type_name":type_name})
    html_dict.update({"type_description": MagicType.objects.get(type_name = type_name).type_description})

    try:
        st = MagicType.objects.get(type_name = type_name).type_subtypes.all()
    except:
        render(request, "ext_404.html")
    else:
        subtypes = []
        for s in st:
            subtypes.append(s.subtype_name)

        html_dict.update({"sub":subtypes})

    return render(request, "ext_types_template.html", html_dict)

def testing(request):
    return render(request, "testing.html", {"navbar_template":nav_template})

def api_implement(request):
    html_dict = {"navbar_template":nav_template}
    req = urllib.request.urlopen("http://nbadb.pythonanywhere.com/api/years/?format=json")
    str_response = req.readall().decode('utf-8')
    loc = json.loads(str_response)
    id_list = []
    year_list = []
    recap_list = []
    mvp_list = []
    champion_list = []
    for x in loc:
        year_list.append(x.get("year"))
        recap_list.append(x.get("finals_recap"))
        champion_list.append(x.get("champion"))
        mvp_list.append(x.get("finals_mvp"))

    req = urllib.request.urlopen("http://nbadb.pythonanywhere.com/api/teams/?format=json")
    str_response = req.readall().decode('utf-8')
    teams = json.loads(str_response)
    for n in champion_list:
        temp_id = 0
        for t in teams:
            if (t.get("name") == n):
                temp_id = t.get("id")
                break
        id_list.append(temp_id)
    x = zip(id_list,year_list,recap_list,mvp_list,champion_list)
    z = list(x)
    html_dict.update({"teams":z})
    return render(request, "ext_api_page.html", html_dict)


class MagicSearchView(SearchView):

    def __init__(self, my_form_class=SearchForm):
        super(MagicSearchView, self).__init__(form_class=my_form_class)

    def get_or_results(self):
        q = self.get_query()
        if not q:
            return None
        sq = None
        for phrase in shlex.split(q):
            if not sq:
                sq = SQ(content=phrase)
            else:
                sq |= SQ(content=phrase)
        if not sq :
            return None
        return self.form.searchqueryset.filter(sq)

    def get_and_results(self):
        q = self.get_query()
        if not q:
            return None
        sq = None
        for phrase in shlex.split(q):
            if not sq:
                sq = SQ(content=phrase)
            else:
                sq &= SQ(content=phrase)
        if not sq :
            return None
        return self.form.searchqueryset.filter(sq)

    def create_response(self):
        """
        Generates the HttpResponse.
        """
        context = {
            'query': self.query,
            'terms': shlex.split(self.query),
            'form': self.form,
            'and_results': self.get_and_results(),
            'or_results': self.get_or_results(),
            'suggestion': None,
        }

        context.update(self.extra_context())
        return render_to_response(self.template, context, context_instance=self.context_class(self.request))














































#