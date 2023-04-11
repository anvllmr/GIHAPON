# Insert Chapter 1 here

label story_ch_01:

#Intro Scene
    pause 1.5

    #SFX - Windy
    play music AMB_rain fadein 1.0
    
    pause 1.0

    ex_dream "Urk{cps=*0.15}...{/cps}
    {w=1.0}Agh{cps=*0.15}...{/cps}
    {w=2.0}wh- what is this pressure?{w=1.5}{nw}"
    window hide
    pause 1.5

    play sound SFX_thunder
    with sflash

    pause 0.5
    window show
    ex_dream "It’s so cold{w=1.5}{nw}"
    window hide
    pause 1.5

    window show
    ex_dream "Is it? Is it {=hl}raining{/=hl}?{w=1.5}{nw}"
    window hide
    pause 1.5

    #SFX - Rumbling
    play sound SFX_thunder
    with sflash

    pause 0.8

    play sound SFX_thunder
    with sflash

    pause 0.5
    window show
    ex_dream "ack!{w=1.5}{nw}"
    window hide
    pause 1.5

    window show
    ex_dream "I- I can’t hold on any longer{cps=*0.15}...{/cps}
    {w=1.5}Losing consciousness{cps=*0.15}...{/cps} {w=1.5}{nw}"
    window hide
    pause 1.0

    play sound SFX_thunder
    with sflash

    pause 0.5
    play sound SFX_Sweep

    scene white
    with dissolve

    pause 1.5

    stop music fadeout 1.0

    pause 1.5

    #Screen FX - Fade to White

#SCENE 1 : EXT. SUBURBAN STREET - JUNE 12, 1992. 11:15 A.M.

    #Screen FX - Flash

    window auto
    
    show bgbusint at bus_shake        
    
    pause 0.1

    with sflash

    with sflash

    #SFX - Vehicle Driving
    play music AMB_bus fadein 1.0
    show bgbusint
    pause 1.0

    play sound SFX_Smack
    MC "Aaaaaah!{w=1.0}{nw}" with sshake
    extend" huff
    {w=0.5}huff.
    {w=0.5}{=txt_vo}(Drat! It’s that {=hl}dream{/=hl} again.
    {w=0.5}I can’t with these cramped spaces.)"

    MC "{=txt_vo}(Great,
    {w=0.3}It looks like I’ve made myself a sight for sore eyes for these people with my waking scream.
    {w=0.5}They’re looking at me now.
    {w=0.5}Seems I’ve startled them...)"

    MC "Ah sorry about that."
    window hide
    pause 1.5

    #Show image of Bus Window + View

    pause 1.5

    window show
    MC "Well, looks like I’m near.
    {w=0.5}This bus is nearing the terminal already.
    {w=0.5}Geez, I slept through most of the ride.{w=0.3} Way to miss the view of the ride."

    ex_bus "Alright everyone! We’ve arrived at {=hl}Iliganon City{/=hl}."

    MC "This is it I guess.
    {w}I'm finally going back to this {=hl}little secluded strip of land{/=hl}, huh?"
    window hide

    stop music fadeout 1.0

    pause 0.5

    scene bg-flatcolors2
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}EXT. SUBURBAN STREET - JUNE 12, 1992. 11:15 A.M.{/cps}"
    window hide

    play music BGM_casual
    pause 1.5

    window show
    MC "It's been what? {=hl}5 years{/=hl} already?
    {w=0.5}Iliganon City{cps=*0.15}...{/cps}
    {p}This isn’t a super remarkable town on the get go{w=0.3} but{w=0.5} it’s got breathtaking views from the rivers and the mountain tops."
    window hide
    pause 1.5

    window show
    MC "This feels nostalgic already…
    {p}Though, something feels strange.
    {w=0.5}Feels like there’s less loud and lively sounds of people hanging around."

    MC "To be fair, if it were me, I wouldn't stay here for too long."
    window hide
    pause 1.5

    #Show image of view from Bus Terminal
    pause 1.5

    window show
    MC "Wow{cps=*0.15}...{/cps}
    {w=0.5}so this is Iliganon City now?
    {w=0.5}There seems to be more buildings than before."

    MC "I’d expected this place to be more of a dump than what it is right now.
    {w=0.5}Seems they’ve got their act together since the last time I was here."

    MC "Well, I hope I still know the way to my old house.
    {w=0.5}The least I want to happen is me getting lost in my own childhood hometown."
    window hide

    stop music fadeout 1.0

    pause 1.0

#SCENE 2 : EXT. BARANGAY STREET DIMAHAMPAK - JUNE 12, 1992. 11:30 A.M.

    scene bg-outsidemaxhouse
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}EXT. BARANGAY STREET DIMAHAMPAK - JUNE 12, 1992. 11:30 A.M.{/cps}"
    window hide

    pause 1.5

    window show
    MC "I think I see my house from here."
    window hide

    pause 1.0

    window show
    MC "{=txt_vo}(I’m nearing the gate to my house.
    {w}But wait who’s that by the pathway?)"

    #Show Berto Char Portrait
    show berto - neutral
    with dissolve

    play music BGM_uneasy

    side_berto "Hoy!
    {w=0.5}{=hl}Maximo{/=hl},
    {w=0.5}is that you?"

    MC "{=txt_vo}(Taking a closer look at this guy...
    {w=0.5}He looks familiar)"

    side_berto "Hmm?
    {w}What are you looking at?
    {w}You are Max,
    {w=0.5}aren’t you?"

    MC "{=txt_vo}(Oh, it’s {=hl}Berto{/=hl}.
    {w}Our neighbor and dad’s old Sabong buddy.)"

    MC "{cps=15}...{/cps} uhh.
    {w}Oh Yeah,
    {w}It’s me.
    {w=0.5}I just arrived not too long ago."

    side_berto "Woah,
    {w=0.5}I thought those old hags were bluffing but It really is you.
    {w}Why did you come back, huh?"

    MC "I’m staying for a while, Po."

    side_berto "So,
    {w=0.5}did you just up and forget why you even {=hl}left this place{/=hl}?
    {w}Enjoy shamelessly staying, huh?
    {w}You do know peoples are talking"

    MC "Are you for real?
    {w}Sorry Mr. Berto but I didn’t come here to entertain some half baked gossip."

    MC "Well if you’ll excuse me I have to get to my house."

    side_berto "Whatever Kid.
    {w=0.5}Knowing that you’re back, this town’s gonna go {=hl}under the dumps{/=hl}"
    window hide

    pause 1

    hide berto - neutral
    with dissolve

    stop music fadeout 1.0

    pause 1

    window show
    MC "{=txt_vo}(God, I never got along with Mr. Berto. He’s always been a pain)"
    MC "{=txt_vo}(Anyways,
    {w=0.5}I’ve arrived. Let's see how this place looks after all these years)"
    window hide

#SCENE 3 : INT. MONTERO HOUSE - LIVING ROOM - JUNE 12, 1992. 11:40 A.M.

    scene bg-intmaxhouselr
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - LIVING ROOM - JUNE 12, 1992. 11:40 A.M.{/cps}"
    window hide

    pause 1.5

    window show
    MC "Hello?
    {w=0.5}Anyone home?
    {w=0.5}Hmm{cps=*0.15}...{/cps} seems like {=hl}Auntie Cheng{/=hl} isn’t here. How bout I take load off the couch."

    #SFX - Couch Shuffle

    play sound SFX_Smack
    MC "*cough*" with sshake
    play sound SFX_Smack
    extend " *cough*" with sshake
    extend " I thought Auntie Cheng keeps the house clean?
    {w=0.5} Did she quit?"

    #SFX - Stomach Growl

    MC "{=txt_vo}(Well,
    {w=0.5}obviously, I need to figure out where to eat first, then tidy this place up.)"

    MC "{=txt_vo}(I think there was a {=hl}karinderya{/=hl} nearby. I saw one coming up here.)"
    window hide

