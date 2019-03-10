#########################
# Character Declaration #
#########################
#IMPORTANT CHARACTERS
define yum = Character("Yumi", color="#FFFFFF", voice_tag="yum", callback=speaker("yumi"))
define kam = Character("kam_name", color="#FFFFFF", voice_tag="kam", callback=speaker("kamika"), dynamic=True)
define sta = Character("Stacey", color="#FFFFFF", voice_tag="sta", callback=speaker("stacey"))
define luc = Character("luc_name", color="#FFFFFF", voice_tag="luc", callback=speaker("lucca"), dynamic=True)
define lev = Character("Levi", color="#FFFFFF", voice_tag="lev", callback=speaker("levi"))
define moe = Character("Moe", color="#FFFFFF", voice_tag="moe", callback=speaker("moe"))
define sat = Character("S-Tan", color="#FFFFFF", voice_tag="sat", callback=speaker("satan"))

init python:
    DefineImages('bgs', prepend='bg')
    DefineImages('cgs', prepend='cg')
    layerorder = ['base','mouth','eyes','brow','cry', 'cry0', 'cry1', 'cry2', 'cry3', 'cry4', 'cry5', 'blush', 'glasses', 'angryvein', 'sweatdrop']
    DefineImages("sprites", composite=True, overrideLayerOrder=layerorder)

        #use map emotes to compile complex emotions with layers

    #STACEY
    MapEmote('stacey smugclosed', 'stacey md_default ec_default brow_default')
    MapEmote('stacey smug', 'stacey base md_default ed_default brow_default')
    MapEmote('stacey confused', 'stacey md_flat ed_default brow_raised')
    MapEmote('stacey neutral', 'stacey md_sad ed_default brow_default')
    MapEmote('stacey neutrallook', 'stacey base md_sad ed_side brow_default')
    MapEmote('stacey smuglook', 'stacey base md_default ed_side brow_default')
    MapEmote('stacey grinclosed', 'stacey base mc_grin ec_side brow_default')
    MapEmote('stacey grin', 'stacey base mc_grin ed_default brow_default')
    MapEmote('stacey sarcasticlook', 'stacey base md_think ed_side brow_raised')
    MapEmote('stacey sarcastic', 'stacey base md_think ed_default brow_raised')
    MapEmote('stacey eyebrow', 'stacey base md_sad ed_default brow_raised')
    MapEmote('stacey eyebrowlook', 'stacey base md_sad ed_side brow_raised')
    MapEmote('stacey mad', 'stacey base md_sad ed_default brow_sad')
    MapEmote('stacey madclosed', 'stacey base md_sad ec_default brow_mad')
    MapEmote('stacey sadclosed', 'stacey base md_sad ec_default brow_sad')
    MapEmote('stacey therock', 'stacey base md_default ed_default brow_raised')

    #KAMIKA LOOKING AT READER, HUMAN DISGUISE
    MapEmote('kamika u thinkingclosed', 'kamika pose1 public md_default ec_default brow_furrow')
    MapEmote('kamika u thinking', 'kamika pose1 public md_default ed_default brow_furrow')
    MapEmote('kamika u evilgrin', 'kamika pose1 public mc_grin ed_squint brow_mad')
    MapEmote('kamika u surprise', 'kamika pose1 public m_shout ed_default brow_surprise')
    MapEmote('kamika u angrysurprise', 'kamika pose1 public m_shout ed_default brow_mad')
    MapEmote('kamika u shout', 'kamika pose1 public md_mad ed_default brow_mad angryvein')
    MapEmote('kamika u glare', 'kamika pose1 public md_sad ed_squint brow_mad')
    MapEmote('kamika u shoutclosed', 'kamika pose1 public md_mad ec_default brow_mad angryvein')
    MapEmote('kamika u mad', 'kamika pose1 public md_mad ed_default brow_mad')
    MapEmote('kamika u madclosed', 'kamika pose1 public md_mad ec_default brow_mad')
    MapEmote('kamika u confident', 'kamika pose1 public md_happy ed_default brow_mad')
    MapEmote('kamika u smugclosed', 'kamika pose1 public md_happy ec_default brow_sad')
    MapEmote('kamika u smug', 'kamika pose1 public md_happy ed_default brow_sad')
    MapEmote('kamika u smugsquint', 'kamika pose1 public md_happy ed_squint brow_sad')
    MapEmote('kamika u wideeyes', 'kamika pose1 public md_default ed_default brow_surprise')
    MapEmote('kamika u happyclosed', 'kamika pose1 public md_happy ec_happy brow_surprise')
    MapEmote('kamika u happy', 'kamika pose1 public md_happy ed_happy brow_surprise')
    MapEmote('kamika u sigh', 'kamika pose1 public md_mad happy ec_default brow_sad')
    MapEmote('kamika u silenced', 'kamika pose1 public mc_baka ed_default brow_surprise')
    MapEmote('kamika u pout', 'kamika pose1 public md_pout ed_default brow_mad')
    MapEmote('kamika u poutclosed', 'kamika pose1 public md_pout ec_default brow_mad')
    MapEmote('kamika u whine', 'kamika pose1 public md_sad ed_squint brow_sad cry0')
    MapEmote('kamika u exclaim', 'kamika pose1 public md_shout ed_default brow_surprise')
    MapEmote('kamika u neutral', 'kamika pose1 public md_default ed_default brow_default')
    MapEmote('kamika u neutralclosed', 'kamika pose1 public md_default ec_default brow_default')
    MapEmote('kamika u confidentclosed', 'kamika pose1 public md_happy ec_default brow_mad')
    MapEmote('kamika u licklips', 'kamika pose1 public m_licklips ed_squint brow_mad')
    MapEmote('kamika u seduce', 'kamika pose1 public md_happy ed_default brow_furrow')
    MapEmote('kamika u seducesquint', 'kamika pose1 public md_happy ed_squint brow_mad')
    MapEmote('kamika u mad', 'kamika pose1 public md_mad ed_default brow_mad')
    MapEmote('kamika u simmons', 'kamika pose1 public m_simmons ed_squint brow_raise')
    MapEmote('kamika u simmonsclosed', 'kamika pose1 public m_simmons ec_happy brow_raise')
    MapEmote('kamika u questionsquint', 'kamika pose1 public md_pout ed_squint brow_raise')
    MapEmote('kamika u question', 'kamika pose1 public md_pout ed_default brow_raise')
    MapEmote('kamika u deadpan', 'kamika pose1 public md_frownside ed_squint brow_default')
    MapEmote('kamika u confused', 'kamika pose1 public md_frownside ed_default brow_raise')
    MapEmote('kamika u shoutclosed', 'kamika pose1 public md_mad ec_default brow_mad angryvein')
    MapEmote('kamika u evilsmile', 'kamika pose1 public md_happy ed_default brow_mad')
    MapEmote('kamika u evilsmileclosed', 'kamika pose1 public md_happy ec_default brow_mad')
    MapEmote('kamika u evilgrin', 'kamika pose1 public mc_grin ec_default brow_mad')
    MapEmote('kamika u badliar', 'kamika pose1 public md_happy ed_happy brow_sad')
    MapEmote('kamika u badliarclosed', 'kamika pose1 public md_happy ec_happy brow_sad')
    MapEmote('kamika u squirm', 'kamika pose1 public mc_grin ec_happy brow_sad')
    MapEmote('kamika u evilsmileclosed', 'kamika pose1 public md_happy ed_squint brow_mad')
    MapEmote('kamika u panic', 'kamika pose1 public m_shout ed_default brow_surprise')
    MapEmote('kamika u desperate', 'kamika pose1 public md_happy ed_default brow_sad')
    MapEmote('kamika u desperateclosed', 'kamika pose1 public md_happy ec_default brow_sad')
    MapEmote('kamika u ouch', 'kamika pose1 public m_shout ec_default brow_mad')
    MapEmote('kamika u eyebrow', 'kamika pose1 public md_default ed_default brow_raise')
    MapEmote('kamika u sad', 'kamika pose1 public md_sad ed_default brow_sad')
    MapEmote('kamika u sadclosed', 'kamika pose1 public md_sad ec_default brow_sad')
    MapEmote('kamika u sadsquint', 'kamika pose1 public md_sad ed_squint brow_sad')
    MapEmote('kamika u seduceclosed', 'kamika pose1 public md_happy ec_default brow_furrow')
    MapEmote('kamika u evilsmilesquint', 'kamika pose1 public md_happy ed_squint brow_mad')
    #PAST THIS POINT IS NEW SHIT

    #KAMIKA LOOKING AT READER (DEMON FORM)
    MapEmote('kamika d thinkingclosed', 'kamika pose1 base md_default ec_default brow_furrow')
    MapEmote('kamika d thinking', 'kamika pose1 base md_default ed_default brow_furrow')
    MapEmote('kamika d evilgrin', 'kamika pose1 base mc_grin ed_squint brow_mad')
    MapEmote('kamika d surprise', 'kamika pose1 base m_shout ed_default brow_surprise')
    MapEmote('kamika d angrysurprise', 'kamika pose1 base m_shout ed_default brow_mad')
    MapEmote('kamika d shout', 'kamika pose1 base md_mad ed_default brow_mad angryvein')
    MapEmote('kamika d glare', 'kamika pose1 base md_sad ed_squint brow_mad')
    MapEmote('kamika d shoutclosed', 'kamika pose1 base md_mad ec_default brow_mad angryvein')
    MapEmote('kamika d mad', 'kamika pose1 base md_mad ed_default brow_mad')
    MapEmote('kamika d madclosed', 'kamika pose1 base md_mad ec_default brow_mad')
    MapEmote('kamika d confident', 'kamika pose1 base md_happy ed_default brow_mad')
    MapEmote('kamika d smugclosed', 'kamika pose1 base md_happy ec_default brow_sad')
    MapEmote('kamika d smug', 'kamika pose1 base md_happy ed_default brow_sad')
    MapEmote('kamika d smugsquint', 'kamika pose1 base md_happy ed_squint brow_sad')
    MapEmote('kamika d wideeyes', 'kamika pose1 base md_default ed_default brow_surprise')
    MapEmote('kamika d happyclosed', 'kamika pose1 base md_happy ec_happy brow_surprise')
    MapEmote('kamika d happy', 'kamika pose1 base md_happy ed_happy brow_surprise')
    MapEmote('kamika d sigh', 'kamika pose1 base md_mad happy ec_default brow_sad')
    MapEmote('kamika d silenced', 'kamika pose1 base mc_baka ed_default brow_surprise')
    MapEmote('kamika d pout', 'kamika pose1 base md_pout ed_default brow_mad')
    MapEmote('kamika d whine', 'kamika pose1 base md_sad ed_squint brow_sad cry0')
    MapEmote('kamika d exclaim', 'kamika pose1 base md_shout ed_default brow_surprise')
    MapEmote('kamika d neutral', 'kamika pose1 base md_default ed_default brow_default')
    MapEmote('kamika d neutralclosed', 'kamika pose1 base md_default ec_default brow_default')
    MapEmote('kamika d confidentclosed', 'kamika pose1 base md_happy ec_default brow_mad')
    MapEmote('kamika d licklips', 'kamika pose1 base m_licklips ed_squint brow_mad')
    MapEmote('kamika d seduce', 'kamika pose1 base md_happy ed_default brow_furrow')
    MapEmote('kamika d seduceclosed', 'kamika pose1 base md_happy ec_default brow_furrow')
    MapEmote('kamika d seducesquint', 'kamika pose1 base md_happy ed_squint brow_mad')
    MapEmote('kamika d mad', 'kamika pose1 base md_mad ed_default brow_mad')
    MapEmote('kamika d simmons', 'kamika pose1 base m_simmons ed_squint brow_raise')
    MapEmote('kamika d simmonsclosed', 'kamika pose1 base m_simmons ec_happy brow_raise')
    MapEmote('kamika d questionsquint', 'kamika pose1 base md_pout ed_squint brow_raise')
    MapEmote('kamika d question', 'kamika pose1 base md_pout ed_default brow_raise')
    MapEmote('kamika d deadpan', 'kamika pose1 base md_frownside ed_squint brow_default')
    MapEmote('kamika d confused', 'kamika pose1 base md_frownside ed_default brow_raise')
    MapEmote('kamika d shoutclosed', 'kamika pose1 base md_mad ec_default brow_mad angryvein')
    MapEmote('kamika d evilsmile', 'kamika pose1 base md_happy ed_default brow_mad')
    MapEmote('kamika d evilsmileclosed', 'kamika pose1 base md_happy ec_default brow_mad')
    MapEmote('kamika d evilgrin', 'kamika pose1 base mc_grin ec_default brow_mad')
    MapEmote('kamika d badliar', 'kamika pose1 base md_happy ed_happy brow_sad')
    MapEmote('kamika d badliarclosed', 'kamika pose1 base md_happy ec_happy brow_sad')
    MapEmote('kamika d squirm', 'kamika pose1 base mc_grin ec_happy brow_sad')
    MapEmote('kamika d evilsmileclosed', 'kamika pose1 base md_happy ed_squint brow_mad')
    MapEmote('kamika d panic', 'kamika pose1 base m_shout ed_default brow_surprise')
    MapEmote('kamika d desperate', 'kamika pose1 base md_happy ed_default brow_sad')
    MapEmote('kamika d desperateclosed', 'kamika pose1 base md_happy ec_default brow_sad')
    MapEmote('kamika d ouch', 'kamika pose1 base m_shout ec_default brow_mad')
    MapEmote('kamika d eyebrow', 'kamika pose1 base md_default ed_default brow_raise')
    MapEmote('kamika d sad', 'kamika pose1 base md_sad ed_default brow_sad')
    MapEmote('kamika d sadclosed', 'kamika pose1 base md_sad ec_default brow_sad')
    MapEmote('kamika d sadsquint', 'kamika pose1 base md_sad ed_squint brow_sad')
    MapEmote('kamika d poutclosed', 'kamika pose1 base md_pout ed_default brow_mad')
    MapEmote('kamika d evilsmilesquint', 'kamika pose1 base md_happy ed_squint brow_mad')
    #PAST THIS POINT IS NEW SHIT


    #KAMIKA LOOKING AWAY
    MapEmote('kamika s annoyedside', 'kamika pose2 base md_default ed_aside brow_mad')
    MapEmote('kamika s sigh', 'kamika pose2 base md_default ec_default brow_mad')
    MapEmote('kamika s annoyed', 'kamika pose2 base md_default ed_default brow_mad')
    MapEmote('kamika s simmonsclosed', 'kamika pose2 base md_simmons ec_happy brow_mad')
    MapEmote('kamika s smug', 'kamika pose2 base md_smirk ed_default brow_mad')
    MapEmote('kamika s hystericallaugh', 'kamika pose2 base m_happy ec_happy brow_mad')
    MapEmote('kamika s annoyedclosed', 'kamika pose2 base md_default ec_default brow_mad')
    MapEmote('kamika s grit', 'kamika pose2 base mc_grimace ed_default brow_mad')
    MapEmote('kamika s gritclosed', 'kamika pose2 base mc_grimace ec_default brow_mad')
    MapEmote('kamika s gritside', 'kamika pose2 base mc_grimace ed_aside brow_mad')
    MapEmote('kamika s sad', 'kamika pose2 base md_default ed_default brow_sad')
    MapEmote('kamika s sadside', 'kamika pose2 base md_default ed_aside brow_sad')

    #LUCCA
    MapEmote('lucca h neutral', 'lucca base md_default ed_default brow_default')
    MapEmote('lucca h nervous', 'lucca base md_default ed_default brow_sad')
    MapEmote('lucca h nervousopen', 'lucca base m_default ed_default brow_sad')
    MapEmote('lucca h nervousclose', 'lucca base md_default ec_default brow_sad')
    MapEmote('lucca h nervouser', 'lucca base md_default ed_default brow_sadder')
    MapEmote('lucca h nervouseropen', 'lucca base m_default ed_default brow_sadder')
    MapEmote('lucca h sigh', 'lucca base m_sad ec_default brow_sad')
    MapEmote('lucca h uwah', 'lucca base m_uwah ec_uwah brow_sad')
    MapEmote('lucca h doh', 'lucca base mc_default ec_uwah brow_sadder blush')
    MapEmote('lucca h happy', 'lucca base md_happy ed_happy brow_default')
    MapEmote('lucca h happyclosed', 'lucca base md_happy ec_happy brow_default')
    MapEmote('lucca h bashful', 'lucca base md_happy ed_happy brow_sad')
    MapEmote('lucca h ohno', 'lucca base md_uwah ed_default brow_sad')
    MapEmote('lucca h aaaa', 'lucca base m_uwah ed_default brow_sad')
    MapEmote('lucca h bigaaaa', 'lucca base m_uwah ed_default brow_sadder')
    MapEmote('lucca h nervoussmile', 'lucca base md_happy ed_default brow_sad')
    MapEmote('lucca h guilty', 'lucca base md_sad ec_default brow_sad')
    MapEmote('lucca h mad', 'lucca base md_mad ed_default brow_mad')
    MapEmote('lucca h madblush', 'lucca base md_mad ed_default brow_mad blush')
    MapEmote('lucca h happy', 'lucca base md_happy ed_happy brow_sad')
    MapEmote('lucca h sad', 'lucca base md_sad ed_sad brow_sad')
    MapEmote('lucca h sadsmile', 'lucca base md_happy ed_sad brow_sad')

    #LUCCA WITHOUT HAT
    MapEmote('lucca n neutral', 'lucca nohat md_default ed_default brow_default')
    MapEmote('lucca n nervous', 'lucca nohat md_default ed_default brow_sad')
    MapEmote('lucca n nervousopen', 'lucca nohat m_default ed_default brow_sad')
    MapEmote('lucca n nervousclose', 'lucca nohat md_default ec_default brow_sad')
    MapEmote('lucca n nervouser', 'lucca nohat md_default ed_default brow_sadder')
    MapEmote('lucca n nervouseropen', 'lucca nohat m_default ed_default brow_sadder')
    MapEmote('lucca n sigh', 'lucca nohat m_sad ec_default brow_sad')
    MapEmote('lucca n uwah', 'lucca nohat m_uwah ec_uwah brow_sad')
    MapEmote('lucca n doh', 'lucca nohat mc_default ec_uwah brow_sadder blush')
    MapEmote('lucca n happy', 'lucca nohat md_happy ed_happy brow_default')
    MapEmote('lucca n happyclosed', 'lucca nohat md_happy ec_happy brow_default')
    MapEmote('lucca n bashful', 'lucca nohat md_happy ed_happy brow_sad')
    MapEmote('lucca n ohno', 'lucca nohat md_uwah ed_default brow_sad')
    MapEmote('lucca n aaaa', 'lucca nohat m_uwah ed_default brow_sad')
    MapEmote('lucca n bigaaaa', 'lucca nohat m_uwah ed_default brow_sadder')
    MapEmote('lucca n nervoussmile', 'lucca nohat md_happy ed_default brow_sad')
    MapEmote('lucca n guilty', 'lucca nohat md_sad ec_default brow_sad')
    MapEmote('lucca n mad', 'lucca nohat md_mad ed_default brow_mad')
    MapEmote('lucca n madblush', 'lucca nohat md_mad ed_default brow_mad blush')
    MapEmote('lucca n happy', 'lucca nohat md_happy ed_happy brow_sad')
    MapEmote('lucca n sad', 'lucca nohat md_sad ed_sad brow_sad')
    MapEmote('lucca n sadsmile', 'lucca nohat md_happy ed_sad brow_sad')

    #MOE
    MapEmote('moe neutral', 'moe base md_default brow_default')
    MapEmote('moe neutrallook', 'moe base md_default ed_side brow_default')
    MapEmote('moe squint', 'moe base md_default ed_squint brow_default')
    MapEmote('moe neutralclosed', 'moe base md_default ec_default brow_default')
    MapEmote('moe madside', 'moe base md_default ed_side brow_mad')
    MapEmote('moe mad', 'moe base md_default ed_default brow_mad')
    MapEmote('moe madclosed', 'moe base md_default ec_default brow_mad')
    MapEmote('moe sigh', 'moe base md_default ec_default brow_sad')
    MapEmote('moe sighsweat', 'moe base md_default ec_default brow_sad sweatdrop')
    MapEmote('moe smug', 'moe base md_happy ed_default brow_mad')
    MapEmote('moe smuglook', 'moe base md_happy ed_side brow_mad')
    MapEmote('moe smugclosed', 'moe base md_happy ec_default brow_mad')


    #MADE BY ALF, DOUBLECHECK LATER
    MapEmote('stacey neutralclosed', 'stacey base md_sad ec_default brow_default')
    MapEmote('stacey therocklook', 'stacey base md_default ed_side brow_raised')
    MapEmote('stacey evil', 'stacey base md_default ed_default brow_mad')
    MapEmote('stacey madlook', 'stacey base md_sad ed_side brow_mad')
    MapEmote('stacey eyebrowclosed', 'stacey base md_sad ec_default brow_raised')
    MapEmote('lucca h waah', 'lucca base md_default ed_default brow_sadder cry1')
    MapEmote('lucca h sniff', 'lucca base md_sad ed_default brow_sad cry1')
    MapEmote('lucca n waah', 'lucca nohat md_default ed_default brow_sadder cry1')
    MapEmote('lucca n sniff', 'lucca nohat md_sad ed_default brow_sad cry1')
    MapEmote('kamika u quiet', 'kamika pose1 public md_default ed_default brow_sad')
    MapEmote('kamika d quiet', 'kamika pose1 base md_default ed_default brow_sad')
    MapEmote('kamika u disappointed', 'kamika pose1 public md_default ec_default brow_sad')
    MapEmote('kamika d disappointed', 'kamika pose1 base md_default ec_default brow_sad')
    MapEmote('kamika u seducetongue', 'kamika pose1 public m_lick ed_default brow_sad')
    MapEmote('kamika d seducetongue', 'kamika pose1 base m_lick ed_default brow_sad')
    MapEmote('kamika u stew', 'kamika pose1 public mc_baka ed_default brow_mad')
    MapEmote('kamika d stew', 'kamika pose1 base mc_baka ed_default brow_mad')
    MapEmote('kamika u quietsquint', 'kamika pose1 public md_default ed_squint brow_sad')
    MapEmote('kamika d quietsquint', 'kamika pose1 base md_default ed_squint brow_sad')
    MapEmote('kamika u shock', 'kamika pose1 public md_default ed_default brow_surprise')
    MapEmote('kamika d shock', 'kamika pose1 base md_default ed_default brow_surprise')
    MapEmote('kamika u quietclosed', 'kamika pose1 public md_default ec_default brow_sad')
    MapEmote('kamika d quietclosed', 'kamika pose1 base md_default ec_default brow_sad')
    MapEmote('kamika u sob', 'kamika pose1 public md_default ed_default brow_sad cry3')
    MapEmote('kamika d sob', 'kamika pose1 base md_default ed_default brow_sad cry3')
    MapEmote('kamika u sobsquint', 'kamika pose1 public md_default ed_squint brow_sad cry3')
    MapEmote('kamika d sobsquint', 'kamika pose1 base md_default ed_squint brow_sad cry3')
    MapEmote('kamika u screamclosed', 'kamika pose1 public md_mad ec_happy brow_mad')
    MapEmote('kamika d screamclosed', 'kamika pose1 base md_mad ec_happy brow_mad')
    MapEmote('kamika u madcry', 'kamika pose1 public md_mad ed_default brow_mad cry2')
    MapEmote('kamika d madcry', 'kamika pose1 base md_mad ed_default brow_mad cry2')
    MapEmote('kamika u madcrysquint', 'kamika pose1 public md_mad ed_squint brow_mad cry3')
    MapEmote('kamika d madcrysquint', 'kamika pose1 base md_mad ed_squint brow_mad cry3')
    MapEmote('kamika u surprisecry', 'kamika pose1 public md_default ed_default brow_surprise cry2')
    MapEmote('kamika d surprisecry', 'kamika pose1 base md_default ed_default brow_surprise cry2')

