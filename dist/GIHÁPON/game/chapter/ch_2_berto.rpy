label ch_02_berto_Q1:
    window hide
    pause 0.5
    window show
    MC "Is Jobert a good “drinking” friend?"
    
    show berto - surprised
    play sound SFX_Smack
    side_berto "Wha? 
    {w=0.5}How’d you know we go out for drinks?" with sshake
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "Dodong from Dikumakain told us."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - sad at center
    with decay10inleft
    window show
    side_berto "Hmmm{cps=*0.5}...{/cps}"
    show berto - annoyed
    with dissolve
    side_berto "Yeah, 
    we used to hang out {=hl}every evening before{/=hl}. 
    {w=0.5}Recently that’s been rare. 
    {w=0.5}So we only hang out when we both see each other at Dikumakain"

    MC "Oh really? 
    {w=0.5}Aside from drinking, 
    {w=0.5}were you guys close"
    show berto - neutral
    with dissolve
    side_berto "Can’t really say we were close. 
    {w=0.5}I understood his life’s woes and he understood mine. 
    {w=0.5}We have some sort of mutual respect."
    show berto - annoyed
    with dissolve
    side_berto "I’ll say, 
    {w=0.5}he’s kind of annoying when he gets too drunk. 
    {w=0.5}He’s talkative when drinking alright but when he’s got a handful of beers down the drain he gets {=hl}TALKATIVE{/=hl}."
    
    MC "{=txt_vo}(So Jobert gets too chatty when getting drunk, 
    {w=0.5}huh? 
    {w=0.5}What should I ask Mr. Berto next?)"

    menu:
        MC "{=txt_vo}(So Jobert gets too chatty when getting drunk, 
        huh? 
        What should I ask Mr. Berto next?)"

        "Does he talk too much?":
            jump ch_02_berto_Q1_1
        "Why don’t you stop him from drinking?":
            jump ch_02_berto_Q1_2
    return

label ch_02_berto_Q1_1:
    window hide
    pause 0.5
    show berto - neutral
    with dissolve
    window show
    side_berto "In general, 
    {w=0.5}no. 
    {w=0.5}Poor guy, 
    {w=0.5}only gets to pour out his emotions when {=hl}he drowns himself in alcohol{/=hl}. 
    {w=0.5}He’s gotten himself in all sorts of trouble for it."
    show berto - sad
    with dissolve
    side_berto "Can’t blame him fully though, 
    {w=0.5}he’s been dealt with {=hl}bad cards{/=hl}."

    MC "What do you mean by that?"
    show berto - annoyed
    with dissolve
    side_berto "I don’t know if I’m at liberty to share his problems with you. 
    {w=0.5}I don’t wanna be accused of gossiping."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "We promise you sir all of this is going to be between us. 
    {w=0.5}Take that as a contract of confidentiality."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - sad at center
    with decay10inleft
    window show
    side_berto "I guess, 
    {w=0.5}if this is to find out who did the thing with Mrs. Malano."
    show berto - neutral
    with dissolve
    side_berto "Well, 
    {w=0.5}a few years ago he lost a great deal in his life. 
    {w=0.5}First he {=hl}lost his job{/=hl} then he {=hl}lost his wife{/=hl}."

    side_berto "He’d always go on and on about this when we go drinking."

    MC "I didn’t know that happened to him. 
    {w=0.5}Now I understand why he sounds like he wants the world to burn down."

    MC "{=txt_vo}(If I were to lose my job and my wife, 
    {w=0.5}I’d freak out a lot too.)"
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    azzi "Doesn’t give him the excuse to go on a rampage around town every time he’s drunk"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "Don’t I know it? 
    {w=0.5}Recently he’d even arrived at Dikumakain, 
    {w=0.5}already drunk out of his butt."

    side_berto "When I asked him why he’s already drunk. 
    {w=0.5}He said to me that he’d already gone out and had a few bottles with a “buddy” of his"
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    azzi "He goes out to drink with {=hl}another person{/=hl}?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - neutral at center
    with decay10inleft
    window show
    side_berto "Apparently, 
    {w=0.5}and since that’s been a recurring thing he’d be twice as drunk compared to when we drank together in the past. 
    {w=0.5}It’s a pain when he starts a scene."

    MC "{=txt_vo}(He {=hl}lost his job and his wife{/=hl}? 
    {w=0.5}And now we find out he has another {=hl}drinking buddy{/=hl}? 
    {w=0.5}What should I ask him next?)"

    menu:
        MC "{=txt_vo}(He {=hl}lost his job and his wife{/=hl}? 
        And now we find out he has another {=hl}drinking buddy{/=hl}? 
        What should I ask him next?)"

        "Ask about Jobert’s wife?":
            jump ch_02_berto_Q1_1_1

        "Ask about drinking buddy?":
            jump ch_02_berto_Q1_1_2

    return