#SCENE 4 : DIKUMAKAIN KARINDERIA EXT. BARANGAY STREET DIMAKITA - JUNE 12, 1992. 12:15 P.M.

    #Show Stills of Neighboorhood

    scene bg-extdikumakain
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}DIKUMAKAIN KARINDERIA EXT. BARANGAY STREET DIMAKITA - JUNE 12, 1992. 12:15 P.M.{/cps}"
    window hide

    pause 1.5

    play music BGM_palengcare

    window show
    MC "Dikumakain Karinderia...
    {w=0.5}What a weird name for a place where you’d eat."

    MC "{=txt_vo}(As I say that,
    {w=0.5}I see a figure slowly approaching me from the Karinderia.
    {w} He seems familliar)"
    window hide    

    pause 1.0

    show dodong - confused
    with dissolve
    
    $ Dodong = "???"

    window show
    side_dodong "Uhmm...
    {w=0.5}Excuse me sir, can I help you?
    {w=0.5}You’ve been staring at our sign for quite a bit."
    
    MC "{=txt_vo}(Oh, it's Dodong.
    {w=0.5}We used to play a lot when we were kids and high school buddies.)"
    
    MC "{=txt_vo}(I remember when our parents were furious at us because he convinced me to stay with him all night in a computer shop and went home at 6 AM.) "
    window hide

    #Show dodong surprised

    show dodong - surprised
    with dissolve
    
    pause 0.5
    $ Dodong = "Dodong"

    window show
    side_dodong "Hey wait a minute!
    {w=0.5}{=hl}Max{/=hl}!?
    {w}Long time no see, Max.
    {w}I didn’t know you were in town."

    MC "Hey, Dodong.
    {w=0.5}It’s been a while..."

    MC "{=txt_vo}(As I say that, Dodong pulls me inside the Karinderya to the counter)"

    MC "Hey, Wait!"
    window hide

    show dodong at offscreenright
    with decay10inleft

    pause 1
    
    #Scene Transition to Interior

    scene bg-intdikumakain
    with pushright

    show dodong - neutral at center
    with decay10inleft

    pause 1

    window show
    side_dodong "How are you?
    {w=0.5}What have you been up to?
    {w=0.5}After graduation, you {=hl}disappeared{/=hl} without a trace.
    {w}We're very worried about you, Max." 
    
    side_dodong "Your folks don't live here anymore, but why are you here?"
    
    MC "..."

    MC "{=txt_vo}(I guess he doesn't know?)"

    MC "Yeah...
    {w=0.5}We suddenly had to move back then.
    {w}Didn’t get a chance to tell you guys."
    
    MC "I actually have some business here
    {w}so I’m staying for a while..."

    side_dodong "Oh, really?
    {w=0.5}Like what?
    {w=0.5}Are you-"
    window hide

    #Screen FX - Screen Shake
    #Screen FX - Flash
    #SFX - Crash Sound

    show dodong - surprised at right
    with decay10inleft

    show dy - neutral at left with decay10inleft 
    with sflash

    #Dodong Surprised
    #Tektiv Goes in

    $ Dy = "???"
    
    window show
    play sound SFX_Smack
    d "Dong!{w=0.5}{nw}" with sshake
    extend " Can you get me Pinakbet with Rice?
    {w=0.5}Don’t forget the sabaw."
    window hide

    show dodong - confused
    with dissolve
    #Dy slides to left

    show dy - neutral at offscreenleft
    with decay10inleft

    window show
    MC "What the?
    {w=0.5}Rude?
    {w=0.5}Who even is this guy?
    {w=0.5}He just bumped me on the shoulder with no tact."
    window hide

    #Dy slides back in

    show dy - neutral at left
    with decay10inright

    window show
    d "Also give me a bottle of ice cold coke."
    window hide

    #Dy slides t oleft

    show dy - neutral at offscreenleft
    with decay10inleft

    show dodong - happy
    with dissolve

    window show
    side_dodong "Yes, Sir!
    {w=0.5}Coming up"
    window hide

    #dodong slides to the right

    show dodong at offscreenright
    with decay10inright

    window show
    MC "{=txt_vo}(Dodong is preparing the food for this guy.
    {w=0.5}He knows his stuff,
    {w=0.5}picking up the food from the pot pretty swiftly.)"
    window hide

    pause 0.5

    window show
    side_dodong "Here you go, Sir!"
    window hide

    pause 0.5
    #dodong slides back

    show dodong - neutral at center
    with decay10inleft

    pause 0.5    
    
    window show
    side_dodong "That’s investigator {=hl}Tektiv Dy{/=hl}."

    MC "Investigator?
    {w=0.5}He’s a bit of a clutz if I ever saw one."

    side_dodong "Ah,
    {w=0.5}It’s probably because he’s been on this {=hl}case being called off{/=hl} if he doesn’t meet the deadline on time."

    MC "{=txt_vo}(That’s interesting.
    {w=0.5}What could have made the case go for so long?)"
    
    MC "Oh, no wonder. What’s the case he’s investigating?"
    window hide

    #Tektiv cuts in

    $ Dy = "Dy"

    show dodong - neutral at right
    with decay10inleft

    show dy - neutral at left
    with decay10inleft

    window show
    d "Oh yeah,
    {w=0.5}about that coke?
    {w=0.5}Uhm scrap that, do you have coffee by chance?"
    
    d "I’m rather drowsy right now.
    {w=0.5}I need a little “pick me up.”"
    $dy_talking = False

    side_dodong "Sure, let me get that for you!"
    side_dodong "Hold that thought, I'll be right back."

    MC "Sure, no problem."
    window hide

    #Dodong slides back out
    
    
    show dodong - neutral at offscreenright
    with decay10inleft

    pause 1.0

    stop music fadeout 1.0
    
    show dy at center
    with decay10inleft

    show dy - thinking
    with dissolve
    pause 1.5

    show dy - confused
    with dissolve
    pause 0.5

    window show
    MC "{=txt_vo}(Oh no, He’s looking at me)"
    window hide

    play music BGM_tektiv

    pause 0.5

    window show
    d "Hmmm…
    {w=0.5}I haven't seen you around here before,
    {w=0.5}yet you look {=hl}familiar{/=hl}."
    d "And who might you be?"

    MC "{=txt_vo}(Now you're asking me that?
    {w=0.5}I think it should’ve been the other way around.)" 
    MC "{=txt_vo}(Didn’t he just say I looked familiar?
    {w=0.5}Should I tell him my name?)"
    window hide

    menu:
        "Tell him my name":
            
            window show
            MC "I just arrived here.
            {w=0.5}My name’s {=hl}Max Christian{/=hl}"

            pause 0.5
            show dy - thinking
            with dissolve
            pause 0.5

            play sound SFX_Foreshadow

            d "{=hl}Max Christian{/=hl} huh..."
    
            window hide
            
            show dy at left
            with decay10inleft

            show dodong - happy at right
            with decay10inleft

            window show
            side_dodong "Here’s a hot cup of coffee sir!"

            show dy - smug
            with dissolve
            
            d "Thanks kid!"
    

            MC "(Was it safe to be saying my name to him?)"
            window hide

        "Stay Silent":

            window show
            MC "..."
            window hide

            pause 1.0

            show dy - annoyed
            with dissolve

            window show
            
            d "Hmm...
            {w=1.0}Silent type eh?"
    
            window hide

            show dy at left
            with decay10inleft

            show dodong - happy at right
            with decay10inleft

            window show
            side_dodong "Here’s a hot cup of coffee sir!"
            window hide

            pause 0.5

            show dodong - confused
            with dissolve

            window show
            side_dodong "..."
            window hide

            window show
            d "..."
            window hide

            show dodong - happy
            with dissolve

            window show
            side_dodong "Oh, him?
            {w=0.5}That’s {=hl}Max Christian{/=hl}.
            {w=0.5}An old friend of mine."

            show dy - smug
            with dissolve

            d "Thanks kid!
            {w=0.5}So your name’s Max?"
    
            window hide

            pause 0.5

            window show
            MC "Ah..
            {w=0.5}yes"

            MC "{=txt_vo}(Well just great,
            {w=0.5}Dodong had to say my name.
            {w=0.5}Now this guy knows who I am)"

            show dy - thinking
            with dissolve

            play sound SFX_Foreshadow

            d "{=hl}Max Christian{/=hl} huh..."
            window hide

    pause 1.5
    
    window show
    MC "..."
    
    MC "Oh geez,
    {w=0.5}is it 2 PM already?"
    MC "Dodong,
    {w=0.5}sorry but I’m actually in a hurry.
    {w=0.5}Can we talk later?"

    show dy - confused
    with dissolve

    d "Leaving so soon?
    {w=0.5}Well then,
    {w=0.5}I’ll be seeing you around,
    {w=0.2}kid."
    window hide

    show dy - neutral
    with dissolve
    
    pause 0.5

    hide dy
    with dissolve

    stop music fadeout 1.0

    show dodong at center
    with decay10inleft

    pause 1.0

    show dodong - surprised
    with dissolve

    window show
    side_dodong "But wait Max,
    {w=0.5}you haven’t even bought anything.
    {w=0.5}And by the looks of it earlier, you’re starving."
    window hide

    pause 1.0
    play sound SFX_stomach
    with sshake2
    pause 3.35

    show dodong - thinking
    with dissolve

    window show
    side_dodong "You know what,"

    show dodong - happy
    with dissolve

    extend "{w=0.5} here!
    {w=0.5}On the house."
    window hide

    pause 0.5

    show item_food_2 at truecenter
    with irisin

    pause 1.5

    hide item_food_2
    with irisout

    pause 0.5

    window show

    MC "{=txt_vo}(Dodong hands me a {=hl}packed lunch{/=hl}.
    {w=0.5}It’s warm and smells good too)"

    MC "A-
    {w=0.5}Are you sure?
    {w=0.5}I don’t want to take anything without paying."

    show dodong - neutral
    with dissolve

    side_dodong "No, no!
    {w=0.5}It’s fine.
    {w=0.5}Think of it as a welcome back gift.
    {w=0.5}It has been years since I last saw you."

    side_dodong "It’s good to see you back, Max."
    window hide

    pause 1.0
    
    window show
    MC "..."

    MC "Thank you very much, Dodong.
    {w=0.5}It’s also good seeing you again.
    {w=0.5}{=txt_vo}(Though to be honest, I don’t see anything good in me coming back here)"

    side_dodong "Anyways,
    {w=0.5}I don’t wanna hold you on for much longer.
    {w=0.5}See you around Max."

    hide dodong
    with dissolve

    MC "{=txt_vo}(I gave Dodong a smile and left the establishment)"

    MC "Forgot how generous Dodong is.
    {w=0.5}Well for now I’ll be heading back to the house"
    window hide

#SCENE 5 : INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 12, 1992. 4:00 P.M.

    scene bg-intmaxbedroom
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 12, 1992. 4:00 P.M.{/cps}"
    window hide

    pause 1.0

    play music BGM_goodnight

    pause 1.0

    show item_food_2 at truecenter
    with irisin

    pause 1.5

    hide item_food_2
    with irisout

    pause 0.5
    #SFX - Burp
    #Show Image of Dish

    window show
    MC "Man...
    {w=0.5}That packed lunch Dodong made almost gave me a food coma."
    MC "{=txt_vo}(The dish,
    {w=0.5}despite being so simple,
    {w=0.5}had so much flavor once you bite into it!)"
    window hide

    pause 1.5

    window show
    MC "*sigh*
    {w=0.5}Well,
    {w=0.5}I gotta go down and clean this up now.
    {w=0.5}Don’t want ants crawling all over my room."
    window hide

    pause 1.5

    #SFX - Crash
    play sound SFX_Smack 
    with sshake
    pause 0.5
    play sound SFX_paper
    with sshake
    pause 3.0
    #SFX - Papers Falling
    show item_maxbag_letter at truecenter
    with irisin

    pause 1.5

    hide item_maxbag_letter
    with irisout
    #Show image of Bag with contents spilling out
    pause 0.5

    window show
    MC "Agghh!
    {w=0.5}{cps=90}Ouch Ouch Ouch Ouch!{/cps}"

    MC "Way to go Max,
    {w=0.5}stubbing your toe against the obvious chair in front of you."

    MC "And great,
    {w=0.5}now my stuff fell out of my bag"

    play sound SFX_Smack
    MC " *cough*{w=0.5}{nw}" with sshake
    play sound SFX_Smack
    extend " *cough*" with sshake

    MC "I gotta be more careful.
    {w=0.5}And what’s more,
    {w=0.5}I gotta get to cleaning this dusty place up."
    window hide
    
    pause 1.0
    show item_letter at truecenter
    with irisin
    pause 1.5

    window show
    MC "..."

    MC "Whatever’s written on this paper is the reason why I’m back here."

    #Show contents of letter

    MC "Who sent this and why?"

    MC "{=txt_vo}(If I recall,
    {w=0.5}this was sent to me a {=hl}week ago{/=hl}.)"
    window hide

    hide item_letter at truecenter
    with irisout

    pause 0.5
    play sound SFX_Sweep
    pause 1.0
    scene bg-fbmaxhouse
    with sflash
    
    #SFX - Knocking
    play sound SFX_knock

    pause 1.5

    
    window show
    MC "{=txt_vo}(What? Someone’s at the door?)"

    ex_mailman "Magandang Umaga, Sir.
    {w=0.5}Is Mr. Maximo Christian living here?"

    MC "Yes...
    {w=0.5}That's me.
    {w=0.5}Why?"
    window hide

    pause 1.0
    show item_letter at truecenter
    with irisin
    pause 1.0

    window show
    MC "Uh...
    {w=0.5}Salamat."

    MC "{=txt_vo}(A letter?
    {w=0.5}For me?)"

    MC "{=txt_vo}(I don’t believe I’m expecting someone to send me one.)"
    window hide
    hide item_letter at truecenter
    with irisout
    pause 0.5
    play sound SFX_Sweep

    pause 1.0
    scene bg-intmaxbedroomnight
    with wwipe
    pause 1.5

    window show
    
    MC "Whoops
    {w=0.5}look at the time,
    {w=0.5}it seems I must’ve zoned out."
    window hide
    
    pause 1.0
    
    window show
    MC "This is exhausting." 
    MC "*Yawns*
    {w=0.5}Maybe...
    {w=0.5}I should get some...
    {w=0.5}sleep..."
    window hide

    stop music fadeout 1.0

#SCENE 6 : INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 13, 1992. 11:00 A.M.

    show black
    with dissolve

    pause 1.0

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 13, 1992. 11:00 A.M.{/cps}"
    window hide

    pause 1.0

    window show
    MC "zzzzzzzzzzzzzzzz{cps=*0.15}.......{/cps}"
    window hide

    pause 1.0
    show bg-intmaxbedroom behind black
    hide black
    play sound SFX_pots
    "CRASHHHHHHH {w=0.5}{nw}" with sshake
    window hide 
    show black
    with dissolve

    pause 2.0
    window show
    play sound SFX_Smack
    MC "What the-?{w=0.5}{nw} " with sshake
    play sound SFX_Smack
    extend "Who’s there!?" with sshake
    window hide

    scene bg-intmaxbedroom
    with fade
    pause 1.0

    window show
    MC "{=txt_vo}(Could it be my {=hl}parents{/=hl}? Did they know I went back here?)"

    MC "{=txt_vo}(But it’s impossible that my parents would come back after what happened.)"
    
    MC "{=txt_vo}(Did someone break in?)"

    MC "{=txt_vo}(I should check downstairs, better bring my bat just to be sure.)"
    window hide

