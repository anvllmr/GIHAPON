label ch_03_good:

#CHAPTER 3 GOOD ENDING

#INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 17, 1992. 8:00 A.M.
    scene bg-intmaxbedroom
    with fade
    pause 1.0

    $ Wynona = "Wynona"

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 17, 1992. 8:00 A.M.{/cps}"
    window hide
    
    pause 1.0

    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake

    pause 2.0

    play sound SFX_Call3
    pause 0.5
    window show
    MC "Hello?"

    d "Can you visit the police station right now? 
    {w=0.5}We got some information from Maya."

    play sound SFX_Smack
    MC "Really? 
    {w=0.5}Sure, 
    {w=0.5}I’m on my way" with sshake
    window hide 

    #INT. DY’S OFFICE - JUNE 17, 1992. 9:00 A.M.

    scene bg-dyoffice
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}DY’S OFFICE - JUNE 17, 1992. 9:00 A.M.{/cps}"
    window hide
    
    pause 1.0

    show dy - neutral
    with dissolve

    play music BGM_tektiv

    window show
    d "Oh here you are."

    MC "So how’s the interrogation?"
    show dy - confused
    with dissolve
    d "This is yours, 
    {w=0.5}right?"
    window hide
    pause 0.5

    play sound SFX_Mystery
    show item_letter at truecenter
    with irisin

    pause 2.0

    hide item_letter
    with irisout

    pause 0.5

    window show
    MC "{=txt_vo}(It’s the letter){/=txt_vo} Yeah, 
    {w=0.5}thanks. 
    {w=0.5}So what else did she say?"
    window hide
    

    pause 0.5
    play sound SFX_Sweep
    pause 1
    scene bg-dyofficepast
    show mayapast - sad
    with sflash
    #Flashback

    pause 0.5

    window show
    side_maya "I was only forced to do that because they threatened me and my Lola. 
    {w=0.5}I didn’t mean to hurt the woman; 
    {w=0.5}I was panicking to get away because I got caught."

    side_maya "They wanted me to get that “letter” and give it to them in exchange for money and my Lola’s safety. 
    {w=0.5}I couldn’t say no{cps=*0.5}...{/cps}"
    window hide

    pause 0.5
    play sound SFX_Sweep
    pause 1

    scene bg-dyoffice
    show dy - thinking
    with sflash

    pause 0.5
    
    window show
    d "I think we now have a lead."

    MC "So it’s the-"
    window hide
    stop music fadeout 0.5
    pause 0.5

    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake

    pause 2.0

    play sound SFX_Call3
    pause 0.5
    window show

    #Max’s phone rang

    MC "{=txt_vo}(It’s Wynona)"

    MC "Hello?"

    play music BGM_cool
    play sound SFX_Smack
    char_wyn "Hey! 
    {w=0.5}I heard what happened to your Aunt. 
    {w=0.5}Are you guys alright?" with sshake

    MC "Yeah, 
    {w=0.5}she’s at the hospital right now. 
    {w=0.5}Why did you call?"

    char_wyn "Uhm, 
    {w=0.5}you sound tired{cps=*0.5}...{/cps} 
    {w=0.5}I just called maybe if you need help or something{cps=*0.5}...{/cps}"

    MC "We’re fine, 
    {w=0.5}Wynona."

    char_wyn "I heard someone broke in at your house, 
    {w=0.5}did they steal something?"

    MC "Wynona, 
    {w=0.5}I need to go."

    char_wyn "Uhm alright, 
    {w=0.5}take care. 
    {w=0.5}Call me anytime, 
    {w=0.5}okay?"

    MC "Bye, 
    {w=0.5}Wynona."
    window hide
    pause 0.5
    play sound SFX_Call3
    stop music fadeout 1.0
    hide item_phone
    with irisout
    window show
    MC "{=txt_vo}(I should be cautious of them from now on.)"

    MC "Detective, 
    {w=0.5}I’m going somewhere first. 
    {w=0.5}I’ll see you later."
    show dy - neutral
    with dissolve
    d "Sure, 
    {w=0.5}be careful."
    window hide

    pause 0.5

    #Cemetery - JUNE 17, 1992. 11:00 A.M.
    scene bg-cemetery
    with fade
    pause 1.0

    $ Mariano = "Mariano"

    window show
    sys_nar "{cps=30}CEMETERY - JUNE 17, 1992. 11:00 A.M.{/cps}"
    window hide

    play music AMB_nature
    
    pause 1.0

    window show
    MC "Hey, 
    {w=0.5}happy birthday. 
    {w=0.5}Lheona"
    window hide

    pause 0.5
    play music BGM_sad

    window show
    MC "{=txt_vo}(Lheona was my closest friend. 
    {w=0.5}I didn’t know why she became so distant after hanging out with Wynona.)"

    MC "{=txt_vo}(One day, 
    {w=0.5}she went out to meet someone. 
    {w=0.5}I followed her to a secluded part of the river and I tried talking to her about what's going on but it turned into an argument.)"

    MC "{=txt_vo}(If only I didn’t lash out like that, 
    {w=0.5}she wouldn’t fall in that darn river. 
    {w=0.5}I was supposed to help her get out of the water but I felt a sharp pain at the back of my head and I lost consciousness.)"

    MC "{=txt_vo}(I still feel guilty about what happened to her. 
    {w=0.5}I was suspected as the culprit but Lheona’s body was never found.)"

    MC "{=txt_vo}(They didn’t have conclusive evidence to convict me of Lheona’s disappearance. 
    {w=0.5}If only I talked to her calmly and let her explain, 
    {w=0.5}she would still be here.)"
    window hide
    stop music fadeout 1.0
    pause 0.5

    show item_letter at truecenter
    with irisin

    pause 1.5

    play sound SFX_walk
    hide item_letter
    with irisout

    pause 1.0

    show mariano - angry
    with dissolve
    play sound SFX_Mystery

    #Max gets the letter inside his bag and reads it.
    #*Footsteps SFX* A man arrived; it was Mariano.

    window show
    side_mariano "Wh-{w=0.5}{nw}"
    play sound SFX_Smack
    extend "why are you here? 
    {w=0.5}I told you to not show your face to me." with sshake

    MC "I think it’s impossible for us to not meet because we live in the same town."

    play sound SFX_Smack
    side_mariano "Then you shouldn’t visit my sister’s grave again." with sshake

    MC "Lheona is still my friend. 
    {w=0.5}How many times do I have to prove myself that I am not the suspect?"

    play sound SFX_Smack
    side_mariano "Go away you don't deserve to be here." with sshake

    show mariano - thinking
    play sound SFX_Idea
    side_mariano "Wait, 
    {w=0.5}what’s that?" with sflash

    MC "It’s a letter I received a few weeks ago."

    show mariano - neutral
    with dissolve

    side_mariano "From who?"

    MC "I don’t know."
    
    show mariano - thinking
    with dissolve

    side_mariano "Have you read it?"

    MC "Yeah-"

    show mariano - neutral
    with dissolve

    play sound SFX_clothruffle
    with sshake

    side_mariano "Let me see that."
    window hide

    pause 0.5

    show item_letter at halfleft
    with irisin
    #Letter:
    "Max, I know you had nothing to do with Lheona’s disappearance. 
    {w=0.5}I know the truth about what happened five years ago." 
    "Please come back where it all happened. 
    {w=0.5}There’s a chance you might uncover the secrets of this town."
    window hide

    hide item_letter
    with irisout

    pause 0.5
    
    show mariano - angry
    play sound SFX_Smack
    side_mariano "What the- 
    {w=0.5}what does this mean? 
    {w=0.5}Where did it come from?" with sshake

    MC "I don’t have any idea where it came from and who sent it."

    play sound SFX_Smack
    side_mariano "Have you checked at the post office? 
    {w=0.5}Did you even try finding out who sent it?" with sshake

    MC "I’ve been looking for the sender since I got here! 
    {w=0.5}I also wanted to know what really happened to Lheona and who took her." 

    play music BGM_sad

    MC "If only we didn’t argue that day, 
    {w=0.5}we could have avoided that incident. 
    {w=0.5}I’m sorry for what happened to Lheona; 
    {w=0.5}I should’ve protected her."

    show mariano - sad
    with dissolve
    side_mariano "It’s just- I care for Lheona so much. 
    {w=0.5}She’s my sister but I- 
    {w=0.5}couldn’t protect her."

    side_mariano "My parents struggled a lot after Lheona’s disappearance and I couldn’t do anything."

    MC "I know you also struggled that’s why I can’t blame you if you’re mad at me-"

    show mariano - angry
    side_mariano "No- 
    {w=0.5}I actually knew that you’re not the culprit like I can see you’re just a child that time."

    side_mariano "I’m sorry I used you as an excuse for my own faults; 
    {w=0.5}I kept on blaming you for Lheona’s incident when I didn’t even know the truth." with sshake

    MC "That’s alright, 
    {w=0.5}Mariano." 

    MC "Uhm, 
    {w=0.5}I guess I should go."
    window hide

    show mariano - neutral
    with dissolve

    window show 
    side_mariano "Hey, before you go. 
    {w=0.5}I got a picture here of Lheona. 
    {w=0.5}Maybe you should have it."

    MC "{=txt_vo}(This photo, It’s Lheona, 
    {w=0.5}Mariano, 
    {w=0.5}a Man, 
    {w=0.5}and Wynona. 
    {w=0.5}Wait the man with a tiger tattoo)"
    window hide

    stop music fadeout 0.5

    scene black
    with sflash

    pause 0.5
    window show
    play sound SFX_Idea
    MC "That tattoo!" with sflash
    play sound SFX_Omen
    MC "It's the last thing I saw before blacking out during that incident!" 
    window hide

    pause 2.0
    play music BGM_sadmemory
    scene ending
    with fade

    pause 3.0

    scene credits
    with fade

    pause 5.0

    scene black
    with fade

    pause 1.0
    window show
    sys_nar "You've unlocked the Good Ending!"
    sys_nar "Thank you for playing our game!" 
    sys_nar "For evaluation please use {a=https://forms.gle/LrzHUbbRKhyjK4JG8}this link!{/a}. We would appreciate it if you answer!"
    window hide

    pause 1.5

    $ MainMenu(confirm=False)()

    #*Flashback of the exact tattoo* Shows the incident where he saw a glimpse of the tattoo of the man who assaulted max.*

    #*Black screen*

    #Last line
    #“That tattoo… I know who that is”

    #To be continued… aka End!

