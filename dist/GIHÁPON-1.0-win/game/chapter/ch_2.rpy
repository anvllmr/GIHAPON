# Insert Chapter 2 here

label story_ch_02:

#SCENE 1 : EXT. MONTERO HOUSE - JUNE 14, 1992. 12:26 P.M.
    $ Wynona = "???"

    show black
    with dissolve

    pause 1

    play sound SFX_knock

    pause 1.5

    window show 

    char_wyn "Hello!? 
    {w=0.5}Anyone home!?"

    MC "Wait a second{cps=*0.15}...{/cps} 
    {w=0.5}Isn’t that-"
    window hide

    pause 0.5

    scene bg-extmaxhouse
    with fade
    pause 1.0

    $ Wynona = "Wynona"

    window show
    sys_nar "{cps=30}EXT. MONTERO HOUSE - JUNE 14, 1992. 12:26 P.M.{/cps}"
    window hide

    pause 1.0

    play sound SFX_Mystery
    show wynona - neutral
    with dissolve

    pause 0.5

    play music BGM_cool

    pause 0.5
    window show
    MC "Hey, 
    {w=0.5}what are you doing here?"

    show wynona - pleased
    with dissolve

    char_wyn "I brought you what I promised!"
    window hide
    pause 0.5

    show item_grocery at truecenter
    with irisin

    pause 1.5

    hide item_grocery
    with irisout

    pause 0.5

    window show
    play sound SFX_Idea
    MC "Oh! 
    {w=0.5}Wynona{cps=*0.15}...{/cps} 
    {w=0.5}You really don’t need to do this{cps=*0.15}...{/cps} 
    {w=0.5}thank you." with sflash

    show wynona - sad
    with dissolve

    char_wyn "No, 
    {w=0.5}I just wanted to apologize for making you drop the stuff you bought from the market."

    show wynona - happy
    with dissolve

    char_wyn "Plus I wanted to thank you for giving this back"

    window hide
    pause 0.5

    show item_locket at truecenter
    with irisin

    pause 1.5

    hide item_locket
    with irisout

    pause 0.5

    window show

    char_wyn "Yes, 
    {w=0.5}this locket is very dear to me."

    MC "Well yeah. 
    {w=0.5}No worries. 
    {w=0.5}It’s my pleasure."
    window hide 
    pause 0.5
    window show
    MC "{cps=*0.15}...{/cps}"
    window hide 
    pause 0.5
    show wynona - neutral
    with dissolve
    window show
    MC "So{cps=*0.15}...{/cps}
    {w=0.5} Uhm- are you going somewhere?"

    show wynona - confused
    with dissolve

    char_wyn "Actually, 
    {w=0.5}my mom wants you to join us for lunch."

    MC "Woah, 
    {w=0.5}wait why?-"

    show wynona - thinking
    with dissolve

    char_wyn "You’re not busy right? 
    {w=0.5}Mom really gets pushy with this stuff so if you’re free"

    MC "Uhm I don’t know{cps=*0.15}...{/cps}
    {w=0.5}I was hoping to-"

    show wynona - confused
    play sound SFX_Smack
    char_wyn "Just join us, 
    {w=0.5}please? 
    {w=0.5}Mom is really persistent. 
    {w=0.5}Sorry if she’s a bit pushy. 
    {w=0.5}We’ll wait for you in the car." with sshake

    MC "Alright, 
    {w=0.5}alright. 
    {w=0.5}wait a sec. 
    {w=0.5}I’ll just let my Auntie Cheng know."
    window hide 

    hide wynona
    with dissolve

    stop music fadeout 1.0

    pause 1.0

#SCENE 2 : FANCY RESTAURANT - AFTERNOON JUNE 14, 1992. 1:30 P.M.
    $ Margaret = "???"
    scene bg-fancyresto
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}FANCY RESTAURANT - AFTERNOON JUNE 14, 1992. 1:30 P.M.{/cps}"
    window hide

    pause 1.0

    show wynona - neutral at offscreenright
    show mamynona - neutral
    with dissolve
    play sound SFX_Mystery

    pause 1.0
    play music BGM_cool

    window show
    side_mamawyn "Nice to finally meet you, 
    {w=0.5}Max.
    {w=0.5}I'm Margaret Balandra"

    $ Margaret = "Margaret"

    MC "Uhmm... 
    {w=0.5}Nice to meet you too, 
    {w=0.5}Mrs. Balandra."

    show mamynona - serious
    play sound SFX_Smack
    side_mamawyn "Waiter! 
    {w=0.5}The menu please." with sshake

    ex_waiter "Of course ma’am here you go."

    show mamynona - pleased
    with dissolve

    side_mamawyn "We’ll have set 4 with a bottle of {=hl}Château Léoville-Poyferré.{/=hl}"

    ex_waiter "Yes, 
    {w=0.5}I’ll have your order in 20 minutes."

    side_mamawyn "Thank you."

    show mamynona - neutral
    with dissolve

    side_mamawyn "So Max, 
    {w=0.5}what kind of relationship do you have with my Wynona?"
    window hide
    
    show mamynona at left
    show wynona - surprised at right
    with decay10inleft

    pause 0.5

    window show
    play sound SFX_Smack
    char_wyn "Mom! 
    {w=0.5}He’s an old schoolmate, 
    {w=0.5}nothing more. 
    {w=0.5}He returned my locket when I bumped into him, 
    {w=0.5}I owed him for that." with sshake

    show mamynona - pleased
    show wynona - confused
    with dissolve

    side_mamawyn "Oh no don’t worry sweetie, 
    {w=0.5}I don’t mean anything about my line of questioning."

    show mamynona - neutral
    with dissolve

    side_mamawyn "I just wanted to know who my daughter’s been associating with these days. 
    {w=0.5}I just wanted to meet the one who made sure my daughter’s precious locket would be returned"

    MC "Don’t worry, 
    {w=0.5}Mrs. Balandra. 
    {w=0.5}We’re just acquaintances."

    side_mamawyn "Oh, 
    {w=0.5}really?"

    side_mamawyn "Didn’t you say your last name was Montero?"

    MC "Uhmm{cps=*0.15}...{/cps} 
    {w=0.5}I don’t believe I have. 
    {w=0.5}But yes, 
    {w=0.5}My last name’s Montero."

    show wynona - sad
    with dissolve

    char_wyn "{cps=*0.15}...{/cps}"

    side_mamawyn "That’s great. 
    {w=0.5}Hmmm. 
    {w=0.5}Montero…"

    side_mamawyn "Montero{cps=*0.15}...{/cps} 
    {w=0.5}I don’t know why but that name seems familiar to me."

    show wynona - confused
    with dissolve

    char_wyn "Is it mom?"

    MC "I don’t believe I’ve met you before Mrs. Balandra."

    show mamynona - pleased
    with dissolve

    side_mamawyn "Ah! 
    {w=0.5}I’ve got it! 
    {w=0.5}Your father and I have met before. 
    {w=0.5}Way back we used to hang out."

    MC "What? 
    {w=0.5}For real?"

    show mamynona - neutral
    with dissolve

    side_mamawyn "It’s true. 
    {w=0.5}Though it is too bad. 
    {w=0.5}If I recall you were a bit too young so I doubt you’d remember anything about me."

    MC "{=txt_vo} (Dad never mentioned anything about the Balandras…)"
    window hide

    pause 0.5
    stop music fadeout 1.0
    pause 0.5

    window show
    show wynona - happy
    play sound SFX_Idea
    char_wyn "The food's here! I’m starving, 
    {w=0.3} let’s eat." with sflash
    window hide

    #FADE TO BLACK
    show black
    with dissolve
    
    pause 1.0

    play music BGM_mystery
    show wynona - neutral
    pause 0.5
    hide black 
    with dissolve
    
    pause 0.5
    #FADE IN
    window show
    side_mamawyn "So Max. 
    {w=0.5}I’ve heard that you moved away a few years ago."

    MC "Yes, 
    {w=0.5}as a matter fact it was 5 years ago when we decided to move."

    show mamynona - serious
    with dissolve

    side_mamawyn "Is that so? 
    {w=0.5}That’s too bad. 
    {w=0.5}You would’ve witnessed the rise of the local business industry here."

    MC "Yes, 
    {w=0.5}it's a bit jarring to see all these flashy new establishments all around the town"

    show wynona - sad
    with dissolve

    char_wyn "{cps=*0.15}...{/cps}"

    side_mamawyn "Jarring? 
    {w=0.5}I won't take offense to that but to tell you the truth our family has helped with raising the economy here."

    MC "Yeah, 
    {w=0.5}I've heard about that from Wynona's boss."

    show mamynona - neutral
    with dissolve

    side_mamawyn "Oh so you've met Ms. Dimasipa. 
    {w=0.5}A wonderful woman that she is. 
    {w=0.5}But of course that fine establishment she oversees would eventually need someone to take over in the future." 
    side_mamawyn "That is why my daughter is there, 
    {w=0.5}she will take the reins in the future for Iliganon City's Publication."

    show wynona - confused
    with dissolve

    char_wyn "Mom.  
    {w=0.5}Max doesn't need to know all about this stuff."

    show mamynona - serious
    with dissolve

    side_mamawyn "He certainly does, 
    {w=0.5}dear. 
    {w=0.5}If you’re staying in this town, 
    {w=0.5}then you'd better know the names of the big players."

    MC "{=txt_vo}(Big players? 
    {w=0.5}This Mrs. Balandra sure does love talking up their ego)"

    show mamynona - neutral
    show wynona - sad
    with dissolve

    side_mamawyn "So Max for whatever reason have you come back to this town?"

    MC "Well actually, 
    {w=0.5}to be frank, 
    {w=0.5}I have no idea."

    show mamynona - serious
    with dissolve

    side_mamawyn "Y-you have no idea? 
    {w=0.5}hahaha You are one peculiar kid.
    {w=0.5}One doesn't simply come back to a place like this without reason.
    {w=0.5}Especially someone with a history to this place."

    MC "{=txt_vo}(Wait, 
    {w=0.5}what is she insinuating with history with this town?)"

    MC "Err{cps=*0.15}...{/cps} 
    {w=0.5}Uhmmm{cps=*0.15}...{/cps}"
    
    show wynona - confused
    with dissolve
    
    char_wyn "Mom, 
    {w=0.5} I think you're making Max uncomfortable with your grilling."

    show mamynona - pleased
    with dissolve

    side_mamawyn "Me? 
    {w=0.5}Grilling? 
    {w=0.5}well I digress. 
    {w=0.5}Maybe some people don't need a reason for going places I guess."

    MC "Yeah maybe that's the case haha."
    window hide

    stop music fadeout 1.0
    pause 0.5

    window show 
    play sound SFX_Foreshadow
    MC "{=txt_vo}(Why'd the conversation become heated all of the sudden)"
    window hide

    #FADE TO BLACK
    show black
    with dissolve
    
    pause 1.0

    play music BGM_cool
    show wynona - neutral
    show mamynona - neutral
    pause 0.5
    hide black 
    with dissolve
    
    pause 0.5
    #FADE IN
    window show
    play sound SFX_Idea
    MC "Phew. 
    {w=0.5}That’s probably the best food I’ve had since arriving." with sflash

    show mamynona - pleased
    with dissolve

    side_mamawyn "Well I’m glad you could come and enjoy the fruits of Balandra’s business endeavors"

    show wynona - confused
    play sound SFX_Smack
    char_wyn "Mom!" with sshake

    show mamynona - serious
    with dissolve

    side_mamawyn "What darling? 
    {w=0.5}I’ll need to have a word with you later"

    show wynona - sad
    with dissolve

    char_wyn "Fine{cps=*0.15}...{/cps}"

    MC "Well thank you for the food Mrs. Balandra. 
    {w=0.5}I appreciate bringing me here."

    show mamynona - pleased
    with dissolve

    side_mamawyn "It is my pleasure Max. 
    {w=0.5}Just so you know max just be careful around here."

    show mamynona - serious
    with dissolve

    side_mamawyn "I know that business has been booming but that only raised the crime rate."

    MC "Uhmm yeah I’m sure I’ll be safe around here Mrs. Balandra."

    show mamynona - pleased
    with dissolve

    side_mamawyn "Well, 
    {w=0.5}I hope you do. 
    {w=0.5}There’s been recent cases of disappearances and robbery so you’d best be mindful."

    char_wyn "{cps=*0.15}...{/cps}"

    MC "Yeah sure. 
    {w=0.5}I think I’ll head out, 
    {w=0.5}Auntie Cheng must be looking for me now."

    side_mamawyn "Goodbye, 
    {w=0.5}Max Montero."
    window hide 

    stop music fadeout 1.0

    hide mamynona
    with dissolve
    pause 0.5

    show wynona at center
    with decay10inleft

    pause 0.5

    show wynona - confused
    with dissolve

    pause 0.5

    hide wynona
    with dissolve


    #FADE OUT

    #SCENE EXT RESTAURANT

    scene bg-extdikumakainevening
    with fade

    play music AMB_nature
    pause 1.0

    window show
    MC "{=txt_vo}(Looks like I’ve been out for a while. 
    {w=0.5}I hope I didn’t worry Auntie Cheng)"

    play sound SFX_Idea
    char_wyn "Hey Max! 
    {w=0.5}Wait." with sflash
    window hide

    pause 0.5

    play sound SFX_Mystery
    show wynona - neutral
    with dissolve

    pause 0.5
    window show

    MC "Wynona?"

    show wynona - pleased
    with dissolve

    char_wyn "I just wanted to say thank you for coming with us today. 
    {w=0.5}I know my mom can be tough but I’m glad you could come."

    play sound SFX_Smack
    MC "Glad I could come! 
    {w=0.5}Thank you again." with sshake

    char_wyn "Anyway that’s all. 
    {w=0.5}I don’t wanna hold you on for too long. 
    {w=0.5}See you Max!"

    MC "See you Wynona."
    window hide
    
    stop music fadeout 1.0

    pause 0.5
    show wynona - happy
    with dissolve
    pause 0.5
    hide wynona
    with dissolve
    pause 1.0

