label scene7iii:
scene dormhallway

#CHECK: flags for Scene 6 choice
#MIGHT NEED WORK; GONNA WRITE UP A SECTION FOR IF YUMI GOES TO SEE STACEY INSTEAD

"I get hit with a feeling of dread approaching my dorm room. I even took the long way back home to stave off the inevitable..."
"Is it just the thought that I can't leave her alone for one second without her causing trouble? Or am I just a glutton for punishment?"
"God, I can already imagine what she might say to me as soon as I get back."
"'Took you long enough, now lick my feet, peasant!' Or {i}something{/i} like that."
"I'm stuck thinking of all the possible ways she might mess with me as I make my way back to my dorm room."

if sawstacey = True:
    jump angrykamika
else:
    jump showerkamika

label showerkamika:
#BRANCH: use if opted to head to Kamika in Scene6
"But when I round the corner and head down the hall back to my room... I hear something."

voice "c-7iii-1.wav" #Kamika (Ariane Marchese)
kam "...lala... lalala...~"

voice "c-7iii-2.wav" #Yumi (Kathy Pfautsch)
yum "Huh...?"

"There's a pleasant sound filling the air. Not a particularly random sound, but one that's controlled and deliberate."
"It's constantly changing pitch and volume, but it never gets obnoxious. It's ebbing and flowing with all the careful precision in the world..."
"...Is that... singing?"

voice "c-7iii-3.wav" #Yumi (Kathy Pfautsch)
yum "..."

"Thinking it must be coming from someone else's room, I enter my own room in silence."

scene dormroom with dissolve

"...Except the singing only gets louder when I enter my room."
"I should be raising complaints about this, yet for some reason, I can't muster the will to. Singing like that shouldn't even be considered an inconvenience."
"Not only is there singing, but I can hear the shower in the bathroom running... and Kamika is nowhere to be found in here or my bedroom."
"Part of me wants to gag at the thought of giving her any sort of compliment, but the other half... wants to keep listening."
"I put my ear to the bathroom door, close my eyes... and listen."

#show CG of Kamika singing in the shower

voice "c-7iii-4.wav" #Kamika (Ariane Marchese)
kam "I know you feel the fire inside my heeeart~ It's burnin' so brightly for you~"

voice "c-7iii-5.wav" #Kamika (Ariane Marchese)
kam "I know how scared you are to even staaart~ Just don't ever say 'adieu~'"

voice "c-7iii-6.wav" #Kamika (Ariane Marchese)
kam "I want you stay, I want you to love me now and forever~"

voice "c-7iii-7.wav" #Kamika (Ariane Marchese)
kam "Baby pleeeease, don't let this beeee..."

voice "c-7iii-8.wav" #Kamika (Ariane Marchese)
kam "Our last night togetherrrr~"

"She sings with a passion and a drive that's hitherto unheard of..."
"Why was she ever talking about 'taking over the world' with singing like this?"
"...That {i}is{/i} Kamika in there, right?"
"I knock on the door and ask just to be safe."

voice "c-7iii-9.wav" #Yumi (Kathy Pfautsch)
yum "Kamika? Is that you in there?"

voice "c-7iii-10.wav" #Kamika (Ariane Marchese)
kam "EEP!"

voice "c-7iii-11.wav" #Kamika (Ariane Marchese)
kam "I-I mean, who's to say? Why don't you come on in and find out~?"

"...Yeah, no doubt about it. That's definitely her."

voice "c-7iii-12.wav" #Yumi (Kathy Pfautsch)
yum "N-no thanks, I'm good."

voice "c-7iii-13.wav" #Kamika (Ariane Marchese)
kam "Oh well, your loss~"

#fade CG
scene dormroom with dissolve

"I spend the next few precious moments catching up on my anatomy homework."
"What a relief it is to be able to relax in my own dorm room and not worry about some stupid demon. Even if their singing is better than I could have imagined..."
"In no time at all, however, my peace and quiet is interrupted by Kamika emerging from the bathroom."

