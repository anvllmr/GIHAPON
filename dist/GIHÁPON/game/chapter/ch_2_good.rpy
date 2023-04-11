label ch_02_good:

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
    d "We just wanted to talk peacefully."
    window hide

    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - angry at center
    with decay10inleft

    window show
    side_jobert "You will get{nw}"
    play sound SFX_Smack
    extend " nothing from me." with sshake

    MC "We just wanted to ask for some information since you’re near our house."

    side_jobert "Again, 
    {w=0.5}you will get nothing from me."

    MC "The more you deny it the more we will suspect you."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft
    window show
    d "Max{cps=*0.5}...{/cps}"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - confused at center
    with decay10inleft
    window show
    side_jobert "Just because I was near your house I have something to do with what happened to your Aunt."
    
    show jobert - angry
    play sound SFX_Smack
    side_jobert "Can you please stop involving me with whatever your cases are? 
    {w=0.5}I’m so done with those!" with sshake
    window hide
    show dy - confused at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft
    window show
    d "Sir, 
    {w=0.5}calm down. 
    {w=0.5}We just wanted some information. 
    {w=0.5}Also, 
    {w=0.5}we saw blood trails leading towards your house and we’re curious why there are so many of them."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - surprised at center
    with decay10inleft
    window show
    side_jobert "I-I don’t know! 
    {w=0.5}M-Maybe it’s from some animal fighting around my house."

    MC "{=txt_vo}(His eyes are jittering and he’s stuttering his words. 
    {w=0.5}It’s like he’s looking for answers)"
    window hide
    show dy - neutral at left
    show azzi - angry at right
    show jobert at offscreenright
    with decay10inleft
    window show
    azzi "Do you think we’ll believe that kind of reasoning? 
    {w=0.5}Even a child would know that’s an excuse."
    
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - angry at center
    with decay10inleft
    window show
    play sound SFX_Smack
    side_jobert "Fine! 
    {w=0.5}Then don’t believe me! 
    {w=0.5}I don’t care about you people! 
    {w=0.5}Go away because I don’t know anything and you’ll just waste your time badgering me with these questions." with sshake

    #SFX *was about to shut the door*

    MC "{=txt_vo}(This isn't a good start. 
    {w=0.5}It looks like he’s about to shut us out again. 
    {w=0.5}I should think of something to do.) "

    MC "{=txt_vo}(Should we talk calmly? 
    {w=0.5}Or should we talk aggressively?)"

    menu:
        MC "{=txt_vo}(Should we talk calmly? Or should we talk aggressively?)"
        "Talk Calmly":
            window hide
            pause 0.5
            window show
            play sound SFX_Idea
            MC "Hey, 
            {w=0.5}Jobert! 
            {w=0.5}I know we’re not on good terms but we really need information." with sflash

            MC "We assure you that you are not a suspect in this case. 
            {w=0.5}You may be a witness."

            MC "We just want to know about the blood trails leading towards your house."
            window hide
            show dy - neutral at left
            show azzi - confused at right
            show jobert at offscreenright
            with decay10inleft
            window show
            azzi "Yes, 
            {w=0.5}we just need to identify who it belongs to."
            window hide
            show dy at offscreenleft
            show azzi at offscreenleft
            show jobert - sad at center
            with decay10inleft
            window show
            side_jobert "Uhm{cps=*0.5}...{/cps}"
            window hide
            show dy - angry at left
            show azzi - confused at right
            show jobert at offscreenright
            with decay10inleft
            window show
            d "You smell like alcohol, 
            {w=0.5}have you been drinking?"
            window hide
            show dy at offscreenleft
            show azzi at offscreenleft
            show jobert - angry at center
            play sound SFX_Smack
            side_jobert "N-no I haven’t!" with sshake
            window hide
            show dy - neutral at left
            show azzi - smug at right
            show jobert at offscreenright
            with decay10inleft
            window show
            azzi "Weh! 
            {w=0.5}You smell like Blue Horse- 
            {w=0.5}and you literally look hungover."
            window hide
            show dy at offscreenleft
            show azzi at offscreenleft
            show jobert - angry at center
            play sound SFX_Smack
            side_jobert "You little-" with sshake
            window hide

            play sound SFX_Gleam
            hide jobert with sflash

            pause 0.5

            play sound SFX_clothruffle
            with sshake

            pause 0.5

            window show
            play sound SFX_Idea
            azzi "Whoa!" with sflash
            window hide
            
            pause 0.5

            play sound SFX_glassbreak
            #SFX *attacks Azzi*
            pause 0.5
            show jobert - neutral at offscreenright
            window show
            MC "{=txt_vo}(Azzi dodges making jobert hit a side table with a picture frame. 
            {w=0.5}The picture falls, 
            {w=0.5}making the glass shatter.)"
            window hide
            show dy - angry at left
            show azzi - angry at right
            with decay10inleft
            window show
            d "Who is this?"

            MC "It’s your wife isn’t, 
            {w=0.5}Jobert?"
            window hide
            show dy at offscreenleft
            show azzi at offscreenleft
            show jobert - surprised at center
            with decay10inleft
            window show
            side_jobert "Wha- 
            {w=0.5}How did you know it was my wife?"

        "Talk Aggressively":
            window hide
            pause 0.5
            window show
            play sound SFX_Idea
            MC "Tell us about the blood trails first! 
            {w=0.5}This interrogation won’t go anywhere if you keep changing the topic! 
            {w=0.5}Because of these, 
            {w=0.5}you may end up as a suspect." with sflash

            MC "May I remind you, 
            {w=0.5}these blood trails lead to your house Jobert!"
            show jobert - angry
            play sound SFX_Smack
            side_jobert "Shut up!*" with sshake
            window hide
            pause 0.5
            play sound SFX_Woosh
            with sflash
            pause 0.5
            play sound SFX_crash
            pause 0.5
            
            show dy - angry at left
            show azzi - angry at right
            show jobert at offscreenright
            with decay10inleft
            window show
            play sound SFX_Smack
            d "What the- 
            {w=0.5}What was that for!?" with sshake
            window hide
            show dy at offscreenleft
            show azzi at offscreenleft
            show jobert - angry at center
            play sound SFX_Smack
            side_jobert "Leave! 
            {w=0.5}All of you!" with sshake

            MC "Just answer the question! 
            {w=0.5}Jobert, 
            {w=0.5}you're making this hard for yourself and everyone else!"

            side_jobert "Why you!"
            window hide

            play sound SFX_Gleam
            hide jobert with sflash

            pause 0.5

            play sound SFX_clothruffle
            with sshake

            pause 0.5

            window show
            play sound SFX_Idea
            MC "Oww!"
            window hide
            
            pause 0.5

            play sound SFX_glassbreak
            show jobert - neutral at offscreenright
            pause 0.5

            show dy - annoyed at left
            show azzi - confused at right
            with decay10inleft
            window show
            azzi "Are you alright?"

            MC "Yeah- 
            {w=0.5}Urg." with sshake

            d "Who is this?"

            MC "It’s his wife. 
            {w=0.5}Ex-wife exactly."

            window hide
            show dy at offscreenleft
            show azzi at offscreenleft
            show jobert - surprised at center
            with decay10inleft
            window show
            side_jobert "Wha- 
            {w=0.5}How did you know it was my wife?"