#SCENE 3 : EXT. BARANGAY STREET DIMAHAMPAK - JUNE 14, 1992. 5:30 P.M.
    scene bg-outsidemaxhouseeve
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}EXT. BARANGAY STREET DIMAHAMPAK - JUNE 14, 1992. 5:30 P.M.{/cps}"
    window hide

    play music AMB_nature
    pause 1.0
    MC "{=txt_vo}(We only ate and talked but that was already exhausting…)"

    MC "{=txt_vo}(What a small world, 
    {w=0.5}huh? 
    {w=0.5}Mrs. Balandra knew my Dad. 
    {w=0.5}I should call him soon and ask him about that.)"

    MC "{=txt_vo}(Can’t believe the Balandras own half of the businesses here in Iliganon City. 
    {w=0.5}Maybe, 
    {w=0.5}I can ask them about the {=hl}Synghs{/=hl}, 
    {w=0.5}about {=hl}Lheona?{/=hl})"
    window hide 

    pause 0.5
    stop music fadeout 1.0
    play sound SFX_ambulance

    pause 7.0
    window show
    play sound SFX_Idea
    MC "An {=hl}ambulance?{/=hl} Wait a minute it’s going towards my house. What’s going on here?" with sflash

    MC "I gotta go check!"
    window hide 

    pause 0.5

#SCENE 4 : EXT. MONTERO HOUSE - JUNE 14, 1992. 5:35 P.M.
    $Azzi = "???"

    scene bg-extmaxhouseevening
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}EXT. BARANGAY STREET DIMAHAMPAK - JUNE 14, 1992. 5:30 P.M.{/cps}"
    window hide

    play music AMB_nature
    pause 1.0
    
    window show
    play sound SFX_Idea
    side_dodong "Max! 
    {w=0.5}There you are!" with sflash
    window hide

    play sound SFX_Mystery
    show dodong - sad
    with dissolve
    pause 0.5

    window show
    play sound SFX_Smack
    MC "What happened here!?" with sshake
    stop music fadeout 0.5
    play music BGM_forbode
    side_dodong "Someone broke into your house, 
    {w=0.5}A-auntie Cheng was found unconscious on the floor."

    play sound SFX_Smack
    MC "What! 
    {w=0.5}Where is she?" with sshake

    play sound SFX_Smack
    MC "Auntie Cheng!" with sshake
    window hide

    show dodong at offscreenright
    with decay10inleft
    pause 0.5
    
    window show
    play sound SFX_Smack
    azzi "Hey! 
    {w=0.5}Get away from the victim!" with sshake
    window hide

    pause 0.5
    
    play sound SFX_Mystery
    show azzi - confused at left
    show dy - neutral at right
    with dissolve

    window show
    play sound SFX_Smack
    MC "She’s my Aunt!" with sshake

    d "She’s your Aunt, 
    {w=0.5}huh? 
    {w=0.5}She’s alright, 
    {w=0.5}don’t worry. 
    {w=0.5}She’s just unconscious. 
    {w=0.5}Also, 
    {w=0.5}I need you to answer a few questions for me about the victim."

    MC "B-but I need to go with Auntie Cheng-"

    show azzi at offscreenleft
    show dy at left
    show dodong at right
    with decay10inleft

    side_dodong "I can go with her, 
    {w=0.5}Max."

    MC "Is that alright? 
    {w=0.5}What about your karinderya?"

    side_dodong "Don’t worry about it. 
    {w=0.5}I’ll call Mariano."

    MC "Thank you, 
    {w=0.5}Dodong{cps=*0.15}...{/cps}"
    window hide

    stop music fadeout 1.0

    hide azzi
    hide dy 
    hide dodong
    with dissolve
    
    pause 0.5