show kamika d confidentclosed

voice "c-7iii-14.wav" #Kamika (Ariane Marchese)
kam "Ahh, now {i}that{/i} felt good~! I'm impressed this shower system manages to be so thorough~"

show kamika d happyclosed
voice "c-7iii-15.wav" #Kamika (Ariane Marchese)
kam "It's been so long since I had a proper shower... My skin feels all tingly~"

show kamika d licklips

voice "c-7iii-16.wav" #Kamika (Ariane Marchese)
kam "You can feel for yourself, if you'd like~"

voice "c-7iii-17.wav" #Yumi (Kathy Pfautsch)
yum "No matter how much you scrub, you'll {i}never{/i} be clean."

show kamika d sigh

voice "c-7iii-18.wav" #Kamika (Ariane Marchese)
kam "Aww, Yumi, I'm crushed..."

"I feel nauseous all of a sudden. How come every time I talk to her it feels like going through the adult magazines on the news rack?"

show kamika d neutral

voice "c-7iii-19.wav" #Kamika (Ariane Marchese)
kam "So you got a good listen to my singing, did you? I hoped I could do it in peace without {i}you{/i} around."

show kamika d glare

voice "c-7iii-20.wav" #Kamika (Ariane Marchese)
kam "Lemme guess; you're gonna tell me to keep it down, aren't you?"

voice "c-7iii-21.wav" #Yumi (Kathy Pfautsch)
yum "What, your singing? I {i}did{/i} hear that, and..."

voice "c-7iii-22.wav" #Yumi (Kathy Pfautsch)
yum "...it's really good, actually."

show kamika d wideyes
voice "c-7iii-23.wav" #Kamika (Ariane Marchese)
kam "...Really?"

show kamika s annoyedside
voice "c-7iii-24.wav" #Kamika (Ariane Marchese)
kam "I-I mean, of course {i}you{/i} would think it's good! You wouldn't know talent if it fell into your backyard!"

show kamika s annoyedclosed
voice "c-7iii-25.wav" #Kamika (Ariane Marchese)
kam "I-it's nothing {i}that{/i} special, alright?! It's just something I happened to pick up, that's all!"

voice "c-7iii-26.wav" #Yumi (Kathy Pfautsch)
yum "No, I'm serious. That was like a professional singing just now. You've got a singing voice that most people would only dream of having."

voice "c-7iii-27.wav" #Yumi (Kathy Pfautsch)
yum "If you really worked on that, I'm sure you'd have an amazing career ahead of you."

show kamika s gritside
voice "c-7iii-28.wav" #Kamika (Ariane Marchese)
kam "Mmn..."

"You'd think she'd be delighted to get a compliment, but now she just looks frustrated."
"What is it with demons having these overtly specific hang-ups? I don't think I'll ever get it..."

show kamika s sad

voice "c-7iii-29.wav" #Kamika (Ariane Marchese)
kam "It's not like that'll matter."

show kamika s sadside
voice "c-7iii-30.wav" #Kamika (Ariane Marchese)
kam "No matter how hard I try, I'll never be as good as you want me to be."

voice "c-7iii-31.wav" #Yumi (Kathy Pfautsch)
yum "Huh? Why not?"

show kamika s grit
voice "c-7iii-32.wav" #Kamika (Ariane Marchese)
kam "..."

show kamika d shoutclosed

voice "c-7iii-33.wav" #Kamika (Ariane Marchese)
kam "{i}Geez{/i}, why are we even talking about this?! You need to butt out of my business!"

if minion:
    jump trueloyalty
else:
    jump begtokamika

label angrykamika:
#BRANCH: use if went to see Stacey
#MEMO: write this!
"I let myself into my room, letting my things fall to the floor."

show kamika d glare with dissolve
voice "c-7iii-34.wav" #Kamika (Ariane Marchese)
kam "You're late."

voice "c-7iii-35.wav" #Yumi (Kathy Pfautsch)
yum "...Mm?"

