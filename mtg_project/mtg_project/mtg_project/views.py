from django.shortcuts import render
from mtg_project.models import MagicCard, MagicSet, MagicType
import random

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
    return render(request, "splash_page.html", {"navbar_template":nav_template})

#SPLASH PAGE FOR SETS
def set_splash(request):
    global set_list
    html_dict = {"navbar_template":nav_template}
    sets = []

    for st in set_list:
        try:
            s = MagicSet.objects.get(set_ID=st)
        except:
            render(request, "404.html")
        else:
            s = s.__dict__
            set_id = s['set_ID']
            set_name = s['set_name']
            lower_set_id = set_id.lower()
            set_dict = {"id":set_id, "lower_id":lower_set_id, "name":set_name}
            sets.append(set_dict)
    html_dict.update({"set_list":sets})

    return render(request, "set_splash_page.html", html_dict)

#SPLASH PAGE FOR CARDS
def cards_splash(request):
    html_dict = {"navbar_template":nav_template}
    try:
        sets = list(MagicSet.objects.all())
    except:
        render(request, "404.html")
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
                render(request, "404.html")

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
                    render(request, "404.html")

            set_num += 1

        all_the_cards = zip(cards_to_render, set_ids)
        html_dict.update({"cards_and_sets":all_the_cards})

    return render(request, "cards_splash_page.html", html_dict)


#SPLASH PAGE FOR TYPES
def types_splash(request):
    html_dict = {"navbar_template":nav_template}
    types = []
    type_ids = []

    try:
        t = list(MagicType.objects.all())
    except:
        render(request, "404.html")
    else:
        for v in t:
            types.append(v.type_name)
            type_ids.append(v.id)

    result = zip(type_ids, types)
    html_dict.update({"types":result})
    return render(request, "types_splash.html", html_dict)

def unh(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"unh"})
    try:
        s = MagicSet.objects.all().filter(set_ID="UNH")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_unh.html", html_dict)

def ug(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"ug"})
    try:
        s = MagicSet.objects.all().filter(set_ID="UG")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_ug.html", html_dict)

def ths(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"ths"})
    try:
        s = MagicSet.objects.all().filter(set_ID="THS")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_ths.html", html_dict)

def rtr(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"rtr"})
    try:
        s = MagicSet.objects.all().filter(set_ID="RTR")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_rtr.html", html_dict)

def mma(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"mma"})
    try:
        s = MagicSet.objects.all().filter(set_ID="MMA")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_mma.html", html_dict)

def m14(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"m14"})
    try:
        s = MagicSet.objects.all().filter(set_ID="M14")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_m14.html", html_dict)

def jou(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"jou"})
    try:
        s = MagicSet.objects.all().filter(set_ID="JOU")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_jou.html", html_dict)

def gtc(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"gtc"})
    try:
        s = MagicSet.objects.all().filter(set_ID="GTC")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_gtc.html", html_dict)

def fut(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"fut"})
    try:
        s = MagicSet.objects.all().filter(set_ID="FUT")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_fut.html", html_dict)

def dgm(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"dma"})
    try:
        s = MagicSet.objects.all().filter(set_ID="DGM")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_dma.html", html_dict)

def cns(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"cns"})
    try:
        s = MagicSet.objects.all().filter(set_ID="CNS")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})

    return render(request, "set_cns.html", html_dict)

def bng(request):
    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id":"bng"})
    try:
        s = MagicSet.objects.all().filter(set_ID="BNG")
    except:
        render(request, "404.html")
    html_dict.update({"set_name":s[0].set_name})
    html_dict.update({"num_cards":s[0].set_num_cards})
    html_dict.update({"release_date":s[0].set_release_date})
    set_num_id = s[0].id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    for x in c:
        cards.append({"card_id":x.card_ID, "card_name":x.card_name})

    html_dict.update({"cards":cards})
    return render(request, "set_bng.html", html_dict)


#ABOUT PAGE
def about(request):
    return render(request, "about.html", {"navbar_template":nav_template})

#A TESTING PAGE
def sets_template(request):
    return render(request, "sets_template.html")

def enchantment_creature(request):
    return render(request, "type_enchantment_creature.html")

def legendary_creature(request):
    return render(request, "type_legendary_creature.html")

def artifact(request):
    return render(request, "type_artifact.html")

#THE HOW TO PLAY PAGE
def how_to_play(request):
    return render(request, "how_to_play.html", {"navbar_template":nav_template})


#THE 404 PAGE
def error(request):
    return render(request, "404.html")

#THE TEMPLATED PAGE THAT EVERY CARD USES
def card_template(request, card_id):
    html_dict = {"navbar_template":nav_template}
    try:
        attr_list = MagicCard.objects.get(card_ID = card_id)
    except:
        return render(request, "404.html")
    else:
        attr_list = attr_list.get_card_attr()

    try:
        s = MagicSet.objects.get(set_name=str(attr_list[2]))
    except:
        return render(request, "404.html")


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

    return render(request, "card.html", html_dict)


def type_template(request, type_id):
    html_dict = {"navbar_template":nav_template}
    try:
        typeName = MagicType.objects.all().filter(id=type_id)[0].type_name
    except:
        render(request, "404.html")

    html_dict.update({"type_name":typeName})

    try:
        st = MagicType.objects.get(id = type_id).type_subtypes.all()
    except:
        render(request, "404.html")
    else:
        subtypes = []
        for s in st:
            subtypes.append(s.subtype_name)

        html_dict.update({"sub":subtypes})

    return render(request, "type.html", html_dict)