label ch_02_berto_Q1_1_1:
    window hide
    pause 0.5
    window show

    MC "So Jobert’s wife died?"
    window hide
    pause 0.5
    window show
    show berto - surprised
    play sound SFX_Idea
    side_berto "!" with sflash

    show berto - angry
    play sound SFX_Smack
    side_berto "What? 
    {w=0.5}You moron, 
    {w=0.5}I never said that." with sshake

    MC "Ahaha well since you said lost his wife, 
    {w=0.5}I thought maybe she passed away."

    show berto - annoyed
    with dissolve

    side_berto "No, 
    {w=0.5}that’s not it. 
    {w=0.5}She merely left him."
    window hide
    show dy - thinking at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "Wife took off eh?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - neutral at center
    with decay10inleft
    window show
    side_berto "It was when Jobert lost his job. 
    {w=0.5}Back a few years ago, 
    {w=0.5}it was hard living in this economy. 
    {w=0.5}Money was tight and putting food down the table was a challenge."

    side_berto "Jobert unfortunately lost his job and his wife left him for it. 
    {w=0.5}Everything happened so suddenly, 
    {w=0.5}he was left in a shock."

    MC "That’s what happened to him. 
    {w=0.5}Geez, 
    {w=0.5}that’s a lot."

    MC "{=txt_vo}(I wonder why he lost his job then)"

    side_berto "Not to mention the icing on the cake. 
    {w=0.5}He was suspected in a case 5 years ago."
    window hide
    show dy - sad at left
    show azzi - sad at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "{cps=*0.5}...{/cps}"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - neutral at center
    with decay10inleft
    pause 0.5
    play sound SFX_Idea
    MC "What!?
    {w=0.5}{=txt_vo}(Could it be?)" with sflash
    show berto - annoyed
    with dissolve
    side_berto "The same case you were involved in Max."
    window hide
    show dy - thinking at left
    show azzi - angry at right
    show berto at offscreenright
    
    play sound SFX_Smack
    azzi "Max!? 
    {w=0.5}You were involved in a case?" with sshake

    MC "{=txt_vo}(So is this why Jobert was so aggressive towards me in the get go?)"

    MC "{=txt_vo}(Does he think that I have something to do with all that happened 5 years ago?)"

    jump ch_02_berto_end_1

    return

label ch_02_berto_Q1_1_2:
    window hide
    pause 0.5
    window show
    MC "You mentioned that he arrives already drunk?"

    show berto - neutral
    with dissolve

    side_berto "Yes."

    MC "And he goes drinking with this “Buddy” of his?"

    side_berto "Yeah, 
    {w=0.5}pretty much sums it up."

    MC "Do you have any information on who that person is? Did Jobert ever talk about them?"

    side_berto "I have no idea who she is"

    play sound SFX_Idea
    MC "She? Oh, it's a woman then?" with sflash

    side_berto "Yeah, Jobert told me in his drunk state. 
    {w=0.5} Never mentioned a name though. He just kept referring to his buddy with a “She”."

    MC "You sure that’s the only thing he told you about his buddy?"

    show berto - angry
    play sound SFX_Smack
    side_berto "Look here,
    {w=0.5} I’m no Jobert encyclopedia,
    {w=0.5} okay?
    {w=0.5} If you wanna know more,
    {w=0.5} you might as well ask him." with sshake

    jump ch_02_berto_end_2

    return