show kamika d shout
voice "c-7iii-36.wav" #Kamika (Ariane Marchese)
kam "You're {i}super{/i} late. Do you have any idea how long you've kept me waiting!?"

voice "c-7iii-37.wav" #Yumi (Kathy Pfautsch)
yum "...I'unno. I have a social life. Mingling is a part of it."

show kamika d shoutclosed
voice "c-7iii-38.wav" #Kamika (Ariane Marchese)
kam "A minion has to prioritize not wasting their master's time!"

if minion = False:
    jump yumicorrectskamika
else:
    jump yumimustbeg
label yumicorrectskamika:
voice "c-7iii-39.wav" #Yumi (Kathy Pfautsch)
yum "...I don't recall volunteering to be your minion?"

show kamika d glare
voice "c-7iii-40.wav" #Kamika (Ariane Marchese)
kam "Wh- I- that's besides the point!"

voice "c-7iii-41.wav" #Yumi (Kathy Pfautsch)
yum "Whatever. You had something you wanted to talk to me about?"

show kamika d shoutclosed
voice "c-7iii-42.wav" #Kamika (Ariane Marchese)
kam "Pah! Forget it! I'm in a bad mood now!"

voice "c-7iii-43.wav" #Yumi (Kathy Pfautsch)
yum "...What, you waited the whole time for me, and now you don't wanna talk to me? What's your problem?"

show kamika d exclaim
voice "c-7iii-44.wav" #Kamika (Ariane Marchese)
kam "You're the problem, you duplicitous wench! We're done here!"

voice "c-7iii-45.wav" #Yumi (Kathy Pfautsch)
yum "W-wench...?"
jump spurnedkamika

label yumimustbeg:

voice "c-7iii-46.wav" #Yumi (Kathy Pfautsch)
yum "This is college, Kamika. Setting up industry connections? Life-long friendships and partnerships?"

show kamika d smug
voice "c-7iii-47.wav" #Kamika (Ariane Marchese)
kam "Pah! You don't need any of that when you have me!~"

voice "c-7iii-48.wav" #Yumi (Kathy Pfautsch)
yum "...Extremely questionable."

show kamika d thinkingclosed
voice "c-7iii-49.wav" #Kamika (Ariane Marchese)
kam "Ugh, you're so conceited. It really grinds my gears..."

show kamika d seduce
voice "c-7iii-50.wav" #Kamika (Ariane Marchese)
kam "...But I'm in a good enough mood to come around and forgive you. Squeeze you in for a five o'clock evil plan brainstorm.~"

voice "c-7iii-51.wav" #Yumi (Kathy Pfautsch)
yum "...Ugh... if you insist."

show kamika d neutral
voice "c-7iii-52.wav" #Kamika (Ariane Marchese)
kam "Ohhh, I don't like that tone. Opportunities like these rarely come for free.~"

show kamika d smug
voice "c-7iii-53.wav" #Kamika (Ariane Marchese)
kam "I can't let an insect like you walk all over me. I'm {i}no{/i} insect."

"Could've fooled me. She's basically a cockroach, she's impossible to get rid of..."

show kamika d evilgrin
voice "c-7iii-54.wav" #Kamika (Ariane Marchese)
kam "Uehehehe... Now {i}kneel.{/i}"

voice "c-7iii-55.wav" #Yumi (Kathy Pfautsch)
yum "...Pardon?"

show kamika evilsmile
voice "c-7iii-56.wav" #Kamika (Ariane Marchese)
kam "Get on your knees and {i}beg{/i} for my forgiveness!~"

voice "c-7iii-57.wav" #Yumi (Kathy Pfautsch)
yum "...Are you insane??"

jump begtokamika

label trueloyalty:
#BRANCH: dialogue path based on not seeing stacey AND agreeing to be minion

show kamika d shout
voice "c-7iii-58.wav" #Kamika (Ariane Marchese)
kam "{i}You're{/i} the minion, and {i}I'm{/i} the mistress! I should {i}never{/i} have to divulge any of {i}my{/i} personal business to the likes of {i}you!{/i} Got it?!"