###---------------------------------------------------------###
    window hide
    pause 0.5
    
    show jobert - sad
    with dissolve
    
    window show
    MC "We went to Berto and he told us about your ex-wife. 
    {w=0.5}It’s what you keep talking about when you’re drunk."
    window hide
    show dy - neutral at left
    show azzi - angry at right
    show jobert at offscreenright
    with decay10inleft
    window show
    azzi "What happened? 
    {w=0.5}Why did she leave you?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - sad at center
    with decay10inleft
    window show

    side_jobert "That darn disappearance. 
    {w=0.5}I was suspected in a case here five years ago; 
    {w=0.5}that’s why my wife left me. 
    {w=0.5}She didn’t believe me that I was wrongly accused!"
    window hide
    show dy - sad at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft
    window show
    d "Jobert, 
    {w=0.5}that won’t happen ever again. 
    {w=0.5}Sorry about your wife leaving you."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - neutral at center
    with decay10inleft
    window show
    side_jobert "*Sigh* 
    {w=0.5}I just don’t want to go back to that situation again."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft
    window show
    d "That’s why we’re asking you for help. 
    {w=0.5}You are not a suspect here, 
    {w=0.5}Jobert."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - sad at center
    with decay10inleft
    window show
    side_jobert "{cps=*0.5}...{/cps}"
    window hide
    show dy - confused at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft
    window show
    d "Jobert?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - neutral at center
    with decay10inleft
    window show

    side_jobert "Okay, 
    {w=0.5}okay, 
    {w=0.5}I’ll tell you what happened here yesterday."

    MC "{=txt_vo}(Finally we’re getting somewhere)"

    side_jobert "I was just minding my own business yesterday. 
    {w=0.5}I was ready to go out and buy some alcohol when I heard loud banging on my door."

    side_jobert "A buddy of mine was calling for help. 
    {w=0.5}When I opened the door, 
    {w=0.5}I saw her there, 
    {w=0.5}her arm was drenched in blood from a cut."

    side_jobert "She didn’t tell me why she was here at my house but she was visibly distressed."

    side_jobert "I wasn’t aware that her blood made a trail from your house. 
    {w=0.5}So please believe me when I tell you I had nothing to do with what happened to your Aunt!"

    MC "Who’s this buddy of yours?"
    show jobert - sad
    with dissolve
    side_jobert "Her name is Maya. 
    {w=0.5}She works at the convenience store by Palengcare Market."

    MC "!"

    MC "{=txt_vo}(Wait a second. 
    {w=0.5}It couldn’t be)"

    window hide

    play sound SFX_Idea
    scene black
    show maya - annoyed
    with sflash

    pause 1.0

    scene bg-intjoberthouse
    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft
    show jobert - neutral at center
    with sflash
    
    pause 0.5

    show dy - thinking at left
    show azzi - confused at right
    show jobert at offscreenright
    with decay10inleft
    window show

    d "Maya who?"

    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show jobert - neutral at center
    with decay10inleft
    window show

    side_jobert "Maya Pula. 
    {w=0.5}She’s a good person, 
    {w=0.5}Detective. 
    {w=0.5}I’m sure whatever happened, 
    {w=0.5}there was something behind it." 
    window hide
    stop music fadeout 1.0
    pause 1.0
    hide jobert
    with dissolve
    pause 0.5
    
    show dy - neutral at left
    show azzi - confused at right
    with decay10inleft

    window show
    d "Thanks, 
    {w=0.5}Jobert."
    window hide

    pause 0.5

    window show
    d "Hmmmm{cps=*0.5}...{/cps} 
    {w=0.5}Looks like we need to pay Maya a visit."

    MC "I’m pretty sure I’ve met her before. 
    {w=0.5}We should check out the convenience store."
    window hide

    pause 0.5