#SCENE 7 : INT. MONTERO HOUSE - KITCHEN - JUNE 13, 1992. 11:05 A.M.

    scene bg-intmaxhousekitchen
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - KITCHEN - JUNE 13, 1992. 11:05 A.M.{/cps}"
    window hide

    pause 1.0

    window show
    MC "{=txt_vo}(I think I see a figure flailing about the kitchen.)"

    show cheng - hidden
    with dissolve
    
    MC "{=txt_vo}(how should I approach this?)"
    window hide

    menu ch01_sc07_01:
        "Shout!":
            $ev_ch01_sc07_chengapproach = 1

            window show
            MC "Who Are You!?"

            $ Auntie = "???"

            side_cheng "EEEEK!
            {w=0.5}TABANG
            {w=0.5}MAY KAWATAAAN!"
            window hide

            play sound SFX_pansmack

            scene bg-blackscreen
            with sflash

            window show
            MC "{=txt_vo}(OUCH!
            {w=0.5}I JUST GOT SMACKED ON THE FACE!)"
            MC "{=txt_vo}(Wait...
            {w=0.5}Am I-
            {w=0.5}Oh no,
            {w=0.5}I’m losing consciousness.)"
            window hide
            
            pause 0.5
            
            window show
            side_cheng "MAX!?
            {w=0.5}MAXXX!!!"
            window hide

            pause 1.5

            scene bg-intmaxhousekitchen
            with fade
            pause 1.5

            window show
            MC "Urk..."
            window hide

            pause 0.5
            
            window show
            MC "Ughhh..."
            window hide

            pause 0.5

            window show
            MC "{=txt_vo}(I see a figure over me, they seem quite worried.)"
            window hide

            pause 0.5
            play sound SFX_Mystery
            show cheng - surprise
            with dissolve
            pause 1.0

            play music BGM_friendly

            window show
            side_cheng "Max?{w=0.5}{nw}"
            play sound SFX_Smack
            extend" Maximo!{w=0.5}{nw}" with sshake
            extend " Ay nako anak,
            {w=0.5}you had me worried there.
            {w=0.5}I’m so sorry.
            {w=0.5}Auntie Cheng doesn’t know her own strength it seems."

            $ Auntie = "Auntie Cheng"

            MC "Auntie...
            {w=0.5}Cheng...?"

            show cheng - confused
            with dissolve

            side_cheng "I’ll have you know,
            {w=0.5}you shouldn't go behind this delicate hearted lady’s back and shout while holding a bat menacingly."

            side_cheng "You almost took a couple of years off of me."

            MC "{=txt_vo}(This is {=hl}Prudencia Jhordalyn Malano{/=hl},
            {w=0.5}or {=hl}Auntie Cheng{/=hl} for short.
            {w=0.5}Our House Caretaker.)"

            MC "{=txt_vo}(She’d go here once in while to make sure the place is tip top shape.)"

            MC "I’m sorry too Auntie Cheng.
            {w=0.5}If only I’ve known you were coming."
            window hide

            pause 0.5

            window show
            MC "{=txt_vo}(Ackk!
            {w=0.5}My head’s still hurting from the impact.)"

            show cheng - neutral
            with dissolve

            side_cheng "So sorry gid anak!"
            window hide

            pause 0.5

            
            #SFX - Hug

            pause 0.5

            show cheng - happy
            with dissolve

            window show
            MC "{=txt_vo}(Auntie suddenly grabs me and puts me into a tight hug.)" with sshake

            show cheng - neutral
            with dissolve

            side_cheng "I’ll patch you up later ha, anak."

            MC "{=txt_vo}(Her grip,
            {w=0.5}it’s too tight.
            {w=0.5}I feel like I might lose consciousness again.)"
            window hide
            
            window show
            MC "Urkkk..."
            window hide

            show cheng - happy
            with dissolve

            window show
            side_cheng "Oh! Sorry. Was the hug too much? Again, Auntie Cheng doesn’t know her own strength."
        "Approach slowly":
            $ev_ch01_sc07_chengapproach = 2

            $ Auntie = "Auntie Cheng"
            window show
            MC "{=txt_vo}(Alright,
            {w=0.5}I’ll slowly approach and see who it is.)"
            window hide

            window show
            MC "{=txt_vo}(Wait a second{cps=5}...{/cps}
            {w=0.5}I think...
            {w=0.5}I think I know who that is)"
            window hide

            pause 0.5
            play sound SFX_Mystery
            show cheng - neutral
            with dissolve
            pause 1.0

            play music BGM_friendly

            window show
            MC "Auntie Cheng!?
            {w=0.5}{=txt_vo}(How- When did she get here?)"

            show cheng - surprise
            play sound SFX_Smack
            side_cheng "WHAT!{w=0.5}{nw}" with sshake
            play sound SFX_Smack
            extend" WHO ARE YOU-{w=0.5}{nw}" with sshake
            play sound SFX_Smack
            extend " JUSKO!" with sshake

            MC "{=txt_vo}(This is {=hl}Prudencia Jhordalyn Malano{/=hl},
            {w=0.5}or {=hl}Auntie Cheng{/=hl} for short.
            {w=0.5}Our House Caretaker.)"

            MC "{=txt_vo}(She’d go here once in while 
            to make sure the place is tip top shape)"

            show cheng - thinking
            with dissolve
            side_cheng "Hmm{cps=5}...{/cps}"
            show cheng - surprise
            with dissolve
            play sound SFX_Idea
            extend "{w=0.5}{=hl} Maximo{/=hl}?{nw}" with sflash
            extend"{w=0.5} Ay Hala!
            {w=0.5}It’s you!"

            show cheng - happy
            with dissolve            

            play sound SFX_clothruffle
            with sshake

            MC "{=txt_vo}(Gahh!{w=0.5}{nw}"
            extend " Auntie suddenly grabs me and puts me into a tight hug)"
            
            show cheng - neutral
            with dissolve

            side_cheng "Why are you here?
            {w=0.5}When did you arrive?"

            MC "{=txt_vo}(Her grip,
            {w=0.5}it’s too tight.
            {w=0.5}I feel like I might lose consciousness)"

            MC "Urkkk{cps=5}...{/cps}"

            show cheng - happy
            with dissolve

            side_cheng "Oh!
            {w=0.5} Sorry. Was the hug too much?
            {w=0.5} Seems that Auntie Cheng doesn’t know her own strength.
            {w=0.5} Ohohoho!"

    MC "{=txt_vo}(Finally,
    {w=0.5}Auntie lets go of me.)"

    MC "Anyways,
    {w=0.5}why are you here Auntie Cheng?
    {w=0.5}I thought-"

    side_cheng "Oh, wait!
    {w=0.5}The food is almost done."

    side_cheng "Nak,
    {w=0.5}wait for me at the dining area so we can eat and catch up, okay?
    {w=0.5}Wait lang."

    MC "Well ok then."
    window hide

    stop music fadeout 1.0