voice "c-7iii-59.wav" #Yumi (Kathy Pfautsch)
yum "Alright, I get it! Sorry for giving you a {i}compliment{/i}, Jesus..."

show kamika d neutralclosed

voice "c-7iii-60.wav" #Kamika (Ariane Marchese)
kam "Humph! You'd {i}better{/i} be sorry! We can't have conversations like this distracting us from our {i}real{/i} goal!"

show kamika d confident

voice "c-7iii-61.wav" #Kamika (Ariane Marchese)
kam "And {i}speaking{/i} of that, I've just finished preparing an itinerary for the first phase of our plan!"

"Well {i}finally{/i}, it looks like I'm getting somewhere with her."

voice "c-7iii-62.wav" #Yumi (Kathy Pfautsch)
yum "Well? What's the plan, then?"

show kamika d happy

voice "c-7iii-63.wav" #Kamika (Ariane Marchese)
kam "Finally! You're starting to show some initiative! Someone looking to prove herself to me!"

voice "c-7iii-64.wav" #Yumi (Kathy Pfautsch)
yum "Ugh..."

jump kamikapowerpoint


label begtokamika:
#if kamika wants you to beg (because you either went to see stacey, or didn't agree to be a minion, but not both)
voice "c-7iii-66.wav" #Kamika (Ariane Marchese)

show kamika d evilsmile
kam "What was that, my little minion? I don't think I heard enough begging~"

voice "c-7iii-67.wav" #Yumi (Kathy Pfautsch)
yum "...Are you serious?"

show kamika d neutral
voice "c-7iii-68.wav" #Kamika (Ariane Marchese)
kam "Oh, you think I was going to forgive you {i}that{/i} easily? You disappoint me so much..."

voice "c-7iii-69.wav" #Yumi (Kathy Pfautsch)
yum "What? I'm allowed to see other people. You honestly have a problem with that?"

voice "c-7iii-70.wav" #Yumi (Kathy Pfautsch)
yum "...What am I saying, {i}of course you do{/i}."

show kamika d mad
voice "c-7iii-71.wav" #Kamika (Ariane Marchese)
kam "A good minion has eyes only for their empress! No one else!"

show kamika d evilgrin
voice "c-7iii-72.wav" #Kamika (Ariane Marchese)
kam "If you want to get back into my good graces, you'll have to get on your knees and {i}beg{/i} to see the fruits of my labor!~"

"God {i}dammit{/i}, this fucking demon has to make {i}EVERYTHING{/i} a pain in the ass..."

"If I want to know anything about Kamika's plan, I might have to prostrate myself in front of her. Is it worth it...?"

menu:
    "Beg for forgiveness.":
        $ kamika_points += 1
        jump prostateyourself
    "Tell her off.":
        jump screwyoukamika

label prostateyourself:

"I clasp my hands together and give her a pleading look once more."

voice "c-7iii-73.wav" #Yumi (Kathy Pfautsch)
yum "Oh, {i}please{/i} forgive my impudence, mistress! I just wanna know {i}SO BADLY{/i} about your delightfully devilish ideas!"

#show kam laughing

show kamika d evilsmileclosed
voice "c-7iii-74.wav" #Kamika (Ariane Marchese)
kam "{i}Nyahahaha~!{/i} Well, with begging like that, who am I to leave my {i}favorite{/i} minion in the dark~?"

"Any more of this shit and I'm gonna have an aneurysm."

jump kamikapowerpoint

label screwyoukamika:


voice "c-7iii-75.wav" #Yumi (Kathy Pfautsch)
yum "Are you serious?"

show kamika d seduce
voice "c-7iii-76.wav" #Kamika (Ariane Marchese)
kam "Ueeeehehehehehe! I'm {i}always{/i} serious, my dear. Now your knees are {i}awfully{/i} far from the floor, aren't they?"

voice "c-7iii-77.wav" #Yumi (Kathy Pfautsch)
yum "You're serious."