#MINOR CHARACTERS
define dee = Character('Mr. Deeks', color="#FFFFFF", voice_tag="dee")
define ber = Character('Mrs. Bern.', color="#FFFFFF", voice_tag="ber")
define mst = Character('M. Student', color="#FFFFFF", voice_tag="mst")
define fst = Character('F. Student', color="#FFFFFF", voice_tag="fst")
define pg1 = Character('Rando 1', color="#FFFFFF", voice_tag="pg1")
define pg2 = Character('Rando 2', color="#FFFFFF", voice_tag="pg2")

######################
# Flags              #
######################
default minion = False
default sawstacey = False
default helpkamika = False
default kamika_points = 0
default stacey_points = 0
default lucca_points = 0
default prismpower = False
default staceyroute = False
default luccaroute = False
default kamikaroute = False

##################
# BG Declaration #
##################

image cafe = "bgs/cafe.png"
image classroom = "bgs/classroom.png"
image dormbed = "bgs/dormbed.png"
image dormhallway = "bgs/dormhallway.png"
image dormroom = "bgs/dormroom.png"
image lecturehall = "bgs/lecturehall.png"
image outsidedorm = "bgs/outsidedorm.png"
image outsideschool = "bgs/outsideschool.png"
image paintingroom = "bgs/paintingroom.png"
image rooftopnight = "bgs/rooftopnight.png"
image dumpsters = "bgs/dumpsters.png"
image moeroom = "bgs/moeroom.png"
image classhallway = "bgs/classhallway.png"
image alley = "bgs/alley.png"
image foresttrail = "bgs/foresttrail.png"
image graffitiwoods = "bgs/graffitiwoods.png"
image library = "bgs/library.png"
image ruins = "bgs/ruins.png"
image outsidedormnight = "bgs/outsidedormnight.png"
image outsideschoolnight = "bgs/outsideschoolnight.png"
image foresttrailnight = "bgs/foresttrailnight.png"
image dormroomparty = "bgs/partydorm_bg_edit.png"
image dormaftermath = "bgs/partydorm_bg_edit2.png"