#SCENE 8 : INT. MONTERO HOUSE - DINING AREA - JUNE 13, 1992. 12:00 P.M.
    scene bg-intmaxhousedining
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - DINING AREA - JUNE 13, 1992. 12:00 P.M.{/cps}"
    window hide

    pause 1.0

    play music BGM_casual

    window show

    MC "{=txt_vo}(The aroma of Auntie Cheng's cooking,
    {w=0.5}it feels nostalgic.
    {w=0.5}I missed this smell.)"
    window hide

    pause 0.5
    show cheng - neutral
    with dissolve
    pause 0.5

    window show
    side_cheng "Tsaran!"

    window show
    pause 0.5
    show item_food_1 at truecenter
    with irisin

    pause 1.5

    hide item_food_1
    with irisout

    pause 0.5
    window hide

    MC "Wow! Auntie Cheng, This definitely looks delicious!"
    
    show cheng - confused
    with dissolve

    side_cheng "You know what Max?
    {w=0.5}You should eat more." 

    side_cheng "Poor boy,
    {w=0.5}you really need some more meat on your bones!"

    show cheng - happy
    with dissolve

    side_cheng "Good thing I visited this week."

    MC "I know, I know,
    {w=0.5}Auntie Cheng.
    {w=0.5}Thank you."
    window hide 

    pause 0.5
    play sound SFX_eating
    with sshake
    pause 1.0

    window show
    play sound SFX_Idea
    MC "{=txt_vo}(!{w=0.3}{nw}" with sflash
    extend "{w=0.5} Wow,
    {w=0.5}this flavor!
    {w=0.5}It really reminds me of home.)"

    if ev_ch01_sc07_chengapproach == 1:

        show cheng - confused
        with dissolve

        side_cheng "You know what Max,
        {w=0.5}you really shook my spirit when you shouted at me earlier."
        
        side_cheng "You should’ve let me know that you were coming."

        side_cheng "I would have prepared more for your arrival,
        {w=0.5}but oh well."
    
    if ev_ch01_sc07_chengapproach == 2:
        
        show cheng - confused
        with dissolve
        
        side_cheng "You know what Max,
        {w=0.5}You should’ve let me know that you were coming."
        
        side_cheng "I would have prepared more for your arrival,
        {w=0.5}but oh well."
    
    MC "{=txt_vo}(That’s right.
    {w=0.5}Would probably be a lot cleaner)"

    MC "I thought you’d be here earlier than me, Auntie Cheng.
    {w=0.5}No one was inside so I just let myself in."
    
    show cheng - happy
    with dissolve

    side_cheng "Oh my!
    {w=0.5}Silly me.
    {w=0.5}Auntie Cheng seemingly has forgotten to lock the door."

    show cheng - neutral
    with dissolve

    side_cheng "Sigh{cps=*0.15}...{/cps}
    {w=0.5}I’m getting quite forgetful as days go by."

    MC "{=txt_vo}(Great, I hope that doesn’t become a regular thing)"

    show cheng - confused
    with dissolve

    side_cheng "Well,
    {w=0.5}even though I was {=hl}hired by your parents{/=hl} to take care of this house,{nw}"

    show cheng - happy

    extend "{w=0.5} this old soul still needs to adventure around and see the sights."

    MC "({cps=*0.15}...{/cps}
    {w=0.5}Old Soul?
    {w=0.5}Seeing the sights?)"
    window hide

    pause 0.5

    show cheng - angry
    with dissolve

    pause 0.5

    window show

    side_cheng "{cps=*0.15}...{/cps}"

    side_cheng "Hey, what’s with that look?"

    show cheng - confused
    with dissolve

    side_cheng "I’ll have you know,
    {w=0.5}I take time to travel around since no one’s really staying here often."

    side_cheng "Can’t really get myself to stay here and do nothing.
    {w=0.5}I’ll grow wrinkly as a prune if I stay here and do nothing."

    MC "Well atleast what you’re doing seems fun."

    side_cheng "Yes it is.
    {w=0.5}Don’t tell your parents
    {w=0.5}but
    {w=0.5}I’d usually only visit here twice or thrice a month."

    MC "Wait,{w=0.5}{nw}"
    play sound SFX_Smack
    extend " what!?{w=0.5}{nw}" with sshake
    extend " So you’d leave this place unlocked and leave for who knows how long?"

    show cheng - happy
    with dissolve

    side_cheng "Ohoho Don’t be angry dearie.
    {w=0.5}That blunder only happened this once."

    MC "And when was the last time you were here?"

    show cheng - thinking
    with dissolve

    side_cheng "Hmmm{cps=*0.15}...{/cps}
    {w=0.5}If {w=0.5}I {w=0.5}recall {w=0.5}{cps=*0.15}...{/cps}"
    pause 0.5

    show cheng - happy
    with dissolve

    side_cheng "About{cps=*0.15}...{/cps} {w=0.8}{nw}"
    play sound SFX_Mystery
    extend "{=hl}two weeks{/=hl} ago!" with sflash

    window hide 

    pause 1

    MC "{cps=*0.15}...{/cps}"

    MC "{=txt_vo}(2 Weeks?)"

    MC "So you left this house unlocked for {=hl}2 whole{nw}" 
    play sound SFX_Smack
    extend " weeks{/=hl}!?" with sshake

    side_cheng "Well,
    {w=0.5}that was then and this is now.
    {w=0.5}Nothing of consequence happened so it’s quite okay"

    MC "{=txt_vo}(What do you mean okay.
    {w=0.5}You’ve given so much opportunity for robbers to break into our house.
    {w=0.5}You’re lucky no one’s broken in yet)"

    show cheng - neutral
    with dissolve

    side_cheng "And since you’re here,
    {w=0.5}I might stay here for longer to keep you company."

    side_cheng "Again,
    {w=0.5}I usually come here {=hl}twice or thrice{/=hl} a month."

    MC "Well that’s great,
    {w=0.5}I guess."

    show cheng - happy
    with dissolve

    side_cheng "Oh now that you’re here,
    {w=0.5}I actually have some chika."

    show cheng - thinking
    with dissolve

    side_cheng "I remember months after you moved away,
    {w=0.5}the business of the {=hl}Balandra's suddenly rose to the top.{/=hl}"

    show cheng - neutral
    with dissolve

    side_cheng "Their businesses have really boomed since the last few years.
    {w=0.5}You still remember them,
    {w=0.5}don't you?"
    
    MC "Balandra?
    {w=0.5}That name sounds familiar."

    side_cheng "You should know them,
    {w=0.5}they owned that famous little bakery near the school  you went to."

    side_cheng "We’d sometimes go there when I picked you up after classes if you recall."

    MC "Oh that’s them?
    {w=0.5}Wow they really rose up huh."

    show cheng - thinking
    with dissolve

    side_cheng "Yes,
    {w=0.5}and they’re not merely an owner of a small bakery.
    {w=0.5}They now have {=hl}convenience stores, restaurants, stationary stores{/=hl} and{cps=*0.15}...{/cps} "

    show cheng - happy
    with dissolve

    side_cheng "Actually,
    {w=0.5}there’s too much.
    {w=0.5}I can’t even recall most of them."

    show cheng - neutral
    with dissolve

    MC "That’s kind of insane for a short amount of time.
    {w=0.5}Well,
    {w=0.5}{=hl}5 years{/=hl} isn’t that small now that I think about it."
        
    show cheng - sad
    with dissolve

    side_cheng "On the other hand, poor {=hl}Syngh Family{/=hl}. "

    show cheng - confused
    with dissolve

    side_cheng "After their little {=hl}incident{/=hl}, their business just declined.
    {w=0.5}Though, I’ve heard that their {=hl}son{/=hl} is patching things up,
    {w=0.5}albeit slowly."

    show cheng - thinking
    with dissolve

    side_cheng "Weren’t you close with them,
    {w=0.5}right,{w=0.5}{nw}"
    play sound SFX_Mystery
    extend " Max?"

    
    
    window hide
    pause 0.5
    window show

    MC "{cps=*0.15}...{/cps}"

    window hide
    pause 0.5
    window show

    show cheng - surprise
    with dissolve

    side_cheng "Oh sorry Nak.
    {w=0.5}That was a bit insensitive of me."

    window hide
    pause 0.5
    show cheng - sad
    with dissolve
    pause 0.5
    show cheng - neutral
    with dissolve
    window show

    side_cheng "Anyways,
    {w=0.5}Nak,
    {w=0.5}are you going somewhere today?"

    MC "Uhmmm,
    {w=0.5}I don’t think so{cps=*0.15}...{/cps}
    {w=0.5}Why?"

    side_cheng "I was thinking.
    {w=0.5}Could you go out and get some {=hl}groceries{/=hl} for me?"

    MC "{cps=*0.15}...{/cps}Sure,
    {w=0.5}auntie.
    {w=0.5}I can do that."

    side_cheng "{=hl}Palengcare Market{/=hl}.
    {w=0.5}I hope you still remember how to get there"

    side_cheng "I’ll contact {=hl}Ana{/=hl} that you’ll be fetching the goods for me."

    MC "Ana?"

    side_cheng "{=hl}Riana Jessie{/=hl},
    {w=0.5}you remember her right.
    {w=0.5}Heck, she used to be your {=hl}classmate{/=hl} Max.
    {w=0.5}Surely you haven’t forgotten?"

    MC "Oh yeah,
    {w=0.5}of course I haven’t.
    {w=0.5}I just don’t remember calling her Ana."

    side_cheng "Well in any case here’s your pamasahe.
    {w=0.5}While you're out,
    {w=0.5}I'll clean up the house.
    {w=0.5}Don’t wanna hear you having coughing fits while rummaging about."

    MC "Alright auntie,
    {w=0.5}I’ll be heading out now."

    show cheng - happy
    with dissolve

    side_cheng "Halong anak!"
    window hide

    stop music fadeout 1.0

#SCENE 9 : PALENGCARE MARKET - JUNE 13, 1992. 1:40 P.M.
    scene bg-palengcare
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}PALENGCARE MARKET - JUNE 13, 1992. 1:40 P.M.{/cps}"
    window hide

    pause 1.0

    play music BGM_palengcare

    window show

    MC "{=txt_vo}(Alright I’m here.)"
    
    window hide
    pause 0.5
    window show
    
    MC "{=txt_vo}(Uhm,
    {w=0.5}what happened here?)"

    MC "{=txt_vo}(This place used to be so crowded.)"
    window hide
    
    pause 0.5
    show riana - neutral
    with dissolve
    pause 0.5
    window show
    
    MC "{=txt_vo}(That must be Ana,
    {w=0.5}the owner’s youngest{cps=*0.15}...{/cps}) "
    window hide
    
    show riana - happy
    with dissolve

    window show
    side_ana "Max!
    {w=0.5}Hey!"
    window hide

    pause 0.5

    window show
    side_ana "Is that you, Max?
    {w=0.5}It is!
    {w=0.5}Oh it’s been so long.
    {w=0.5}You practically just {=hl}vanished{/=hl} those years ago!"
  
    side_ana "It’s really good to see you.
    {w=0.5}I hope you didn’t just up and forget about us."

    MC "Hi, Riana.
    {w=0.5}And yes I’ve decided to take a small visit to the town I grew up in."

    show riana - neutral
    with dissolve

    side_ana "Well,
    {w=0.5}that’s great.
    {w=0.5}I got a call earlier from Mrs. Malano."
    
    side_ana "She told me she wouldn’t come today to pick up her groceries.
    {w=0.5}She said that someone really {=hl}exciting{/=hl} is gonna pick them up for her."

    side_ana "And for the latter part,
    {w=0.5}she certainly was correct."

    MC "Wait,
    {w=0.5}so Auntie Cheng calls here first before buying groceries."

    side_ana "Yeah.
    {w=0.5}We sorta have a little {=hl}contract{/=hl} going on,
    {w=0.5}our shop and her.
    {w=0.5}It’s like, all corporate and stuff.
    {w=0.5}Really business insider,
    {w=0.5}if you know what I mean."
    
    show riana - happy
    with dissolve
    
    MC "Yeah
    {w=0.5}{=txt_vo}(I’ll be honest. I don’t actually know what she means)"
    
    show riana - neutral
    with dissolve
    
    side_ana "So you’re correct.
    {w=0.5}We prepare the goods for her before she arrives."

    show riana - sad
    with dissolve

    side_ana "We owe her a lot actually.
    {w=0.5}Hence this little set up we’ve got.
    {w=0.5}She’d also give a very generous amount of tips.{w=0.5}{nw}"
    play sound SFX_Mystery
    extend" Makes you wonder where she gets all her money."

    show riana - neutral
    with dissolve

    side_ana "But,
    {w=0.5}oh well.
    {w=0.5}That’s probably another mystery for another day"

    MC "{=txt_vo}(Wow.
    {w=0.5}Auntie Cheng is genuinely a good person,
    {w=0.5}not only to my family and I,
    {w=0.5}but also to other people)"
    window hide

    pause 0.5

    window show
    side_ana "Now Max,
    {w=0.5}I’d love to talk all about the good stuff with Mrs. Malano but I bet you she’d have my ear if I keep you here for longer."

    side_ana "So,
    {w=0.5}do you wanna check your list if we’ve got all the ingredients Mrs. Malano asked?"

    MC "Oh yeah wait a second."

    MC "{=txt_vo}(Wait-
    {w=0.5}where did I put the list of groceries again?-
    {w=0.5}Oh,
    {w=0.5}pocket.)"
    window hide

    pause 0.5

    window show
    MC "{=txt_vo}(Alright,
    {w=0.5}I think I have everything I need)"

    MC "Yeah,
    {w=0.5}I think that’s about all of it.
    {w=0.5}I’d be happy to pay for it now."

    show item_grocery at halfleft
    with irisin

    side_ana "Oh,
    {w=0.5}alrighty. For everything here from the talong,
    {w=0.5}sayote,
    {w=0.5}some eggs and other stuff{cps=*0.15}...{/cps}"
    window hide

    pause 0.5

    show riana - happy
    with dissolve

    window show
    side_ana "Well,
    {w=0.5}that’s 420 pesos."

    $ Wynona = "???"

    window hide

    hide item_grocery
    with irisout
    
    stop music fadeout 0.5

    play sound SFX_Gleam
    show riana - sad
    with sflash

    pause 0.3

    show riana at left

    play sound SFX_Smack
    show wynona - surprised at right
    with ssmack
    with sshake
    
    play sound SFX_Mystery
    
    pause 0.5
    
    play music BGM_uneasy

    pause 0.5

    window show
    MC "Hey-
    {w=0.5}watch where you’re going!"

    show wynona - sad
    with dissolve

    char_wyn "I
    {w=0.5}-I’m sorry!
    {w=0.5}I have to go!"
    window hide

    play sound SFX_Run
    hide wynona
    with ssmack 

    pause 0.5
    
    window show

    MC "Whoa-
    {w=0.5}SHE JUST LEFT!?"

    show riana - angry
    with dissolve

    side_ana "Hey you!
    {w=0.5}You can’t just clumsily bump into my customer like that and run away!
    {w=0.5}Hey I’m talking to you-"

    show riana - sad
    with dissolve

    side_ana "Darn,
    {w=0.5}she just booked it."
    window hide

    stop music fadeout 1.0

    show riana at center
    with decay10inleft
    pause 0.5

    play music BGM_palengcare

    pause 0.5
    window show

    side_ana "Hey.
    {w=0.5}Do you need some help?"

    MC "{=txt_vo}(Oh no,
    {w=0.5}I didn’t notice that I dropped my grocery bag,
    {w=0.5}now some of it is on the floor and ruined.
    {w=0.5}Hey wait,
    {w=0.5}what’s that on the floor?
    {w=0.5}It looks{nw}"
    play sound SFX_Idea
    extend " {=hl}sparkly{/=hl})"
    window hide
    pause 0.5
    show item_locket at truecenter
    with irisin

    pause 1.5

    hide item_locket
    with irisout

    pause 0.5
    #SHOW CG OF PENDANT

    window show
    side_ana "Sorry to say Max,
    {w=0.5}but some of the stuff you bought got ruined from the impact."

    MC "Who was that just now?
    {w=0.5}{=txt_vo}(I can’t help but feel like I’ve met that person before)"

    show riana - neutral
    with dissolve

    side_ana "I believe that was {=hl}Wynona Balandra{/=hl}.
    {w=0.5}Well, it looked like her anyway.
    {w=0.5}She ran so fast I couldn’t tell if it was really her."

    side_ana "Just so you know though,
    {w=0.5}she’s really well known in this town."

    MC "Wynona Balandra?
    {w=0.5}{=txt_vo}(Balandra!
    {w=0.5}That’s the people who own that Bakery)"

    side_ana "Yeah.
    {w=0.5}She’s the daughter of the family who helped boost the economy of Iliganon City."

    MC "Wow,
    {w=0.5}really.
    {w=0.5}That’s a big feat.
    {w=0.5}This town used to be {=hl}quieter{/=hl} a few years ago."

    show riana - sad
    with dissolve

    side_ana "I can’t help but feel like this community market was left out though.
    {w=0.5}If you’ve noticed there’s a lot less customers going here to buy."

    side_ana "Shops here had to close down due to profits not able to recoup for the space rent costs."

    side_ana "I fear that will happen to our shop one day.
    {w=0.5}For now however,
    {w=0.5}customers like Mrs. Malano really helped us stay on the food chain."

    MC "That’s unfortunate.
    {w=0.5}I hope things will get better for you guys."

    MC "Anyway,
    {w=0.5}do you know where I can find Wynona?"

    MC "She dropped this {=hl}pendant{/=hl} when she hit me."

    show riana - neutral
    with dissolve

    side_ana "That’s one expensive looking pendant."

    MC "You probably know their businesses right?
    {w=0.5}Can you tell me where?
    {w=0.5}I might be able to return this to her."

    show riana - sad
    with dissolve

    side_ana "Oh sorry bud,
    {w=0.5}you do know they own a lot of business here.
    {w=0.5}I couldn’t even pinpoint where that Wynona might be."

    MC "Aw man,
    {w=0.5}what do I do with this then?"

    side_ana "You could try the convenience store near here.
    {w=0.5}It's also owned by the Balandra’s."
    
    show riana - angry
    with dissolve

    side_ana "I have to warn you however.
    {w=0.5}The clerk there- Well let’s just say they {=hl}aren’t the easiest person{/=hl} ever."

    MC "Thank you,
    {w=0.5}I might do that.
    {w=0.5}I’ll see you later Riana,
    {w=0.5}and nice meeting you again!"
    window hide

    pause 0.5

    play sound SFX_Run

    pause 0.5

    window show
    show riana - happy
    with dissolve

    side_ana "No problem Max!
    {w=0.5}It was also great- Hey wait!
    {w=0.5}You forgot your groceries-"

    show riana - sad
    with dissolve

    side_ana "And just like that he’s gone.
    {w=0.5}Oh well."
    window hide

    stop music fadeout 1.0