label ch_02_berto_Q1_2:
    window hide
    pause 0.5
    window show

    MC "Why don’t you stop him from drinking?"

    show berto - angry
    play sound SFX_Smack
    side_berto "Hey now, 
    {w=0.5}what do you mean? 
    {w=0.5}You think I’m responsible for that chump?" with sshake

    show berto - annoyed
    with dissolve

    side_berto "I may drink with him but he’s not my child or something. 
    {w=0.5}He’s a grown man and he can decide what to do with himself. 
    {w=0.5}Including facing the consequences of his actions!"

    MC "No I didn’t mean it like that, 
    {w=0.5}you could just stop him from ordering drinks when you go out drinking. 
    {w=0.5}That way he wouldn’t go and cause a scene."

    play sound SFX_Smack
    side_berto "Now what do you know? 
    {w=0.5}Why didn’t I think about that? 
    {w=0.5}Listen here kid, 
    {w=0.5}recently he comes to Dikumakain already drunk." with sshake
    
    show berto - angry
    play sound SFX_Smack
    side_berto "Tell me, 
    {w=0.5}how’s a guy supposed to stop him if he already arrives intoxicated?" with sshake
    window hide
    show dy - annoyed at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "He’s already drunk by the time he arrives?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto at center
    with decay10inleft
    window show
    play sound SFX_Smack
    side_berto "Yeah! 
    {w=0.5}When I asked him why he’s already drunk. 
    {w=0.5}He said to me that he’d already gone out and had a few bottles with a “buddy” of his" with sshake

    window hide
    show dy - thinking at left
    show azzi - angry at right
    show berto at offscreenright
    with decay10inleft
    window show

    azzi "He goes out to drink with {=hl}another person{/=hl}?"

    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show

    side_berto "Apparently, 
    {w=0.5}and since that’s been a recurring thing he’d be twice as drunk compared to when we drank together in the past. 
    {w=0.5}It’s a pain when he starts a scene."
    window hide
    
    menu:
        
        "Ask about drinking buddy?":
            jump ch_02_berto_Q1_1_2
        "I guess you’re not his friend anymore?":
            jump ch_02_berto_Q1_2_1
    return

label ch_02_berto_Q1_2_1:
    window hide
    pause 0.5
    window show
    MC "I guess you’re not his friend anymore?"
    show berto - angry
    play sound SFX_Smack
    side_berto "WHAT!? 
    {w=0.5}Are you making fun of me? 
    {w=0.5}What kind of question is that?" with sshake

    MC "I mean it seems he isn’t drinking with you first. 
    {w=0.5}He’s always out there with someone and downing bottles of beer instead of you."

    show berto - annoyed
    with dissolve

    side_berto "Look I don’t even care who he drinks with okay? 
    {w=0.5}What he does in his is his business not mine. 
    {w=0.5}If he goes out to drink with someone first then so be it."

    jump ch_02_berto_end_3
    return

label ch_02_berto_Q2:
    window hide
    pause 0.5
    window show
    MC "How does Jobert treat you?"

    show berto - neutral
    with dissolve

    side_berto "Depends on his mood. 
    {w=0.5}On the good days he’d be calm. 
    {w=0.5}When he’s in a bad mood he grumbles a lot. 
    {w=0.5}For some reason he doesn’t become outright rude towards me when he gets moody."

    MC "Is that so? 
    {w=0.5}{=txt_vo}(He surely was outright rude towards me if I had any say in it.)"
    show berto - annoyed
    with dissolve
    side_berto "Look I know everyone in this town hates him and all but I think he’s misunderstood."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show

    azzi "How about you, Mr. Ventura? 
    {w=0.5}Do you hate him?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "He annoys me sometimes but I don’t hate him. 
    {w=0.5}I tolerate him at best. 
    {w=0.5}I understand him and he understands me."

    MC "How can you tell that?"

    side_berto "When we drink ofcourse. 
    {w=0.5}He and I would toss a few drinks for a while"

    MC "{=txt_vo}(Seems that there’s some common ground between Mr. Berto and Jobert. 
    {w=0.5}I just wished he’d tolerate Jobert’s drinking habits less. 
    {w=0.5}What should I ask him next?)"

    menu: 
        MC "{=txt_vo}(Seems that there’s some common ground between Mr. Berto and Jobert. 
        I just wished he’d tolerate Jobert’s drinking habits less. 
        What should I ask him next?)"

        "You guys have a mutual understanding?":
            jump ch_02_berto_Q2_1
        "Why don’t you stop him from drinking?":
            jump ch_02_berto_Q1_2
        
    return