###################
# CGs             #
###################

#FULL CGS
image phonedefault = "cgs/phone/phone_default.png"
image phone1 calling = "cgs/phone/phone_calling.png"
image phone1 levineutral = "cgs/phone/phone_levi1.png"
image phone1 levieyebrow = "cgs/phone/phone_levi2.png"
image phone1 levideadpan = "cgs/phone/phone_levi3.png"
image phone1 levirant = "cgs/phone/phone_levi4.png"
image phone1 levisigh = "cgs/phone/phone_levi5.png"
image phone1 stanhappy = "cgs/phone/phone_s-tan1.png"
image phone1 stanwink = "cgs/phone/phone_s-tan2.png"
image phone1 stanclosed = "cgs/phone/phone_s-tan3.png"
image phoneyumi neutrallisten = "cgs/phone/phone_yumi1.png"
image phoneyumi neutraltalk = "cgs/phone/phone_yumi2.png"
image phoneyumi eyebrow = "cgs/phone/phone_yumi3.png"
image phoneyumi surprise = "cgs/phone/phone_yumi4.png"
image phoneyumi dread = "cgs/phone/phone_yumi5.png"
image phoneyumi rant = "cgs/phone/phone_yumi6.png"
image phoneyumi annoyed = "cgs/phone/phone_yumi7.png"
image phoneyumi sigh = "cgs/phone/phone_yumi8.png"