#SCENE 10 : CONVENIENCE STORE - JUNE 13, 1992. 2:10 P.M.
    scene bg-conveniencestore
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}CONVENIENCE STORE - JUNE 13, 1992. 2:10 P.M.{/cps}"
    window hide

    pause 1.0
    $ Maya = "Clerk"
    
    MC "So that's why Palengcare is no longer crowded.
    {w=0.5}Everyone shops here instead{cps=*0.15}...{/cps}"

    show maya - neutral
    with dissolve

    pause 0.5

    play music BGM_smug

    pause 0.5

    window show

    MC "Excuse me,
    {w=0.5}Hi-"

    side_maya "Hello{cps=*0.15}...{/cps}"

    MC "Is Ms. Wynona here?"

    side_maya "{cps=*0.15}...{/cps}"

    MC "{=txt_vo}(Did she just ignore me? Great)"

    MC "Uhmmm{cps=*0.15}...{/cps}
    {w=0.5}Hello?
    {w=0.5}I wanted to ask if Ms. Wynona here?"

    side_maya "{cps=*0.15}...{/cps}"

    MC "Ms. Wynona?
    {w=0.5}I think she has {=hl}long hair{/=hl} and she {=hl}wore green{/=hl} today?
    {w=0.5}Errr{cps=*0.15}...{/cps}
    {w=0.5}This place.
    {w=0.5}It’s owned by the {=hl}Balandra’s{/=hl} right?"

    side_maya "{cps=*0.15}...{/cps}"

    MC "{cps=*0.15}...{/cps}Hey I’m asking you a question!
    {w=0.5}Can't you hear or something?
    {w=0.5}Or are you just gonna ignore me?"

    show maya - annoyed
    with dissolve

    side_maya "{cps=*0.15}Tch...{/cps}" with sshake

    MC "Did you just-"

    #side_maya "{cps=*0.15}{/cps}{w=1.0}{nw}"
    
    show maya - angry
    with dissolve
    
    play sound SFX_Smack
    side_maya "{cps=*1.25}Listen here Mr. When you’re in this establishment you go by the store aisles, get a bag of snacks, a bottle of soda, or maybe pack of candy or something-{/cps}{w=0.5}{nw}" with sshake

    play sound SFX_Smack
    side_maya "{cps=*1.25}{/cps}You come back here at the counter, you give me money and I give you your change and receipt. That’s how you shop here.{w=0.5}{nw}" with sshake

    play sound SFX_Smack
    side_maya "{cps=*1.75}Do you think I’m responsible for the whereabouts of this Wynona you are talking about?{/cps}{w=0.5}{nw}" with sshake

    play sound SFX_Smack
    side_maya "{cps=*1.75}I’d probably have better chances of knowing when it will rain in the coming days than knowing where she is. Like why would I even know a single thing about her?{/cps}{w=0.5}{nw}" with sshake

    play sound SFX_Smack
    side_maya "{cps=*1.75}Do you perhaps see that we’re selling Wynona on aisle 3? If you’d given it a second look you definitely wouldn’t, have you? {/cps}{w=0.25}{nw}" with sshake

    play sound SFX_Smack
    side_maya "{cps=*1.75}But, I don't know about you, maybe you see something I haven’t. With that would you care to elaborate?{/cps}{w=0.25}{nw}" with sshake

    play sound SFX_Smack
    side_maya "{cps=*2.0}Well, judging by how you look you wouldn’t even probably know what you’re talking about.{/cps}{w=0.25}{nw}" with sshake
    
    play sound SFX_Smack
    side_maya "{cps=*2.0}Look when I applied for this job I never signed up to deal with your type. Always looking for something not even sold in these shops. Wynona Balandra? The daughter of my Boss’s Boss?{/cps}{w=0.25}{nw}" with sshake

    MC "{=txt_vo}(Geez, so this is what Riana meant by \"not easy\".)"

    MC "{=txt_vo}(Hmmm... maybe her boss knows?)"

    MC "Hey about your boss-"

    #side_maya "{cps=*2.0}{/cps}{w=0.25}{nw}"

    play sound SFX_Smack
    side_maya "{cps=*2.0}My boss? What boss, do you even know what you’re talking about? You probably mean my manager. Let me tell you about him. He’s the greatest- Not!{/cps}{w=0.25}{nw}" with sshake
    
    play sound SFX_Smack
    side_maya "{cps=*2.0}I asked him for a raise because oooh boy little old Maya, she was always doing her best. She works hard day and night to get this place running{/cps}{w=0.25}{nw}" with sshake
    
    play sound SFX_Smack
    side_maya "{cps=*2.0}Heck, I even had to deal with this local drunkard. Everybody hates him because he’s so annoyingly boisterous.{/cps}{w=0.25}{nw}" with sshake
   
    play sound SFX_Smack
    side_maya "{cps=*2.0}Well I agree! But let me tell you about him- Even if he’s always making a ruckus I kinda relate to him somehow. You know why? Let me tell you-{/cps}{w=0.25}{nw}" with sshake
    window hide
    
    with blackout
    
    pause 0.5

    window show

    side_maya "Hufff{cps=*0.15}...{/cps}
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}So-
    {w=0.5}So that’s
    {w=0.5}why
    {w=0.5}I-
    {w=0.5}I.
    {w=0.5}I-
    {w=0.5}don’t know
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}Huff{cps=*0.15}...{/cps}"

    side_maya "W{w=0.5}-Where to find this{w=0.5} W{w=0.5}-Wynona person
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}Huff{cps=*0.15}...{/cps}"
    
    side_maya "H{w=0.5}-{nw}"
    play sound SFX_Smack
    extend "Hey!{w=0.5}{nw}" with sshake
    extend " A{w=0.5}-are you even listening!?"

    MC "{=txt_vo}({cps=*0.15}……………………………{/cps}{w=0.5}{nw}"
    play sound SFX_Idea
    extend"!)" with sflash

    MC "{=txt_vo}(Oh wait,
    {w=0.5}why am I here again?
    {w=0.5}That’s right I’m here for Wynona)"

    MC "Hey,
    {w=0.5}maybe you could ask your {=hl}manager{/=hl} where Wynona is?
    {w=0.5}She dropped her pendant so I came to give it back."

    side_maya "Wha?
    {w=0.5}Manager?
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}O-Okay wait a second{cps=*0.15}...{/cps}"

    MC "{=txt_vo}(I think she got tame from being {=hl}lightheaded{/=hl} after her barrage)"
    window hide

    show maya - annoyed
    with dissolve
    
    pause 0.5
    show item_phone at halfleft
    with irisin
    #SFX Phone Dial
    play sound SFX_Call1
    pause 2.0

    play sound SFX_Call2
    pause 3.2

    play sound SFX_Call3

    pause 0.5
    window show
    side_maya "{size=-10}Yes it’s me
    {w=0.5}huff{cps=*0.15}...{/cps}
    {w=0.5}huff{cps=*0.15}...{/cps}
    {w=0.5}I’m okay.
    {w=0.5}Why am I out of breath?
    {w=0.5}That’s not the point here {color=#A54226}Christopher{/color}.
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}huff{cps=*0.15}...{/cps}
    {w=0.5}Yes I am calling you by your first name!{/size}"
    
    side_maya "{size=-10}Listen,
    {w=0.5}there's someone here who wants to know where Wynona is.
    {w=0.5}They wanted to return Wynona’s stuff.{/size}"
    
    side_maya "{size=-10}Yeah?
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}I’ll write it down{cps=*0.15}...{/cps}{/size}"
    
    show maya - angry
    with dissolve

    side_maya "{size=-10}No!
    {w=0.5}I am not going back there.
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}Huff{cps=*0.15}...{/cps}
    {w=0.5}I have {color=#A54226}no choice in the matter{/color}?{nw}"
    play sound SFX_Foreshadow
    extend " {w=0.5}No listen.
    {w=0.5}This conversation is over,{/size}{w=0.5}{nw}"
    play sound SFX_Smack
    extend " Bye!" with sshake
    window hide
    
    pause 0.5
    play sound SFX_Call3
    pause 0.5
    
    hide item_phone
    with irisin

    pause 0.5

    show maya - annoyed
    with dissolve

    pause 0.5

    window show 
    side_maya "Okay Mr.
    {w=0.5}You’re lucky I got lightheaded.
    {w=0.5}Anyway,
    {w=0.5}here.
    {w=0.5}It’s the address to your girlfriend.
    {w=0.5}That’s where she works.
    {w=0.5}I'm out of here."
    window hide
    
    pause 0.5
    play sound SFX_Run
    hide maya
    with dissolve
    pause 1

    stop music fadeout 1.0
    pause 0.5

    window show 
    MC "Thank you-
    {w=0.5}No wait,
    {w=0.5}she’s not my girlfriend!"

    MC "Whatever.
    {w=0.5}So this is where she is?
    {w=0.5}I think I can get there in a few."
    window hide

#SCENE 11 : ILIGANON CITY TIMES PUBLICATION OFFICE - JUNE 13, 1992. 2:54 P.M.
    scene bg-newsoffice
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}ILIGANON CITY TIMES PUBLICATION OFFICE - JUNE 13, 1992. 2:54 P.M.{/cps}"
    window hide

    pause 1.0

    $ Jane = "???"
    $ Receptionist = "Receptionist"

    window show
    MC "Hi,
    {w=0.5}good afternoon.
    {w=0.5}I’m looking for {=hl}Ms. Wynona Balandra{/=hl}?
    {w=0.5}Is she here right now?"

    ex_desk "Good afternoon,
    {w=0.5}Sir.
    {w=0.5}Yes,
    {w=0.5}but may I know your name,
    {w=0.5}Sir?"

    MC "I’m Maximo Montero.
    {w=0.5}I just wanted to return something."

    ex_desk "Wait a second,
    {w=0.5}Sir."
    window hide

    pause 1.0

    window show
    play sound SFX_Idea
    with sflash
    side_jane "And you sir.
    {w=0.5}I can’t help but hear that you request the presence of Ms. Balandra.
    {w=0.5}And what pray tell,
    {w=0.5}do you want from Miss Balandra?"
    window hide
    
    window show
    MC "Uh-
    {w=0.5}{cps=*0.5}Errr-{/cps}"
    window hide

    pause 0.5

    show jane - neutral
    with dissolve

    play sound SFX_Mystery

    pause 1.5

    play music BGM_mystery

    window show
    side_jane "Speak louder boy,
    {w=0.5}we're all ears for you."

    MC "I-
    {w=1.0}I’m here to give her pendant back."

    show jane - thinking
    with dissolve

    side_jane "Why?
    {w=0.5}Is she your ex-girlfriend or something?
    {w=0.5}Come to give back possessions with bad memories?"

    show jane - neutral
    with dissolve

    MC "N-
    {w=0.5}no!
    {w=0.5}I don’t even know her.
    {w=0.5}I’ve only bumped into her earlier at the market."

    show jane - pleased
    with dissolve


    side_jane "Hohoho I’m just teasing you.
    {w=0.5}No need to get uptight."

    $ Jane = "Jane"
    show jane - neutral
    with dissolve

    side_jane "Anyways,
    {w=0.5}{=hl}Jane Dimasipa{/=hl}.
    {w=0.5}The humble {=hl}Editor in chief{/=hl} in this fine establishment."

    side_jane "I’m also {=hl}Ms. Wynona Balandra’s boss{/=hl}.
    {w=0.5}Nice to meet you,
    {w=0.5}Sir{nw}"
    play sound SFX_Mystery
    extend" {=hl}Maximo Christian Montero{/=hl}." with sflash

    MC "Uhmm Nice to meet you too Ms. Dimasipa.
    {w=0.5}Though,
    {w=0.5}I don’t recall saying my name to you?"

    show jane - pleased
    with dissolve

    side_jane "You are such a funny boy!
    {w=0.5}Have you forgotten?
    {w=0.5}You’ve {=hl}gone and announced your name{/=hl} to our receptionist there."

    show jane - thinking
    with dissolve

    side_jane "Surely that hasn’t been {=hl}dashed{/=hl} from your memory just now."

    play sound SFX_Idea
    with sflash

    MC "{=txt_vo}(I’m pretty sure I only said {=hl}Maximo Montero{/=hl},
    {w=0.5}not {=hl}Maximo Christian Montero{/=hl})"

    play sound SFX_Foreshadow
    MC "{=txt_vo}(How’d she know my {=hl}second name?{/=hl}
    {w=0.5}Weird{cps=*0.15}...{/cps}
    {w=0.5}Well anyway this is one eccentric editor in chief if I do say so myself)"
    window hide

    pause 0.5
    show jane - neutral
    with dissolve
    pause 0.5

    window show
    side_jane "Well anyway,
    {w=0.5}I’m curious.
    {w=0.5}What truly is your relation to Ms. Balandra? Ex-boyfriend was my best guess."

    MC "I told you,
    {w=0.5}I’ve only bumped into her earlier today.
    {w=0.5}She dropped this locket so I went out-"

    show jane - angry
    with dissolve

    side_jane "You’ve gone out of your way to look for where she is right now?
    {w=0.5}But it is curious how you were able to locate someone who was a total stranger to you."

    show jane - surprised
    with dissolve

    side_jane "Surely you weren’t absolute strangers? There must’ve been a connection between you and her?"

    MC "Well{cps=*0.15}...{/cps}
    {w=0.5}{=hl}a friend who works at the market knows her{/=hl}.
    {w=0.5}I just used the information given to me to look for her."

    show jane - pleased
    with dissolve

    side_jane "My my,
    {w=0.5}incredible.
    {w=0.5}You remind me of a{nw}"
    play sound SFX_Mystery
    extend " {=hl}certain someone{/=hl}{nw}"
    extend " when it comes to sleuthing critical information."

    show jane - thinking
    with dissolve

    side_jane "Oh well.
    {w=0.5}Wynona,
    {w=0.5}she’s very hard working,
    {w=0.5}yet her will and resolve is often too weak."

    MC "Uhmm{cps=*0.15}...{/cps}
    {w=0.5}Excuse me?"

    show jane - pleased
    with dissolve

    side_jane "Oh don’t worry my dear,
    {w=0.5}I’m just rambling."

    MC "{=txt_vo}(What was that about?)"

    show jane - angry
    with dissolve

    side_jane "Just so you know,
    {w=0.5}boy,
    {w=0.5}Wynona Balandra’s family has {=hl}boosted the town’s economy{/=hl}.
    {w=0.5}If you’ve observed there’s been more establishments built around the area."

    show jane - thinking
    with dissolve

    side_jane "Things have been going uphill since their businesses boomed these past few years"

    MC "Yeah,
    {w=0.5}this town’s really changed since the last time I've been here.
    {w=0.5}they even had these convenience stores up."

    MC "{=txt_vo}(Though the old {=hl}Palencare Market felt almost like a ghost town{/=hl}.
    {w=0.5}What’s up with that?)"

    show jane - pleased
    with dissolve

    side_jane "Great observation Maximo!
    {w=0.5}However one must leave with a question,{w=0.5}{nw}"
    play sound SFX_Foreshadow
    with sflash
    extend " “{=hl}At what cost?{/=hl}”"

    MC "What do you mean by that?"
    window hide    

    pause 1.0 

    play sound SFX_Idea
    stop music fadeout 0.25
    show jane - surprised
    with sflash

    pause 1.0

    window show
    ex_desk "Sorry to interrupt Ms. Dimasipa,
    {w=0.5}Ms. Balandra is calling Mr. Montero into her office."

    show jane - thinking
    with dissolve

    side_jane "Oh well.
    {w=0.5}Sorry to have cut this wonderful conversation short but Ms. Balandra’s ready for you."
    show jane - pleased
    with dissolve
    side_jane "Talk to you later,
    {w=0.5}Mr. Montero."
    window hide

    pause 0.5

    window show
    MC "Uhmm Ok,
    {w=0.5}See you later Ms. Dimasipa."
    window hide

    hide jane
    with dissolve

    window show
    MC "{=txt_vo}(That was one weird conversation)"

    MC "{=txt_vo}(Anyways,
    {w=0.5}it seems Wynona’s here)"
    window hide

    pause 0.5

