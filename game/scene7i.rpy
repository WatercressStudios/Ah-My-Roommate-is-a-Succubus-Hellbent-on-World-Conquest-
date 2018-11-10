label scene7i:
scene campus

#MEMO: Replace all instances of S-Tan hyphen with the star later
"It's as I'm heading back up to the dorms that I recognize a certain ridiculous cowboy hat furtively sneaking into the distance."

"Yep, that's Lucca alright, though I don't know where she's going with that heavy backpack. I don't think I've seen her bring it to class, and there aren't any classroom buildings in that direction, anyway."

"Come to think of it, I just don't know what's in that direction, period."

"...Okay, screw it, I'm curious."

"If nothing else, I should probably talk to Lucca about the disappointing experience I had calling Satan."

"Making my way down the sidewalk, I notice that the road wends into the trees, creating a canopy-like effect. After I've been walking for a minute or two, I realize that that's all I can see anymore."

"Nothing but trees, and a road that seems to get more poorly-maintained the further I walk along it."

"It's vaguely spooky... but, somehow, knowing I'm following a {i}demon{/i} into it just makes the moment feel farcical."

"I guess after all the time I've spent around demons, I automatically regard anything to do with them as fundamentally ridiculous..."

"Though Lucca is too far ahead of me for me to see, this road only goes the one way, so unless she decided to break off and vanish into the woods, I don't think I've lost her."

"I don't think she's the type to do that sort of thing, at any rate."

"Only a few minutes of walking later, the trees part, and in the clearing, I see something I never would have expected to see:"

"...Dorms."

"Yep, these buildings are definitely student housing... though I've never heard of them."

"The metal railing and scaffolding leading to the second floor is totally rusted over, and the concrete stairways are literally crumbling - there's literally piles of rocky debris at the bottom of the steps, the way upstairs blocked off by construction tape."

"Around them, the grass around them is totally unmowed, the tall underbrush threatened to encroach into the covered walkways. It's like a tableau of growth and decay."

"I guess these buildings have been... decommissioned, or condemned. Clearly, nobody's lived in this ghost town for a while."

"Well, except for the various deer I can see grazing off in the distance. I guess they like this place, since it's so quiet and undisturbed."

"Maybe this is where Kamika was squatting before she decided to invade my living space..."

##sfx: Sound of an aerosol can

"Is that... spray paint I hear?"

"Amidst the yawning emptiness of the housing complex, the sound carries as if it was right next to me. It seems to be coming from around the nearest building."

show lucca nervous with dissolve
"Is that Lucca? What's she doing?"

"Leaving the sidewalk, I trudge into the tall, neglected grass to investigate, mentally praying that I don't wind up with any tick bites. Lyme disease is terrifying."

"Sure enough, along the side of the building that faces away from the road, Lucca's there, brandishing a purple can of spray paint."

voice "c-7i-1.wav" #Yumi (Kathy Pfautsch)
yum "...Lucca?"

show lucca bigaaaa
voice "c-7i-2.wav" #Lucca (Victoria Wong)
luc "YAAH!"

show lucca doh
"She pops up from her poised position like a released spring and slashes in my direction with the can, as though brandishing a longsword."

"Fortunately for me, I'm standing far enough away that the paint particles don't actually reach me or my stuff..."

voice "c-7i-3.wav" #Yumi (Kathy Pfautsch)
yum "Err, sorry, sorry! It's just me!"

show lucca nervouser
voice "c-7i-4.wav" #Lucca (Victoria Wong)
luc "O-oh, Yumi! I-I thought you were..."

"She's so obviously worked up and panicked that I immediately feel guilty for sneaking up on her."

"Though, I guess turnabout is fair play. She did it to me earlier!"

voice "c-7i-5.wav" #Yumi (Kathy Pfautsch)
yum "I'm {i}really{/i} sorry! I just saw you going down this road and wanted to see where it led..."

show lucca guilty
voice "c-7i-6.wav" #Lucca (Victoria Wong)
luc "Ah... I didn't know you were behind me..."

voice "c-7i-7.wav" #Yumi (Kathy Pfautsch)
yum "I wasn't trying to stalk you, really! I just needed to talk to you about stuff anyway and-"

show lucca nervous
voice "c-7i-8.wav" #Yumi (Kathy Pfautsch)
yum "Wait."

"My eyes glide over to the wall of the building, where an unfinished mural covers the neglected wall, a dreamscape of electric indigo, sapphire, and lilac tones."


#choice
#>>"This is good!"
#>>"This is illegal."

menu:
    "This is good!":
        $ lucca_points += 1
        jump praiselucca
    "This is illegal.":
        jump criminallucca