show kamika d neutral
voice "c-7iii-78.wav" #Kamika (Ariane Marchese)
kam "Now does count under \"always\", does it not?"

voice "c-7iii-79.wav" #Yumi (Kathy Pfautsch)
yum "Oh my God, you're actually serious."

voice "c-7iii-80.wav" #Yumi (Kathy Pfautsch)
yum "What the fuck is {i}wrong{/i} with you."

show kamika d wideeyes
voice "c-7iii-81.wav" #Yumi (Kathy Pfautsch)
yum "Wait, no. We don't have time for that. What the fuck is {i}right{/i} with you?"

voice "c-7iii-82.wav" #Kamika (Ariane Marchese)
kam "Um."

voice "c-7iii-83.wav" #Yumi (Kathy Pfautsch)
yum "Why in the name of Satan's strawberry asshole do you think {i}anyone{/i} would put up with your bullshit, let alone {i}beg{/i} for it?"

voice "c-7iii-84.wav" #Yumi (Kathy Pfautsch)
yum "What does anyone have to gain from this except you?"

voice "c-7iii-85.wav" #Yumi (Kathy Pfautsch)
yum "How are you so utterly, completely braindead in your approach to relationships that you think this is okay?"

show kamika d mad
voice "c-7iii-86.wav" #Yumi (Kathy Pfautsch)
yum "Are you actually that stupid? Is anyone actually this stupid?"

voice "c-7iii-87.wav" #Yumi (Kathy Pfautsch)
yum "I used to babysit. There was this kid I was watching over. She ate a penny."

voice "c-7iii-88.wav" #Yumi (Kathy Pfautsch)
yum "For some reason, she thought that was a good thing, so she ate more pennies."

voice "c-7iii-89.wav" #Yumi (Kathy Pfautsch)
yum "That kid? That kid was stupid. And {i}she is still not this stupid.{/i}"

show kamika d glare
voice "c-7iii-90.wav" #Yumi (Kathy Pfautsch)
yum "{i}You are more of an idiot than the kid who eats pennies, Kamika.{/i}"

voice "c-7iii-91.wav" #Yumi (Kathy Pfautsch)
yum "{i}She was eight.{/i}"

show kamika d shoutclosed
voice "c-7iii-92.wav" #Kamika (Ariane Marchese)
kam "Ugh, excuse me! I would never eat anything as worthless as pennies."

show kamika d smugclosed
voice "c-7iii-93.wav" #Kamika (Ariane Marchese)
kam "Only the finest currency is permitted to give my body energy, thank you very much!"

voice "c-7iii-94.wav" #Yumi (Kathy Pfautsch)
yum "Oh my god you're really that insane."

show kamika d deadpan
voice "c-7iii-95.wav" #Yumi (Kathy Pfautsch)
yum "I was kidding. There was no kid who eats pennies."

voice "c-7iii-96.wav" #Yumi (Kathy Pfautsch)
yum "But now there is. It's you. The kid who eats {i}fucking quarters.{/i}"

show kamika d angryshout
voice "c-7iii-97.wav" #Kamika (Ariane Marchese)
kam "I am not a kid!"

voice "c-7iii-98.wav" #Yumi (Kathy Pfautsch)
yum "You are so utterly lacking in self awareness that you wouldn't even be able to tell if you were on fire."

show kamika d mad
voice "c-7iii-99.wav" #Kamika (Ariane Marchese)
kam "I am {i}always{/i} on fire!"

voice "c-7iii-100.wav" #Yumi (Kathy Pfautsch)
yum "This. This right here. This is the problem."

voice "c-7iii-101.wav" #Yumi (Kathy Pfautsch)
yum "You act like you're hot shit that everyone loves. You're not. You're cold shit."

voice "c-7iii-102.wav" #Yumi (Kathy Pfautsch)
yum "You are the coldest shit. The frozen fucking tundra of defecation."

show kamika d wideeyes
voice "c-7iii-103.wav" #Yumi (Kathy Pfautsch)
yum "Hell literally froze over your shit."