#SCENE 5 : INT. MONTERO HOUSE - JUNE 14, 1992. 5:50 P.M.
    $Azzi = "Azzi"

    scene bg-intmaxhousedining
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30} INT. MONTERO HOUSE - JUNE 14, 1992. 5:50 P.M.{/cps}"
    window hide
    
    pause 1.0

    show dy - neutral at offscreenright
    show azzi - confused
    play sound SFX_Idea
    azzi "Whoa, 
    {w=0.5}What happened to your face?" with sflash

    MC "I was punched by some drunkard{cps=*0.15}...{/cps} 
    {w=0.5}Why?"

    play music BGM_azzi

    azzi "Where were you today? 
    {w=0.5}Why weren't you with the victim?"

    MC "I had lunch with some acquaintances{cps=*0.15}...{/cps} 
    {w=1.0}Wait a second, 
    {w=0.5}are you suspecting{nw}"
    play sound SFX_Smack
    extend" me?" with sshake

    show azzi - smug
    play sound SFX_Idea
    azzi "There’s a possibility! 
    {w=0.5}You weren’t here all day then “coincidentally” something happened with your aunt." with sflash

    MC "What!? 
    {w=0.5}Are you serious? 
    {w=0.5}Why would I even want to hurt Auntie Cheng!? 
    {w=0.5}Let alone come back to the crime scene where all the police are stationed!"

    show azzi - angry
    with dissolve

    azzi "Maybe you have something against the victim, 
    {w=0.5}we never know!"
    window hide

    play sound SFX_bonk
    show azzi - confused
    with sshake
    pause 0.5

    show azzi at left
    show dy - angry at right
    with decay10inleft
    pause 0.5

    window show
    d "Hey, 
    {w=0.5}what nonsense are you babbling about?"

    show azzi - happy
    play sound SFX_Idea
    azzi "Ah- 
    {w=0.5}Boss!" with sflash

    show dy - neutral
    with dissolve

    d "Don’t mind him, 
    {w=0.5}This is {=hl}Azzi Stan{/=hl}. 
    {w=0.5}He’s working with me."

    $ Azzi = "Azzi"

    show azzi - neutral
    with dissolve

    azzi "I’m just connecting the dots, 
    {w=0.5}boss! 
    {w=0.5}You have to think outside of the box sometimes"

    show dy - annoyed
    with dissolve

    d "Well your box Azzi, 
    {w=0.5}It’s all botched up and full of holes."

    show dy - angry
    play sound SFX_Smack

    d "Don’t accuse someone with no evidence! 
    {w=0.5}Haven’t we gone over this!?" with  sshake
    window hide 

    stop music fadeout 1.0
    pause 0.5
    show dy - neutral
    with dissolve
    pause 0.8

    play music BGM_tektiv
    window show
    d "By the way, 
    {w=0.5}I talked to some officers and they found {=hl}traces of blood near the broken window{/=hl}. The culprit probably got hurt while breaking it to escape."
    d "They’ll check it if it’s from your Auntie Cheng or the culprit. 
    {w=0.5}We’ll get the result in a day or two."

    MC "Oh, 
    {w=0.5}okay. 
    {w=0.5}Is Auntie Cheng gonna be alright?"

    show dy - thinking
    with dissolve

    d "She’s in stable condition, 
    {w=0.5}she’s just unconscious."

    MC "That’s a relief"

    show dy - neutral
    with dissolve

    d "According to the preliminary check, 
    {w=0.5}there weren't any wounds on her."

    show dy - thinking
    with dissolve

    d "She had a bruise however, 
    {w=0.5}a {=hl}blunt object{/=hl} was used to strike the victim rendering her unconscious."

    show dy - neutral
    with dissolve

    d "We have the weapon used, 
    {w=0.5}and it was this {=hl}small statue{/=hl}. Do you recognize this Max?"
    window hide
    pause 0.5

    show item_statue at truecenter
    with irisin

    pause 1.5

    hide item_statue
    with irisout

    pause 0.5

    window show
    MC "Yes, 
    {w=0.5}it’s one of the decorations from our living room."

    show dy - thinking
    with dissolve

    d "Interesting{cps=*0.15}...{/cps}"

    show dy - neutral
    with dissolve

    d "Also, 
    {w=0.5}the witnesses saw the culprit run away. 
    {w=0.5}According to an eyewitness, 
    {w=0.5}the suspect was {=hl}wearing a black hoodie, cap, and pants.{/=hl}"

    d "They’re not sure about the gender of our assailant because of how fast everything went but it has been noted that the culprit had a {=hl}slim figure.{/=hl}"

    MC "{=txt_vo}(Who could’ve done it. 
    {w=0.5}We don’t really have anything of great value in our house for us to get broken in)"

    MC "Thanks for the information, 
    {w=0.5}Detective."

    show azzi - confused
    with dissolve

    azzi "Hmm{cps=*0.15}...{/cps} 
    {w=0.5}Detective. 
    {w=0.5}Doesn’t it strike you that this guy also has a slim figure, 
    {w=0.5}you know he might-"

    play sound SFX_Smack
    MC "Hey! 
    {w=0.5}My name is not this guy, 
    {w=0.5}it’s Max." with sshake
    
    show dy - angry

    play sound SFX_Smack
    d "Azzi!" with sshake

    show azzi - sad
    with dissolve

    pause 0.5
    #azzi sulks, again.

    show dy - thinking
    with dissolve

    d "Do you have any idea if there could be someone with a motive against Mrs. Malano?"

    MC "As far as I know I can’t really spell you any names that have some vendetta against Auntie Cheng. 
    {w=0.5}She doesn’t stay here that often."

    MC "Even the shopkeeper from the market said that Auntie was nice to her"

    d "Is that so? 
    {w=0.5}Hmmm… 
    {w=0.5}So we can rule out personal grudges as the motive for the crime here."

    show azzi - confused
    with dissolve

    azzi "But we’ve only asked Max so far."

    show dy - neutral
    with dissolve

    d "If the motive was to hurt Mrs. Malano she wouldn’t be alive right now. 
    {w=0.5}The culprit would’ve {=hl}finished the job.{/=hl}"

    d "Also we can rule out that Mrs. Malano was targeted."

    azzi "Why would that be, 
    {w=0.5}inspector?"

    d "One reason."
    window hide
    pause 0.5

    show item_statue at truecenter
    with irisin

    pause 1.5

    hide item_statue
    with irisout

    pause 0.5

    window show
    MC "The statue?"

    show dy - confused
    with dissolve

    d "If you were planning a murder what salient points must you consider?"

    show azzi - angry
    with dissolve

    azzi "Hmmm{cps=*0.15}...{/cps} 
    {w=0.5}I can’t think about murdering someone inspector. 
    {w=0.5}I’m not a criminal!"
    show dy - angry

    play sound SFX_Smack
    d "This is just a hypothetical, 
    {w=0.5}Azzi! 
    {w=0.5}sigh{cps=*0.15}...{/cps}" with sshake

    MC "Well, 
    {w=0.5}if it were me I’d think about {=hl}who{/=hl} I should murder, 
    {w=0.5}{=hl}why{/=hl} I’d murder, 
    {w=0.5}and {=hl}where{/=hl} and {=hl}when{/=hl} I murder."

    show dy - smug
    with dissolve

    d "That is correct Max, 
    {w=0.5}I hope you don’t have any plans with that in the future. 
    {w=0.5}Hahaha!"

    MC "That’s not funny, 
    {w=0.5}Inspector!"

    show dy - thinking
    with dissolve

    d "Anyway you are missing a key factor."

    MC "And that is?"

    show dy - smug
    with dissolve

    d "How. 
    {w=0.5}It’s elementary my dear Max."

    MC "{=txt_vo}({cps=*0.15}...{/cps} 
    {w=0.5}Was that a Sherlock impression?)"

    show dy - thinking
    with dissolve

    d "What our culprit was lacking was a {=hl}murder weapon{/=hl}. 
    {w=0.5}If you were going to plan a murder, 
    {w=0.5}you would need a murder weapon."

    show dy - neutral
    with dissolve

    d "Our culprit however did not bring one. 
    {w=0.5}When confronting Mrs. Malano, 
    {w=0.5}they needed to use {=hl}something from the scene{/=hl}, 
    {w=0.5}which was your statue."

    d "By that reasoning, 
    {w=0.5}attempted murder is out of the question. 
    {w=0.5}Maybe for some reason they didn’t factor in that Mrs. Malano would be in the house today."

    d "We don’t know what motive the break in was for, 
    {w=0.5}but it certainly wasn’t to hurt Mrs. Malano"

    d "We have yet to find out why."

    MC "Wow {=txt_vo}(Wow I didn’t expect Inspector Dy to be this smart.)"
    show dy - angry

    play sound SFX_Smack
    d "Hey, 
    {w=0.5}what did you think I was?" with sshake

    MC "Ehh what? {=txt_vo}(did he hear my thoughts)"

    d "It’s written on your face kid, 
    {w=0.5}it doesn’t take an astrophysicist to tell."

    show dy - neutral
    with dissolve

    d "Anyway sorry to say kid but your house is gonna be off limits for a while. 
    {w=0.5}We have yet to fully investigate here."

    d "Do you have any place to stay tonight?"

    MC "Wait what? 
    {w=0.5}But I don’t know where I can crash for the night."
    
    show dy - confused
    with dissolve
    
    d "Uhhh{cps=*0.15}...{/cps} 
    {w=0.5}I can’t really help you with that kid."

    MC "{=txt_vo}(Hmm{cps=*0.15}...{/cps} actually maybe I can help with Dy’s investigation.)"

    MC "Can I help with the investigation? 
    {w=0.5}It’s my house anyway. 
    {w=0.5}I can help tell you things about it!"

    show dy - neutral
    with dissolve

    d "Uhm{cps=*0.15}...{/cps} 
    {w=0.5}Civilians aren't allowed to interfere with our work, 
    {w=0.5}Max."

    MC "But-"
    window hide

    pause 0.5
    show dy - surprised  
    show azzi - confused  
    play sound SFX_ring
    with sshake
    stop music fadeout 0.2
    show item_phone at truecenter
    with irisin
    pause 1.0
    #Dy’s phone rings.
    window show
    show dy - neutral
    with dissolve

    d "Ah wait. 
    {w=0.5}I gotta take this."
    window hide 
    hide item_phone
    with irisout
    show dy at offscreenright
    show azzi at center
    with decay10inleft
    pause 0.5
    window show
    MC "{=txt_vo}(Great, now I don’t get to sleep in my bed tonight?)"
    window hide
    show dy at right
    show azzi at left
    with decay10inleft
    pause 0.5
    window show
    d "We should go to the hospital. 
    {w=0.5}Dodong said Auntie Cheng is awake."

    MC "Really? 
    {w=0.5}But what of the investigation-"

    d "Argh. 
    {w=0.5}Let’s just continue that later."
    window hide 

    hide dy
    hide azzi
    with dissolve

    pause 0.5