image laptop nc = "cgs/laptop/Laptop 1v2.png"
image laptop km = "cgs/laptop/Laptop 2v2.png"
image laptop y = "cgs/laptop/Laptop 3v2.png"
image laptop ky = "cgs/laptop/Laptop 4v2.png"
image laptop ks = "cgs/laptop/Laptop 5v2.png"
image laptop default = "cgs/laptop/laptopdefault.png"

image slide powerpoint1 = "cgs/laptop/powerpoint1.png"
image slide powerpoint2 = "cgs/laptop/powerpoint2.png"
image slide powerpoint3 = "cgs/laptop/powerpoint3.png"
image slide powerpoint4 = "cgs/laptop/powerpoint4.png"
image slide powerpoint5 = "cgs/laptop/powerpoint5.png"
image slide powerpointtitle = "cgs/laptop/powerpointtitle.png"
image slide shittyearth = "cgs/laptop/shittyearth.png"
image slide kamikawins = "cgs/laptop/shittykamika.png"
image slide kamikadraw = "cgs/laptop/shittykamika1.png"
image laptop playlist = "cgs/laptop/playlist.png"

image moeintro = "cgs/MoeIntroCG.png"
image kamikaintro = "cgs/KamikaIntroCG.png"

image kamikabed1 = "cgs/kamika_bed_1.png"
image kamikabed2 = "cgs/kamika_bed_2.png"