show kamika d angrysurprise
voice "c-7iii-104.wav" #Kamika (Ariane Marchese)
kam "Okay, screw you! Just because you're jealous doesn't mean you can talk to me like that!"

voice "c-7iii-105.wav" #Yumi (Kathy Pfautsch)
yum "Then maybe you should make a rational decision for once in your life and go somewhere where you can't hear me."

show kamika d shoutclosed
voice "c-7iii-106.wav" #Kamika (Ariane Marchese)
kam "Fine!"

hide kamika with dissolve
"She storms out in a huff."

voice "c-7iii-107.wav" #Kamika (Ariane Marchese)
kam "Bitch!"

#sfx doorslam
"And she slams the door. How quaint."

"Thank God. Free at last."
jump s7iiimerge
#MEMO: let's see what slike comes up with


label kamikapowerpoint:
#BRANCH: if you agreed to help Kamika by begging or by being a TRUE LOYALIST

#CG: show CG of Kamika showing Phase 1 Powerpoint presentation intro on a laptop

show kamika d happyclosed
voice "c-7iii-65.wav" #Kamika (Ariane Marchese)
kam "Alright, come hither. We have {i}so much{/i} to discuss!~"

"Before long, Kamika puts together another presentation - again, using {i}my{/i} laptop - and proceeds to divulge her plan to me."

voice "c-7iii-108.wav" #Kamika (Ariane Marchese)
kam "Phase 1 of 'Kamika's Ultimate Plan for Worldwide Enrapture' is a simple task, but nonetheless extremely important!"

voice "c-7iii-109.wav" #Yumi (Kathy Pfautsch)
yum "Do you just sit around making PowerPoints all day? Don't you have {i}anything{/i} better to do with your time?"

voice "c-7iii-110.wav" #Kamika (Ariane Marchese)
kam "Th-that's neither here nor there, minion!"

voice "c-7iii-111.wav" #Kamika (Ariane Marchese)
kam "The events contained within will be the deciding factor in how the rest of the operation proceeds, so listen up and listen well!"

#CG: show next slide in CG, mediocre acrylic paint drawing of Kamika watching a singer

voice "c-7iii-112.wav" #Yumi (Kathy Pfautsch)
yum "Still using my art supplies, ugh. I don't even care anymore..."

voice "c-7iii-113.wav" #Kamika (Ariane Marchese)
kam "What I've learned from watching your world is that {i}anyone{/i} can be captivated by a good singer!"

voice "c-7iii-114.wav" #Kamika (Ariane Marchese)
kam "Singing has the power to bring together people from all over the world, and a good singer can enthrall the hearts of many with hardly any effort at all!"

voice "c-7iii-115.wav" #Yumi (Kathy Pfautsch)
yum "...So your plan is to become a professional singer? Isn't that what I just-"

voice "c-7iii-116.wav" #Kamika (Ariane Marchese)
kam "Are you interrupting me with a pointless diatribe yet again?"

voice "c-7iii-117.wav" #Yumi (Kathy Pfautsch)
yum "No, I just... you know what, nevermind. Go on."

voice "c-7iii-118.wav" #Kamika (Ariane Marchese)
kam "So {i}anyways{/i}, we need to draw together a crowd through singing, and {i}who{/i} is able to do that?"

voice "c-7iii-119.wav" #Yumi (Kathy Pfautsch)
yum "A professional diva?"

#CG: show next slide in CG, mediocre acrylic paint drawing of Kamika singing to an adoring crowd

voice "c-7iii-120.wav" #Kamika (Ariane Marchese)
kam "{i}Me{/i}, obviously!"

voice "c-7iii-121.wav" #Yumi (Kathy Pfautsch)
yum "Oh. I guess compromises have to be made..."

voice "c-7iii-122.wav" #Kamika (Ariane Marchese)
kam "There's no way the humans of this world will be able to resist the charming voice of an all-powerful succubus such as myself!"

