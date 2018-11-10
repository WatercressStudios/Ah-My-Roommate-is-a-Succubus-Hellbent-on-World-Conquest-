label scene13:
scene classroom

#fade in from black, classroom
voice "c-13-1.wav" #Mister Deeks (???)
dee "-And that is why the so called \"anime\" style is nothing more than an amalgamation of poor techniques that should not, under any circumstances, be the only thing you practice."

voice "c-13-2.wav" #Mister Deeks (???)
dee "That's not to say it is a terrible medium on it's own, just that you should be improving far beyond what the style demands of you before you set such a limitation on yourself."

voice "c-13-3.wav" #Mister Deeks (???)
dee "Class dismissed!"

#POINT CHECK: IF insufficient points for any route; BAD END
if stacey_points > 0:
    jump s13continue
elif lucca_points > 0:
    jump s13continue
elif kamika_points = 3:
    jump s13continue
else:
    jump hermitend

label hermitend:
"Another day, another dreadful class."
"I wish I could say that's the only unpleasant thing going on in my life."
"Too many people, too much drama, all of it absurd."
"Though, I suppose it's not so bad."
"...Whatever, I should just focus on preparing for the next class."
jump scene14iv


#IF sufficient points for any route; continue scene

label s13continue:

show stacey neutral at centerleft with dissolve
voice "c-13-4.wav" #Yumi (Kathy Pfautsch)
yum "I can't believe he spent almost an entire hour talking about children's shows."

voice "c-13-5.wav" #Stacey (Ashe Thurman)
sta "Maybe he just hasn't researched enough."

voice "c-13-6.wav" #Yumi (Kathy Pfautsch)
yum "Does he look like the kind of guy who watches, let alone researches, anime?"

show stacey eyebrow
voice "c-13-7.wav" #Stacey (Ashe Thurman)
sta "He seemed to like that Bobo's Strange Journey show a lot."

voice "c-13-8.wav" #Yumi (Kathy Pfautsch)
yum "Good taste."

show stacey grin
voice "c-13-9.wav" #Stacey (Ashe Thurman)
sta "So, how are things on the roommate front? She suck your soul out yet?"

voice "c-13-10.wav" #Yumi (Kathy Pfautsch)
yum "That girl couldn't drain a juice box, let alone a soul."

show stacey smug
voice "c-13-11.wav" #Stacey (Ashe Thurman)
sta "You think? I mean, her lungs should be strong enough."

voice "c-13-12.wav" #Yumi (Kathy Pfautsch)
yum "That's not what I me- ya know what, you're right."

voice "c-13-13.wav" #Yumi (Kathy Pfautsch)
yum "It's strange, for a demon she's rather... What's the word for it...?"

show stacey therock
voice "c-13-14.wav" #Stacey (Ashe Thurman)
sta "Sucky?"

voice "c-13-15.wav" #Yumi (Kathy Pfautsch)
yum "Feels too literal. I wanna say \"naive\" but that seems contradictory somehow."

show stacey confused
voice "c-13-16.wav" #Stacey (Ashe Thurman)
sta "I'd say she's beyond classification then."

voice "c-13-17.wav" #Yumi (Kathy Pfautsch)
yum "Really? Aren't you, like, the expert when it comes to demons?"

voice "c-13-18.wav" #Stacey (Ashe Thurman)
sta "Don't know what to tell you, friend. Moe is a pretty standard dude."

voice "c-13-19.wav" #Yumi (Kathy Pfautsch)
yum "Standard dude or standard demon?"

show stacey grin
voice "c-13-20.wav" #Stacey (Ashe Thurman)
sta "Same shit TBH, fam."

show stacey smug
voice "c-13-21.wav" #Stacey (Ashe Thurman)
sta "One time I went over to his room and there was this huge racket you could hear all the way from the hall."

voice "c-13-22.wav" #Stacey (Ashe Thurman)
sta "When I knocked on his door, the sound suddenly stopped. When he finally answered, a minute and a half later, I asked him about it."

voice "c-13-23.wav" #Stacey (Ashe Thurman)
sta "He started shaking and spouting off something about a bug infestation."

show stacey evil
voice "c-13-24.wav" #Stacey (Ashe Thurman)
sta "Very convenient he had a box of tissues by his computer, 'just in case'."

voice "c-13-25.wav" #Yumi (Kathy Pfautsch)
yum "Damn, he really is normal."

show stacey smug
voice "c-13-26.wav" #Stacey (Ashe Thurman)
sta "Shocking, I know."

#variable lucca name = ???

show lucca neutral at centerright, flipimage with easeinright
voice "c-13-27.wav" #Lucca (Victoria Wong)
luc "I h-hope I'm not interrupting anything..."

voice "c-13-28.wav" #Yumi (Kathy Pfautsch)
yum "Oh, hey Lucca."

show stacey confused
voice "c-13-29.wav" #Stacey (Ashe Thurman)
sta "Yumi, you know the cowgirl?"

voice "c-13-30.wav" #Yumi (Kathy Pfautsch)
yum "We go way back, she's another demon, sort of."

show lucca mad
voice "c-13-31.wav" #Lucca (Victoria Wong)
luc "I'm right here, you know!"