#SCENE 12 : WYNONA'S OFFICE - AFTERNOON JUNE 13, 1992. 3:15 P.M.
    scene bg-wynonasoffice
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}WYNONA'S OFFICE - AFTERNOON JUNE 13, 1992. 3:15 P.M.{/cps}"
    window hide

    pause 1.0

    $ Wynona = "Wynona" 
  
    play sound SFX_Mystery

    show wynona - thinking
    with dissolve
    pause 1.0

    play  music BGM_cool

    pause 1.0
    
    window show
    play sound SFX_Idea
    
    show wynona - surprised
    with sflash
    MC "{=hl}Ms. Balandra{/=hl}?
    {w=0.5}I’m Max,
    {w=0.5}I’ve come here to return this to you."
    
    char_wyn "I-
    {w=0.5}I’m really{nw}"
    extend " sorry{nw}" with sshake
    play sound SFX_Smack
    extend" about what happened earlier.
    {w=0.5}I even made you drop the things you were buying from the market."

    MC "Oh it’s no big deal actually-
    {w=0.5}Wait,
    {w=0.5}my{nw}"
    play sound SFX_Idea 
    extend " {=hl}groceries{/=hl}!{w=0.5}{nw}" with sshake
    extend " I think I forgot to bring what was left."

    MC "{=txt_vo}(Auntie Cheng is gonna kill me)"

    char_wyn "I was really in a hurry and-
    {w=0.5}Oh gosh I also lost my {=hl}pendant{/=hl} that I had in my purse."

    show wynona - sad
    with dissolve

    char_wyn "Darn this day couldn’t get any worse. 
    {w=0.5}Oh my gosh.
    {w=0.5}I also have a meeting in a few minutes and I am not prepared one bit"

    MC "So I guess this is yours?"
    window show
    pause 0.5
    show item_locket at truecenter
    with irisin

    pause 1.5

    hide item_locket
    with irisout

    pause 0.5
    window hide

    play sound SFX_Idea 
    show wynona - surprised
    char_wyn "Oh-
    {w=0.5}Why do you have this!?
    {w=0.5}How did you-" with sflash

    MC "You dropped it earlier when we bumped into each other."

    show wynona - confused
    with dissolve

    char_wyn "What am I saying?
    {w=0.5}I should be thanking you about now."

    show wynona - happy
    with dissolve

    char_wyn "Thank you so much Max!{w=0.5}{nw}"
    show wynona - confused
    with sflash
    play sound SFX_Mystery
    extend " But how were you able to find where I worked?"

    MC "You remember {=hl}Riana{/=hl} right?
    {w=0.5}She was the shopkeeper at the market and also one of my classmates back in hs."

    MC "By extension she knows who you are because apparently you’re {=hl}schoolmates{/=hl},
    {w=0.5} right?"

    MC "She told me your family owned that convenience store by the market.
    {w=0.5}So I went there and your employee told me you work here. "
    
    show wynona - sad
    with dissolve

    char_wyn "Err{cps=*0.15}...{/cps}
    {w=0.5}That’s just my {=hl}parents’{/=hl} store,
    {w=0.5}not mine, haha. "

    MC "Your family is pretty famous here in Iliganon,
    {w=0.5}huh?
    {w=0.5}Your boss told me that you guys have helped the economy a lot these years?"

    MC "That’s amazing actually,
    {w=0.5}you’ve even got a bunch of businesses here."

    show wynona - pleased
    with dissolve

    char_wyn "Only a few,
    {w=0.5}ahaha{cps=*0.15}...{/cps}"

    MC "Few?
    {w=0.5}Really?"

    show wynona - confused
    with dissolve

    char_wyn "Let’s stop talking about that.
    {w=0.5}By the way,
    {w=0.5}where have you been?
    {w=0.5}When did you come back?{cps=*0.15}...{/cps}"

    MC "Not long ago actually but how’d you know I’ve been gone?"

    show wynona - sad
    with dissolve

    char_wyn "Errr-
    {w=0.5}{cps=*0.15}...{/cps}
    {w=0.5}From{nw}"
    
    show wynona - surprised
    play sound SFX_Idea
    
    extend " {=hl}Riana{/=hl}!{w=0.5}{nw}" with sflash
    
    show wynona - happy
    play sound SFX_Smack
    
    extend " Yes!{w=0.5}{nw}" with sshake 
    extend " Definitely from Riana.
    {w=0.5}She told me you left here {=hl}5 years ago{/=hl}.
    {w=0.5}Actually we’ve met once before so I knew about you way back."

    MC "Really?
    {w=0.5}I’m sorry I forgot.
    {w=0.5}My last high school years {=hl}weren't very nice{/=hl}."

    MC "But hey,
    {w=0.5}can you tell me when we’ve met?
    {w=0.5}I think I actually remember you now that I think about it but I can't seem to recall when exactly."
    
    show wynona - thinking
    with dissolve

    char_wyn "Ah!
    {w=0.5}It was a {=hl}christmas party{/=hl} where the same year levels went to the beach!
    {w=0.5}It was{w=0.5}{nw}"
    show wynona - surprised
    extend " Lhe-{w=0.5}" with sshake
    window hide

    pause 0.5

    show wynona - sad
    with dissolve

    pause 0.5

    window show
    char_wyn "{cps=*0.15}...{/cps}
    {w=0.5}Uhmmm my {=hl}close friend{/=hl}{w=0.5}{cps=*0.15}...{/cps}
    {w=0.5}{size=-10}introduced me to you though our time together was only brief.{/size=-10}"

    MC "{=txt_vo}(Wait what was she about to say?
    {w=0.5}She kinda {=hl}choked up{/=hl}.
    {w=0.5}I gotta ask her who was this close friend,
    {w=0.5}she claims.)"

    MC "Wynona{cps=*0.15}...{/cps}
    {w=0.5}Who was this friend who introduced us?"
    window hide
    
    pause 1.0

    stop music fadeout 1.0

    pause 1.5

    play sound SFX_alarm
    show wynona - surprised
    with sflash

    pause 3.5
    
    play music BGM_cool
    show wynona - confused
    with dissolve
    
    pause 0.5

    window show
    char_wyn "Oh it’s already time for my meeting with the board.
    {w=0.5}I’m so sorry to cut this conversation short Max."
    window hide

    pause 0.5
    show wynona - sad
    with dissolve
    pause 0.5
    show wynona - neutral
    with dissolve
    pause 0.5

    window show
    char_wyn "Actually wait,
    {w=0.5}can I get your{nw}"
    play sound SFX_Idea
    extend " {=hl}number{/=hl}?
    {w=0.5}I’ll repay you for dropping your groceries." with sflash

    MC "No,
    {w=0.5}you don’t have to-"

    play sound SFX_Smack
    char_wyn "Please!
    {w=0.5}That was really rude of me.
    {w=0.5}I'll make it up to you.
    {w=0.5}I’ll make sure to call you when I have them." with sshake

    MC "Ok Fine{cps=*0.15}...{/cps}"
    
    show wynona - confused
    with dissolve

    char_wyn "Anyways,
    {w=0.5}I’m so sorry for bumping into you earlier!
    {w=0.5}I gotta go Max.
    {w=0.5}See you soon!"
    
    MC "Alright,
    {w=0.5}I’ll see myself out."
    window hide
    
    stop music fadeout 1.0

    pause 0.5
    show wynona - happy
    with dissolve
    pause 0.5
    hide wynona
    with dissolve
    pause 1.0