#SCENE 6 : INT. HAVEN HOSPITAL - MIDNIGHT JUNE 15, 1992. 1:22 A.M.
    scene bg-hospitalroom
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30} INT. HAVEN HOSPITAL - JUNE 15, 1992. 1:22 A.M.{/cps}"
    window hide
    
    pause 1.0

    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft

    show dodong - surprised
    play sound SFX_Idea
    side_dodong "Finally, you guys are here." with sflash

    play music BGM_casual

    play sound SFX_Smack
    MC "Auntie! How are you!?" with sshake

    show dodong at right
    show cheng - happy at left behind dy
    play sound SFX_Idea
    side_cheng "I’m alright, 
    {w=0.5}Max. 
    {w=0.5}Hello Detective and...?" with sflash
    window hide
    pause 0.5
    show dodong at offscreenright 
    show cheng at offscreenright

    show dy at left
    show azzi at right
    with decay10inleft
    play sound SFX_Mystery
    pause 0.5
    window show
    azzi "Azzi, 
    {w=0.5}po. 
    {w=0.5}Detective’s assistant!"

    d "What did the doctor say?"
    window hide
    
    show dodong - neutral at right
    show cheng - neutral at left

    show dy at offscreenleft
    show azzi at offscreenleft
    with decay10inleft
    
    window show
    show dodong - sad
    with dissolve
    side_dodong "It’s just a mild concussion. 
    Auntie needs to rest here for a few days."

    MC "I’m sorry I wasn't able to go with you, 
    {w=0.5}Auntie{cps=*0.15}...{/cps}"

    side_cheng "Max, 
    {w=0.5}it’s okay— 
    {w=0.5}I’m okay{cps=*0.15}...{/cps} 
    {w=0.5}So, 
    {w=0.5}how’s the investigation?"
    window hide
    
    show dodong at offscreenright 
    show cheng at right

    show dy at left
    with decay10inleft
    
    window show
    d "They found traces of blood. 
    {w=0.5}It’s either yours or the culprit. 
    {w=0.5}Also, 
    {w=0.5}it may give you peace of mind that murder wasn’t a motive for the crime."

    show cheng - thinking
    with dissolve

    side_cheng "Oh my, 
    {w=0.5}honestly that doesn’t really help."

    show dy - thinking
    with dissolve

    d "We’re not really sure yet, 
    {w=0.5}but can you elaborate what happened first, 
    {w=0.5}Auntie?"

    show cheng - confused
    with dissolve

    side_cheng "Hm, 
    {w=0.5}I was out, 
    {w=0.5}I had to buy some ingredients I was missing because Max had a small altercation at the market yesterday."

    show cheng - sad
    with dissolve

    side_cheng "When I came back, 
    {w=0.5}I noticed that the back door wasn’t bolted and was slightly opened. 
    {w=0.5}My mistake was I didn’t mind it. 
    {w=0.5}I thought it was just me forgetting to lock things again"

    side_cheng "Then I proceeded to wash the dishes and heard some scuttling noises from the second floor. 
    {w=0.5}I heard a click, 
    {w=0.5}like a door locking. 
    {w=0.5}So I went to investigate."

    show cheng - confused
    with dissolve

    side_cheng "I went up but saw no one. 
    {w=0.5}Since no one was there I decided to get back to what I was doing. 
    {w=0.5}As I was going down I heard a crash sound from the living room."

    side_cheng "I ran as fast as I could towards the room then from the corner of my eye I saw the figure of the culprit."

    show cheng - sad
    with dissolve

    side_cheng "I was about to say something when they suddenly pushed me. 
    {w=0.5}I grabbed the culprit’s arm and began shouting. 
    {w=0.5}That’s when they picked up something from the table and my vision just went black."

    show cheng - confused
    with dissolve

    side_cheng "Before I lost consciousness though, 
    {w=0.5}I recall hearing a loud noise like glass shattering."

    MC "Do you remember what they looked like?"

    side_cheng "The culprit was wearing all black. 
    {w=0.5}I’m not really sure what they look like because of their balaclava, 
    {w=0.5}they were shorter than Max, 
    {w=0.5}and had a slim figure."

    d "Thank you so much for your cooperation, 
    {w=0.5}Mrs. Malano! This experience must be traumatic for you. 
    {w=0.5}You should take a rest."

    show cheng - happy
    with dissolve

    side_cheng "Don’t worry too much about me, 
    {w=0.5}Detective. 
    {w=0.5}Just another entry to 
    {w=0.5}”Auntie Cheng’s Journal of Wild Experiences”. 
    {w=0.5}Thank you again."

    show dy - confused
    with dissolve

    d "Uhh{cps=*0.15}...{/cps} 
    {w=0.5}sure!"
    window hide

    show black
    with dissolve
    stop music fadeout 1.0
    show cheng - neutral
    pause 0.2
    hide black
    with dissolve
    pause 0.5

    show dy - smug
    with dissolve    

    window show
    d "Alright then, 
    {w=0.5}I’ll be taking my leave, 
    {w=0.5}Azzi let’s go. 
    {w=0.5}Max, 
    {w=0.5}you should also rest."
    window hide

    show dy at offscreenleft
    show cheng at center
    with decay10inleft

    window show
    MC "{=txt_vo}(He’s leaving? 
    {w=0.5}But what about the investigation?)"

    MC "I’ll be right back, 
    {w=0.5}Auntie."
    window hide

    hide cheng
    with dissolve

    pause 0.5

#SCENE 7 : INT. HAVEN HOSPITAL - MIDNIGHT JUNE 17, 1992. 2:12 A.M.
    scene bg-hospitalhallway
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30} INT. HAVEN HOSPITAL HALLWAY - JUNE 15, 1992. 2:12 A.M.{/cps}"
    window hide
    
    pause 1.0

    play music BGM_goodnight

    window show
    play sound SFX_Smack
    MC "Dy, Wait!" with sshake
    window hide

    play sound SFX_Mystery
    show dy - neutral at right
    show azzi - neutral at left
    with dissolve
    
    pause 0.5
    window show
    d "What is it, 
    {w=0.5}Max?"

    MC "So, 
    {w=0.5}can I join the investigation?"

    show dy - angry
    play sound SFX_Smack

    d "I told you already, 
    {w=0.5}you can’t! 
    {w=0.5}You shouldn't be meddling with our work. 
    {w=0.5}You’re the victim here-" with sshake

    show azzi - smug
    with dissolve

    azzi "I’m not opposed to the idea, 
    {w=0.5}Boss. 
    {w=0.5}Max can help in this investigation. 
    {w=0.5}I just can feel his vibe helping us out."
    
    show azzi - happy
    with dissolve

    azzi "He definitely has great ideas. 
    {w=0.5}He even thought like a murderer earlier. 
    {w=0.5}With a murder mastermind at our side I think we can pinpoint our culprit."

    show azzi - neutral 
    with dissolve

    MC "What are you talking about?"

    show dy - annoyed
    play sound SFX_Smack

    d "Give me a break! 
    {w=0.5}This isn’t the only case I’m working on, 
    {w=0.5}okay? 
    {w=0.5}Both of you should stop this nonsense." with sshake

    MC "Detective, 
    {w=0.5}please let me help the investigation. 
    {w=0.5}I’ve got this feeling that the reason why this happened is because I came back."

    show dy - confused
    with dissolve

    d "What do you mean?"

    MC "I’m not entirely sure. 
    {w=0.5}But, 
    {w=0.5}I have a feeling there might be a connection to this case to why I’m here."

    show dy - annoyed
    with dissolve

    d "You lost me there son. 
    {w=0.5}And I’m not comfortable involving you in the investigation. 
    {w=0.5}Especially {=hl}you.{/=hl}"

    show dy - confused
    with dissolve

    MC "What do you mean? 
    {w=0.5}Gahhh Just give me a chance, 
    {w=0.5}I’m sure I can help you somehow! 
    {w=0.5}I won’t stop asking you to let me join this investigation. 
    {w=0.5}I promise you I’ll be useful, 
    {w=0.5}really!"

    MC "You know what? 
    {w=0.5}I'll even visit you tomorrow, 
    {w=0.5}Detective!"

    show dy - annoyed
    with dissolve

    d "There’s nothing I can make you to stop, 
    {w=0.5}is there? Gahh{cps=*0.15}...{/cps} 
    {w=0.5}Do as you wish. 
    {w=0.5}No word of this to anyone else okay? 
    {w=0.5}I might get in trouble for involving citizens."

    MC "Really I won’t disappoint! 
    {w=0.5}Wait, 
    {w=0.5}so can I stay in my house tonight?"

    show dy - thinking
    with dissolve

    d "That- 
    {w=0.5}Sorry but you can’t tonight. 
    {w=0.5}Let the police investigate first and then you can come back."

    MC "Darn then I don’t have a place to stay tonight"
    window hide
    pause 0.5

    play sound SFX_walk

    pause 0.5
    show dy at left
    show azzi at offscreenleft
    with decay10inleft
    show dodong - surprised at right
    with dissolve
    pause 0.5

    window show
    side_dodong "Oh Mr. Dy, 
    {w=0.5}I thought you went home."
    
    show dy - smug
    with dissolve
    
    d "Oh I have an idea. 
    {w=0.5}Dodong, 
    {w=0.5}do you have a spare room at your house tonight? 
    {w=0.5}Max needs a place to crash while the police continue to investigate Max’s house."

    show dodong - thinking
    with dissolve

    side_dodong "Uhmm Yeah we have a spare. 
    {w=0.5}Though, 
    {w=0.5}I apologize in advance for any baby screaming and crying."

    MC "Great, 
    {w=0.5}I have a place to stay. 
    {w=0.5}Wait, 
    {w=0.5}Dodong, 
    {w=0.5}you have a baby? 
    {w=0.5}You’re a{nw}"
    play sound SFX_Smack
    extend " father!?" with sshake

    show dodong - happy 
    with dissolve

    side_dodong "Father of one! 
    {w=0.5}And yeah she’s turning 1 this november."

    MC "{=txt_vo}(My highschool classmates having children already? 
    {w=0.5}I’m not gonna get any younger am I)"

    MC "That’s amazing. 
    {w=0.5}Thanks for letting me crash at your place Dodong."

    show dodong - neutral
    with dissolve

    side_dodong "No worries!"

    show dy - neutral
    with dissolve

    d "Since that’s settled, 
    {w=0.5}I’ll be heading out, 
    {w=0.5}see you boys."

    MC "I’ll see you tomorrow Inspector. 
    {w=0.5}Don’t forget about our agreement."

    d "Yeah yeah…"
    window hide
    
    stop music fadeout 1.0

    pause 0.5
    
    show black
    with dissolve
    hide dy
    hide azzi
    hide dodong
    pause 0.5

    hide black 
    with dissolve 

    #Later on:

    #DY’s POV
    pause 0.5

    show azzi - confused at center
    with dissolve
    
    pause 0.5
    
    window show
    azzi "Hey, 
    {w=0.5}why’d you agree on Max helping out with the investigation just like that? 
    {w=0.5}You’re usually more. 
    {w=0.5}How should I say this{cps=*0.15}...{/cps}"

    d "I’m usually what?"

    azzi "I don’t know{cps=*0.15}...{/cps}
    {w=0.5}Errr... {w=0.5}{nw}"
    play sound SFX_Idea
    extend " difficult to deal with?" with sflash

    d "sigh{cps=*0.15}...{/cps} 
    {w=0.5}Am I really?
    {w=0.5}{=txt_vo}(To be honest Azzi, 
    {w=0.5}You’re more infuriating to deal with sometimes)"

    d "Well he’s special."

    azzi "Special in what way."

    d "He doesn’t know this but Max and I go way back. 
    {w=0.5}He’s just forgotten I guess?"

    d "He’s the key to solving the case."

    azzi "This case?"

    d "{=txt_vo}(No{cps=*0.15}...{/cps} 
    {w=0.5}The case from 5 years ago"

    d "Yawn. 
    {w=0.5}Azzi, 
    {w=0.5}I’m tired, 
    {w=0.5}let's call it a night. 
    {w=0.5}I’ll go on ahead. 
    {w=0.5}See you tomorrow!"

    show azzi - angry
    play sound SFX_Smack
    azzi "Hey, 
    {w=0.56}you haven’t answered my question. Unfair!" with sshake
    window hide

    hide azzi
    with dissolve

    pause 0.5
    #Azzi Exits the Scene

    #Show Ominous Figure
    show black
    with dissolve
    hide dy
    hide azzi
    hide dodong
    pause 1.0

    hide black 
    with dissolve 

    pause 0.5

    show ex_omen
    with dissolve
    pause 0.25
    play sound SFX_Omen

    pause 2.5

    window show
    ex_of "{cps=*0.15}...{/cps}"
    window hide

    pause 0.5

    hide ex_omen
    with dissolve

    pause 1.0
    #Ominous Figure Exits the Scene