image jojo1 = "cgs/showdown/Scene 9-1 p1v4 (Resized).png"
image jojo2 = "cgs/showdown/Scene 9-1 Jojo v4 (Resized).png"

image rooftop1 = "cgs/Scene 18 v4 16x9Cropped Resized.png"
image rooftop2 = "cgs/Scene 18 v4 Resized.png"

image moesmolder1 = "cgs/moedemongrills2_cg__smolder1__ad.png"
image moesmolder2 = "cgs/moedemongrills2_cg__smolder0__ad.png"

image energyspark one = "cgs/energyspark1.png"
image energyspark two = "cgs/energyspark2.png"

image rehearsal neutral = "cgs/stacydemongrills2_cg__rehearse_1_ad.png"
image rehearsal pout = "cgs/stacydemongrills2_cg__rehearse_2_ad.png"
image rehearsal look = "cgs/stacydemongrills2_cg__rehearse_3_ad.png"

image moesmoulder default = "cgs/moedemongrills2_cg__smolder1__ad.png"
image moesmoulder maximum = "cgs/moedemongrills2_cg__smolder0__ad.png"

image kamikapose butt = "cgs/kamikademongrills2_cg_'pose1'_ad.png"
image kamikapose shiny = "cgs/kamikademongrills2_cg_'pose2'_ad.png"

