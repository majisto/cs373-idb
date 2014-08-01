from django.shortcuts import render, get_object_or_404
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

set_story_dict = { "BNG" : "No longer content to walk the planes of the Multiverse seeking pleasure, the planeswalker Xenagos returns to Theros to become the god of revels. The boundaries that separate everyday existence from Nyx are growing dangerously thin. Strange creatures of enchantment, called Nyxborn or Born of the Gods, are pouring into the mortal world as Xenagos threatens to disrupt the very nature of the plane. Mogis, the god of slaughter sends hordes of mortal and Nyxborn minotaurs against the human cities Akros, Meletis and Setessa. Elspeth Tirel leads an army of heroes to break the minotaur siege at Akros. The humans were victorious, but the victory celebration after the battle becomes the ultimate ritual to launch Xenagos into Nyx as a god. Elspeth is blamed for his ascension and driven away in disgrace.",
                    "CNS" : "All new cards in Conspiracy depict the environment of the Paliano, the High City on the plane of Fiora, which is the home of Dack Fayden and the setting of the Magic comic book published by IDW",
                    "DGM" : "The Implicit Maze is a system of mana paths or leylines through the guildgates and districts of Plane that has manifested after the Guildpact was destroyed. On instruction of Niv-Mizzet and using Jace Beleren's notes, it was discovered by Ral Zarek. The maze was created by Azor I to be revealed in case the Guildpact dissolved. In this way, the founder of the Azorius Senate tried to foster an atmosphere of peaceful collaboration. At the end of the maze in the Forum of Azor lies great power. In order for it to be solved, all the guilds of Ravnica must participate at once. Niv-Mizzet has announced that each guild will has send one champion as its delegate in the running of the maze. At an appointed time, the champions meet at the Transguild Promenade, and embark on a race through the twists and turns of the maze. The one who triumphs, gains the power behind it for his or her guild. Others fall to its dangers.",
                    "FUT" : "The quest to mend Dominaria’s temporal and planar damage continues. A temporal rift connected to an alternate Dominaria has enabled Phyrexian horrors to cross over into the present day. Freyalise is gone, having given her planeswalker's spark and her life to close that rift, thereby protecting her sanctum of Skyshroud one last time.But time fractures still plague Dominaria. The damage to the planar fabric at Tolaria was so severe that it couldn't be healed — not in the present day. The heroes seek out the planeswalker Karn, the only being ever to travel through time. To heal Tolaria’s rift, Karn uses the full extent of his planeswalking power to enter the rift and return to the past, to the moment before the archwizard Barrin cast a spell that obliterated countless Phyrexians and himself. Karn succeeds and seals the planar rift before Barrin’s actions can rip it open. In the next moment, Karn is lost. Even as Venser begins to realize his full potential, the planeswalker Jeska returns to Dominaria for the first time since Karona fell. Her friend and ally Karn is gone, and someone will pay. An ancient, evil intelligence drives Jeska’s wrath and threatens to undermine Teferi and Jhoira’s efforts to complete Dominaria’s healing: Leshrac has returned.",
                    "GTC" : "Jace begins to piece together the greater mystery of the Implicit Maze. It's now a race to see who will unlock its secrets.",
                    "JOU" : "The plane of Theros is in chaos. Gods and mortals are pitted against each other, and terrifying monsters stalk the land. Heroes strive for glory while new and terrifying constellations take shape in the night sky. Supported by Ajani, Elspeth travels to Nyx and kills Xenagos. Afraid of her power, Heliod kils Elspeth.",
                    "M14" : "",
                    "MMA" : "",
                    "RTR" : "As the name of the expansion implies, Return to Ravnica is set in Ravnica, a plane comprising a singular megalopolis or ecumenopolis, in which a vast and diverse variety of inhabitants co-exist. Once, the law of city and plane of Ravnica was dictated by the Guildpact and was controlled in relative harmony by the ten guilds, each of which representing a color pairing of the five colors of Magic. In Dissension, however, the Guildpact had been broken. Faced with a magical code that is built into the very foundations of the city-world itself, Jace Beleren marches into the numinous depths of Ravnica’s underbelly in search of the promise of powerful magic. Once buried in past, the code resurfaces as Ravnica’s power-hungry mage guilds, unbound by the Guildpact that had once maintained order, struggle for control of the plane.",
                    "THS" : "Theros is watched over by a pantheon of 15 powerful gods. The gods, though residing in Nyx, are able to take on many forms and often walk among mortals. Each also has a unique color identity. The five core gods are mono-coloured and make up the central pillars of the Theran belief system. The colour identities of these five are: Heliod (white), Thassa (blue), Erebos (black), Purphoros (red), and Nylea (green). The ten minor gods represent the two colour pairings and will be introduced in Born of the Gods and Journey into Nyx.",
                    "UG"  : "All 94 cards in the Unglued set each had a single word printed on the bottom of the card. When combined in proper numerical order with other cards in the series spell out the following secret message: \"Here are some cards that didn't make it to print: Socks of Garfield, Hot Monkey Love, Colonel's Secret Recipe, Squee's Play, Banned in France, Spoon, Disrobing Scepter, Butt Wolf, Lotus Roach, Sesame Efreet, Needless Reminder Text, Chicken Choker, Clockwork Doppelganger, Henway, HELP I'M TRAPPED IN CARTA MUNDI, Mad Cow, Poke, Lord of Wombats, Gratuitous Babe Art, Brothers' War Bonds, Dwarven Kickboxer, Mickey's Drunk, Pact with the Wastes, CoP:BO, Urza's Chia Pet, Thallid Shooter, Shoelace, When Chihuahuas Attack, Wall of Cookies, Kobold Ninja, Mucusaur, Kjeldoran Outhouse, Bear in the Woods, Dental Thrull, Flavatog, Cereal Killer.\"",
                    "UNH" : "Much like Unglued before it, each card in the Unhinged set -including Super Secret Tech- has a single word printed on the bottom of the card after the artist's name and card number. When all cards are placed in the proper order with other cards in the series they spell out a \"secret message\" detailing cards that allegedly did not make it into the set. Placing all the Unhinged cards in reverse alphabetical order will cause the following message to appear: \"Here are some more cards that didn't make it: Moronic Tutor; Lint Golem; Wave of Incontinence; I'm Quitting Magic; Bob from Accounting; Castrate; Mishra's Bling Bling; Dead Bunny Isle; Circle of Protection: Pants; Time Fart; Sliver and Onions; Kobold Ass Master; Thanks, Barn; Mild Mongrel; Robo-Samurai; Obligatory Angel; Chump-Blocking Orphan; Wrath of Dog; Celery Stalker; Hugs-a-lot Demon; Assticore; Codpiece of the Chosen; Hurl; What the Cluck?!; Nachomancer; Scrubotomy; Arcbound Noah; Darksteel Spork; Look at Me, I'm Accounts Receivable; Hydro Djinn; Bad Stone Rain Variant; S.O.B.F.M.; Pinko Kami; Purple Nurple; Form of Uncle Istvan; Them's Fightin' Wards; Spleen of Ramos; Fifteenth Pick; Squizzle, Goblin Nabizzle; Zombie Cheerleading Squad; Two-Way Myr; Bone Flute 2: Electric Boogaloo; Magic Offline; Nutclamp; Bwahahahaaa!; Dragon Ass; Phyrexian Sno-Cone Machine; Chimney Pimp; R.T.F.C.; Greased Weasel; Flame War; We Don't Need No Stinkin' Merfolk; Ting!; and Disrobing Scepter (again!).\"" }