#SCENE 8 : DY’S OFFICE JUNE 17, 1992. 9:00 A.M.

    scene black
    with fade
    pause 1.0
    #SCENE BLACK SCREEN
    play sound SFX_knock
    #SFX KNOCKING   
    pause 1.0

    window show
    MC "Inspector?"

    MC "{=txt_vo}(Hmmm{cps=*0.15}...{/cps} No answer?)"

    MC "{=txt_vo}(He should be here according to the receptionist.)"

    MC "{=txt_vo}(Though, 
    {w=0.5}the door’s not locked. 
    {w=0.5}Guess I’ll go see if he’s here)"
    window hide

    play sound SFX_door1

    pause 2.5

    scene bg-dyoffice
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}  DY’S OFFICE - JUNE 17, 1992. 9:00 A.M.{/cps}"
    window hide
    
    pause 1.0

    window show
    MC "Inspector Dy?"
    window hide

    show dy - sad
    with dissolve
    pause 0.5

    window show 
    d "{cps=*0.15}...{/cps}"

    MC "Can't you hear me or something?"

    MC "{=txt_vo}(Great he’s ignoring me)"
    window hide
    pause 0.5
    window show 
    MC "{cps=*0.15}...{/cps}"

    MC "{=txt_vo}(Wait, 
    {w=0.5}he’s holding something. 
    {w=0.5}Let me get a closer look)"

    window hide
    pause 0.5

    play sound SFX_Mystery
    show item_photoframedy at truecenter
    with irisin

    pause 2.0

    hide item_photoframedy
    with irisout

    pause 0.5

    window show
    play sound SFX_Idea

    MC "What’s that?"

    show dy - surprised
    play sound SFX_Smack
    d "Jesus, 
    {w=0.5}Max. 
    {w=0.5}When and how did you get in here?" with sshake

    MC "I just got here. 
    {w=0.5}I asked one of your friends downstairs if you were in."

    MC "Sigh{cps=*0.15}...{/cps}  
    {w=0.5}Atleast give me the courtesy of not ignoring me."

    MC "So anyway, 
    {w=0.5}who’s that with you in the picture?"

    show item_photoframedy at halfleft
    with irisin

    show dy - sad
    with dissolve

    d "Hmmm{cps=*0.15}...{/cps} 
    {w=0.5}This? 
    {w=0.5}Oh, 
    {w=0.5}It’s- 
    {w=0.5}His name is Carlo. 
    {w=0.5}An old partner."

    MC "Oh, 
    does he still work here?"

    show dy - neutral
    with dissolve

    d "It’s a long story."

    MC "Well since we’re waiting on Azzi maybe you could tell me."

    show dy - confused
    with dissolve

    d "You seriously really wanna hear it?"

    MC "Yeah, 
    {w=0.5}let’s hear it."

    show dy - confused
    with dissolve

    d "Sigh{cps=*0.15}...{/cps} 
    {w=0.5}Alright then{cps=*0.15}...{/cps}"

    show dy - neutral
    with dissolve

    d "Carlo was a rookie investigator like Azzi."

    show dy - sad
    with dissolve

    d "He was really diligent and meticulous. 
    {w=0.5}Had great potential, 
    {w=0.5}he did."

    show dy - neutral
    with dissolve

    d "He was also one of my good friends."

    #FLASHBACK SCENE - DY’S OFFICE:
    window hide
        
    pause 0.5
    play sound SFX_Sweep
    pause 1
    scene black
    with sflash

    pause 0.5

    play music BGM_sadmemory

    pause 0.5

    play sound SFX_knock

    pause 1.5
    
    window show
    side_carlo "Inspector! 
    {w=0.5}It’s me, 
    {w=0.5}Carlo!"
    window hide

    pause 0.5

    window show
    d "Yes, 
    {w=0.5}come in Carlo!"
    window hide

    play sound SFX_door1
    pause 2.5

    scene bg-dyofficepast
    with fade

    pause 0.5

    show carlopast - neutral
    with dissolve

    pause 0.5

    window show
    d "So, 
    {w=0.5}what do you have for me boy?"

    side_carlo "Well remember that conversation we had about the crime scene?"

    d "Yes, 
    {w=0.5}something that you’ve brought up. 
    {w=0.5}The “Hollow flooring” you claimed"

    show carlopast - serious
    with dissolve

    side_carlo "So everyone else in the investigation team claimed they’ve already inspected all there is with the crime scene."

    show carlopast - neutral
    with dissolve

    side_carlo "But like I’ve said the flooring in that house felt off. 
    {w=0.5}Whenever I walked in this certain spot the thumping of my footsteps sounded a lot more hollow"

    d "Any update on that?"

    side_carlo "Took me a while to get permission to look through the crime scene again since nobody takes me seriously in this station but I’ve found a small storage space beneath those floor boards."

    d "Good one Carlo!"

    side_carlo "I’ve found what would be substantial evidence that would lead to the culprit of the case. 
    {w=0.5}I’ve already submitted them so pin pointing the culprit may be sooner than we’d think"

    d "That’s great. 
    {w=0.5}Absolutely phenomenal work Carlo."

    show carlopast - happy
    with dissolve

    side_carlo "No, 
    {w=0.5}Thank you Inspector. 
    {w=0.5}Without you believing in me, 
    {w=0.5}I wouldn’t have the resolve to look into this further. 
    {w=0.5}I am in deep respect for you, 
    {w=0.5}Sir!"
    window hide

    pause 0.5
    play sound SFX_Sweep
    pause 1.0

    scene bg-dyoffice
    show dy - sad
    with sflash

    #Narration
    pause 0.5

    window show
    d "Carlo was a phenomenal asset in my investigations. 
    {w=0.5}He would always think outside the box when it comes to working on a case."
    d "Though with a little bit of an unorthodox way of working, 
    {w=0.5}but hey, 
    {w=0.5}he does the job with finesse."

    #PRESENT DY’S OFFICE:
    show dy - neutral
    with dissolve

    MC "He seems like a nice guy but where’s he now? 
    {w=0.5}I bet he could be a great help with the current case."

    show dy - sad
    with dissolve

    d "Well he{cps=*0.15}...{/cps} 
    {w=0.5}Unfortunately we lost contact with him because of a particular case we were assigned in the past."

    #FLASHBACK - POLICE STATION - MORNING

    #Narration

    d "We were in a case together. 
    {w=0.5}Carlo was really determined to catch the suspect."
    window hide
        
    pause 1
    play sound SFX_Sweep
    pause 1
    scene bg-dyofficepast
    with sflash
    #Show image of Phone
    pause 1.0

    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake

    pause 1.5

    window show
    d "Ahh! 
    {w=0.5}A phone call?"
    window hide

    play sound SFX_Call3
    pause 0.5
    #PHONE CALL:
    window show
    play sound SFX_Smack
    side_carlo "Inspector! 
    {w=0.5}I finally found something!" with sshake

    d "Really?"

    play sound SFX_Idea
    side_carlo "A Lead! 
    {w=0.5}Can you believe it? 
    {w=0.5}And it’s a strong one too!" with sflash

    side_carlo "Hey hear me out, 
    {w=0.5}let's meet up later, 
    {w=0.5}there’s some things I’d like to discuss with you."

    d "I don’t know Carlo. 
    {w=0.5}It’s quite late, 
    {w=0.5}can it wait until tomorrow?"

    play sound SFX_Smack
    side_carlo "No Tektiv, 
    {w=0.5}justice waits for no one. 
    {w=0.5}Let’s meet at the usual spot, 
    {w=0.5}6PM. 
    {w=0.5}I just gotta get something from my apartment. 
    {w=0.5}Aight sir, 
    {w=0.5}Gotta bounce!" with sshake

    d "Hey wait! 
    {w=0.5}{cps=*0.5}...{/cps} 
    {w=0.5}He hung up. 
    {w=0.5}{=txt_vo}(That Kid’s really something else)"
    window hide

    hide item_phone
    with irisout

    pause 0.5

    #Narration

    window show
    d "{=txt_vo}He was saying that he found a strong lead to the case and he mentions that he wants to meet up with me to talk about it. 
    {w=0.5}He’ll meet me after he gets something from his Apartment."
    window hide
 
    #SCENE COFFEE SHOP - AFTERNOON

    pause 1
    play sound SFX_Sweep
    pause 1
    scene bg-fbcoffeeshop
    with sflash
    
    pause 0.5

    window show
    d "{=txt_vo}(What’s taking this guy so long, 
    {w=0.5}it's been 2 hours.)"
    window hide

    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake

    pause 1.5

    window show
    d "Officer Cruz, 
    {w=0.5}what’s up?"

    play sound SFX_Smack
    ex_officer "Detective Dy! 
    {w=0.5}A fire broke out here in an Apartment near Garo. 
    {w=0.5}I need some back up." with sshake

    d "Can you give me the exact address?"

    ex_officer "I’ll text it to you, 
    {w=0.5}Detective."
    window hide

    hide item_phone
    with irisout

    stop music fadeout 1.0

    pause 0.5
    #Narration

    window show
    d "{=txt_vo}I got a message from one of my colleagues saying that a fire broke out in one of the residential apartments near Garo. 
    {w=0.5}I was mortified when I saw the exact address."
    d "{=txt_vo}it was Carlo’s place."
    window hide

    #SCENE 12 CRIME SCENE/RESIDENTIAL APARTMENT - LATE AFTERNOON

    #CG -  Apartment on Fire
    pause 0.5
    play sound SFX_Sweep
    pause 1
    scene bg-fbapartment
    with sflash
    
    play music AMB_Fire fadein 1.0

    pause 1.5

    play sound SFX_Idea
    d "{=txt_vo}(This can’t be!)" with sflash

    ex_fire "Wait, 
    {w=0.5}Sir! 
    {w=0.5}It’s dangerous!"

    play sound SFX_Smack
    d "An officer is still inside! 
    {w=0.5}We need to get him out!" with sshake

    ex_officer "The firefighters are doing it right now, 
    {w=0.5}Sir! 
    {w=0.5}You’re getting in their way!"

    play sound SFX_Smack
    d "Get out of my way!" with sshake

    play sound SFX_Smack
    d "Dang it! 
    {w=0.5}This can’t be!" with sshake

    #SFX - Loud Fire Roar

    d "No- 
    {w=0.5}Carlo!"
    window hide

    stop music fadeout 1.0

    #END OF FLASHBACK

    pause 0.5
    play sound SFX_Sweep
    pause 1.0

    scene bg-dyoffice
    show dy - sad
    with sflash

    window show
    d "I haven’t seen him since, 
    {w=0.5}and the police for whatever reason don't seem to want to investigate any further of the matter{cps=*0.5}...{/cps}"
    window hide

    pause 0.5

    show dy - neutral
    with dissolve
    play music BGM_tektiv
    pause 0.5
    window show
    d "In any case this is why I don’t want other people to hang around during any of my cases."

    MC "What about Azzi?"
    
    show dy - confused
    with dissolve

    d "Azzi he- 
    {w=0.5}He’s more of a special case. 
    {w=0.5}As much as I’d want him to stay away for his safety, 
    {w=0.5}He forced it upon himself to be my Assistant."
    
    show dy - annoyed
    with dissolve

    d "I have no choice in the matter. 
    {w=0.5}I just gotta be careful with him."

    MC "{=txt_vo}(Detective Dy went through a lot, 
    {w=0.5}huh. 
    {w=0.5}Years went by but it’s obvious he hasn’t forgotten about what happened. 
    {w=0.5}So that’s why he acts that way towards Azzi; 
    {w=0.5}he’s afraid it might happen again.)"

    MC "So this Case, 
    {w=0.5}What was it about?"

    d "{cps=*0.5}...{/cps} 
    {w=0.5}Well-"
    window hide

    stop music fadeout 1.0

    pause 0.5

    play sound SFX_door2
    with sshake

    pause 1.0

    
    show dy surprised at left
    show azzi - neutral at right
    play sound SFX_Smack
    play music BGM_azzi
    azzi "Boss!- 
    {w=0.5}Oh hey, 
    {w=0.5}Max!" with sflash

    show dy - angry
    play sound SFX_Smack
    d "Where have you been??" with sshake

    show azzi - happy
    show dy surprised
    play sound SFX_Idea
    azzi "I got the blood results! 
    {w=0.5}I haven’t opened it yet." with sflash

    show dy - angry
    with dissolve

    window show
    d "Give me that."
    window hide

    pause 0.5

    play sound "audio/SFX_actionmenu_show_2.wav"
    with sshake

    pause 0.5


    show azzi - neutral
    with dissolve

    window show
    azzi "It’s not a match!"

    show dy - thinking
    with dissolve

    d "I actually speculated from the start that the blood wasn’t from Auntie Cheng."
    
    show azzi - smug
    with dissolve

    azzi "I also had the blood cross-checked if it was Max’s-"

    show azzi - confused
    play sound SFX_Idea
    MC "See! 
    {w=0.5}I told you I’m not the culprit!" with sflash

    show azzi - confused
    with dissolve

    azzi "Max, 
    {w=0.5}it’s not yours or your{nw}"
    play sound SFX_Foreshadow
    extend " aunt’s blood."

    MC "What a spectacular observation,{w=0.5}{nw}"
    play sound SFX_Smack
    extend " Azzi!" with sshake

    show azzi - sad
    with dissolve

    azzi "Max, 
    {w=0.5}I’m sorry I suspected you."

    MC "*Sigh* 
    {w=0.5}It’s aight."
    window hide

    show black
    with dissolve
    stop music fadeout 1.0

    pause 0.5

    show azzi - neutral
    show dy - neutral
    hide black
    with dissolve

    pause 0.5


    pause 0.5

    window show
    play music BGM_thinking
    azzi "So, 
    {w=0.5}what’s the next step? 
    {w=0.5}I suggest that we should cross check the blood with everyone living in the town."

    show dy - thinking 
    with dissolve

    d "No no, 
    {w=0.5}there’s too many people in the town and having everyone tested would cost too much. 
    {w=0.5}We should go back to the crime scene and look for more clues."
    
    show dy - neutral 
    with dissolve

    d "Unfortunately we weren’t able to investigate everything at your house Max."

    MC "What do you mean?"

    d "Your room was locked. We couldn’t get in. 
    {w=0.5}We definitely didn’t want to break your door down. 
    {w=0.5}And Hey! 
    {w=0.5}I actually called you after you left the hospital. 
    {w=0.5}Maybe you should pick up your phone once in a while"

    MC "What? 
    {w=0.5}But I don’t usually lock my door when I go out. 
    {w=0.5}I especially don’t recall locking my door when I went out that day."

    MC "And I was probably fast asleep when you called."
    
    show dy - thinking 
    with dissolve

    d "Anywho, 
    {w=0.5}we need you to unlock that later when we go back to your house. 
    {w=0.5}You have a key right?"

    MC "Key?{cps=*0.15}...{/cps} 
    {w=0.5}Darn I don’t have one! I just came back to my house, 
    {w=0.5}remember?"

    show dy - confused 
    with dissolve

    d "Are you serious? 
    {w=0.5}But if you just came back. 
    {w=0.5}How’d you get into your house in the first place?"

    MC "If you recall, 
    {w=0.5}my Aunt is really a ”Pro” when locking stuff. 
    {w=0.5}She forgot to lock the doors and left it like that for 2 weeks while she wasn’t home."

    show dy - annoyed
    with dissolve

    d "{cps=*0.15}...{/cps} 
    {w=0.5}That’s uhhh something. 
    {w=0.5}Tchh{cps=*0.15}...{/cps} Is there anyway for us to get to your room though?"
    window hide

    #FLASHBACK SCENE FROM 2 DAYS AGO BEDROOM SCENE:
    pause 0.5
    play sound SFX_Sweep
    pause 1

    scene bg-intmaxbedroomnightpast
    show chengpast - neutral
    with sflash

    pause 0.5

    window show
    side_cheng "I just wanted to let you know since you’re gonna be here for a while, 
    {w=0.5}I’ve finished cleaning."

    side_cheng "All the dishes, 
    {w=0.5}cooking tools, 
    {w=0.5}utensils are in the cupboards and cabinets in the kitchen."

    side_cheng "Fresh sheets are in the closet by the living room hallway, 
    {w=0.5}and spare keys for the house are in the small {=hl}safebox{/hl} in the living room."
    window hide

    pause 0.5
    play sound SFX_Sweep
    pause 1

    scene bg-dyoffice
    show dy - confused at left
    show azzi - confused at right
    with sflash
    
    pause 0.5
    
    window show
    MC "Now that you’ve mentioned. 
    {w=0.5}Auntie Cheng actually said something a few days ago."

    show dy - neutral
    with dissolve
    
    d "Oh really? 
    {w=0.5}What was it?"

    MC "There’s a Safebox in the living room with spare keys in it. 
    {w=0.5}It should have the keys to my room."

    show dy - smug
    with dissolve

    d "Well that’s great, 
    {w=0.5}we should head there now."

    MC "Alright!"
    window hide

    pause 0.5

    stop music fadeout 1.0

    scene black
    with fade
    
    jump story_ch_02_investigation