image kamikaend = "cgs/Scene 18 v4 16x9Cropped Resized.png"

#MINOR CGS
image transformdemon = "cgs/transformdemon.png"
image transformhuman = "cgs/transformhuman.png"

image sexfogf = "cgs/sexfogfront.png"
image sexfogb = "cgs/sexfogback.png"
image white = "bgs/white.png"

#######
# VFX #
#######

###################
# SFX             #
###################
define turnpage = "sfx/turn_page_thick_magazine_002.wav"
define smack = "sfx/Desk Smack.ogg"
define slam = "sfx/Desk Slam.ogg"
define bump = "sfx/Bump.ogg"
define shove = "sfx/Shove.ogg"
define dooropen = "sfx/Door Open.ogg"
define doorclose = "sfx/Door Close.ogg"
define clatter = "sfx/Trash Can.ogg"
define aerosolcan = "sfx/Aerosol Can.ogg"
define doorslam = "sfx/Door Slam.ogg"
define feedback = "sfx/Mic Feedback Alt.ogg"
define doorunlock = "sfx/Door Unlock.ogg"
define bedsprings = "sfx/Bed Springs.ogg"
define click  = "sfx/Click.ogg"
define slidewindow  = "sfx/Window Slide.ogg"
define ringtone = "sfx/Cell Ring.ogg"
define beep = "sfx/Beep.ogg"
define phonevibrate = "sfx/Cell Vibrate.ogg"
define explosion = "sfx/Explosion.ogg"
define throw = "sfx/Throw.ogg"
define cheer = "sfx/Cheering.ogg"
define stomping = "sfx/Stomping.ogg"
define thud = "sfx/Thud.ogg"
define chuckle = "sfx/Laughter.ogg"