voice "c-7iii-123.wav" #Kamika (Ariane Marchese)
kam "Once they hear me sing, they'll start tripping over themselves just to lose themselves to the sound of my voice~"

voice "c-7iii-124.wav" #Kamika (Ariane Marchese)
kam "And by the time I'm finished, I'll have amassed a crowd of followers who will just be {i}begging{/i} me to leave them in permanent enrapture~!"

voice "c-7iii-125.wav" #Kamika (Ariane Marchese)
kam "It'll be the {i}perfect{/i} way to start building my beautiful utopia!"

voice "c-7iii-126.wav" #Yumi (Kathy Pfautsch)
yum "Okay... And what'll you do after that? Do you even have a way to sing to a whole crowd in the first place?"

voice "c-7iii-127.wav" #Kamika (Ariane Marchese)
kam "Don't worry about the little details; I've got it all under control!"

"It sounds like such a simple plan, and that's what scares me the most."
"If she's able to use her singing as a means to convert an entire audience of people... there's no telling {i}what{/i} she might do after that."

show kamika d confident

"I mean. If she's able to. That's a {i}biiiiiiiiiig{/i} if."

#fade CG

voice "c-7iii-128.wav" #Kamika (Ariane Marchese)
kam "We'll initiate the plan tomorrow as soon as possible! Don't be late!"

voice "c-7iii-129.wav" #Yumi (Kathy Pfautsch)
yum "Uh, if you want me as soon as possible, then you might want to wait until later in the day. We still have classes in the morning."

show kamika d neutral

voice "c-7iii-130.wav" #Kamika (Ariane Marchese)
kam "What, are you really so concerned with {i}those{/i} obligations? We're making {i}history{/i} here, you know!"

voice "c-7iii-131.wav" #Yumi (Kathy Pfautsch)
yum "I paid good money to move here and take classes, and I don't have the time to skip out on them for any of this."

voice "c-7iii-132.wav" #Yumi (Kathy Pfautsch)
yum "If you want my help, you're going to have to work around my schedule. That's just the way it is."

show kamika d sigh
voice "c-7iii-133.wav" #Kamika (Ariane Marchese)
kam "...Very well. But I still expect you in my presence as {i}soon{/i} as you have some free time, understood?!"

voice "c-7iii-134.wav" #Yumi (Kathy Pfautsch)
yum "I got it, I got it."

"She acts as though she's exempt from being a student, too. If anything, she'll probably get kicked out long before her plans even succeed."

voice "c-7iii-135.wav" #Yumi (Kathy Pfautsch)
yum "Are we done for the day? I still have things to do."

show kamika d mad
voice "c-7iii-136.wav" #Kamika (Ariane Marchese)
kam "Not so fast! I have one more thing to bring up."

show kamika d thinkingclosed

voice "c-7iii-137.wav" #Kamika (Ariane Marchese)
kam "While you were on your little walk earlier, you didn't happen to be {i}cheating{/i} on me, didn't you?"

voice "c-7iii-138.wav" #Yumi (Kathy Pfautsch)
yum "...What?"

show kamika d thinking

voice "c-7iii-139.wav" #Kamika (Ariane Marchese)
kam "You know what I mean! Are you hiding a boyfriend from me? What about a {i}girlfriend{/i}, huh?"

show kamika d glare
voice "c-7iii-140.wav" #Kamika (Ariane Marchese)
kam "Were you conspiring with someone in secret instead of coming back to me as you should have?"

voice "c-7iii-141.wav" #Yumi (Kathy Pfautsch)
yum "What are you talking about? I haven't been 'conspiring in secret' with anyone!"

show kamika d thinkingclosed

voice "c-7iii-142.wav" #Kamika (Ariane Marchese)
kam "I'm just making sure we completely understand one another here. If you're going to be my minion, you must make my master plan your top priority!"

show kamika d evilsmile
voice "c-7iii-143.wav" #Kamika (Ariane Marchese)
kam "That means I expect your presence before me at {i}all times!{/i} You must devote your existence {i}only{/i} to me!"