set_details_dict = {"BNG" : "Born of the Gods is a small set with {{num_cards}} cards. It was released on {{release_date}}.",
                    "CNS" : "Conspiracy is a special large set with {{num_cards}} cards. It was released on {{release_date}}.",
                    "DGM" : "Dragon's Maze is a small set with {{num_cards}} cards. It was released on {{release_date}}.",
                    "FUT" : "The set features {{num_cards}} cards, 81 of which are timeshifted \"pre-prints\", i.e. cards that have not been printed before but may appear in a future set, also known as futureshifted. Each of the cards features some quality that has never appeared in the game before, such as a new keyword ability (Fleshwrither), the application of a new keyword for an old ability (Thornweald Archer), or even referencing cards and card types that do not exist yet (Goldmeadow Lookout, Steamflogger Boss). Each of these unique aspects appear on only a small number of cards, indicating that they may be more properly explored in later sets. Additionally, most of the cards in some way reference unexplored planes, hinting at potential themes and locations for upcoming sets. The cards also feature a new \"futuristic\" card frame to hint at potential changes to the layout of Magic cards and to denote which cards are actually timeshifted. However, it has been confirmed that the Future Sight frame will not become the norm for subsequent sets. The new card frame sports specific symbols for different card types. As with Planar Chaos, the cards have the standard colored rarity symbols. It was released on {{release_date}}.",
                    "GTC" : "Gatecrash contains {{num_cards}} cards (101 commons, 80 uncommons, 53 rares, 15 mythic rares), including randomly inserted premium versions of all cards in the set. Like Return to Ravnica, the preceding expansion set, Gatecrash focuses on the guild system and multicolor cards. The five guilds returning in Gatecrash are the Boros Legion, House Dimir, Gruul Clans, Orzhov Syndicate, and Simic Combine. Despite being a large expansion, Gatecrash does not contain any basic lands (Return to Ravnica has some extra). The set features two planeswalkers; one, Gideon, Champion of Justice, is an established planeswalker, whilst the other, Domri Rade is a new. The expansion symbol is a pointed arch of a gate. It was released on {{release_date}}.",
                    "JOU" : "Like its predecessors, Journey into Nyx has a ancient Greek themed top-down design, making use of many mythological tropes. The set contains {{num_cards}} cards (60 Common, 60 Uncommon, 35 Rare, 10 Mythic) and includes randomly inserted premium versions of all cards. Fitting in with the \"enchantment matters\" theme, 59 of the set's 165 cards carry the enchantment type. The set introduces the Lamia creature type. It was released on {{release_date}}.",
                    "M14" : "Magic 2014 contains {{num_cards}} cards (101 Common, 60 Uncommon, 53 Rare, 15 Mythic, 20 Basic Lands), including randomly inserted premium versions of all cards. The returning mechanic for this Core Set was Slivers. Even more than the previous set, Magic 2014 is strongly integrated with its digital counterpart, Duels of the Planeswalkers. In celebration of Magic 's 20th anniversary, the logo of the set has the mythic orange / bronze color instead of the usual yellow or blue. The set puts the spotlight on Chandra. This meant a new Planeswalker card aimed at making a splash in Constructed, many Chandra-themed support cards, and flavor throughout the set attached to her persona. It was released on {{release_date}}.",
                    "MMA" : "Modern Masters is a {{num_cards}} card set consisting of reprints of cards originally printed between Eighth Edition and Alara Reborn. Thus every card is legal in the Modern format and other formats in which the sets are legal from which the cards originate. It was designed to fill the need of reprinting certain cards to make them more easily available to current or prospective Modern players, without re-introducing those cards into Standard. The set also does not contain any cards which are on the banned list of the Modern format at the time of its design. Modern Masters is exclusively booster-based, thus no satellite products such as Preconstructed decks are branded with the set. Each booster contains 15 playable cards: 10 commons, 3 uncommons and one rare or mythic rare, and one foil card of any rarity replacing the basic land which would normally be found in a booster as Modern Masters does not contain a run of basic lands. Due to the higher expected average value of the cards contained in a booster and the lower print run, the MSRP of one booster of Modern Masters is set to $6.99 (with the MSRP of a booster of the current draft set being $3.49). Due to the higher MSRP booster displays only contain 24 packs, which is also the number required for a regular draft (three boosters for each of eight players), as the set was designed specifically for draft. A number of cards also change rarity from their original printing as mythic rare wasn't introduced until the Alara block, and/or receive new artwork. It was released on {{release_date}}.",
                    "RTR" : "Return to Ravnica contains {{num_cards}} cards (25 basic lands, 101 commons, 80 uncommons, 53 rares, 15 mythic rares), including randomly inserted premium versions of all cards in the set. As was the case with the original Ravnica block, Return to Ravnica focuses on the guild system and multicolor cards. Five guilds — the Azorius Senate, Golgari Swarm, Izzet League, Cult of Rakdos, and Selesnya Conclave — are featured in Return to Ravnica; the other five guilds appear in the following expansion, Gatecrash. Because R&D had to fit in five guilds, rather than four, the set contained more uncommon cards than usual. It it is unknown what the expansion symbol of this is set is meant to represent, though some people think it is a stylized Orzhov Mitre. It was released on {{release_date}}.",
                    "THS" : "Theros contains {{num_cards}} cards (20 basic lands, 121 commons, 60 uncommons, 53 rares, 15 mythic rares), and includes randomly inserted premium versions of all cards. The set has an ancient Greek themed top-down design, making use of many mythological tropes (Heroes, Monsters and Gods). It is the first set to thematically take place on the plane of Theros. It is mostly monocolored with a handful of gold cards. Theros block is an enchantment block that plays off building blocks in M14 and Return to Ravnica block. The mood and tone are those of Greek myth: adventure, achievement, accomplishment, a hero's journey. Many existing creature types are reworked to match the Greek flavor. Apart from Minotaurs, it's not a tribal set. There are three Planeswalkers in the set, namely Elspeth and two new ones: Ashiok and Xenagos. There is an above average amount of legendary permanents. The expansion symbol depicts an stylized temple and altar. It was released on {{release_date}}.",
                    "UG"  : "The set included {{num_cards}} silver-border cards, 5 black-border cards (lands) and 6 Token creatures. The lands are special full art lands which have extended artwork inside an oval frame stretching from the top to bottom of the card. On top of that oval frame is a round gem of the appropriate color with the at the time current tap symbol. At the bottom is a slightly larger featuring the appropriate mana symbol. The top left corner has the name of the basic land while the bottom left corner simply reads \"Land\" with Artist and copyright information as well as collectors number running along the bottom. Unlike other sets which feature up to four distinct arts per basic land, Unglued only has one art per basic land. The rest of Unglued are silver-bordered joke cards which are still functional. Names, flavor texts, types and mechanics as well as the art featured on the card parody the game, individual cards, concepts, the history or players of the game. Unglued and its followup Unhinged are also the only sets in which the artwork of non-Planeswalker cards of extend outside the artframe. The card B.F.M. (Big Furry Monster) even extends over two cards. Some cards have specialized frames allowing for other jokes. Unglued also makes special mention of Chickens and Clamfolks as creature types. A follow up set, tentatively called Unglued 2: The Obligatory Sequel, never got made. This was another set than Unhinged. It was released on {{release_date}}.",
                    "UNH" : "Unhinged included {{num_cards}} silver-bordered cards and 5 black-bordered cards (the basic lands), all of which had foil versions which occur in a similar rate to \"normal\" Magic Sets. The set boasts many jokes, and has even set a precedent or two of its own for tournament-worthy Magic. Many cards are references to previous cards. The set is only available in English due to the difficulty to translate. Unhinged features a sixth color: pink. Water Gun Balloon Game can create a pink permanent and for abilities that let you produce mana of any color, you can choose {P} pink. However, there is no Unhinged (Basic) Land card that can produce pink mana. In addition, Avatar of Me can be whatever the color of your eyes are, allowing brown and hazel mana. One card, called Super Secret Tech, only exists as a foil rare card and technically affects the foil card concept as a whole. Its rarity is supposedly ten times more common than that of other Unhinged foil rare cards. It was released on {{release_date}}."}

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