label ch_02_berto_Q2_1:
    window hide
    pause 0.5
    window show

    MC "You guys have a mutual understanding?"

    show berto - neutral
    with dissolve
    side_berto "We both have similar life struggles okay kid? 
    {w=0.5}We’d talk about this during our drinking sessions. 
    {w=0.5}Too bad he’d always arrive already drunk these days."

    MC "That’s a bummer. 
    {w=0.5}How come he’s already drunk?"

    show berto - neutral
    with dissolve

    side_berto "The man’s already drank a few with a “Buddy” of his."

    side_berto "I’ll be honest, 
    {w=0.5}I was shocked at first. 
    {w=0.5}That man has found a buddy to have a drink with other than me? 
    {w=0.5}Kinda proud of him since he’s really unliked in these parts."

    MC "{=txt_vo}(So Jobert seems to run off and drink with somebody else. 
    {w=0.5}Who could that be? 
    {w=0.5}Should I press further?)"
    menu:
        MC "{=txt_vo}(So Jobert seems to run off and drink with somebody else. 
        Who could that be? 
        Should I press further?)"
    
        "Ask about drinking buddy?":
            jump ch_02_berto_Q1_1_2
        "What were you two struggling with?":
            jump ch_02_berto_Q2_1_1
    return

label ch_02_berto_Q2_1_1:
    window hide
    pause 0.5
    window show
    MC "What were you two struggling with?"
    show berto - angry
    play sound SFX_Smack
    side_berto "What? 
    {w=0.5}Why are you asking me that?" with sshake

    MC "I wanted to know what made you both friends."

    show berto - annoyed
    with dissolve

    side_berto "He’s not my friend, 
    {w=0.5}kid. 
    {w=0.5}He’s merely an acquaintance I have a few things in common with. 
    {w=0.5}Friend is the last thing I’d label him."

    show berto - angry
    play sound SFX_Smack
    side_berto "You know what? 
    {w=0.5}I thought you’d want to know more about Jobert. 
    {w=0.5}But the last few questions you had were more scrutinizing my own business." with sshake

    MC "No that's not-"

    jump ch_02_berto_end_3