#CONVENIENCE STORE - JUNE 16, 1992. 5:05 P.M.
    $ Maya = "Maya"
    
    scene bg-conveniencestore
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}CONVENIENCE STORE - JUNE 16, 1992. 5:05 P.M.{/cps}"
    window hide

    pause 1.0
    
    show dy - neutral at left
    show azzi - neutral at right
    with dissolve

    window show
    d "So is she here?"

    azzi "They said Maya took a day off."

    d "Did you ask where she might be right now?"

    azzi "I actually asked for her address- 
    {w=0.5}here it is."

    MC "Then, 
    {w=0.5}let’s go."
    window hide

    pause 0.5

#EXT. MAYA’S HOUSE - JUNE 16, 1992. 5:30 P.M.
    scene bg-mayahouse
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}MAYA’S HOUSE - JUNE 16, 1992. 5:30 P.M.{/cps}"
    window hide

    play music AMB_nature

    pause 1.0
    
    show dy - neutral at left
    show azzi - neutral at right
    with dissolve

    window show
    azzi "Hello, 
    {w=0.5}anybody home?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    with decay10inleft

    pause 0.5

    play sound SFX_Mystery
    show lola - neutral
    with dissolve

    pause 0.5

    window show

    side_lola "Yes?"
    window hide
    show dy at left
    show azzi - happy at right
    show lola at offscreenright
    with decay10inleft
    window show
    azzi "Good Afternoon, 
    {w=0.5}Po! 
    {w=0.5}Is Maya home right now?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show lola - happy at center
    with decay10inleft
    window show
    side_lola "Are you my Apo’s friends? 
    {w=0.5}Come inside."
    window hide
    show dy at left
    show azzi - confused at right
    show lola at offscreenright
    with decay10inleft
    window show
    stop music fadeout 0.2
    azzi "Uhm-"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show lola - neutral at left
    show maya - angry at right
    play sound SFX_Smack
    play music BGM_smug
    side_maya "Who are you!?" with sshake
    window hide
    show dy at left
    show azzi at right
    show lola at offscreenright
    show maya at offscreenright
    with decay10inleft
    window show
    d "Are you Maya? 
    {w=0.5}We would like to ask you a few questions."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show lola at left
    show maya - annoyed at right
    with decay10inleft
    window show
    side_maya "Lola, 
    {w=0.5}can you go inside? 
    {w=0.5}I’ll talk to them for a bit."

    show lola - sad
    with dissolve

    side_lola "Well alright, 
    {w=0.5}Apo{cps=*0.5}...{/cps}"
    window hide
    hide lola
    with dissolve
    show maya at center
    with decay10inleft
    window show
    MC "{=txt_vo}(What’s that? 
    {w=0.5}You could barely see it but it seems Maya has a bandage under her arm, 
    {w=0.5}hmm{cps=*0.5}...{/cps})"
    
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "Maya, 
    {w=0.5}were you at Montero’s residence yesterday?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya - angry at center
    with decay10inleft
    window show
    side_maya "N-no, 
    {w=0.5}I’m at the convenience store working. 
    {w=0.5}As per usual."

    play sound SFX_Idea
    MC "Then what happened to your arm? 
    {w=0.5}Why do you have a bandage?" with sflash

    show maya - scared
    play sound SFX_Smack

    side_maya "I-I was helping my Lola fix the cabinet yesterday, 
    {w=0.5}that’s where I got a scratch." with sshake

    show maya at right
    show lola - sad at left

    play sound SFX_Smack

    side_lola "What? 
    {w=0.5}No you did not! 
    {w=0.5}You weren’t even here yesterday!" with sshake

    play sound SFX_Smack
    side_maya "Lola! 
    {w=0.5}I told you to get inside!" with sshake

    side_lola "You told me you got that cut from the store? 
    {w=0.5}Where did you really get that, 
    {w=05}Apo?"

    show maya - scared
    play sound SFX_Smack
    side_maya "N-no, 
    {w=0.5}I wasn’t there yesterday, 
    {w=0.5}Lola." with sshake
    window hide
    show dy - confused at left
    show azzi at right
    show lola at offscreenright
    show maya at offscreenright
    with decay10inleft
    window show
    d "You weren’t there yesterday?"

    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show lola at left
    show maya - scared at right
    with decay10inleft
    window show

    side_maya "No- 
    {w=0.5}uhm.. 
    {w=0.5}I mean yes."

    window hide
    show dy - neutral at left
    show azzi at right
    show lola at offscreenright
    show maya at offscreenright
    with decay10inleft
    window show

    d "Maya, 
    {w=0.5}I think you should go with us to the police station."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show lola - neutral at left
    show maya - angry at right
    play sound SFX_Smack
    side_maya "What?! 
    {w=0.5}No! 
    {w=0.5}I don’t want to go there!" with sshake
    
    show lola - sad
    with dissolve

    side_lola "Why what’s wrong, 
    {w=0.5}Officer?"

    show maya - angry
    play sound SFX_Smack
    side_maya "Lola, 
    {w=0.5}nothing’s wrong! 
    {w=0.5}I can’t go to the police station." with sshake

    MC "Why?"

    side_maya "They aren’t going to like it when I’m there."

    MC "They?"
    window hide
    show dy - angry at left
    show azzi - confused at right
    show lola at offscreenright
    show maya at offscreenright
    with decay10inleft
    window show
    d "Does someone not want you to talk?"
    
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show lola at left
    show maya  at right
    with decay10inleft
    window show

    side_lola "Apo, 
    {w=0.5}Just tell them the truth. 
    {w=0.5}You didn’t do anything, 
    {w=0.5}right?"
    window hide
    stop music fadeout 1.0

    pause 1.0

    show maya - scared
    with dissolve

    pause 0.5

    play sound SFX_Run
    hide maya
    with sflash
    pause 0.5
    play sound SFX_Mystery
    #side_maya #SFX Running(Looking Frantic and runs away)
    pause 1.0

    show lola at center
    with decay10inleft

    pause 0.5

    play sound SFX_Smack
    side_lola "Apo! 
    {w=0.5}Can you guys bring her back, 
    {w=0.5}please??" with sshake

    MC "We’ll be right back, 
    {w=0.5}Lola."