label story_ch_02_contd:

#SCENE 1 : DIKUMAKAIN KARINDERIA - JUNE 16, 1992. 3:25 P.M.
    scene bg-intdikumakain
    with fade
    pause 1.0

    $ Dodong = "Dodong"

    window show
    sys_nar "{cps=30}DIKUMAKAIN KARINDERIA - JUNE 16, 1992. 3:25 P.M.{/cps}"
    window hide
    
    pause 1.0

    play music BGM_palengcare

    show dodong - happy at offscreenleft
    show dy - angry at left
    show azzi - confused at right
    with dissolve

    play sound SFX_eating
    d "*CHOMP* *CHOMP* *CHOMP*" with sshake

    play sound SFX_eating
    d "*GOBBLE* *GOBBLE* *GOBBLE*" with sshake

    play sound SFX_eating
    d "*CHOMP* *CHOMP* *CHOMP*" with sshake

    play sound SFX_eating
    d "*GLOMP* *GLOMP* *GLOMP*" with sshake

    play sound SFX_Idea
    MC "Wow. 
    {w=0.5}Inspector, 
    {w=0.5}you’re just wolfing down your food at mach speed." with sflash

    MC "You should probably pause and take a breather, 
    {w=0.5}or else you’ll choke on your food."

    show dy - smug
    play sound SFX_Mystery
    d "Ermph north ghonna chorke on my mphood!" with sshake

    MC "What? 
    {w=0.5}{=txt_vo}(I can’t understand what he saying when he’s stuffing his mouth like this)"

    azzi "Don’t mind him, 
    {w=0.5}Max. 
    {w=0.5}He’s like this when he’s {=hl}stressed.{/=hl}"

    MC "Errr{cps=*0.5}...{/cps} 
    {w=0.5}Ok then, 
    {w=0.5}I’ll take your word for it."
    window hide
    pause 0.5

    show azzi at offscreenright
    show dy at right
    show dodong - happy at left
    with decay10inleft

    pause 0.5

    window show
    play sound SFX_Smack
    side_dodong "Hey guys! 
    {w=0.5}Inspector, 
    {w=0.5}here’s your third platter of {=hl}chicken fried rice{/=hl} you ordered." with sshake

    show dodong - neutral
    with dissolve

    side_dodong "Also brought you some baked goods, 
    {w=0.5}on the house since you’ve been such a great customer!"
    window hide
    pause 0.5

    show dy - happy
    with dissolve

    show azzi at right
    show dy at left
    show dodong at offscreenleft
    with decay10inleft

    pause 0.5

    window show
    azzi "Hey, 
    {w=0.5}maybe you should actually slow down this time inspector. 
    {w=0.5}You’re gonna get a stomach ache later due to indigestion."

    show dy - smug
    play sound SFX_gulp
    d "*GULP* 
    {w=0.5}Ahhhh{cps=*0.5}...{/cps} 
    {w=0.5}Phew, 
    {w=0.5}Dodong’s cooking man, 
    {w=0.5}it’s really on a league of its own." with sshake

    show dy - annoyed
    with dissolve

    d "Ughhh{cps=*0.5}...{/cps} 
    {w=0.5}Today was disappointing. 
    {w=0.5}Just when we finally have some sort of lead to this case."

    show azzi - sad
    with dissolve

    azzi "{cps=*0.5}...{/cps}"

    azzi "I’m sorry, 
    {w=0.5}if I weren’t so clumsy earlier, 
    {w=0.5}we wouldn’t have gotten kicked out."

    show dy - neutral
    with dissolve

    d "Oh well, 
    {w=0.5}next time just be a little careful when looking around."

    show azzi - confused
    with dissolve

    azzi "I understand."

    show dy - smug
    with dissolve

    d "I’ll be right back. 
    {w=0.5}I'll just get a last order in."

    MC "{cps=*0.5}...{/cps}Ok inspector."
    window hide

    pause 0.5

    show dy at offscreenleft
    show azzi at center
    with decay10inleft

    pause 0.5

    window show
    MC "{=txt_vo}(How much can this guy eat?)"

    show azzi - neutral
    with dissolve

    azzi "Also Max, 
    {w=0.5}you said that the {=hl}guy{/=hl} from earlier gave you that {=hl}bruise{/hl} on your eye. 
    {w=0.5}So what’s the story behind that?"

    play sound SFX_Idea
    MC "What? 
    {w=0.5}Oh, 
    {w=0.5}this. 
    {w=0.5}To be honest, 
    {w=0.5}I have no idea. 
    {w=0.5}When I bumped into him the other day he just went full agro on me." with sflash

    MC "I’m pretty sure I didn’t do anything offensive to him. 
    {w=0.5}I merely stepped in to defend Dodong."

    show azzi - confused
    with dissolve

    azzi "Wow, 
    {w=0.5}talk about anger issues."

    MC "What puzzles me however, 
    {w=0.5}is that he seems to know me. 
    {w=0.5}I don’t know him, 
    {w=0.5}at least as far as I can recall, 
    {w=0.5}anyway."

    MC "{=txt_vo}(Did I ever encounter him before? 
    {w=0.5}Thinking about it makes me unsure about my own memory)"

    show azzi - angry
    with dissolve

    azzi "That sure is weird."

    show azzi - confused
    play sound SFX_Idea
    d "I’m pretty sure that’s just Jobert’s default attitude" with sflash
    window hide

    pause 0.5

    show dy - neutral at left
    show azzi at right
    with decay10inleft

    pause 0.5
    
    window show
    MC "Huh? 
    {w=0.5}What do you mean inspector?"

    d "We’ve received a couple of complaints against him in the past years. 
    {w=0.5}He’s always making trouble wherever he goes. 
    {w=0.5}It’s not surprising if he went agro on you when you encountered him."

    show dy - annoyed
    with dissolve

    d "Not to mention he was drunk. 
    {w=0.5}It’s even worse when he gets intoxicated."

    azzi "Now that you mentioned it, 
    {w=0.5}I’ve seen his name before on our records."

    show dy - thinking
    with dissolve

    d "Let’s say he’s been locked up for loitering a few times."

    show dy - surprised
    play sound SFX_Mystery
    side_dodong "In my opinion he should be locked up for {=hl}longer.{/=hl}" with sflash

    d "Dodong?"
    window hide
    pause 0.5

    show azzi at offscreenright
    show dy at right
    show dodong - happy at left
    with decay10inleft

    pause 0.5

    window show
    side_dodong "Here’s your order inspector. 
    {w=0.5}Sorry for eavesdropping. 
    {w=0.5}I heard Jobert’s name and I couldn’t help but listen in."

    show dy - happy
    with dissolve

    d "Thank you Dodong! 
    {w=0.5}And believe me, 
    {w=0.5}I agree with you Dodong, 
    {w=0.5}he should be serving more time for causing trouble around these parts."
    
    show dy - neutral
    with dissolve

    show dodong - confused
    with dissolve

    side_dodong "So what’s the deal, 
    {w=0.5}did he cause trouble for you guys?"

    MC "Kind of."
    
    show azzi at right
    show dy at left
    show dodong at offscreenleft
    with decay10inleft

    azzi "He’s kinda involved with the Mrs. Malano’s case. 
    {w=0.5}We don’t have definitive proof yet but he is one of our leads."

    show azzi at offscreenright
    show dy at right
    show dodong - surprised at left
    with decay10inleft

    side_dodong "Wait,{w=0.5}{nw}"
    play sound SFX_Smack 
    extend " what!? 
    {w=0.5}So you’re telling me he’s got something to do with the whole break in?" with sshake
    window hide

    play sound SFX_Idea
    scene black
    show jobert - pleased
    with sflash

    pause 0.5

    scene bg-intdikumakain
    show dodong - sad at left
    show dy - neutral at right
    show azzi - angry at offscreenright
    with sflash
    #FADE TO BLACK
    pause 0.5
    #FADE BACK IN
    window show
    show dodong - angry
    play sound SFX_Smack 
    side_dodong "That bastard! 
    {w=0.5}Of course, 
    {w=0.5}he would be involved in stirring trouble." with sshake

    show dy - thinking
    with dissolve

    d "We don’t know yet for sure since we don’t have his statement yet but we’re surely at an impasse here."

    show dodong - sad
    with dissolve

    side_dodong "Sorry to hear that."

    show dy - annoyed
    with dissolve

    d "We don’t even have anyone who can tell us about him anyway. 
    {w=0.5}He doesn’t have that many friends nor his family around to give us information."

    show dodong - thinking
    with dissolve

    side_dodong "Hmmm{cps=*0.5}...{/cps} 
    {w=0.5}actually."

    MC "What are you thinking of Dodong?"

    show dodong - surprised
    play sound SFX_Idea
    side_dodong "There might be {=hl}someone{/=hl} who knows a thing or two about Jobert." with sflash 

    show dy - surprised
    play sound SFX_Smack
    d "Wait there is?" with sshake

    show dodong - angry
    with dissolve

    side_dodong "Yeah, 
    {w=0.5}{=hl}his drinking buddy.{/=hl} 
    {w=0.5}That’s the only time he doesn’t cause much trouble when he drinks here. 
    {w=0.5}It’s when he’s with that friend of his."

    show azzi - angry at right
    show dy at offscreenright
    with decay10inleft

    azzi "Well who’s this friend?"

    show dodong - sad
    with dissolve

    side_dodong "The problem is, 
    {w=0.5}this friend is also somewhat hard to deal with."

    show azzi - confused
    with dissolve

    azzi "Can we get a name?"

    show dodong - angry
    with dissolve

    side_dodong "It’s {=hl}Mr. Albert Ventura{/=hl}. 
    {w=0.5}I think you all know him as {=hl}Berto.{/=hl}"
    window hide

    play sound SFX_Mystery
    scene black
    show berto - neutral
    with sflash

    pause 0.5

    scene bg-intdikumakain
    show dodong - sad at left
    show dy - neutral at offscreenright
    show azzi - confused at right
    with sflash
    pause 0.5
    
    window show
    MC "That old coot!?"

    MC "{=txt_vo}(Uggghhh{cps=*0.5}...{/cps} 
    {w=0.5}The thought of us talking to him is something I despise.)"

    show azzi at right
    show dy at left
    show dodong at offscreenleft
    with decay10inleft
    
    d "Do you know Mr. Ventura, 
    {w=0.5}Max?"

    MC "Kind of. 
    {w=0.5}He used to be my dad’s Sabong buddy. 
    {w=0.5}Ever since we’ve moved away however, 
    {w=0.5}he became really {=hl}cold{/=hl} towards us. 
    {w=0.5}He’s been bitter ever since"

    MC "He lives just next to my house."

    show dy - smug
    play sound SFX_Idea

    d "Great! I think we should go and visit this Mr. Ventura. 
    {w=0.5}He might be able to help us deal with Jobert." with sflash

    MC "I’ll let you know now that Dodong’s right. 
    {w=0.5}He’s a bit difficult to talk to. 
    {w=0.5}He’s always so rude."

    show dy - neutral
    with dissolve

    d "No worries, 
    {w=0.5}I’m sure we can reason out with him somehow."   
    window hide

    stop music fadeout 1.0

    pause 0.5

    window show
    d "{cps=*0.5}...{/cps}"
    window hide

    pause 0.5

    window show
    d "Now that we’re getting some productive stuff here,{w=0.5}{nw}"
    show dy - smug
    play sound SFX_Mystery
    extend " maybe I have room for another serving or two. 
    {w=0.5}Dodong!" with sflash
    
    show azzi at offscreenright
    show dy at right
    show dodong at left
    with decay10inleft

    play sound SFX_Idea
    side_dodong "Right on it sir!" with sflash

    show azzi at right
    show dy at left
    show dodong - happy at offscreenleft
    with decay10inleft

    play sound SFX_Smack
    MC "Inspector!" with sshake
    window hide
    #FADE TO BLACK
    scene black
    with fade

    window show
    MC "{=txt_vo}(Inspector’s appetite was another {=hl}mystery{/=hl} we’ve encountered today)"

    MC "{=txt_vo}(Who knew someone could order that many. 
    {w=0.5}Forget that he said  he’d order one or two more servings. 
    {w=0.5}He went on and ordered more than that, and even one for take out!)"

    MC "(Anyways we decided to go pay Mr. Berto a visit after a fun time at Dikumakain. 
    {w=0.5}Not something I’m looking forward to)"
    window hide

    pause 0.5

