label scene8:
scene black

"..."
"This is definitely one of the most restless nights I've had in a long while."
"Every time I try to doze off, I keep worrying something's gonna happen to me in my sleep."
"If that wasn't bad enough, sometimes those thoughts manifest into actual dreams."
"I've had too many horrible dreams about demons in the past several hours for one night, too much to even describe in detail."
"So now I'm in this weird state where I can't fall asleep, but even if I {i}could{/i}, I'm not sure if I {i}want{/i} to."
"So I keep my eyes shut in an attempt to get {i}some{/i} sleep, while keeping myself from passing out and experiencing those nightmares again..."
"..."
"I hate this."
"I want this night to be over."
"I want to wake up and go to class as if nothing ever happened."
"Why does this demon shit have to follow me {i}here?{/i}"
"I never asked to be stuck with an idiot younger brother who won't shut up about them."
"Was I really that bad in a past life? Are the demons following me around because of that?"
"I don't know... it's getting so hard to think."
"My mind swims with useless, empty thoughts while I struggle on the balancing act of being both asleep and awake at the same time."
"And just when it feels like everything starts fading away... a voice enters my head."

voice "c-8-1.wav" #Kamika (Ariane Marchese)
kam "It's almost time, Yumi~"

"...My eyes dare not open."
"Is this a dream? Or am I awake right now? I'll regret the answer either way, so I try not to think about it."
"But the voice in my head continues."

voice "c-8-2.wav" #Kamika (Ariane Marchese)
kam "Very soon, my brilliant plan will be set into motion."

voice "c-8-3.wav" #Kamika (Ariane Marchese)
kam "It's been such a long time coming, but now... now is the time to make it a reality."

voice "c-8-4.wav" #Kamika (Ariane Marchese)
kam "By the end of this week, the entire school will be drunk with adoration for their true mistress~"

voice "c-8-5.wav" #Kamika (Ariane Marchese)
kam "You can picture it now, can't you? Everyone around you, young and old, will be celebrating my name and worshipping me as their goddess~"

voice "c-8-6.wav" #Kamika (Ariane Marchese)
kam "There will be no tears, no bloodshed... The masses will be too encaptivated to even fight back."

voice "c-8-7.wav" #Kamika (Ariane Marchese)
kam "It will be the end of what you once knew... and the beginning of my beautiful utopia~"

#BRANCH: dialogue path based on not helping Kamika
if helpkamika = True:
    jump s8minion
else:
    jump s8free

label s8free:
voice "c-8-8.wav" #Kamika (Ariane Marchese)
kam "And not even {i}you{/i}, dear Yumi, will be able to stop it~"

voice "c-8-9.wav" #Kamika (Ariane Marchese)
kam "You can struggle and scream all you want, but by the time you do anything, you will be too late."

voice "c-8-10.wav" #Kamika (Ariane Marchese)
kam "Everyone you know and love will become my loyal slave, leaving you with nobody."

voice "c-8-11.wav" #Kamika (Ariane Marchese)
kam "You will be forgotten and alone."

voice "c-8-12.wav" #Kamika (Ariane Marchese)
kam "...But it's only after I've broken your spirit that I'll break your mind as well."

voice "c-8-13.wav" #Kamika (Ariane Marchese)
kam "You'll come to realize what a fool you've been, so you'll come crawling to me, {i}begging{/i} me to shower you with love and affection."

voice "c-8-14.wav" #Kamika (Ariane Marchese)
kam "So don't you worry your pretty little head... I'll give you what you crave in due time~"
jump s8merge

#BRANCH: dialogue path based on helping Kamika

label s8minion:
voice "c-8-15.wav" #Kamika (Ariane Marchese)
kam "But you wanted this to happen anyway, didn't you dear Yumi~?"

voice "c-8-16.wav" #Kamika (Ariane Marchese)
kam "You realized it was pointless to defy me, and now your wisdom has become my greatest asset."

voice "c-8-17.wav" #Kamika (Ariane Marchese)
kam "We'll captivate everyone you know and love and convert them to my side, where they will gladly stay forevermore."

voice "c-8-18.wav" #Kamika (Ariane Marchese)
kam "Everyone will realize what truly matters thanks to you."

voice "c-8-19.wav" #Kamika (Ariane Marchese)
kam "And then, once we've claimed the entire world... I'll give you your eternal reward."

voice "c-8-20.wav" #Kamika (Ariane Marchese)
kam "I'll give you attention and love, {i}every night{/i}, just between the two of us. And you will gladly accept it, just as you have accepted me."

voice "c-8-21.wav" #Kamika (Ariane Marchese)
kam "Once we've accomplished our goals, I'll make you the happiest woman on the planet~"
jump s8merge

#MERGE: dialogue paths converge here

label s8merge:
"What is she even saying? Do I {i}want{/i} to find out? Is it better to ignore her?"
"Every part of my brain is rife with indecision... but against my better judgement, my eyes slowly open anyways."
"And what I find..."