label ch_03_neutral:

#CHAPTER 3 NEUTRAL ENDING

#INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 17, 1992. 8:00 A.M.
    scene bg-intmaxbedroom
    with fade
    pause 1.0

    $ Wynona = "Wynona"

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 17, 1992. 8:00 A.M.{/cps}"
    window hide
    
    pause 1.0

    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake

    pause 2.0

    play sound SFX_Call3
    pause 0.5
    window show

    MC "Hey, 
    {w=0.5}Detective. 
    {w=0.3}How’s the interrogation going?"

    d "I’m sorry, Max. 
    {w=0.5}We didn’t get anything from Maya. 
    {w=0.5}We can’t confirm the identity of Maya’s employer."

    MC "What? 
    {w=0.5}So what’s gonna happen to Maya?"

    d "We’ll deal with it, 
    {w=0.5}Max. 
    {w=0.5}I’ll contact you soon about Maya’s punishment."

    MC "Alright, 
    {w=0.5}Detective. 
    {w=0.5}I’ll visit Lheona today. 
    {w=0.5}Talk to you soon."

    play sound SFX_Call3
    hide item_phone
    with irisout

    MC "(I guess I need to find something that will make Maya confess all by myself, 
    {w=0.5}but I have to visit Lheona first. 
    {w=0.5}I will certainly find the truth for this.)"

    window hide

    #Cemetery - JUNE 17, 1992. 11:00 A.M.

    scene bg-cemetery
    with fade
    pause 1.0

    $ Mariano = "Mariano"

    window show
    sys_nar "{cps=30}CEMETERY - JUNE 17, 1992. 11:00 A.M.{/cps}"
    window hide

    play music AMB_nature
    
    pause 1.0

    window show
    MC "Hey, 
    {w=0.5}happy birthday. 
    {w=0.5}Lheona"
    window hide

    pause 0.5
    play music BGM_sad

    window show
    MC "{=txt_vo}(Lheona was my closest friend. 
    {w=0.5}I didn’t know why she became so distant after hanging out with Wynona.)"

    MC "{=txt_vo}(One day, 
    {w=0.5}she went out to meet someone. 
    {w=0.5}I followed her to a secluded part of the river and I tried talking to her about what's going on but it turned into an argument.)"

    MC "{=txt_vo}(If only I didn’t lash out like that, 
    {w=0.5}she wouldn’t fall in that darn river. 
    {w=0.5}I was supposed to help her get out of the water but I felt a sharp pain at the back of my head and I lost consciousness.)"

    MC "{=txt_vo}(I still feel guilty about what happened to her. 
    {w=0.5}I was suspected as the culprit but Lheona’s body was never found.)"

    MC "{=txt_vo}(They didn’t have conclusive evidence to convict me of Lheona’s disappearance. 
    {w=0.5}If only I talked to her calmly and let her explain, 
    {w=0.5}she would still be here.)"
    window hide
    stop music fadeout 1.0
    pause 0.5
    play sound SFX_walk
    pause 1.5
    play sound SFX_Mystery
    show jobert - neutral
    with dissolve

    pause 1.0
    #*Footsteps SFX* Jobert arrived.

    play sound SFX_Smack
    MC "Wh-why are you here?" with sshake

    show jobert - sad
    with dissolve
    play music BGM_sad
    play sound SFX_Idea
    side_jobert "It’s her birthday, 
    {w=0.5}isn't it?" with sflash

    MC "Yeah, 
    {w=0.5}how did you know?"

    show jobert - neutral
    with dissolve

    side_jobert "I asked the detective where you are. 
    {w=0.5}I actually wanted to talk to you."

    MC "Oh, 
    {w=0.5}about what?"

    show jobert - sad
    with dissolve

    side_jobert "First, 
    {w=0.5}I wanted to apologize for acting like an idiot."

    MC "Yeah, 
    {w=0.5}It’s fine. 
    {w=0.5}Thanks for telling us about Maya."

    show jobert - neutral
    with dissolve

    side_jobert "Uhm by the way, 
    {w=0.5}what’s your relationship with Lheona?"

    MC "She was a close friend."

    show jobert - sad
    with dissolve

    side_jobert "..."

    MC "Do you know her?"

    show jobert - pleased
    with dissolve

    side_jobert "Of course, 
    {w=0.5}she’s the famous daughter of the Syngh’s family and I was accused of her disappearance."

    MC "You were accused?"

    show jobert - confused
    with dissolve

    side_jobert "Yeah, 
    {w=0.5}I saw you unconscious beside the river. 
    {w=0.5}I just tried to help you but they accused me as one of the suspects."

    MC "You were the one who helped me? 
    {w=0.5}Why didn’t you say something?"

    show jobert - sad
    with dissolve

    side_jobert "I was furious because after that accusation, my life went downhill. 
    {w=0.5}I lost my job and then my wife left me."

    MC "I’m sorry, 
    {w=0.5}Jobert{cps=*0.5}...{/cps} I didn’t know{cps=*0.5}...{/cps}"

    side_jobert "It's fine,
    {w=0.5} I realized you are not to blame.
    {w=0.5} I was just looking for an excuse."
    window hide

    stop music fadeout 1.0

    pause 1.0
    #Silence  
    window show
    show jobert - neutral
    with dissolve

    side_jobert "Anyways, 
    {w=0.5}I hope you find the justice you deserve."

    side_jobert "I'll see you around."

    MC "Thanks, 
    {w=0.5}Jobert."
    window hide

    stop music fadeout 1.0
    pause 0.5

    hide jobert
    with dissolve

    pause 1.0

    scene black
    with fade

    pause 0.5
    window show
    MC "We've found out who was the culprit for the break in.
    {w=0.5}It was Maya."

    MC "However,
    {w=0.5}that only lead to many questions.
    {w=0.5}Most of which,
    {w=0.5}are left unanswered."

    MC "I guess I will soon find out the truth{cps=*0.5}...{/cps}"
    window hide

    pause 2.0
    play music BGM_sadmemory
    scene ending
    with fade

    pause 3.0

    scene credits
    with fade

    pause 5.0

    scene black
    with fade

    pause 1.0
    window show
    sys_nar "You've unlocked the Neutral Ending!"
    sys_nar "Thank you for playing our game!" 
    sys_nar "For evaluation please use {a=https://forms.gle/LrzHUbbRKhyjK4JG8}this link!{/a}. We would appreciate it if you answer!"
    window hide

    pause 1.5

    $ MainMenu(confirm=False)()

    

    #*Jobert slowly walks away and left Max*

    #End