#SCENE 2 : EXT. BARANGAY STREET DIMAHAMPAK - JUNE 16, 1992. 3:50 P.M.

    scene bg-outsidemaxhouse
    with fade
    pause 1.0

    $ Dodong = "Dodong"

    window show
    sys_nar "{cps=30}EXT. BARANGAY STREET DIMAHAMPAK - JUNE 16, 1992. 3:50 P.M.{/cps}"
    window hide
    

    play music AMB_nature

    pause 1.0

    show dy - neutral at offscreenleft
    show azzi - confused
    show berto - neutral at offscreenright
    with dissolve

    window show
    MC "Hmmm{cps=*0.5}...{/cps} 
    {w=0.5}I don’t see Mr. Berto around. 
    {w=0.5}He’s usually sweeping around and sulking."

    azzi "Wait max I think that’s him. 
    {w=0.5}Over there in the distance."
    window hide

    pause 0.5

    show azzi at offscreenleft
    show berto at center
    with decay10inleft
    play sound SFX_Mystery
    pause 1.5

    show azzi at right
    show dy at left
    show berto at offscreenright
    with decay10inleft
    #SHOW BERTO AT SIDE
    pause 0.5

    window show
    d "Alright, 
    {w=0.5}I’ll handle this."

    d "Good Afternoon, 
    {w=0.5}Manong Berto{cps=*0.5}...{/cps}"
    window hide

    pause 0.5

    show dy - annoyed
    with dissolve
    
    pause 0.5

    window show
    MC "{=txt_vo}(Manong Berto seems occupied while sweeping the fallen leaves)"

    show azzi - happy
    show dy - surprised
    play sound SFX_Smack
    stop music fadeout 0.2
    azzi "Excuse me, 
    {w=0.5}Manong Berto!!" with sshake

    play sound SFX_Idea
    MC "{=txt_vo}(Berto is startled, 
    {w=0.5}Oh no…)" with sflash

    show berto - angry at center
    show azzi at offscreenleft
    show dy at offscreenleft
    play music BGM_uneasy
    play sound SFX_Smack
    side_berto "What the- 
    {w=0.5}Why are you shouting kid!? 
    {w=0.5}What do you want?" with sshake

    show dy - annoyed at left
    show azzi - neutral at right
    show berto at offscreenright
    with decay10inleft

    d"Uhm sorry about that Manong Berto, 
    {w=0.5}we’re here to ask you some questions about Jobert."
    window hide

    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    
    window show
    side_berto "Why what about him-"
    
    show berto - angry
    play sound SFX_Smack

    side_berto "What in the heck are you doing here?" with sshake
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "Oh, 
    {w=0.5}they are currently both my colleagues. 
    {w=0.5}Max works for me, 
    {w=0.5}Sir- 
    {w=0.5}Don’t mind him."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    play sound SFX_Smack
    side_berto "Hmph! 
    {w=0.5}Can’t you see I’m busy here. 
    {w=0.5}So, 
    {w=0.5}what do you want from me?" with sshake

    MC "{=txt_vo}(Busy as in sweeping an obviously clean road.)"
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "We’re here because we need to talk to someone. 
    {w=0.5}And that “{=hl}Someone{/=hl}” maybe is someone you know."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - neutral at center
    with decay10inleft
    window show
    side_berto "You lost me there mister."
    window hide
    show dy - neutral at left
    show azzi - smug at right
    show berto at offscreenright
    with decay10inleft
    window show
    azzi "We’re here to ask about Jobert. 
    {w=0.5}We’ve been trying to talk to him but he keeps shutting us out."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto at center
    with decay10inleft
    window show
    side_berto "Ha! 
    {w=0.5}Serves you right. 
    {w=0.5}If that rascal’s decided not to deal with you folks, 
    {w=0.5}then you’re all outta luck."
    window hide
    show dy - confused at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "What do you mean?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - neutral at center
    with decay10inleft
    window show
    side_berto "If he doesn’t want to talk to you then he won’t give you the time of day."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    azzi "But surely, 
    {w=0.5}there’s some way to convince him to talk to us, 
    {w=0.5}is there Mr. Ventura?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto at center
    with decay10inleft
    window show
    side_berto "What do you want me to do, 
    {w=0.5}go to him and ask reeeeaaaaalll nice like with puppy dog eyes?"
    window hide
    show dy - annoyed at left
    show azzi - happy at right
    show berto at offscreenright
    with decay10inleft
    window show
    azzi "I mean it wouldn’t hurt to try, 
    {w=0.5}Mr. Ventura."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "Sure be my guest{cps=*0.5}...{/cps} 
    {w=0.5}Would be something you want to hear right?"
    show berto - neutral
    with dissolve
    side_berto "Look here kid. 
    {w=0.5}Don’t paint me as a fool. 
    {w=0.5}I don’t have the time of day, 
    {w=0.5}let alone to deal with that fella."
    show berto - annoyed
    with dissolve
    side_berto "I’m sure you folks have some better ideas than come to me for this business of yours?"
    window hide
    show dy - annoyed at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "{cps=*0.5}...{/cps}"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - neutral at center
    with decay10inleft
    window show
    side_berto "Is that all? 
    {w=0.5}Well thank you for bothering my fine afternoon gentlemen!"

    MC "{=txt_vo}(Oh no looks like Mr. Berto is already tired of talking to us. 
    {w=0.5}I gotta think of something.)"

    stop music fadeout 0.5

    MC "{cps=*0.5}...{/cps}"

    MC "Wait,{w=0.5}{nw}" 
    play sound SFX_Idea
    extend " Mr. Berto!" with sflash
    show berto - angry
    play sound SFX_Smack
    side_berto "What is it now kid? 
    {w=0.5}If you haven’t taken the hint yet-" with sshake

    MC "You’re friends with Jobert right? 
    {w=0.5}We just want to know more about him. 
    {w=0.5}It’s really important."
    play sound SFX_Foreshadow
    MC "{=hl}Something happened{/=hl} to my Aunt Cheng. 
    {w=0.5}We have a reason to believe that Jobert has something to do with it."

    MC "And until we can get him to talk, 
    {w=0.5}we wouldn’t know for sure."

    show berto - neutral
    with dissolve
    side_berto "{=hl}Mrs. Malano{/=hl}?"
    show berto - sad
    with dissolve
    side_berto "{cps=*0.5}...{/cps}"
    show berto - annoyed
    with dissolve
    play music BGM_smug
    side_berto "Sigh{cps=*0.5}...{/cps} 
    {w=0.5}Fine, 
    {w=0.5}I’ll answer your questions."
    show berto - neutral
    with dissolve
    side_berto "err{cps=*0.5}...{/cps} 
    {w=0.5}well yeah. 
    {w=0.5}Can’t say he’s a bad guy, 
    {w=0.5}but also I couldn’t say he’s a good guy either."

    MC "{=txt_vo}(Great, 
    {w=0.5}I think I’m getting somewhere. 
    {w=0.5}I’ll just need to be careful not to make him annoyed by questions)"

    menu:
        MC "{fast}{=txt_vo}(Great, 
        I think I’m getting somewhere. 
        I’ll just need to be careful not to make him annoyed by questions)"
        #Q1 (GOOD)
        "Is he a good drinking friend?":
            jump ch_02_berto_Q1
        "How does Jobert treat you?":
            jump ch_02_berto_Q2
        "Where were you yesterday?":
            jump ch_02_berto_Q3