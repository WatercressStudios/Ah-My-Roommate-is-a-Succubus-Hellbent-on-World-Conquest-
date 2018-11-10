label scene16:
scene dormhallway with None

show stacey neutral:
    align (0.3, 1.0)
show lucca sad flip with dissolve

"I lean against the wall nearest my door, trying to relax as much as I can."

"It's over. For now. It's way quieter when Kamika isn't cackling or boasting about something or other."
"...It occurs to me that I didn't hear any sick rave beats anymore. Did Kamika turn those off??"

show lucca nervous
show stacey neutrallook
show moe madclosed flip with easeinright:
    align (0.7, 1.0)
"Moe returns from his dorm, approaching us calmly."

voice "c-16-1.wav" #Lucca (Victoria Wong)
luc "S-so..."

voice "c-16-2.wav" #Yumi (Kathy Pfautsch)
yum "Right. I have to say thanks to everyone for helping me with this... situation. I thought I've had enough demons to last a lifetime, but then Kamika..."

voice "c-16-3.wav" #Yumi (Kathy Pfautsch)
yum "You guys really saved my ass."

show stacey smug
voice "c-16-4.wav" #Stacey (Ashe Thurman)
sta "It's whatever."

show lucca happy flip
voice "c-16-5.wav" #Lucca (Victoria Wong)
luc "Y-yeah! It's the least we could do..."

show moe mad flip
voice "c-16-6.wav" #Moe (CJ Heineman)
moe "What're your plans? I've dealt with enough of Kamika's shit, and there's no way in literal Hell I'm talkin' to that bitch."

show moe madlook flip
voice "c-16-7.wav" #Moe (CJ Heineman)
moe "I have to watch the partygoers anyways."

show moe madlook flip
show lucca neutral
show stacey neutrallook
voice "c-16-8.wav" #Moe (CJ Heineman)
moe "...Y'all got a plan for Kamika? Been trying to ignore the problem for a while now on my end..."

show stacey grin
voice "c-16-9.wav" #Stacey (Ashe Thurman)
sta "We could just tie her up."

voice "c-16-10.wav" #Yumi (Kathy Pfautsch)
yum "That sounds awf-wait."

show stacey smug
show lucca nervous
show moe smug flip
"I can't believe I'm actually considering this."

"I can't believe I'm not considering {i}worse{/i}."

voice "c-16-11.wav" #Yumi (Kathy Pfautsch)
yum "...As much as I would want to do that, I doubt it'd keep her. She may be a shitty demon, but she's still a demon."

show stacey neutral
voice "c-16-12.wav" #Stacey (Ashe Thurman)
sta "You just feel bad for her."

show lucca neutral
voice "c-16-13.wav" #Lucca (Victoria Wong)
luc "I-I agree with Yumi..."

show moe sigh
voice "c-16-14.wav" #Moe (CJ Heineman)
moe "Well, whatever you decide to do, count me out. I'll see you nerds later."

show stacey neutralclosed
voice "c-16-15.wav" #Stacey (Ashe Thurman)
sta "Yeah, I have homework and shit to do anyways."

if route = "kamika":
    jump scene17i

elif route = "lucca":
    jump scene17ii

elif route = "stacey":
    jump scene17iii