#SCENE 13 : DIKUMAKAIN KARINDERIA - JUNE 13, 1992. 6:12 P.M.
    scene bg-extdikumakainevening
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}DIKUMAKAIN KARINDERIA EXT. BARANGAY STREET DIMAKITA - JUNE 13, 1992. 6:12 P.M.{/cps}"
    window hide

    pause 1.0

    $ Jobert = "???"

    window show
    MC "Man... 6 P.M.?
    {w=0.5}Geez I’m gonna get an earful from Auntie Cheng."
    window hide

    pause 0.5

    window show
    MC "Hmm!?
    {w=0.5}What’s going on over there?"
    window hide

    pause 1.0

    #SFX - Crash Noise
    play sound SFX_crash
    with sshake

    pause 1.0
    
    show jobert - angry at offscreenleft
    show dodong - angry at offscreenleft
    
    show jobert - angry at right
    show dodong - angry at left
    with decay10inleft

    play music BGM_uneasy
    pause 0.5

    window show
    MC "What the!?
    {w=0.5}Is that{nw}"
    play sound SFX_Idea
    extend "{=hl} Dodong{/=hl}?" with sflash

    play sound SFX_Smack
    side_dodong "Please,
    {w=0.5}stop or else I’ll call the{nw}" with sshake 
    play sound SFX_Smack
    extend " tanods!" with sshake

    play sound SFX_Smack
    side_jobert "AHH!{nw}" with sshake
    extend "{w=0.5} Don’t you{nw}"
    play sound SFX_Smack 
    extend " dare!" with sshake

    window hide

    pause 1.0

    play sound SFX_Gleam
    with sflash
    pause 0.5
    show black
    pause 0.15
    hide black
    play sound SFX_Smack
    with sshake
    #SFX - Crash Noise

    pause 0.5

    window show
    MC "What are you doing!?"

    show dodong - surprised
    with dissolve

    side_dodong "Max-"

    show jobert - surprised
    with dissolve

    play sound SFX_Smack
    side_jobert "Who the heck are you!?
    {w=0.5}Wait a minute-{w=0.5}{nw}" with sshake
    play sound SFX_Smack
    extend "You!?" with sshake

    MC "I don’t know who you are, 
    {w=0.5}but harassing Dodong in his own establishment?"

    show dodong - sad
    with dissolve

    side_dodong "Wait Max I can handle this, 
    {w=0.5}I’m already about to call the Poli-"

    show jobert - angry
    with dissolve

    side_jobert "The gall you have to show your face! 
    {w=0.5}Why I ought to-"

    MC "Wait a second!"
    window hide
    
    pause 0.5
    
    play sound SFX_clothruffle
    with sshake
    
    pause 0.5
    
    window show
    MC "Enough! You’re going too fa-"
    window hide
    
    pause 0.5
    
    play sound SFX_Smack
    with ssmack
    
    pause 0.5
    
    window show
    MC "{=txt_vo}(Oww! 
    {w=0.5}He just punched me!)"

    side_jobert "Man I’ve been waiting years to that"

    side_dodong "Max! 
    {w=0.3}Are you okay?"

    side_dodong "What the heck {=hl}Jobert{/=hl}!?"

    $ Jobert = "Jobert"

    side_jobert "Ha! 
    {w=0.5}Deserved"

    play sound SFX_Run
    hide jobert
    with dissolve

    show dodong at center
    with decay10inleft

    MC "Yeah I’m Okay... 
    {w=0.5}Who the heck was that?"

    side_dodong "{=hl}Jobert{/=hl}. 
    {w=0.5}He does this every time he’s {=hl}drunk{/=hl}. 
    {w=0.5}Last time he made a mess at Inday’s Sari Sari Store."

    side_dodong "He bothers everyone in this town and it affects our businesses.
    {w=0.5}Let’s go inside,
    {w=0.5}we’ll need to get you some ice."
    window hide

    hide dodong
    with dissolve

    stop music fadeout 1.0

    pause 0.5

#SCENE 14 : DIKUMAKAIN KARINDERIA EXT. BARANGAY STREET DIMAKITA - JUNE 13, 1992. 6:12 P.M.
    
    $ Mariano = "???"

    scene bg-intdikumakain
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}DIKUMAKAIN KARINDERIA EXT. BARANGAY STREET DIMAKITA - JUNE 13, 1992. 6:40 P.M.{/cps}"
    window hide

    pause 1.0

    show dodong - sad
    with dissolve

    play music BGM_casual

    MC "I’m sorry I wasn’t able to help you clean up."
    
    show dodong - angry
    side_dodong "Oi- Don’t apologize! 
    {w=0.5}He already did this multiple times. 
    {w=0.5}I’m scared he’ll do something to us if we involve the police. 
    {w=0.5}But next time, 
    {w=0.5}I’ll really sue him for damages." with sshake

    show dodong - sad
    with dissolve

    side_dodong "Too bad he used to be a {=hl}good guy{/=hl} though, 
    {w=0.5}tough life had him acting up like this."

    show dodong - neutral
    with dissolve
    
    side_dodong "Anyways I’m so sorry, 
    {w=0.5}Max. 
    {w=9.5}We haven’t seen each other for years and here you are AGAIN involved in my mess."

    show dodong - surprised
    play sound SFX_Idea
    MC "Oh, 
    {w=0.5}when we were in high school? 
    {w=0.5}Where you forced me to stay with you all night in a computer shop?" with sflash

    show dodong - confused
    with dissolve

    side_dodong "Hey! 
    {w=0.5}I couldn’t go home if I hadn't remove the virus I accidentally downloaded."

    show dodong - happy
    with dissolve

    side_dodong "The owner was furious, 
    {w=0.5}remember?"

    side_dodong "I was so scared I needed you to stay with me."

    MC "That was actually thrilling and fun! And about today, 
    {w=0.5}don’t worry."

    MC "Just report Jobert to the authorities so he won’t be able to do this again."

    show dodong - sad
    with dissolve

    side_dodong "Seriously, 
    {w=0.5}I’m really sorry about today. 
    {w=0.5}That drunkard keeps causing a ruckus in my karinderya these days."

    side_dodong "And not to mention,
    {w=0.5}I've been behind bills.
    {w=0.5}Doesn't help that now I have to pay for damages cause of Jobert"

    MC "You know what,
    {w=0.5}here.
    {w=0.5}I have some extra with me-"

    show dodong - surprised
    play sound SFX_Idea
    side_dodong "Max! 
    {w=0.5}No, 
    {w=0.5}it’s fine-" with sflash

    play sound SFX_Smack
    MC "Accept it already! 
    {w=0.5}Payment for all the trouble Jobert caused."with sshake

    show dodong - sad
    with dissolve

    side_dodong "Sigh{cps=*0.15}...{/cps} 
    {w=0.5}Okay, 
    {w=0.5}whatever. 
    {w=0.5}You haven’t changed a bit, 
    {w=0.5}Max."
    window hide

    stop music fadeout 1.0
    pause 1.5

    play sound SFX_knock
    pause 1.5

    play sound SFX_door1
    pause 1.5
    with sshake

    pause 0.5

    #SFX - Knocking and Door Opening
    window show
    play sound SFX_Smack
    side_mariano "Dodong! 
    {w=0.5}I heard that bastard crashed the place again-" with sshake
    window hide
    pause 0.5

    show dodong at left
    with decay10inleft
    show mariano - angry at right
    with dissolve
    play sound SFX_Mystery
    
    pause 1.5

    show mariano - surprised
    play sound SFX_Idea
    with sflash

    pause 1.0

    show mariano - thinking
    with dissolve

    window show
    side_mariano "Wait a minute... 
    {w=0.5}You?{w=1.0}{nw}"
    show mariano - angry
    play sound SFX_Smack
    extend" You!" with sshake
    window hide

    play music BGM_smug
    pause 0.5
    #SFX - Collar Ruffles
    play sound SFX_clothruffle
    with sshake
    pause 0.5

    window show
    play sound SFX_Smack
    side_mariano "Why the heck are you here!?" with sshake

    MC "{=txt_vo}(Why the heck is {=hl}he{/=hl} here!?)"

    
    play sound SFX_Idea
    side_dodong "Hey! 
    {w=0.5}Mariano, 
    {w=0.5}stop it! 
    {w=0.5}He got punched in the face already!" with sflash

    play sound SFX_Smack
    side_mariano "I don’t care! 
    {w=0.5}Why did he even come back!" with sshake

    side_mariano "And you, 
    {w=0.5}how dare you show your face here after all these {=hl}years{/=hl}!?"

    MC "That’s none of your business,{w=0.5}{nw}"
    play sound SFX_Smack
    extend " bastard! 
    {w=0.5}You won’t listen to me anyway, 
    {w=0.5}so let go of me!" with sshake

    show dodong - angry
    play sound SFX_Smack
    side_dodong "Would you both just quit it! 
    {w=0.5}I’ve had enough shouting today!" with sshake

    side_dodong "And Max is our customer Mr. Mariano, 
    {w=0.5}sir."

    show mariano - surprised
    with dissolve

    side_mariano "Customer? 
    {w=0.5}You? 
    {w=0.5}{=hl}Eating at my establishment{/=hl}? 
    {w=0.5}What kind of sick joke is this?"

    show mariano - angry
    with dissolve

    side_mariano "You may be our customer, 
    {w=0.3}but I will never forget what you did {=hl}5 years ago{/=hl}. 
    {w=0.3}You hear me?"

    MC "B-{w=0.5}But I{cps=*0.15}...{/cps}"

    side_mariano "Yes you-"

    side_dodong "You know what? 
    {w=0.5}I think both of you should go calm down!" with sshake

    side_dodong "You guys can talk it out if you both cool your heads."

    show dodong - confused
    with dissolve

    side_dodong "Pretty sure {=hl}Lheona{/=hl} wouldn't want you guys screaming at each other's faces."

    MC "{cps=*0.15}...{/cps}{w=0.5}{nw}"
    play sound SFX_Idea
    extend "!" with sflash
    show mariano - sad
    with dissolve

    side_mariano "{cps=*0.15}...{/cps}
    {w=1.0}Fine."
    window hide
    pause 0.5
    hide mariano
    with dissolve
    pause 0.5

    play sound SFX_door2

    pause 0.5

    show dodong at center
    with decay10inleft

    pause 0.5
    window show
    MC "But Dodong{cps=*0.15}...{/cps}"

    show dodong - sad
    with dissolve

    side_dodong "It’s fine Max, 
    {w=0.3}I can handle it from here. 
    {w=0.3}You should probably head home."

    MC "{=txt_vo}(Dang I forgot about the {=hl}time{/=hl}. 
    {w=0.5}It’s already {=hl}7pm{/=hl}.)"

    MC "{=txt_vo}(Auntie Cheng’s gonna kill me.)"

    MC "Alright dodong{cps=*0.15}...{/cps} 
    {w=0.5}I’m gonna head out"

    show dodong - happy 
    with dissolve

    side_dodong "See ya, 
    {w=0.5}Max."
    window hide 

    stop music fadeout 1.0

    pause 1.0

    hide dodong
    with dissolve

    pause 0.5
    