#dialogue path from ">>"This looks very illegal.""

label criminallucca:
"...God dammit, I can't go anywhere without seeing these demons causing trouble, can I?"

"I'm not even sure what I'm looking at right now, but right now I don't even care. I turn to glare at Lucca."

voice "c-7i-a.wav" #Yumi (Kathy Pfautsch)
yum "What are you {i}thinking{/i}, Lucca?!"

show lucca nervouser
voice "c-7i-b.wav" #Lucca (Victoria Wong)
luc "Yumi, wait, I-I can explain-!"

voice "c-7i-c.wav" #Yumi (Kathy Pfautsch)
yum "If you're trying to blend into the school, then why are you doing {i}this?{/i}"

voice "c-7i-d.wav" #Yumi (Kathy Pfautsch)
yum "This is super illegal, you know. You could go to {i}jail{/i} for this!"

show lucca waah
voice "c-7i-e.wav" #Lucca (Victoria Wong)
luc "I-I'm sorry! I just... I wanted to express myself..."

"Geez, she's really good at making me feel like the bad guy here. But that doesn't mean I'm gonna allow this to slide."

voice "c-7if.wav" #Yumi (Kathy Pfautsch)
yum "Look, I'm not gonna report you for this or anything. Just... try to clean up after yourself, alright?"

show lucca sniff
voice "c-7i-g.wav" #Lucca (Victoria Wong)
luc "O-okay..."

"She looks utterly crushed... Meanwhile, my eyes drift back to the mural."
jump s7imerge

#dialogue path from ">>"This looks good.""

label praiselucca:
"I'm not quite sure what I'm looking at, but it's fascinating. In terms of linework, it's somewhere between a heraldic rose and one of those dust clouds you see in American newspaper comics when people get into a fight."

"Before I can inspect the creation anything further, Lucca leaps in front of the graffiti with starling alacrity and throws her arms out."

show lucca nervouser
voice "c-7i-h.wav" #Lucca (Victoria Wong)
luc "No, no, no! Please don't look at it before it's finished! It makes me so nervous..."

voice "c-7i-i.wav" #Yumi (Kathy Pfautsch)
yum "It looks really good already, though!"

show lucca ohno
voice "c-7i-j.wav" #Lucca (Victoria Wong)
luc "Aaaah, I don't want to hear that! Getting feedback on a piece before it's done is bad luck!"

"...Who would have ever expected a demon to be superstitious?"

"Or, wait—should a demon be {i}more{/i} likely to be superstitious, because they know more about how the universe works?"

"Nah, nevermind, demons never know anything."

voice "c-7i-k.wav" #Yumi (Kathy Pfautsch)
yum "Okay, okay! I'm sorry. I won't look at it."

show lucca nervous
voice "c-7i-l.wav" #Lucca (Victoria Wong)
luc "Thank you..."

jump s7imerge
#merge

label s7imerge:

voice "c-7i-14.wav" #Yumi (Kathy Pfautsch)
yum "I'm surprised, though. I would never have guessed you were into this sort of thing."

##Lucca smiling

show lucca bashful
voice "c-7i-15.wav" #Lucca (Victoria Wong)
luc "Oh, absolutely! I love graffiti! I've always been fascinated by it."

show lucca passion
voice "c-7i-16.wav" #Lucca (Victoria Wong)
luc "A graffito is a monument to an artist's bravery and daring! Graffiti artists are people who put themselves on the line to turn what {i}is{/i} into what {i}could be{/i}, knowing whatever they create might be gone by tomorrow!"

"Whoa... I don't think I've ever seen her so animated talking about {i}anything{/i}. "

"She's usually so anxious and sheepish, but get her talking about something she's truly passionate about and you can really see the fire behind her eyes..."

"I feel like I should say something, but her enthusiasm is genuinely spellbinding."

voice "c-7i-17.wav" #Yumi (Kathy Pfautsch)
yum "Wait. {i}That's{/i} why you're majoring in Architectural History?"

"At my question, she seems to remember herself, and goes back to shrinking."

show lucca nervous
voice "c-7i-18.wav" #Lucca (Victoria Wong)
luc "Y-yes, well, you see... there's not really any degrees offered in street art, so..."

voice "c-7i-19.wav" #Yumi (Kathy Pfautsch)
yum "Yeah, I guess there wouldn't be."

voice "c-7i-20.wav" #Yumi (Kathy Pfautsch)
yum "It's as good a thing to major in as any, if graffiti is your primary focus. This school doesn't have a program to let students design their own majors..."

show lucca nervousclose
voice "c-7i-21.wav" #Lucca (Victoria Wong)
luc "Yes, and even if I {i}could{/i} design a graffiti major, it would... well, it'd just make me the number one suspect for any graffito found on campus..."