label ch_03_bad:
    #MONTERO HOUSE - JUNE 17, 1992 8:00 P.M.

    scene bg-intmaxbedroomnight
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 16, 1992 8:00 P.M.{/cps}"
    window hide
    
    pause 1.0

    play sound SFX_Mystery
    show ex_omen
    with dissolve

    pause 1.0

    window show
    ex_of "{cps=*0.5}...{/cps}"
    
    play sound SFX_Smack
    ex_of "Unreliable. 
    {w=0.5}I hired them to do one job and they left incriminating evidence." with sshake

    ex_of "{cps=*0.5}...{/cps}"
    window hide

    pause 1.0

    show item_phone at halfleft
    with irisin
    play sound SFX_ring
    with sshake

    pause 2.0

    play sound SFX_Call3
    pause 0.5
    window show
    #PHONE CALL:

    ex_of "Hello?"

    ex_of "Yes, 
    {w=1.0}I’ved arrived... 
    {w=1.0}I understand... 
    {w=1.0}I’ll make sure to{nw}"
    play sound SFX_Omen
    extend" silence the kid. 
    {w=1.0}I won’t disappoint you."
    window hide
    play sound SFX_Call3
    hide item_phone
    with irisout
    pause 0.5
    #PHONE CALL ENDS
    window show
    ex_of "Maximo Christian Montero. 
    {w=0.5}You shouldn’t have come back here."
    window hide
    pause 1.0
    #TEKTIV’S HOUSE - JUNE 17, 1992. 6:40 A.M.

    #DY POV
    scene bg-dyroom
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}TEKTIV’S HOUSE - JUNE 17, 1992. 6:40 A.M.{/cps}"
    window hide
    
    pause 1.0
    
    window show
    d "zzzzzzzzzz{cps=*0.5}...{/cps}"
    window hide
    pause 0.5
    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake
    #SFX Phone rings
    pause 3.0
    hide item_phone
    with irisout

    window show
    d "Urghhh{cps=*0.5}...{/cps}"
    window hide
    pause 0.5
    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake
    #SFX Phone rings
    pause 3.0
    hide item_phone
    with irisout

    window show
    d "{=txt_vo}(Who calls this early in the morning? 
    {w=0.5}I swear if it’s Azzi, 
    {w=0.5}I’ll give him an earful later.)"
    window hide
    pause 0.5
    show item_phone at truecenter
    with irisin
    play sound SFX_ring
    with sshake
    #SFX Phone rings
    pause 3.0

    window show
    play sound SFX_Smack
    d "Arghhh! 
    {w=0.5} What’s a man gotta do to get some sleep here" with sshake
    window hide

    pause 0.5

    play sound SFX_Call3
    #SFX Phone Call:
    pause 0.5

    window show
    play sound SFX_Smack
    side_cheng "Inspector, 
    {w=0.5}what’s wrong with you?" with sshake

    play sound SFX_Idea
    d "I’m sorry, 
    {w=0.5}Auntie Cheng?… 
    {w=0.5}Why what’s up?" with sflash

    play sound SFX_Mystery
    side_cheng "Is Max with you right now?"

    d "No, 
    {w=0.5}why?"

    play sound SFX_Foreshadow
    play music BGM_forbode fadein 1.0
    side_cheng "He hasn’t come home since yesterday{cps=*0.5}...{/cps}"

    d "But I dropped him off yesterday after we ate dinner and we saw him enter your gate."

    play sound SFX_Smack
    side_cheng "What?? 
    {w=0.5}I didn't hear from him last night. 
    {w=0.5}He said he’d call me before bedtime." with sshake

    d "Maybe he just went straight to bed after eating, 
    {w=0.5}Mrs. Malano"

    side_cheng "Maybe, 
    {w=0.5}but I won’t stop worrying if I don’t know for sure. 
    {w=0.5}Would you be so kind and check up on him? 
    {w=0.5}I’m still at the hospital so I can’t check."

    d "Ok, 
    {w=0.5}Auntie Cheng. 
    {w=0.5}We’ll check your house if he’s there."
    window hide

    pause 0.5

    play sound SFX_Call3
    hide item_phone
    with irisout

    pause 0.5

    window show
    d "{=txt_vo}(That’s weird. 
    {w=0.5}I better call him.)"
    window hide
    #SFX End call

    #Dy got nervous and called Max, but he was unreachable. He called Azzi instead.

    pause 0.5
    show item_phone at truecenter
    with irisin
    #SFX Phone Dial
    play sound SFX_Call1
    pause 2.0

    play sound SFX_Call2
    with sshake
    pause 3.2
    


    window show
    d "{=txt_vo}(Max{cps=*0.5}...{/cps} 
    {w=0.5}Pick up{w=1.0}{cps=*0.15}...{/cps})"
    window hide
    play sound SFX_noservice
    pause 3.0
    window show
    play sound SFX_Smack
    d "{=txt_vo}(Drat! 
    {w=0.5}He’s not picking up!)" with sshake

    d "{=txt_vo}(Geez, 
    {w=0.5}why is he unreachable? 
    {w=0.5}Where is he{cps=*0.5}...{/cps}  
    {w=0.5}I should call Azzi and ask if they’re together{cps=*0.5}...{/cps})"

    d "Azzi pick up please."
    window hide
    pause 0.5
    show item_phone at truecenter
    with irisin
    #SFX Phone Dial
    play sound SFX_Call1
    pause 2.0

    play sound SFX_Call2
    with sshake
    pause 3.2

    play sound SFX_Call3

    pause 0.5
    window show

    d "Azzi?"

    azzi "Hey, 
    {w=0.5}Detective? 
    {w=0.5}What’s up?"

    d "Are you with Max right now?"

    azzi "No, 
    {w=0.5}why?"

    d "Auntie Cheng told me that he hasn't heard from Max since last night. 
    {w=0.5}I tried calling him, 
    {w=0.5}but he can’t be reached. 
    {w=0.5}Can you come with me to visit their house?"

    play sound SFX_Smack
    azzi "Where the heck is that guy!? 
    {w=0.5}Sure, 
    {w=0.5}Detective. 
    {w=0.5}I’ll see you later" with sshake
    window hide

    hide item_phone
    with irisout

    pause 0.5
    #*Black Screen*

