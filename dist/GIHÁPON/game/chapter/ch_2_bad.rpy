label ch_02_bad:

#EXT. JOBERT’S HOUSE - JUNE 16, 1992. 4:30 P.M.
    #SFX *knocks at the door*
    scene black
    with fade
    pause 0.5
    #SCENE BLACK SCREEN
    play sound SFX_knock
    #SFX KNOCKING   
    pause 1.5

    window show
    play sound SFX_Smack
    side_jobert  "what now?!" with sshake
    window hide

    play sound SFX_door1

    pause 2.5

    scene bg-intjoberthouse
    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}  JOBERT’S HOUSE - JUNE 16, 1992. 4:30 P.M.{/cps}"
    window hide
    
    pause 1.0

    show jobert - angry
    with dissolve
    play music BGM_uneasy

    pause 0.5

    show dy - neutral at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft

    window show
    d "Good afternoon, 
    {w=0.5}Jobert. 
    {w=0.5}We’re just here for a few questions about the incident nearby."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert at center
    with decay10inleft
    window show
    side_jobert "What- 
    {w=0.5}I don’t have time for this-"
    window hide
    pause 0.5
    play sound SFX_door2
    with sshake
    pause 0.5
    window show
    MC "{=txt_vo}(Jobert was about to close the door but Dy stopped it)"
    window hide
    show dy - angry at left
    show azzi at right
    show jobert at offscreenright
    with decay10inleft
    window show
    d "No- 
    {w=0.5}it’s not like that. 
    {w=0.5}You might have witnessed something yesterday, 
    {w=0.5}we just wanted more information."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert at center
    with decay10inleft
    window show
    side_jobert "Look, 
    {w=0.5}I didn’t see anything yesterday; 
    {w=0.5}I have nothing to do with it. 
    {w=0.5}You can ask the other neighbors or whatever."

    MC "Excuse me, 
    {w=0.5}Jobert. 
    {w=0.5}We’ll be frank with you, 
    {w=0.5}the blood trails led us to your house. 
    {w=0.5}You can either help us here right now or you can argue at the police station."
    play sound SFX_Smack
    side_jobert "So, 
    {w=0.5}what are you insinuating!?" with sshake

    MC "Were you at my house yesterday?"
    play sound SFX_Smack
    side_jobert "I wasn’t!" with sshake
    play sound SFX_Idea
    MC "Then I suggest you cooperate with this investigation." with sflash
    play sound SFX_Smack
    side_jobert "SHUT UP!" with sshake


    side_jobert "You know, 
    {w=0.5}you’re pissing me off. 
    {w=0.5}I don’t have anything to do with whatever incident happened yesterday. 
    {w=0.5}All of you just leave!"

    MC "Jobert, 
    {w=0.5}can you-"

    window hide
    stop music fadeout 0.2
    pause 0.5
    
    play sound SFX_Smack
    with ssmack
    
    pause 0.5
    
    window show

    #SFX Punch

    MC "OUCH!"

    #SFX punch
    play sound SFX_Smack
    side_jobert "I said shut up!" with sshake

    show dy - angry at left
    show jobert at right
    with decay10inleft

    d "That’s it.{w=0.5}{nw}"
    play sound SFX_Handcuff
    extend " That’s for assaulting Mr. Montero." with sshake
    show jobert surprised
    play sound SFX_Smack
    side_jobert "What!? 
    {w=0.5}You’re making a mistake here inspector! 
    {w=0.5}I’m not involved in your little incident" with sshake

    d "We’ll be hearing more of your story at the police station"
    window hide
    scene bg-extjoberthouse
    show azzi - neutral at right
    show dy - neutral at left
    with fade

    pause 0.5

    window show
    play sound SFX_Idea
    azzi "Dy! 
    {w=0.5}Max! 
    {w=0.5}Look what I found." with sflash

    window hide
    pause 0.5

    play sound SFX_Mystery
    show item_phone at truecenter
    with irisin

    pause 2.0

    hide item_phone
    with irisout

    pause 0.5

    window show

    play sound SFX_Idea
    MC "Is that Jobert’s phone?" with sflash

    show azzi - angry
    with dissolve

    azzi "Yeah, 
    {w=0.5}but look at the recent text he sent for an unknown number."
    
    window hide
    
    show item_phone at truecenter
    with irisin
    #Azzi shows the text:
    window show
    side_jobert "{=txt_vo}“They went here but I made them go away. 
    {w=0.5}Make sure I don’t get involved in this.”"

    play sound SFX_Foreshadow
    ex_unknown "{=txt_vo}“I’ll make sure to take care of it.”"
    hide item_phone
    with irisout

    pause 0.5

    MC "What does this mean?"

    show dy - thinking
    with dissolve
    d "I’m not really sure yet. 
    {w=0.5}This cryptic text begs a lot of questions.
    {w=0.5}Clearly he’s involved in this somehow."
    show dy - neutral
    with dissolve
    d "I’ll have the phone history checked at the station. 
    {w=0.5}Maybe we’ll find something about that text message."

    MC "Alright."
    window hide

    show black
    with dissolve
    show azzi - neutral
    pause 0.5

    hide black
    with dissolve

    window show
    MC "{cps=*0.5}...{/cps}{w=0.5}{nw}"
    play sound SFX_Idea
    "!" with sflash

    #Screen Flash and SFX idea

    MC "{=txt_vo}(What was that?)"

    show azzi - confused
    with dissolve

    azzi "What is it max?"

    MC "I don’t know but I feel like we’re being{nw}"
    play sound SFX_Omen
    extend" watched"

    show dy - confused
    with dissolve

    d "Hmmm? 
    {w=0.5}I don’t see anyone around though."

    azzi "Probably just the wind."

    MC "{cps=*0.5}...{/cps}"

    MC "So what do we do now, 
    {w=0.5}Inspector?" 

    show dy - neutral
    with dissolve

    d "We’ll have to question Jobert at the detention center. 
    {w=0.5}We’ll try to find some answers to why the blood trails lead to his house."

    MC "So do you think Jobert was the one who broke in?"

    show dy - thinking
    with dissolve

    d "We can’t say for sure yet. 
    {w=0.5}We don’t have definitive proof of whether he was involved."

    show dy - neutral
    with dissolve

    d "One thing to note for sure though, 
    {w=0.5}he doesn’t have a wound."

    show azzi - angry
    with dissolve

    azzi "He doesn’t? 
    {w=0.5}That’s bizarre. 
    {w=0.5}That means there could’ve been more than one who broke in."

    MC "But Auntie Cheng made no remark of a second or third person."

    show dy - thinking
    with dissolve

    d "We’ll get our answers once we can talk to Jobert. 
    {w=0.5}For now we should go and rest. 
    {w=0.5}It’s been a long day."

    show dy - smug
    with dissolve

    d "How bout a visit to Dikumakain once again for dinner!"

    MC "Yeah!"
    window hide

    scene black
    with fade
    pause 0.5
    #SCREEN FADES TO BLACK
    window show
    MC "{=txt_vo}(Finally we have someone who could possibly pinpoint us to the real culprit of the incident.)"

    MC "{=txt_vo}(I should go and visit the Inspector at the detention center tomorrow.)"
    window hide

    pause 0.5

    jump ch_03_bad
    

