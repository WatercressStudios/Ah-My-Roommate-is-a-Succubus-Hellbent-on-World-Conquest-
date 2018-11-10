#########################
# Character Declaration #
#########################
#IMPORTANT CHARACTERS
define yum = Character("Yumi", color="#FFFFFF", voice_tag="yum", callback=speaker("yumi"))
define kam = Character("Kamika", color="#FFFFFF", voice_tag="kam", callback=speaker("kamika"))
define sta = Character("Stacey", color="#FFFFFF", voice_tag="sta", callback=speaker("stacey"))
define luc = Character("Lucca", color="#FFFFFF", voice_tag="luc", callback=speaker("lucca"))
define lev = Character("Levi", color="#FFFFFF", voice_tag="lev", callback=speaker("levi"))
define moe = Character("Moe", color="#FFFFFF", voice_tag="moe", callback=speaker("moe"))
define sat = Character("S-Tan", color="#FFFFFF", voice_tag="sat", callback=speaker("satan"))

init python:
    DefineImages('bgs', prepend='bg')
    DefineImages('cgs', prepend='cg')
    layerorder = ['base','mouth','eyes','brow','cry', 'glasses', 'optional']
    DefineImages("sprites", overrideLayerOrder=layerorder)

        #use map emotes to compile complex emotions with layers

    #STACEY
    MapEmote('stacey smugclosed', 'stacey base md default ec default brow default')
    MapEmote('stacey smug', 'stacey base md default ed default brow default')
    MapEmote('stacey confused', 'stacey base md flat ed default brow raised')
    MapEmote('stacey neutral', 'stacey base md sad ed default brow default')
    MapEmote('stacey neutrallook', 'stacey base md sad ed side brow default')
    MapEmote('stacey smuglook', 'stacey base md default ed side brow default')
    MapEmote('stacey grinclosed', 'stacey base mc grin ec default side brow default')
    MapEmote('stacey grin', 'stacey base mc grin ed default brow default')
    MapEmote('stacey sarcasticlook', 'stacey base md think ed side brow raised')
    MapEmote('stacey sarcastic', 'stacey base md think ed default brow raised')
    MapEmote('stacey eyebrow', 'stacey base md sad ed default brow raised')
    MapEmote('stacey sad', 'stacey base md sad ed default brow sad')
    MapEmote('stacey sadclosed', 'stacey base md sad ec default brow sad')
    MapEmote('stacey therock', 'stacey base md default ed default brow raised')

    #KAMIKA LOOKING AT READER, HUMAN DISGUISE
    MapEmote('kamika u thinkingclosed', 'kamika pose1 public md default ec default brow furrow')
    MapEmote('kamika u thinking', 'kamika pose1 public md default ed default brow furrow')
    MapEmote('kamika u evilgrin', 'kamika pose1 public mc grin ed squint brow mad')
    MapEmote('kamika u surprise', 'kamika pose1 public m shout ed default brow surprise')
    MapEmote('kamika u angrysurprise', 'kamika pose1 public m shout ed default brow mad')
    MapEmote('kamika u shout', 'kamika pose1 public md mad ed default brow mad optional angryvein')
    MapEmote('kamika u glare', 'kamika pose1 public md sad ed squint brow mad')
    MapEmote('kamika u shoutclosed', 'kamika pose1 public md mad ec default brow mad optional angryvein')
    MapEmote('kamika u mad', 'kamika pose1 public md mad ed default brow mad')
    MapEmote('kamika u madclosed', 'kamika pose1 public md mad ec default brow mad')
    MapEmote('kamika u confident', 'kamika pose1 public md happy ed default brow mad')
    MapEmote('kamika u smugclosed', 'kamika pose1 public md happy ec default brow sad')
    MapEmote('kamika u smug', 'kamika pose1 public md happy ed default brow sad')
    MapEmote('kamika u smugsquint', 'kamika pose1 public md happy ed squint brow sad')
    MapEmote('kamika u wideeyes', 'kamika pose1 public md default ed default brow surprise')
    MapEmote('kamika u happyclosed', 'kamika pose1 public md happy ec happy brow surprise')
    MapEmote('kamika u happy', 'kamika pose1 public md happy ed happy brow surprise')
    MapEmote('kamika u sigh', 'kamika pose1 public md mad happy ec default brow sad')
    MapEmote('kamika u silenced', 'kamika pose1 public mc baka ed default brow surprise')
    MapEmote('kamika u pout', 'kamika pose1 public md pout ed default brow mad')
    MapEmote('kamika u whine', 'kamika pose1 public md sad ed squint brow sad cry 0')
    MapEmote('kamika u exclaim', 'kamika pose1 public md shout ed default brow surprise')
    MapEmote('kamika u neutral', 'kamika pose1 public md default ed default brow default')
    MapEmote('kamika u neutralclosed', 'kamika pose1 public md default ec default brow default')
    MapEmote('kamika u confidentclosed', 'kamika pose1 public md happy ec default brow mad')
    MapEmote('kamika u licklips', 'kamika pose1 public m licklips ed squint brow mad')
    MapEmote('kamika u seduce', 'kamika pose1 public md happy ed default brow furrow')
    MapEmote('kamika u seducesquint', 'kamika pose1 public md happy ed squint brow mad')
    MapEmote('kamika u mad', 'kamika pose1 public md mad ed default brow mad')
    MapEmote('kamika u simmons', 'kamika pose1 public m simmons ed squint brow raise')
    MapEmote('kamika u simmonsclosed', 'kamika pose1 public m simmons ec happy brow raise')
    MapEmote('kamika u questionsquint', 'kamika pose1 public md pout ed squint brow raise')
    MapEmote('kamika u question', 'kamika pose1 public md pout ed default brow raise')
    MapEmote('kamika u deadpan', 'kamika pose1 public md flat ed squint brow default')
    MapEmote('kamika u confused', 'kamika pose1 public md flat ed default brow raise')
    MapEmote('kamika u shoutclosed', 'kamika pose1 public md mad ec default brow mad optional angryvein')
    MapEmote('kamika u evilsmile', 'kamika pose1 public md happy ed default brow mad')
    MapEmote('kamika u evilsmileclosed', 'kamika pose1 public md happy ec default brow mad')
    MapEmote('kamika u evilgrin', 'kamika pose1 public mc grin ec default brow mad')
    MapEmote('kamika u badliar', 'kamika pose1 public md happy ed happy brow sad')
    MapEmote('kamika u badliarclosed', 'kamika pose1 public md happy ec happy brow sad')
    MapEmote('kamika u squirm', 'kamika pose1 public mc grin ec happy brow sad')
    MapEmote('kamika u evilsmileclosed', 'kamika pose1 public md happy ed squint brow mad')
    MapEmote('kamika u panic', 'kamika pose1 public m shout ed default brow surprise')
    MapEmote('kamika u desperate', 'kamika pose1 public md happy ed default brow sad')
    MapEmote('kamika u desperateclosed', 'kamika pose1 public md happy ec default brow sad')
    MapEmote('kamika u ouch', 'kamika pose1 public m shout ec default brow mad')
    MapEmote('kamika u eyebrow', 'kamika pose1 public md default ed default brow raised')
    MapEmote('kamika u sad', 'kamika pose1 public md sad ed default brow sad')
    MapEmote('kamika u sadclosed', 'kamika pose1 public md sad ec default brow sad')
    MapEmote('kamika u sadsquint', 'kamika pose1 public md sad ed squint brow sad')
    #PAST THIS POINT IS NEW SHIT

    #KAMIKA LOOKING AT READER (DEMON FORM)
    MapEmote('kamika d thinkingclosed', 'kamika pose1 base md default ec default brow furrow')
    MapEmote('kamika d thinking', 'kamika pose1 base md default ed default brow furrow')
    MapEmote('kamika d evilgrin', 'kamika pose1 base mc grin ed squint brow mad')
    MapEmote('kamika d surprise', 'kamika pose1 base m shout ed default brow surprise')
    MapEmote('kamika d angrysurprise', 'kamika pose1 base m shout ed default brow mad')
    MapEmote('kamika d shout', 'kamika pose1 base md mad ed default brow mad optional angryvein')
    MapEmote('kamika d glare', 'kamika pose1 base md sad ed squint brow mad')
    MapEmote('kamika d shoutclosed', 'kamika pose1 base md mad ec default brow mad optional angryvein')
    MapEmote('kamika d mad', 'kamika pose1 base md mad ed default brow mad')
    MapEmote('kamika d madclosed', 'kamika pose1 base md mad ec default brow mad')
    MapEmote('kamika d confident', 'kamika pose1 base md happy ed default brow mad')
    MapEmote('kamika d smugclosed', 'kamika pose1 base md happy ec default brow sad')
    MapEmote('kamika d smug', 'kamika pose1 base md happy ed default brow sad')
    MapEmote('kamika d smugsquint', 'kamika pose1 base md happy ed squint brow sad')
    MapEmote('kamika d wideeyes', 'kamika pose1 base md default ed default brow surprise')
    MapEmote('kamika d happyclosed', 'kamika pose1 base md happy ec happy brow surprise')
    MapEmote('kamika d happy', 'kamika pose1 base md happy ed happy brow surprise')
    MapEmote('kamika d sigh', 'kamika pose1 base md mad happy ec default brow sad')
    MapEmote('kamika d silenced', 'kamika pose1 base mc baka ed default brow surprise')
    MapEmote('kamika d pout', 'kamika pose1 base md pout ed default brow mad')
    MapEmote('kamika d whine', 'kamika pose1 base md sad ed squint brow sad cry 0')
    MapEmote('kamika d exclaim', 'kamika pose1 base md shout ed default brow surprise')
    MapEmote('kamika d neutral', 'kamika pose1 base md default ed default brow default')
    MapEmote('kamika d neutralclosed', 'kamika pose1 base md default ec default brow default')
    MapEmote('kamika d confidentclosed', 'kamika pose1 base md happy ec default brow mad')
    MapEmote('kamika d licklips', 'kamika pose1 base m licklips ed squint brow mad')
    MapEmote('kamika d seduce', 'kamika pose1 base md happy ed default brow furrow')
    MapEmote('kamika d seducesquint', 'kamika pose1 base md happy ed squint brow mad')
    MapEmote('kamika d mad', 'kamika pose1 base md mad ed default brow mad')
    MapEmote('kamika d simmons', 'kamika pose1 base m simmons ed squint brow raise')
    MapEmote('kamika d simmonsclosed', 'kamika pose1 base m simmons ec happy brow raise')
    MapEmote('kamika d questionsquint', 'kamika pose1 base md pout ed squint brow raise')
    MapEmote('kamika d question', 'kamika pose1 base md pout ed default brow raise')
    MapEmote('kamika d deadpan', 'kamika pose1 base md flat ed squint brow default')
    MapEmote('kamika d confused', 'kamika pose1 base md flat ed default brow raise')
    MapEmote('kamika d shoutclosed', 'kamika pose1 base md mad ec default brow mad optional angryvein')
    MapEmote('kamika d evilsmile', 'kamika pose1 base md happy ed default brow mad')
    MapEmote('kamika d evilsmileclosed', 'kamika pose1 base md happy ec default brow mad')
    MapEmote('kamika d evilgrin', 'kamika pose1 base mc grin ec default brow mad')
    MapEmote('kamika d badliar', 'kamika pose1 base md happy ed happy brow sad')
    MapEmote('kamika d badliarclosed', 'kamika pose1 base md happy ec happy brow sad')
    MapEmote('kamika d squirm', 'kamika pose1 base mc grin ec happy brow sad')
    MapEmote('kamika d evilsmileclosed', 'kamika pose1 base md happy ed squint brow mad')
    MapEmote('kamika d panic', 'kamika pose1 base m shout ed default brow surprise')
    MapEmote('kamika d desperate', 'kamika pose1 base md happy ed default brow sad')
    MapEmote('kamika d desperateclosed', 'kamika pose1 base md happy ec default brow sad')
    MapEmote('kamika d ouch', 'kamika pose1 base m shout ec default brow mad')
    MapEmote('kamika d eyebrow', 'kamika pose1 base md default ed default brow raised')
    MapEmote('kamika d sad', 'kamika pose1 base md sad ed default brow sad')
    MapEmote('kamika d sadclosed', 'kamika pose1 base md sad ec default brow sad')
    MapEmote('kamika d sadsquint', 'kamika pose1 base md sad ed squint brow sad')
    #PAST THIS POINT IS NEW SHIT


    #KAMIKA LOOKING AWAY
    MapEmote('kamika s annoyedside', 'kamika pose2 base md default ed side brow mad')
    MapEmote('kamika s sigh', 'kamika pose2 base md default ec default brow mad')
    MapEmote('kamika s annoyed', 'kamika pose2 base md default ed default brow mad')
    MapEmote('kamika s simmonsclosed', 'kamika pose2 base md simmons ec happy brow mad')
    MapEmote('kamika s smug', 'kamika pose2 base md smirk ed default brow mad')
    MapEmote('kamika s hystericallaugh', 'kamika pose2 base md happy ec happy brow mad')
    MapEmote('kamika s annoyedclosed', 'kamika pose2 base md default ec default brow mad')
    MapEmote('kamika s grit', 'kamika pose2 base mc grimace ed default brow mad')
    MapEmote('kamika s gritclosed', 'kamika pose2 base mc grimace ec default brow mad')
    MapEmote('kamika s gritside', 'kamika pose2 base mc grimace ed side brow mad')
    MapEmote('kamika s sad', 'kamika pose2 base md default ed default brow sad')
    MapEmote('kamika s sadside', 'kamika pose2 base md default ed side brow sad')

    #LUCCA
    MapEmote('lucca neutral', 'lucca base md default ed default brow default')
    MapEmote('lucca nervous', 'lucca base md default ed default brow sad')
    MapEmote('lucca nervousopen', 'lucca base m default ed default brow sad')
    MapEmote('lucca nervousclose', 'lucca base md default ec default brow sad')
    MapEmote('lucca nervouser', 'lucca base md default ed default brow sadder')
    MapEmote('lucca nervouseropen', 'lucca base m default ed default brow sadder')
    MapEmote('lucca sigh', 'lucca base m sad ec default brow sad')
    MapEmote('lucca uwah', 'lucca base m uwah ec uwah brow sad')
    MapEmote('lucca doh', 'lucca base mc default ec uwah brow sadder blush')
    MapEmote('lucca happy', 'lucca base md happy ed happy brow default')
    MapEmote('lucca happyclosed', 'lucca base md happy ec happy brow default')
    MapEmote('lucca bashful', 'lucca base md happy ed happy brow sad')
    MapEmote('lucca ohno', 'lucca base md uwah ed default brow sad')
    MapEmote('lucca aaaa', 'lucca base m uwah ed default brow sad')
    MapEmote('lucca bigaaaa', 'lucca base m uwah ed default brow sadder')
    MapEmote('lucca nervoussmile', 'lucca base md happy ed default brow sad')
    MapEmote('lucca guilty', 'lucca base md sad ec default brow sad')
    MapEmote('lucca mad', 'lucca base md mad ed default brow mad')
    MapEmote('lucca mad', 'lucca base md mad ed default brow mad optional blush')
    MapEmote('lucca happy', 'lucca base md happy ed happy brow sad')

    #MOE
    MapEmote('moe neutral', 'moe base md default ed default brow default')
    MapEmote('moe neutrallook', 'moe base md default ed side brow default')
    MapEmote('moe squint', 'moe base md default ed squint brow default')
    MapEmote('moe neutralclosed', 'moe base md default ec default brow default')
    MapEmote('moe madside', 'moe base md default ed side brow mad')
    MapEmote('moe mad', 'moe base md default ed default brow mad')
    MapEmote('moe sigh', 'moe base md default ec default brow sad')
    MapEmote('moe sighsweat', 'moe base md default ec default brow sad optional sweatdrop')
    MapEmote('moe smug', 'moe base md happy ed default brow angry')
    MapEmote('moe smuglook', 'moe base md happy ed side brow angry')
    MapEmote('moe smugclosed', 'moe base md happy ec default brow angry')


    #MADE BY ALF, DOUBLECHECK LATER
    MapEmote('stacey neutralclosed', 'stacey base md sad ec default brow default')
    MapEmote('stacey therocklook', 'stacey base md default ed side brow raised')
    MapEmote('stacey evil', 'stacey base md default ed default brow mad')
    MapEmote('stacey madlook', 'stacey base md sad ed side brow mad')
    MapEmote('stacey eyebrowclosed', 'stacey base md sad ec default brow raised')
    MapEmote('lucca waah', 'lucca base md default ed default brow sadder cry 1')
    MapEmote('lucca sniff', 'lucca base md sad ed default brow sad cry 1')
    MapEmote('kamika u quiet', 'kamika pose1 public md default ed default brow sad')
    MapEmote('kamika d quiet', 'kamika pose1 base md default ed default brow sad')
    MapEmote('kamika u disappointed', 'kamika pose1 public md default ec default brow sad')
    MapEmote('kamika d disappointed', 'kamika pose1 base md default ec default brow sad')
    MapEmote('kamika u seducetongue', 'kamika pose1 public m lick ed default brow sad')
    MapEmote('kamika d seducetongue', 'kamika pose1 base m lick ed default brow sad')
    MapEmote('kamika u stew', 'kamika pose1 base mc baka ed default brow mad')
    MapEmote('kamika d stew', 'kamika pose1 base mc baka ed default brow mad')

#MINOR CHARACTERS
define dee = Character('Mr. Deeks', color="#FFFFFF", voice_tag="dee")
define ber = Character('Mrs. Bernardinelli', color="#FFFFFF", voice_tag="ber")
define mst = Character('Male Student', color="#FFFFFF", voice_tag="mst")
define fst = Character('Female Student', color="#FFFFFF", voice_tag="fst")
define pg1 = Character('Partygoer 1', color="#FFFFFF", voice_tag="pg1")
define pg2 = Character('Partygoer 2', color="#FFFFFF", voice_tag="pg2")

######################
# Flags              #
######################
default minion = False
default sawstacey = False
default helpkamika = False
default kamika_points = 0
default stacey_points = 0
default lucca_points = 0

##################
# BG Declaration #
##################

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

#MINOR CGS
image transformdemon = "cgs/transformdemon.png"
image transformhuman = "cgs/transformhuman.png"

#######
# VFX #
#######

###################
# SFX             #
###################

###################
# Music           #
###################
label start:
    jump scene1