"I nod in response."

"I guess it's hard enough for a someone like Lucca to remain inconspicuous among human society {i}without{/i} committing crimes..."

show lucca bashful
voice "c-7i-22.wav" #Lucca (Victoria Wong)
luc "Oh! That's right! Did you manage to call S-Tan?"

voice "c-7i-23.wav" #Yumi (Kathy Pfautsch)
yum "Urrrrgh..."

"Dejectedly, I groan."

voice "c-7i-24.wav" #Yumi (Kathy Pfautsch)
yum "Well, I did succeed in {i}calling{/i} her. Though all it amounted to was a message left on her machine."

show lucca nervous
"She shrugs sadly."

voice "c-7i-25.wav" #Lucca (Victoria Wong)
luc "Um... if it makes you feel any better, I always get the machine, too. I think she just hates the phone..."

voice "c-7i-26.wav" #Yumi (Kathy Pfautsch)
yum "Yeah, well, if it takes her as long to help me out as the recording said, I might be out of luck getting help with Kamika."

voice "c-7i-27.wav" #Yumi (Kathy Pfautsch)
yum "Unless that other demon I talked to can help...?"

show lucca nervouser
voice "c-7i-28.wav" #Lucca (Victoria Wong)
luc "...\"Other demon?\""

voice "c-7i-29.wav" #Yumi (Kathy Pfautsch)
yum "You know. The, um. The envy demon."

show lucca bashful
voice "c-7i-30.wav" #Lucca (Victoria Wong)
luc "Hm? Why would... Oh! You spoke to Levi."

voice "c-7i-31.wav" #Yumi (Kathy Pfautsch)
yum "Right, Levi, that was her name. Would she help?"

show lucca nervous
voice "c-7i-32.wav" #Lucca (Victoria Wong)
luc "Err! No. No, I don't think so... She doesn't blend in public very well. And they've n-never gotten along..."

voice "c-7i-33.wav" #Yumi (Kathy Pfautsch)
yum "Meh. That figures."

show lucca guilty
voice "c-7i-34.wav" #Lucca (Victoria Wong)
luc "It's all just... complicated. Succubi and incubi can be... fractious, together."

voice "c-7i-a.wav" #Yumi (Kathy Pfautsch)
yum "Wait—an incubus? I thought incubi were male?"

show lucca nervouser
"She furrows her brow into an expression of deep concern."

voice "c-7i-b.wav" #Lucca (Victoria Wong)
luc "That’s very unexpectedly gender essentialist of you, Yumi."

voice "c-7i-c.wav" #Yumi (Kathy Pfautsch)
yum  "Oh. {i}Oh{/i}. I didn’t know demons could be—"

voice "c-7i-d.wav" #Lucca (Victoria Wong)
luc "Well, of course."

voice "c-7i-e.wav" #Yumi (Kathy Pfautsch)
yum  "...Duly noted. Sorry about that."

show lucca bashful
voice "c-7i-f.wav" #Lucca (Victoria Wong)
luc "Ah, it's fine. You learn something new every day, right?"

show lucca guilty
voice "c-7i-g.wav" #Lucca (Victoria Wong)
luc "Anyway, the thing with Kamika is... kind of a long story..."

"As much as I tell myself that I really don't care to hear it, a growing part of me -a deeply despised part - is a little intrigued."

"I guess I've spent enough time with demons by now that their internal quarrels feel almost like a sort of guarded family lore."

"Still, now isn't the time."

voice "c-7i-35.wav" #Yumi (Kathy Pfautsch)
yum "Well, speaking of Kamika, I'd better go make sure she doesn't stink up my room any more than she already has."

show lucca neutral
voice "c-7i-36.wav" #Lucca (Victoria Wong)
luc "Oh... her ph-pheromones. Right."

voice "c-7i-37.wav" #Yumi (Kathy Pfautsch)
yum "I guess you mean to stick around and work on this?"

show lucca happy
voice "c-7i-38.wav" #Lucca (Victoria Wong)
luc "Yes, I'll be fine. I should take advantage of the remaining daylight."

voice "c-7i-39.wav" #Yumi (Kathy Pfautsch)
yum "Okay, well, I'll see you tomorrow, and we'll discuss our group project more then?"

show lucca happyclosed
voice "c-7i-40.wav" #Lucca (Victoria Wong)
luc "Y-yes! I look forward to it!"

voice "c-7i-41.wav" #Yumi (Kathy Pfautsch)
yum "Me, too."

"And I am, a lot more than I was before I headed out here..."

jump scene7iii