label ch_02_berto_Q3:
    window hide
    pause 0.5
    window show
    MC "Where were you yesterday?"

    show berto - neutral
    with dissolve
    side_berto "Yesterday? 
    {w=0.5}well as usual i would be tending my gard-"

    show berto - angry
    play sound SFX_Smack
    side_berto "Hey! 
    {w=0.5}Why am I telling you this? 
    {w=0.5}I am in no obligation to tell you what goes on in my life. 
    {w=0.5}Hmph!" with sshake

    show berto - annoyed
    with dissolve

    side_berto "Kids these days all want to know every and any detail they can get from a person."

    MC "Oh we didn't mean to come across as invading your privacy sir!"

    side_berto "Well you aren't doing a good job at it son."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "Well, 
    {w=0.5}for your information sir. 
    {w=0.5}There's been a break in nearby, 
    {w=0.5}fortunately no one was gravely harmed. 
    {w=0.5}We would just like to know if you know anything about that."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "So this is what it is huh? 
    {w=0.5}You're suspecting I had to do anything about this fiasco."
    show berto - angry
    play sound SFX_Smack
    side_berto "Just because I'm a jaded old man doesn't mean I'm out here planning house break ins in my free time." with sshake
    window hide
    show dy - annoyed at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show

    d "We aren't pointing you out as a suspect sir. 
    {w=0.5}We only want a few questions with you."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "Sure, 
    {w=0.5}I bet those questions will twist and turn, 
    {w=0.5}making me out as the suspect for this little break in incident you have here."
    show berto - angry
    play sound SFX_Smack
    side_berto "Well I have news for you, 
    {w=0.5}I'm not involved in this incident here. 
    {w=0.5}That's the bottom line for you sir! 
    {w=0.5}So I have no interest in answering your questions." with sshake
    window hide
    show dy - confused at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "Well I understand that being interrogated can be a stressful thing sir but I assure you-"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - angry at center
    play sound SFX_Smack
    side_berto "Haven't I made myself clear here, 
    {w=0.5}I'm not answering your questions!" with sshake

    MC "{=txt_vo}(Wow this man's a pain to deal with. 
    {w=0.5}I think I should step in and try something.)"

    menu:
        MC "{=txt_vo}(Wow this man's a pain to deal with. I think I should step in and try something.)"

        "Threaten?":
            jump ch_02_berto_Q3_1
        "Deescalate?":
            jump ch_02_berto_Q3_2
    return

label ch_02_berto_Q3_1:
    window hide
    pause 0.5
    window show

    MC "Sir if you keep trying to evade our questions, 
    {w=0.5}you might get suspected for the incident as an Accomplice."
    window hide
    show dy - annoyed at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    play sound SFX_Smack
    d "Hey max!" with sshake

    show azzi - happy
    with dissolve
    azzi "Wow Max you're already following my footsteps with your accusations."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "What are you getting at boy? 
    {w=0.5}Me? 
    {w=0.5}How dare you point me out as an accomplice!"

    side_berto "Like I've said before, 
    {w=0.5}I am NOT involved in this incident of yours!"

    MC "Well that may be true Mr. Berto, 
    {w=0.5}but we know that you're related to someone who may have been involved in the recent break in."

    show berto - surprised
    play sound SFX_Smack

    side_berto "What!?" with sshake

    MC "Yes, 
    {w=0.5}you are acquainted with Mr. Jonathan Robert Salvador."

    show berto - angry
    play sound SFX_Smack

    side_berto "I’m acquainted with him but I’m no accomplice to his shenanigans!" with sshake

    MC "A little information about him can be a huge help in this case, 
    {w=0.5}Sir. 
    {w=0.5}Can you just-"

    show berto - angry
    play sound SFX_Smack

    side_berto "So this is what it is? 
    {w=0.5}You’re pointing fingers at me!?" with sshake

    show berto - annoyed
    with dissolve

    side_berto "Listen here kid, 
    {w=0.5}I’m no accomplice to his crimes. 
    {w=0.5}So if you would be so kind and leave! 
    {w=0.5}I’ve had enough!"

    jump ch_02_berto_end_3