#EXT. BARANGAY STREET DIMAKITA - JUNE 16, 1992. 5:45 P.M.
    scene bg-extdikumakainevening
    with fade
    pause 1.5

    window show
    sys_nar "{cps=30}EXT. BARANGAY STREET DIMAKITA - JUNE 16, 1992. 5:45 P.M.{/cps}"
    window hide

    pause 1.0

    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft

    play sound SFX_Smack
    MC "Maya! 
    {w=0.5}Wait a sec- 
    {w=0.5}we just wanted to talk!" with sshake
    window hide

    pause 0.5
    play sound SFX_Mystery
    show maya - angry
    with dissolve
    pause 1.0

    window show
    side_maya "If I told you a thing, 
    {w=0.5}they’ll hurt me and my Lola. 
    {w=0.5}She’s all I got!"
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "Nothing bad is going to happen to you and your Lola."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya - scared at center
    with decay10inleft
    window show
    play sound SFX_Smack
    side_maya "You don’t know them! 
    {w=0.5}You don’t know what they’re capable of!" with sshake
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "Alright,
    {w=0.5}let’s make a deal. 
    {w=0.5}Whoever they are, 
    {w=0.5}I’ll make sure that your Lola is safe no matter what happens if you talk to us right now. 
    {w=0.5}I can assure you that."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya - sad at center
    with decay10inleft
    window show
    side_maya "{cps=*0.5}...{/cps}"
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "Do we have a deal?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya at center
    with decay10inleft
    window show
    side_maya "ok{cps=*0.5}...{/cps}"
    window hide
    show dy - angry at left
    show azzi - confused at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "So, 
    {w=0.5}tell us. 
    {w=0.5}Were you at the Montero’s yesterday?"
    play music BGM_sad
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya at center
    with decay10inleft
    window show
    side_maya "Uhm- 
    {w=0.5}yes{cps=*0.5}...{/cps}"
    window hide
    show dy - neutral at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "Why were you there? 
    {w=0.5}Why did you break in?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya at center
    with decay10inleft
    window show
    side_maya "I’m not sure but they told me they needed that “letter”."
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "So, 
    {w=0.5}did you get it?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya - neutral at center
    with decay10inleft
    window show
    side_maya "Yeah{cps=*0.5}...{/cps}"
    window hide
    show dy - angry at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "So, 
    {w=0.5}where is it now?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya - sad at center
    with decay10inleft
    window show
    side_maya "{cps=*0.5}...{/cps}"
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    d "Who are they?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show maya - sad at center
    with decay10inleft
    window show
    side_maya "(Anxious) The- 
    {w=0.5}the Ba-"
    window hide
    show dy at left
    show azzi at right
    show maya at offscreenright
    with decay10inleft
    window show
    play sound SFX_Foreshadow
    d "{=hl}Balandra’s{/=hl}?" with sshake

    MC "{=txt_vo}(Why is Dy acting weird? 
    {w=0.5}And why Balandra? 
    {w=0.5}What’s the deal with that letter??)"

    show dy - neutral
    with dissolve

    d "I think we should continue this line of questioning at the police station. 
    {w=0.5}Sorry, 
    {w=0.5}Maya but I have to take you into custody for trespassing on a private property and assaulting Mrs. Malano."
    window hide

    stop music fadeout 1.0

    pause 0.5

    jump ch_03_good
    #Jump Chapter 3 Good Route