#SCENE 15	INT. MONTERO HOUSE - LIVING ROOM  - EVENING  JUNE 13, 1992. 9:03 P.M.

    show black
    with dissolve

    pause 0.5 

    play sound SFX_door1

    scene bg-intmaxhouselr
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - LIVING ROOM - JUNE 13, 1992. 9:03 P.M.{/cps}"
    window hide

    pause 1.0 

    window show
    side_cheng "Max? 
    {w=0.5}Is that you? 
    {w=0.5}Where have you been Anak!?"

    side_cheng "I’ve been waiting for you to get back. 
    {w=0.5}I barely have anything to cook here."

    side_cheng "So what of the ingredients you bought huh?"

    MC "{=txt_vo}(Oh man, 
    {w=0.5}if this day couldn’t get any better)"

    MC "Auntie Cheng, 
    {w=0.5}I’m sorry. 
    {w=0.5}I got into a small accident"

    side_cheng "What do you mean by small accident?
    {w=0.5}We don’t have enough ingredients here to cook a meal-"
    window hide
    pause 0.5
    show cheng - neutral
    with dissolve
    play music BGM_friendly
    pause 0.5
    window show
    show cheng - surprise
    play sound SFX_Smack
    side_cheng "Anak! 
    {w=0.5}What happened to your face? 
    {w=0.5}Is this the accident you mean!?" with sshake

    MC "No no, 
    {w=0.5}I just got a little clumsy and hit someone while at Palengcare. 
    {w=0.5}It was an accident really, 
    {w=0.5}and I kinda dropped all my goods on the dirty floor so{cps=*0.5}...{/cps} 
    {w=0.5}They’re kinda soiled{cps=*0.5}...{/cps}"

    show cheng - confused
    with dissolve

    side_cheng "But what about your face? 
    {w=0.5}Surely dropping your stuff wouldn’t give you a swollen eye right?"

    MC "Well this{cps=*0.5}...{/cps} 
    {w=0.3}I was passing by Dodong’s karinderya and there was this commotion."

    MC "Jobert was there crashing Dodong’s karinderya again. 
    {w=0.5}I tried to stop him but he punched me in the face{cps=*0.5}...{/cps}"

    show cheng - angry
    play sound SFX_Smack
    side_cheng "That drunk bastard? 
    {w=0.5}He’s always giving the locals a headache wherever he is. 
    {w=0.5}I don’t get why he’s allowed to do this again and again." with sshake

    MC "Yeah{cps=*0.5}...{/cps} 
    {w=0.5}I’m sorry about the ingredients Auntie Cheng."

    show cheng - confused
    with dissolve

    side_cheng "Sigh{cps=*0.5}...{/cps} 
    {w=0.5}Well It’s alright I’ll phone one of the local eateries here. 
    {w=0.5}I know a place that does deliveries even at this time."
    
    show cheng - neutral
    with dissolve

    side_cheng "Anyways, 
    {w=0.5}here. 
    {w=0.5}I got you some ice, 
    {w=0.5}put this on your cheek."

    MC "Thank you, 
    {w=0.5}Auntie Cheng."
    window hide

    hide cheng
    with dissolve
    stop music fadeout 1.0
    pause 0.5

#SCENE 16	INT. MONTERO HOUSE - DINING AREA  - EVENING

    scene bg-intmaxhousedining
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - DINING AREA - JUNE 13, 1992. 9:15 P.M.{/cps}"
    window hide

    pause 1.0 

    show cheng - neutral
    with dissolve
    play music BGM_friendly

    pause 0.5

    window show
    MC "So, 
    {w=0.5}I went to the publishing house to meet Wynona Balandra—- 
    {w=0.5}to return the jewelry she dropped while bumping into me."

    show cheng - confused
    with dissolve

    side_cheng "Wynona Balandra? 
    {w=0.5}Isn’t she a snob? 
    {w=0.5}Back then I’d see her walking through Palengcare a lot."

    show cheng - thinking
    with dissolve

    side_cheng "I know their family wants a piece of that place’s land but geez sending their daughter to do surveillance work? Couldn’t be me."

    show cheng - confused
    with dissolve

    side_cheng "I called her but she just stared at me and left. 
    {w=0.5}She used to be friends with you know..."

    MC "Nah, 
    {w=0.5}she even recognized me first. 
    {w=0.5}Apparently, 
    {w=0.5}we were high school classmates. 
    {w=0.5}She also asked for my number- she said she’ll pay me back for the groceries."

    MC "Also, 
    {w=0.5}after what happened with Jobert, 
    {w=0.5}Mariano arrived."

    MC "I had a long day, 
    {w=0.5}Auntie. 
    {w=0.5}*Sigh*"

    show cheng - neutral
    with dissolve

    side_cheng "You met a lot of your old friends today, 
    {w=0.5}huh?"
    window hide

    pause 0.5

    window show
    show cheng - happy
    with dissolve
    side_cheng "You know what? 
    {w=0.5}You should rest, 
    {w=0.5}Max. 
    {w=0.5}Go upstairs, 
    {w=0.5}I'll clean the dishes for you."

    MC "Thank you, 
    {w=0.5}Auntie. 
    {w=0.5}I’ll head up. 
    {w=0.5}Goodnight."
    window hide

    hide cheng
    with dissolve
    stop music fadeout 1.0
    pause 0.5

#SCENE 17	INT. MONTERO HOUSE - BEDROOM - EVENING

    #SFX DOOR KNOCKING
    show black
    with dissolve
    pause 0.5

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 13, 1992. 9:50 P.M.{/cps}"
    window hide

    pause 1.0 

    play sound SFX_knock

    pause 1.0

    window show
    side_cheng "Max? 
    {w=0.5}It’s me auntie cheng"
    window hide

    play sound SFX_door1

    pause 3.0

    scene bg-intmaxbedroomnight
    with fade

    show cheng - neutral
    with dissolve
    play music BGM_goodnight
    pause 0.5    

    window show
    side_cheng "How are you doing Max?"

    MC "I’m fine auntie. 
    {w=0.5}Did you need anything?"

    

    side_cheng "I just wanted to let you know since you’re gonna be here for a while, 
    {w=0.5}I’ve finished cleaning."

    side_cheng "All the dishes, 
    {w=0.5}cooking tools, 
    {w=0.5}utensils are in the cupboards and cabinets in the kitchen."

    side_cheng "Fresh sheets are in the closet by the living room hallway, 
    {w=0.5}and spare keys for the house are in the small {=hl}safebox{/=hl} in the living room."

    MC "That’s great, 
    {w=0.5}thanks for your hard work auntie!"

    show cheng - confused
    with dissolve

    side_cheng "I have to apologize however. Remember me being not good with {=hl}locking{/=hl}?"
        
    side_cheng "Well I {=hl}forgot the code to the safebox{/=hl}. I’ve {=hl}written it somewhere{/=hl} but forgetful auntie strikes again I guess."

    show cheng - happy
    with dissolve

    side_cheng "Future problem for the both of us, 
    {w=0.5}am I right."

    MC "Haha I hope not."

    show cheng - neutral
    with dissolve

    side_cheng "Anyways that is all. 
    {w=0.5}Have a good night’s sleep Max."
    window hide
    pause 0.5
    hide cheng
    with dissolve
    pause 0.5
    window show
    MC "Sigh
    {w=0.3}{=txt_vo}(I'm so exhausted. 
    {w=0.3}Everyone in this town reminds me of Lheona. 
    {w=0.5}First, 
    {w=0.5}meeting her best friend, 
    {w=0.5}then her fown brother, 
    {w=0.5}I even got punched)"

    MC "{=txt_vo}(Well, I guess it’s a given since this town holds a lot of messy memories)"

    MC "{=txt_vo}(Who even sent me that letter? Where do I even start?)"

    play sound SFX_Smack

    MC "Argh!! 
    {w=0.3}All of these things are messing with my head!" with sshake

    MC "I better get some sleep. 
    {w=0.3}I’m so exhausted{cps=*0.15}...{/cps}"
    window hide

    stop music fadeout 1.0

    pause 0.5

    jump story_ch_02




    return