label ch_02_berto_Q3_2:
    window hide
    pause 0.5
    window show

    MC "Mr. Berto, 
    {w=0.5}we believe that you didn't have anything to do with the incident. 
    {w=0.5}If you were, 
    {w=0.5}Auntie Cheng would have mentioned you already. 
    {w=0.5}She was the one who got attacked in the incident."

    show berto - surprised
    play sound SFX_Idea
    side_berto "Wait, 
    {w=0.5}Mrs. Malano was hurt?" with sflash

    play sound SFX_Smack

    side_berto "How is she? 
    {w=0.5}Is she okay?" with sshake

    MC "She's in stable condition sir and would probably be released from the hospital soon."
    show berto - sad
    with dissolve
    side_berto "That's a relief"

    MC "{=txt_vo}(Hmm what's this? 
    {w=0.5}Why'd he have a sudden mood change?)"
    show berto - neutral
    side_berto "Alright, 
    {w=0.5}alright kiddo... 
    {w=0.5}What did you want to know?"

    MC "Thank you Mr. Ventura. 
    {w=0.5}Well sir, 
    {w=0.5}here's the deal. 
    {w=0.5}you are acquainted with Jobert, 
    {w=0.5}right? 
    {w=0.5}I believe you and him frequent Dikumakain for some late night drinks?"

    side_berto "Yeah I know him. 
    {w=0.5}And what of it? 
    {w=0.5}I don't see how he could be involved in this little break in incident."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "Well there were blood trails leading to his house-"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - surprised at center
    play sound SFX_Idea
    side_berto "Blood!? 
    {w=0.5}Don’t tell me he-" with sflash
    
    show berto - annoyed
    with dissolve

    side_berto "Is he a suspect? 
    {w=0.5}I don’t have anything to do with him! 
    {w=0.5}I used to be acquainted with him but I barely talk to him anymore!"

    MC "Why is that so?"
    show berto - neutral
    with dissolve

    side_berto "He’s been arriving drunk already. 
    {w=0.5}He'd already gone out and had a few bottles with a “buddy” of his. 
    {w=0.5}So he’d end up either passed out or stirring up some trouble."
    window hide
    show dy - neutral at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show

    azzi "He goes out to drink with {=hl}another person{/=hl}?"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    side_berto "Apparently, 
    {w=0.5}and since that’s been a recurring thing he’d be twice as drunk compared to when we drank together in the past. 
    {w=0.5}It’s a pain when he starts a scene."

    MC "{=txt_vo}(So Jobert seems to run off and drink with somebody else. 
    {w=0.5}Who could that be? 
    {w=0.5}Is that really true? 
    {w=0.5}Should I press further?)"

    menu:
        MC "{=txt_vo}(So Jobert seems to run off and drink with somebody else. Who could that be? Is that really true?Should I press further?)"

        "I think you’re lying.":
            jump ch_02_berto_Q3_2_1
        "Ask about drinking buddy?":
            jump ch_02_berto_Q1_1_2

label ch_02_berto_Q3_2_1:
    window hide
    pause 0.5
    window show

    MC "Mr. Berto, 
    {w=0.5}I’m afraid I have to ask you to tell the truth."

    show berto - angry
    play sound SFX_Smack
    side_berto "Truth!? 
    {w=0.5}You think I’m lying?" with sshake

    MC "It’s inconceivable that Jobert would have someone else around as a friend. 
    {w=0.5}He’s mostly hated by everyone at this point."
    show berto - annoyed
    with dissolve
    side_berto "You do know how ridiculous that sounds? 
    {w=0.5}Despite being hated there’s probably someone out there he gets along with."

    MC "You probably know something about what Jobert was planning, 
    {w=0.5}did you Mr. Berto."
    window hide
    show dy - annoyed at left
    show azzi - confused at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "I don’t this is going anywhere Max."
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - angry at center
    with decay10inleft
    window show
    play sound SFX_Smack
    side_berto "So this is what it is? 
    {w=0.5}You’re pointing fingers at me!?" with sshake

    side_berto "Listen here kid, 
    {w=0.5}I’m no accomplice to his crimes. 
    {w=0.5}So if you would be so kind and{nw}"
    play sound SFX_Smack
    extend " leave!" with sshake

    jump ch_02_berto_end_3