#3 Dy & Azzi went to the Montero Residence
    scene bg-intmaxbedroom
    with fade
    pause 1.0

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 17, 1992. 8:00 A.M.{/cps}"
    window hide
    
    pause 1.0
    
    show azzi - angry
    with dissolve

    d "The door wasn’t locked"

    azzi "We should look around his bedroom, 
    {w=0.5}Detective."

    d "He isn’t here." 

    show azzi - confused

    play sound SFX_Idea
    azzi "His belongings are still here, 
    {w=0.5}Detective!" with sflash

    d "Wait a second. 
    {w=0.5}How could I be so blind!?"

    azzi "What is it, 
    {w=0.5}detective?"

    d "On my phone’s call history. 
    {w=0.5}There’s several calls from Max around 8:30 P.M."
    
    show azzi - angry
    play sound SFX_Smack
    azzi "What!?" with sshake

    d "Here’s one that’s been recorded."
    window hide

    stop music fadeout 1.0

    pause 0.5

    show item_phone at halfleft
    with irisin

    pause 1.0

    window show

    #MAX CALL
    play sound SFX_static
    MC "{color=#A54226}Mmmmph{cps=*0.15}...{/cps}{w=1.25}{nw}" with sshake
    play sound SFX_static
    extend " h{cps=*0.15}...{/cps}{w=1.25}{nw}" with sshake 
    play sound SFX_static
    extend " urkkk{cps=*0.15}...{/cps}{w=1.25}{nw}" with sshake
    play sound SFX_static 
    extend " h-help!{w=1.25}{nw}" with sshake
    play sound SFX_Omen
    extend " {w=1.25}{nw}"
    window hide

    pause 1.5
    hide item_phone
    with irisout

    play sound SFX_Idea
    d "!" with sflash

    play sound SFX_Smack
    d "No! 
    {w=0.5}MAX! 
    {w=0.5}Not again!" with sshake
    window hide

    pause 0.5
    #SCREEN FADE TO BLACK
    scene black
    with sflash

    pause 0.5
    window show

    d "Once again another case of disappearance happened in this town of Iliganon City. 
    {w=0.5}And once again it was someone who worked under me"
    window hide 
    #Black Screen
    pause 0.5

    window show
    d "Max is gone."
    window hide

    pause 2.0
    play music BGM_sadmemory
    scene ending
    with fade

    pause 3.0

    scene credits
    with fade

    pause 5.0

    scene black
    with fade

    pause 1.0
    window show
    sys_nar "You've unlocked the Bad Ending!"
    sys_nar "Thank you for playing our game!" 
    sys_nar "For evaluation please use {a=https://forms.gle/LrzHUbbRKhyjK4JG8}this link!{/a}. We would appreciate it if you answer!"
    window hide

    pause 1.5

    $ MainMenu(confirm=False)()