from django.shortcuts import get_object_or_404
from mtg_project.models import MagicCard, MagicSet, MagicType, MagicSubtype
from django.http import HttpResponse
import json
import copy



#Helper
EXCLUDE_KEYS = ['id', '_state']

def desired_keys(d, exclude_keys = None):
    if not exclude_keys:
        exclude_keys = EXCLUDE_KEYS
    c = copy.deepcopy(d)
    for key in exclude_keys:
        c.pop(key, None)
    return c;
    #return {key:d[key] for key in d if not key in exclude_keys}

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

#MagicCards
def magic_cards_all(request, indent = 4):

    if request.method == 'GET':
        r_dict = {"meta": {}}
        objects_list = []


        type_names_dict = {m_type.__dict__["id"]:m_type.__dict__["type_name"] for m_type in MagicType.objects.all()}
        subtype_names_dict = {m_subtype.__dict__["id"]:m_subtype.__dict__["subtype_name"] for m_subtype in MagicSubtype.objects.all()}
        set_names_dict = {m_set.__dict__["id"]:m_set.__dict__["set_name"] for m_set in MagicSet.objects.all()}

        for card in MagicCard.objects.all() :
            d = desired_keys(card.__dict__)
            d["card_type"] = type_names_dict[card.__dict__["card_type_id"]]
            d["card_setID"] = set_names_dict[card.__dict__["card_setID_id"]]

            d["card_subtype"] = None
            if d["card_subtype_id"] in subtype_names_dict :
                d["card_subtype"] = subtype_names_dict[card.__dict__["card_subtype_id"]]

            objects_list.append(d)




        r_dict["objects"] = objects_list
        return HttpResponse(json.dumps(r_dict, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

def magic_card_id(request, card_id, indent = 4):
    m_card = get_object_or_404(MagicCard, card_ID = card_id)
    if request.method == 'GET':
        d = desired_keys(m_card.__dict__)
        d["card_type"] = MagicType.objects.get(id = d["card_type_id"]).__dict__["type_name"]
        try:
            d["card_subtype"] = MagicSubtype.objects.get(id = d["card_subtype_id"]).__dict__["subtype_name"]
        except:
            d["card_subtype"] = None
        d["card_setID"] = MagicSet.objects.get(id = d["card_setID_id"]).__dict__["set_ID"]

        return HttpResponse(json.dumps(d, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)


#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

# MagicSets
def magic_sets_all(request, indent = 4):

    if request.method == 'GET':
        r_dict = {"meta" : {}}
        objects_list = [desired_keys(m_set.__dict__) for m_set in MagicSet.objects.all()]
        r_dict["objects"] = objects_list
        return HttpResponse(json.dumps(r_dict, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

def magic_set_id(request, set_id, indent = 4):

    m_set = get_object_or_404(MagicSet, set_ID=set_id)
    if request.method == 'GET':
        cards_in_set = [ card.__dict__['card_ID'] for card in MagicCard.objects.filter(card_setID = m_set) ]
        m_set.__dict__['set_cards'] = cards_in_set
        d = desired_keys(m_set.__dict__)

        return HttpResponse(json.dumps(d, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

#MagicTypes
def magic_types_all(request, indent = 4):
    if request.method == 'GET':
        r_dict = {"meta": {}}
        objects_list = [desired_keys(m_type.__dict__) for m_type in MagicType.objects.all()]
        r_dict["objects"] = objects_list

        return HttpResponse(json.dumps(r_dict, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

def magic_type_name(request,type_name, indent = 4):
    m_type = get_object_or_404(MagicType, type_name=type_name)
    if request.method == 'GET':
        t_subtypes =  list(m_type.type_subtypes.all().values('subtype_name'))  # change to just strings
        subtype_list = []
        for d in t_subtypes:
            subtype_list.append(d["subtype_name"])
        m_type.__dict__['type_subtypes'] = subtype_list
        d = desired_keys(m_type.__dict__)

        return HttpResponse(json.dumps(d, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#MagicSubtype
def magic_subtypes_all(request, indent = 4) :
    if request.method == 'GET':
        r_dict = {"meta": {}}
        objects_list = [desired_keys(m_subtype.__dict__) for m_subtype in  MagicSubtype.objects.all()]
        r_dict["objects"] = objects_list

        return HttpResponse(json.dumps(r_dict, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

def magic_subtype_name(request, subtype_name, indent = 4):
    m_subtype = get_object_or_404(MagicSubtype, subtype_name=subtype_name)
    if request.method == 'GET':
        t_supertypes = list(m_subtype.magic_subtype_set.all().values('type_name'))
        supertype_list = []
        for d in t_supertypes:
            supertype_list.append(d["type_name"])
        m_subtype.__dict__['subtype_supertypes'] = supertype_list
        d = desired_keys(m_subtype.__dict__)

        return HttpResponse(json.dumps(d, sort_keys = True, indent = indent), content_type="application/json")

    else:
        return HttpResponse("Method not allowed", status=400)

#for propert, value in vars(get_object_or_404(MagicType, type_name='Creature')).items():
#    print (propert, ": ", value)