label ch_02_berto_end_1:
    window hide

    stop music fadeout 1.0

    scene bg-outsidemaxhouse
    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft
    show berto - neutral at center    
    with fade

    play music AMB_nature

    pause 1.0
    
    window show
    side_berto "Alright kid, 
    {w=0.5}that’s about all I know. 
    {w=0.5}Hound me all you want but you’re not getting any more information that I can give you."
    window hide
    show dy at left
    show azzi at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "That’s alright Mr. Ventura"

    MC "Yes! 
    {w=0.5}What you told us will be substantial in dealing with Jobert."

    MC "Thank you for cooperating Mr. Berto"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    play sound SFX_Idea
    side_berto "Hmph!" with sflash
    window hide

    pause 0.5

    hide berto
    with dissolve

    pause 0.5

    show dy - neutral at left
    show azzi - neutral at right
    with decay10inleft

    window show
    MC "{=txt_vo}(Okay, 
    {w=0.5}seems we’ve found out that Jobert’s wife left him. 
    {w=0.5}That’s why he’s always so grumpy.)"

    MC "{=txt_vo}(She left him because he was a suspect in a case 5 years ago. 
    {w=0.5}What’s crazy is that, 
    {w=0.5}it’s the same case I was involved in as well.)"

    MC "{=txt_vo}(Seems we’re getting closer to finding out what’s really happening right now. 
    {=xt_vo}To think that the incident is coming back to haunt us.)"
    
    d "I think we should go pay this Jobert person a visit. 
    {w=0.5}We should have enough information to make him talk"

    show azzi - happy
    with dissolve

    azzi "Agreed!"
    window hide

    stop music fadeout 1.0

    pause 0.5

    jump ch_02_good

    return

label ch_02_berto_end_2:
    window hide

    stop music fadeout 1.0

    scene bg-outsidemaxhouse
    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft
    show berto - neutral at center    
    with fade

    play music AMB_nature

    pause 1.0
    
    window show
    side_berto "Alright kid, 
    {w=0.5}that’s about all I know. 
    {w=0.5}Hound me all you want but you’re not getting any more information that I can give you."
    window hide
    show dy at left
    show azzi at right
    show berto at offscreenright
    with decay10inleft
    window show
    d "That’s alright Mr. Ventura"

    MC "Yes! 
    {w=0.5}What you told us will be substantial in dealing with Jobert."

    MC "Thank you for cooperating Mr. Berto"
    window hide
    show dy at offscreenleft
    show azzi at offscreenleft
    show berto - annoyed at center
    with decay10inleft
    window show
    play sound SFX_Idea
    side_berto "Hmph!" with sflash
    window hide

    pause 0.5

    hide berto
    with dissolve

    pause 0.5

    show dy - neutral at left
    show azzi - neutral at right
    with decay10inleft

    window show
    MC "{=txt_vo}(Okay, 
    {w=0.5}seems we’ve found out that Jobert has been drinking with this buddy of his.)"

    MC "{=txt_vo}(I’m not sure yet, 
    {w=0.5}but if we can find out why he drinks with another buddy maybe it can help us with this case.)"

    d "I think we should go pay this Jobert person a visit. 
    {w=0.5}We should have enough information to make him talk"

    show azzi - happy
    with dissolve

    azzi "Agreed!"
    window hide

    stop music fadeout 1.0

    pause 0.5 

    jump ch_02_neutral

    return

label ch_02_berto_end_3:
    window hide

    stop music fadeout 1.0

    scene bg-outsidemaxhouse
    show dy - neutral at offscreenleft
    show azzi - neutral at offscreenleft
    show berto - neutral at center    
    with fade

    play music AMB_nature

    pause 1.0
    
    window show
    show berto - angry
    play sound SFX_Smack
    side_berto "I think you guys are overstaying your welcome. 
    {w=0.5}This has been a waste of time." with sshake

    side_berto "If you would be so kind and leave! I would appreciate that."

    MC "Wait Mr. Berto-"
    window hide

    pause 0.5

    hide berto
    with dissolve

    pause 0.5

    show dy - neutral at left
    show azzi - confused at right
    with decay10inleft

    window show
    azzi "And there he goes{cps=*0.5}...{/cps}"

    show dy - annoyed
    d "Ughhh{cps=*0.5}...{/cps} 
    {w=0.5}Well that was something." with sshake

    azzi "What do we do now?"

    d "I guess let’s just try visiting Jobert one more time."

    MC "{=txt_vo}(Ughhh{cps=*0.5}...{/cps} 
    {w=0.5}How did this go so wrong? 
    {w=0.5}We didn’t get any new information from Mr. Berto)"

    MC "{=txt_vo}(Well we can try paying Jobert another visit I guess{cps=*0.5}...{/cps})"
    window hide

    stop music fadeout 1.0

    pause 0.5

    jump ch_02_bad

    return