#SUSPECT
define pillowsmack = "sfx/Pillow Smack.ogg"
define charge2 = "ambient/Power Up Greater.ogg"
define charge1 = "ambient/Power Up Lesser.ogg"
define doorknock = "sfx/doorknock.ogg"

###################
# Music           #
###################
define titlescreen = "music/Title Screen.ogg"
define ourlastnighttogether = "music/Our Last Night Together - Kamica Song.ogg"
define classtime = "music/Class Time.ogg"
define evilplot = "music/Evil Plot.ogg"
define funkyjam = "music/Funky Jam.ogg"
define kamevil = "music/Kamica Dark Theme_.ogg"
define kamseduce = "music/Kamica Seduction.ogg"
define kamtheme = "music/Kamica Theme.ogg"
define kamreflect = "music/Kamika Reflection.ogg"
define luccatheme = "music/Lucca Theme looped.ogg"
define feels = "music/Much Feels.ogg"
define holdmusic = "music/Phone-On-Hold-Music-_loop_.ogg"
define rave = "music/Rave Music.ogg"
define sadsong = "music/Sad Song.ogg"
define happysong = "music/So Happy.ogg"
define staceytheme = "music/Stacey_s Theme.ogg"
define wordfight = "music/Word Fight.ogg"
define dramamusic = "music/Drama Scene.ogg"
define stantheme = "music/Magical Main.ogg"
define neutralmusic = "music/bensound-theelevatorbossanova.mp3"
define happysong2 = "music/Quircky Shop.ogg"
define moetheme = "music/bensound-sexy.mp3"

###################
# Ambient         #
###################

init python:
    renpy.music.register_channel("ambient","sfx",loop=True,tight=True)

define cafeamb = "ambient/Cafe BFX.ogg"
define showeramb = "ambient/Shower BFX.ogg"
define showerambbehind = "ambient/Shower from Behind Door _ _Steam for Pheromone use_ BFX.ogg"
define trafficamb = "ambient/Traffic BFX.ogg"
define forestamb = "ambient/427400__imjeax__forest-ambient-loop.wav"
define partybass = "ambient/Party.ogg"
define quake = "ambient/Ramble.ogg"

label start:
    jump scene1