show kamika d smug

voice "c-7iii-144.wav" #Kamika (Ariane Marchese)
kam "No exceptions. You are mine, and mine alone."

show kamika d neutral
voice "c-7iii-145.wav" #Kamika (Ariane Marchese)
kam "If I see you with anyone else... our arrangement is over. Am I clear?"

"This intensity in her voice... she wouldn't hesitate to disassociate herself from me if I step out of line even once!"
"If I do go against her, it'll be that much harder to know what she's planning. That is, assuming she even {i}has{/i} anything else planned other than this."
"But I can't betray her trust now, not when I've come this far... I nod my head."

voice "c-7iii-146.wav" #Yumi (Kathy Pfautsch)
yum "Clear as crystal."

show kamika d happy

voice "c-7iii-147.wav" #Kamika (Ariane Marchese)
kam "Very good. Maybe I was right to trust you after all."

show kamika d seduce
voice "c-7iii-148.wav" #Kamika (Ariane Marchese)
kam "Who knows? If things go well, I might just give you a kiss~"

voice "c-7iii-149.wav" #Yumi (Kathy Pfautsch)
yum "I'd rather get a kiss from a hooker than from {i}you.{/i}"

show kamika d confident

voice "c-7iii-150.wav" #Kamika (Ariane Marchese)
kam "Hah! Insult me all you like, but you won't be saying that for much longer once everything is set in motion."

show kamika d happyclosed
voice "c-7iii-151.wav" #Kamika (Ariane Marchese)
kam "Speaking of which, {i}I{/i} have to go make my final preparations for tomorrow."

show kamika d evilgrin
voice "c-7iii-152.wav" #Kamika (Ariane Marchese)
kam "See you then, my dear~"

hide kamika with dissolve

"Kamika disappears into my bedroom, giggling madly to herself."
"Against all the odds, I've gained enough of her favor for her to spill out her plan to me... but I feel as though she's not letting me in on what else she has in store."
"And if tomorrow's plan manages to succeed, who knows what that could mean for the student body?"
"I have to find a way to sabotage it... I won't allow Kamika to have her way with me {i}or{/i} this school!"
"I'll just have to wait for my opportunity. For now, I'd better focus on the things that I can do right now."
$ helpkamika = True
jump s7iiimerge

label spurnedkamika:
#BRANCH: dialogue path based on not helping kamika (either by refusing to beg OR by both not agreeing to be a minion and going to see stacey)

show kamika d mad
voice "c-7iii-153.wav" #Kamika (Ariane Marchese)
kam "And don't think for a second that you're getting on my good side! I {i}know{/i} you're trying to win me over after you spurned me so badly!"

show kamika d glare
voice "c-7iii-154.wav" #Kamika (Ariane Marchese)
kam "Well it's {i}not{/i} going to work! I can't have anyone be half-hearted about serving me; either they give themselves to me willingly, or I {i}make{/i} 'em serve me!"

show kamika madclosed

voice "c-7iii-155.wav" #Kamika (Ariane Marchese)
kam "So if you think I'm gonna let you take advantage of me like this, then you'd better get your head out of your ass {i}right now!{/i} Do I make myself clear?!"

voice "c-7iii-156.wav" #Yumi (Kathy Pfautsch)
yum "Alright, alright! Sorry for giving you a {i}compliment{/i}, Jesus..."

hide kamika with dissolve

"Kamika storms off into my bedroom, not even acknowledging my last sentence."
"Well, that was utterly pointless. I thought maybe we'd reach some common ground, but she's still acting like a complete bitch."
"I really hope I can find a way to resolve all this... I don't think I have much time left."
"I just hope whatever Kamika has planned, it doesn't happen soon."
jump s7iiimerge
#MERGE: dialogue paths converge here

label s7iiimerge:
scene black with dissolve
"I spend the rest of the night catching up on my anatomy homework, and without much else provocation from Kamika, I eventually turn in for the night."
"..."
"... ..."


jump scene8