voice "c-13-32.wav" #Yumi (Kathy Pfautsch)
yum "Don't mind her, she's friendly."

show stacey sarcasticlook
voice "c-13-33.wav" #Stacey (Ashe Thurman)
sta "Are you sure? I hear you're not supposed to trust demons in funny hats."

voice "c-13-34.wav" #Yumi (Kathy Pfautsch)
yum "I was talking about you and your funny hat, actually."

show lucca uwah
voice "c-13-35.wav" #Lucca (Victoria Wong)
luc "I-I'll have you know this hat is fashionable and f-functional..."

show stacey therocklook
voice "c-13-36.wav" #Stacey (Ashe Thurman)
sta "I bet there's a big ol' horn under there. Like a unicorn. Majestic and aerodynamic."

show lucca doh
voice "c-13-37.wav" #Lucca (Victoria Wong)
luc "W-what!? N-No!"

"Stacey takes a good, hard look at Lucca's hat, carefully weighing the possibilities."

voice "c-13-38.wav" #Stacey (Ashe Thurman)
sta "..."

show lucca nervouser
voice "c-13-39.wav" #Lucca (Victoria Wong)
luc "I-It's rude to stare..."

show stacey smug
voice "c-13-40.wav" #Stacey (Ashe Thurman)
sta "Okay, I believe you."

voice "c-13-41.wav" #Yumi (Kathy Pfautsch)
yum "What."

show stacey grin
voice "c-13-42.wav" #Stacey (Ashe Thurman)
sta "If she says there isn't a horn, there isn't one."

voice "c-13-43.wav" #Yumi (Kathy Pfautsch)
yum "Anyway..."

show lucca nervous
voice "c-13-44.wav" #Lucca (Victoria Wong)
luc "Yumi, I have to talk to you. I-In private. Are you free?"

if kamika_points = 3:
    jump kamikaroute
elif stacey_points > lucca_points:
    jump staceyroute
elif lucca_points > stacey_points:
    jump luccaroute
else:
    jump tiebreaker

#IF equal LUCCA and STACEY points

label tiebreaker:
"Oh, shit. I promised both of them I'd help out today. Quick, make something up!"

menu:
    "Go with Stacey":
        voice "c-13-45.wav" #Yumi (Kathy Pfautsch)
        yum "Sorry Lucca, I already made plans. Can it wait?"

        voice "c-13-46.wav" #Lucca (Victoria Wong)
        show lucca sigh
        luc "...I-I guess..."
        jump staceyroute
    "Go with Lucca":
        voice "c-13-47.wav" #Yumi (Kathy Pfautsch)
        yum "Oh crap. Stacey, I'm gonna hafta cancel."

        show stacey confused
        voice "c-13-48.wav" #Stacey (Ashe Thurman)
        sta "Eh? But, you promised..."

        voice "c-13-49.wav" #Yumi (Kathy Pfautsch)
        yum "I know, but this concerns a certain demon with an ego. I'm sorry!"

        show stacey sad
        voice "c-13-50.wav" #Stacey (Ashe Thurman)
        sta "It's cool, I guess... Writing is a lonely task anyway."

        show stacey smug
        voice "c-13-51.wav" #Stacey (Ashe Thurman)
        sta "Go, lay the demon!"

        voice "c-13-52.wav" #Lucca (Victoria Wong)
        luc "Do you mean \"Slay\"?"

        show stacey grinclosed
        voice "c-13-53.wav" #Stacey (Ashe Thurman)
        sta "Close enough."
        jump luccaroute


label staceyroute:

$ route = "stacey"
voice "c-13-54.wav" #Yumi (Kathy Pfautsch)
yum "I would, but I promised Stacey."

show lucca guilty
voice "c-13-55.wav" #Lucca (Victoria Wong)
luc "Not the issue here, but okay."

show stacey eyebrow
voice "c-13-56.wav" #Stacey (Ashe Thurman)
sta "C'mon, let's go somewhere else for this."

jump scene14i


label luccaroute:

$ route = "lucca"
voice "c-13-57.wav" #Yumi (Kathy Pfautsch)
yum "I'll talk to you later, Stacey."

show stacey smug
voice "c-13-58.wav" #Stacey (Ashe Thurman)
sta "Take it easy, Yumi."

show lucca nervoussmile
voice "c-13-59.wav" #Lucca (Victoria Wong)
luc "A-Alright, let's go!"

jump scene14ii


label kamikaroute:

$ route = "kamika"
voice "c-13-60.wav" #Yumi (Kathy Pfautsch)
yum "...Sorry, guys. I just can't sit still knowing Kamika might be up to {i}something{/i}."

voice "c-13-61.wav" #Yumi (Kathy Pfautsch)
yum "I'm gonna have to go and check up on her. I'll call you guys if anything major's happening."

show stacey neutral
voice "c-13-62.wav" #Stacey (Ashe Thurman)
sta "You're the boss, boss. Do whatcha gotta do."

show lucca uwah
voice "c-13-63.wav" #Lucca (Victoria Wong)
luc "B-be careful, Yumi..."

voice "c-13-64.wav" #Yumi (Kathy Pfautsch)
yum "I'll be back soon. Hopefully."

"With trepidation in my heart, I make my way back to the dorms."

jump scene14iii