#CG: show CG of Kamika lying in bed, giving viewer a sultry look

"...is Kamika."
"She's not just whispering to me... she's cuddling up to me! In my own bed! After I {i}just{/i} told her not to touch me!"
"She doesn't even have a hint of remorse on her face as she smiles at me!"

voice "c-8-22.wav" #Kamika (Ariane Marchese)
kam "Good morning, my dear~"

"Rage overtakes me in an instant. I've dealt with this shit enough already!"
"My eyes fling open, and before I know it, I'm flinging a pillow at her while screaming at her face."

#CG: show pillow being thrown at Kamika's face in CG

voice "c-8-23.wav" #Yumi (Kathy Pfautsch)
yum "{i}GET OFF!!!{/i}"

show bedroom with dissolve

"The force of my throw sends Kamika tumbling onto the floor."
"Meanwhile, I'm left huffing and puffing, clearly wide awake now and not putting my consciousness through anymore torture."
"Holy crap, she {i}cannot{/i} take no for an answer..."

show kamika u angrysurprise with dissolve

voice "c-8-24.wav" #Kamika (Ariane Marchese)
kam "Oww...! That {i}hurt{/i}, god dammit! Is that how you {i}thank{/i} people for waking you up?!"

voice "c-8-25.wav" #Yumi (Kathy Pfautsch)
yum "{i}Other{/i} people don't try to {i}sneak into my bed without permission{/i}, you {i}creep!{/i} You are sleeping on the {i}floor{/i} from now on!"

show kamika u shout

voice "c-8-26.wav" #Kamika (Ariane Marchese)
kam "{i}WHAT?!{/i} That's {i}BULLSHIT!!{/i} At least let me sleep on the couch!"

voice "c-8-27.wav" #Yumi (Kathy Pfautsch)
yum "I don't want your gross ass anywhere {i}NEAR{/i} the couch at night! You're sleeping on the floor, {i}no exceptions!{/i}"

show kamika u madclosed

voice "c-8-28.wav" #Kamika (Ariane Marchese)
kam "God, {i}fine{/i}. Didn't think you were gonna be such a {i}bitch{/i} about this!"

"It's taking every ounce of strength within me to not rip this girl's head off right here and now."
"I cast a cursory glance to my alarm clock, only to discover it's nearly 8 AM already!"

voice "c-8-29.wav" #Yumi (Kathy Pfautsch)
yum "Oh god {i}dammit!{/i} I'm gonna be late!"

"I spring out of bed in a rush, trying as hard as I can to get ready for the day. Kamika simply observes me."

if helpkamika = True:
    jump s8minion2
else:
    jump s8free2
#BRANCH: dialogue path based on not helping Kamika

#show kam confident, eyes closed

show kamika u sigh
label s8free2:
voice "c-8-30.wav" #Kamika (Ariane Marchese)
kam "Alright, well while you attend to your {i}human{/i} obligations, {i}I'm{/i} going to go put things in motion!"

show kamika u smug
voice "c-8-31.wav" #Kamika (Ariane Marchese)
kam "You're gonna be left {i}kicking{/i} yourself once you see what I have in store~"

#show kam laughing

show kamika u evilgrinclosed
voice "c-8-32.wav" #Kamika (Ariane Marchese)
kam "Nyahahaha~! Later!"

hide kamika with easeoutright

voice "c-8-33.wav" #Yumi (Kathy Pfautsch)
yum "Wait!"

"And with that, she darts away, leaving me to fend for myself."
"This is bad. I can't let her go off on her own without knowing what she has planned!"
"But I can't just skip class either... my good standing and perfect attendance won't allow it!"
"As much as I hate to admit it, I don't have a lot of choice right now... I'll have to deal with her later in the day."
"For now, I get dressed and make haste towards my morning classes..."

jump scene9i

#BRANCH: dialogue path based on helping Kamika

label s8minion2:

#show kam demanding

show kamika u neutral
voice "c-8-34.wav" #Kamika (Ariane Marchese)
kam "Don't forget; as {i}soon{/i} as you're done with your human obligations, you come straight to me! Got it?"

voice "c-8-35.wav" #Yumi (Kathy Pfautsch)
yum "Ugh, fine, whatever, just lemme get my bearings together already!"

show kamika u confident

voice "c-8-36.wav" #Kamika (Ariane Marchese)
kam "Hehehehe~ We're going to be having {i}so{/i} much fun today~!"

show kamika u confidentclosed

voice "c-8-37.wav" #Kamika (Ariane Marchese)
kam "I'll go and get things ready! Toodles~!"

hide kamika with easeoutright

"And with that, she darts away."
"I have her word that she won't try anything funny while on her own, but how much does that really mean when it's {i}Kamika{/i} we're talking about?"
"Either way, I don't really have a choice right now. I'll go to class as normal, then go along with her dumb idea later."
"For now, I get dressed and make haste towards my morning class..."

jump scene9ii