def set_template(request, set_id):

    html_dict = {"navbar_template":nav_template}
    html_dict.update({"lower_set_id": set_id.lower()})

    m_set = get_object_or_404(MagicSet, set_ID=set_id)

    html_dict.update({"set_name" : m_set.set_name})
    html_dict.update({"num_cards" : m_set.set_num_cards})
    html_dict.update({"release_date" : m_set.set_release_date})
    html_dict.update({"story_text" : set_story_dict[set_id]})
    html_dict.update({"details_text" : set_details_dict[set_id].replace("{{num_cards}}",str(m_set.set_num_cards)).replace("{{release_date}}", str(m_set.set_release_date))})
    set_num_id =m_set.id

    try:
        c = MagicCard.objects.all().filter(card_setID_id=set_num_id)
    except:
        render(request, "404.html")

    cards = []
    index = 0
    for x in c:
        if index == 0 :
            temp = []
        temp.append({"card_id":x.card_ID, "card_name":x.card_name})
        index += 1
        if index == 5 :
            cards.append(temp)
            index = 0
    cards.append(temp)

    html_dict.update({"cards":cards})
    return render(request, "sets_template.html", html_dict)


#ABOUT PAGE
def about(request):
    return render(request, "ext_home_splash.html")

#A TESTING PAGE
# def sets_template(request):
#     return render(request, "sets_template.html")

# def enchantment_creature(request):
#     return render(request, "type_enchantment_creature.html")

# def legendary_creature(request):
#     return render(request, "type_legendary_creature.html")

# def artifact(request):
#     return render(request, "type_artifact.html")

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

    return render(request, "cards_template.html", html_dict)


def type_template(request, type_name): # changed from type_id
    html_dict = {"navbar_template":nav_template}
    #try:
     #   typeName = MagicType.objects.all().filter(id=type_id)[0].type_name
    #except:
    #    render(request, "404.html")

    html_dict.update({"type_name":type_name})

    try:
        st = MagicType.objects.get(type_name = type_name).type_subtypes.all()
    except:
        render(request, "404.html")
    else:
        subtypes = []
        for s in st:
            subtypes.append(s.subtype_name)

        html_dict.update({"sub":subtypes})

    return render(request, "types_template.html", html_dict)







