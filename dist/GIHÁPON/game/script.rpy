init python:
    #Dialogue Voice Sounds
    def voice_1(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/SFX_TextBlip_01.wav", channel="textsfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textsfx", fadeout=0.3)

    def voice_2(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/SFX_TextBlip_02.wav", channel="textsfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textsfx", fadeout=0.3)

    def voice_3(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/SFX_TextBlip_03.wav", channel="textsfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textsfx", fadeout=0.3)

    def voice_4(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/SFX_TextBlip_04.wav", channel="textsfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textsfx", fadeout=0.3)

    def type_1(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/SFX_TypewriterPH.wav", channel="textsfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="textsfx", fadeout=0.2)

# Style hl is used for highlighted text. If there is important text in the dialogue, HL must be applied
style hl:
    color '#A54226'

# Style txt_vo is used for voice over/thoughts
style txt_vo:
    color '#637dc4'

style action_button:
    idle_color "#2A2917"
    hover_color "#A54226"
    insensitive_color "#747474"
    selected_idle_color "#2A2917"
    size 28
    bold True
    italic True
    kerning -1

style preview_ui:
    color "#2A2917"
    pos (20,37)
    kerning -2
    bold True
    size 22

init:
    transform halfleft:
        xalign 0.15
        yalign 0.5

    transform halfright:
        xalign 0.85
        yalign 0.5

    transform offscreentop:
        pos (0.5,-1.0)
        anchor (0.5,0.5)
    
#Mouse Styles
    define config.mouse = { }
    define config.mouse['mouse'] = [( "/images/cursor/cursor_default.png", 0, 0)] 
    define config.mouse['mode_search_def'] = [( "/images/cursor/cursor_search_default.png", 40, 40)]
    define config.mouse['mode_search_not'] = [( "/images/cursor/cursor_search_notdone.png", 40, 40)]
    define config.mouse['mode_search_done'] = [( "/images/cursor/cursor_search_done.png", 40, 40)]

#Decay Transition
    python hide:
        import math

        def decay_time_warp_real(x, k):
            return (1.0 / (1.0 + math.exp(-k * (x - 0.5))) - 1.0 / (1.0 + math.exp(k / 2.0)))

        def decay_in_time_warp_real(x, k):
            return (math.exp(1.0) - math.exp(1.0 - k * x)) / (math.exp(1.0) - math.exp(1.0 - k))

        def decay_out_time_warp_real(x, k):
            return (math.exp(k * x) - 1.0) / (math.exp(k) - 1.0)

        decay_time_warp = renpy.curry(decay_time_warp_real)
        decay_in_time_warp = renpy.curry(decay_in_time_warp_real)
        decay_out_time_warp = renpy.curry(decay_out_time_warp_real)

        define.move_transitions("decay10", 0.6, decay_time_warp(k=10.0), decay_in_time_warp(k=10.0), decay_out_time_warp(k=10.0))

    define pushright = PushMove(0.5, "pushright")

#Screen FX - Shake

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)

    $ sshake = Shake((0, 0, 0, 0), 0.5, dist=15)

    $ sshake2 = Shake((0, 0, 0, 0), 3.0, dist=10)
    
#Screen FX
    define fade = Fade(0.5, 1.0, 0.5, color="#000")
    define blackout = Fade(1.0, 1.0, 1.0, color="#000")
    define sflash = Fade(0.1, 0.0, 0.2, color="#fff")
    define wwipe = Fade(0.1, 0.0, 0.8, color="#fff")
    define ssmack = Fade(0.1, 0.0, 0.1, color="#000000")

    define irisin = CropMove(0.25, "irisin")
    define irisout = CropMove(0.25, "irisout")

    define wiperight = CropMove(0.25, "wiperight")
    define wipeleft = CropMove(0.25, "wipeleft")
    define wipeup = CropMove(0.25, "wipeup")
    define wipedown = CropMove(0.25, "wipedown")


# character init

    define MC = Character("Max", what_color='#E3E3E3', who_color='#078585', image = "prototype", callback=voice_1)

    define d = DynamicCharacter("Dy", what_color='#E3E3E3', callback=voice_2)
    define azzi = DynamicCharacter("Azzi", what_color='#E3E3E3', image = "azzi", callback=voice_1)
    define char_wyn = DynamicCharacter("Wynona", what_color='#E3E3E3', callback=voice_3)
    
    define side_berto = Character("Berto", what_color='#E3E3E3', callback=voice_2)
    define side_jobert = DynamicCharacter("Jobert", what_color='#E3E3E3', callback=voice_2)
    define side_ana = Character("Riana", what_color='#E3E3E3', callback=voice_3)
    define side_maya = DynamicCharacter("Maya", what_color='#E3E3E3', callback=voice_3)
    define side_cheng = DynamicCharacter("Auntie", what_color='#E3E3E3', callback=voice_3)
    define side_dodong = DynamicCharacter("Dodong", what_color='#E3E3E3', callback=voice_1)
    define side_jane = DynamicCharacter("Jane", what_color='#E3E3E3', callback=voice_1)
    define side_mamawyn = DynamicCharacter("Margaret", what_color='#E3E3E3', callback=voice_3)
    define side_carlo = Character("Carlo", what_color='#E3E3E3', callback=voice_1)
    define side_mariano = DynamicCharacter("Mariano", what_color='#E3E3E3', callback=voice_2)
    define side_lola = Character("Lola", what_color='#E3E3E3', callback=voice_3)


    define ex_bus = Character("Bus Driver", what_color='#E3E3E3', callback=voice_2)
    define ex_dream = Character("???", what_color='#E3E3E3', callback=voice_1)
    define ex_mailman = Character("Mailman", what_color='#E3E3E3', callback=voice_2)
    define ex_desk = DynamicCharacter("Receptionist", what_color='#E3E3E3', callback=voice_1)
    define ex_waiter = Character("Waiter", what_color='#E3E3E3', callback=voice_2)
    define ex_police = Character("Police", what_color='#E3E3E3', callback=voice_2)
    define ex_officer = Character("Officer", what_color='#E3E3E3', callback=voice_2)
    define ex_of = Character("???", what_color='#E3E3E3', callback=voice_4)
    define ex_fire = Character("Fire Fighter", what_color='#E3E3E3', callback=voice_1)
    define ex_unknown = Character("???", what_color='#E3E3E3', callback=voice_1)


    define sys_nar = Character(None, what_color='#6bb129', callback=type_1, what_xalign=0.5)

# music init

    #Background Music

    define audio.BGM_tektiv = "<loop 81.95>/audio/BGM_Tektiv.ogg"
    define audio.BGM_sadmemory = "<loop 11.52>/audio/BGM_MelancholicMemories.ogg"
    define audio.BGM_palengcare = "<loop 9.69>/audio/BGM_Palengcare.ogg"
    define audio.BGM_forbode = "<loop 48.0>/audio/BGM_ForebodeTheme.ogg"
    define audio.BGM_casual = "<loop 6.99>/audio/BGM_OpeningInvestigation.ogg"
    define audio.BGM_uneasy = "<loop 5.33>/audio/BGM_Uneasy.ogg"
    define audio.BGM_goodnight = "<loop 6.0>/audio/BGM_Goodnight.ogg"
    define audio.BGM_friendly = "<loop 11.03>/audio/BGM_FriendlyPeople.ogg"
    define audio.BGM_cool = "<loop 19.20>/audio/BGM_CoolPeople.ogg"
    define audio.BGM_mystery = "<loop 2.47>/audio/BGM_Mystery.ogg"
    define audio.BGM_azzi = "<loop 3.85>/audio/BGM_Azzi.ogg"
    define audio.BGM_smug = "<loop 18.85>/audio/BGM_SmugPeople.ogg"
    define audio.BGM_thinking = "<loop 16.82>/audio/BGM_Thinking.ogg"
    define audio.BGM_sad = "<loop 64.00>/audio/BGM_SadTheme.ogg"

    #Ambient Sound

    define audio.AMB_rain = "<loop 1.84>/audio/AMB_Rain.ogg"
    define audio.AMB_nature = "<loop 1.84>/audio/AMB_Nature.ogg"
    define audio.AMB_bus = "<loop 3.69>/audio/AMB_Bus.ogg"
    define audio.AMB_Fire = "<loop 1.84>/audio/AMB_Fire.ogg"

# SFX

    define audio.SFX_Smack = "/audio/SFX_SmackPH.wav"
    define audio.SFX_Idea = "/audio/SFX_Idea.wav"
    define audio.SFX_Mystery = "/audio/SFX_Mysterious.wav"
    define audio.SFX_Foreshadow = "/audio/SFX_Foreshadow.wav"
    define audio.SFX_Gleam = "/audio/SFX_Gleam.wav"
    define audio.SFX_Run = "/audio/SFX_Run.wav"
    define audio.SFX_Call1 = "/audio/SFX_Call1.wav"
    define audio.SFX_Call2 = "/audio/SFX_Call2.wav"
    define audio.SFX_Call3 = "/audio/SFX_Call3.wav"
    define audio.SFX_thunder = "/audio/SFX_thunder.wav"
    define audio.SFX_alarm = "/audio/SFX_alarm.wav"
    define audio.SFX_clothruffle = "/audio/SFX_clothruffle.wav"
    define audio.SFX_Sweep = "/audio/SFX_Sweep.wav"
    define audio.SFX_Fanfare_Item = "/audio/SFX_Fanfare_Item.wav"
    define audio.SFX_safeboxunlocked = "/audio/SFX_safeboxunlocked.wav"
    define audio.SFX_door1 = "/audio/SFX_dooropenclose.wav"
    define audio.SFX_door2 = "/audio/SFX_doorslam.wav"
    define audio.SFX_spray = "/audio/SFX_Spray.wav"
    define audio.SFX_camera = "/audio/SFX_Camera.wav"
    define audio.SFX_knock = "/audio/SFX_Knock.wav"
    define audio.SFX_pots = "/audio/SFX_pots.wav"
    define audio.SFX_pansmack = "/audio/SFX_pansmack.wav"
    define audio.SFX_crash = "/audio/SFX_crash.wav"
    define audio.SFX_wrong = "/audio/SFX_wrong.wav"
    define audio.SFX_walk = "audio/SFX_walk.wav"
    define audio.SFX_ambulance = "audio/SFX_ambulance.wav"
    define audio.SFX_bonk = "audio/SFX_headbump.wav"
    define audio.SFX_ring = "audio/SFX_PhoneRing.mp3"
    define audio.SFX_Omen = "audio/SFX_Omen.wav"
    define audio.SFX_glassbreak = "audio/SFX_glassbreak.wav"
    define audio.SFX_stomach = "audio/SFX_stomach.wav"
    define audio.SFX_eating = "audio/SFX_eating.wav"
    define audio.SFX_gulp = "audio/SFX_gulp.wav"
    define audio.SFX_Woosh = "audio/SFX_Woosh.wav"
    define audio.SFX_Handcuff = "audio/SFX_Handcuff.wav"
    define audio.SFX_noservice = "audio/SFX_noservice.wav"
    define audio.SFX_static = "audio/SFX_static.wav"
    define audio.SFX_paper = "audio/SFX_paper.wav"
    
# Solid Backgrounds

    image white = Solid("#fff")  

# Event Flags Initiation
    # Please indicate events with the following format
    # ev_ch00_sc00_eventname

    
    $ev_ch01_sc07_chengapproach = 0
    $ev_ch02_sc13_mcdoorgotkey = False
    $ev_ch02_sc13_luminol = False
    $ev_ch02_sc14_jobert = False

    $liv_room_visited = False
    $din_room_visited = False
    $kit_room_visited = False
    $max_doorroom_visited = False
    $max_room_visited = False
    $jobert_house_visited = False

    $LivRoom_safebox_code = "0000"
    $LivRoom_safebox_locked = True
    $location_maxroom_locked = True

 

    $inv_key_get = False
    $inv_ID_get = False
    $inv_luminol_get = False
    
    default searched_DinRoom_plate = False
    default searched_DinRoom_calendar = False
    default searched_LivRoom_window = False
    default searched_LivRoom_couch = False
    default searched_LivRoom_curtain = False
    default searched_LivRoom_safebox = False
    default searched_KitRoom_pots = False
    default searched_KitRoom_dishes = False
    default searched_KitRoom_fridge = False
    default searched_KitRoom_journal = False
    default searched_MaxRoom_door = False
    default searched_MaxRoom_window = False
    default searched_MaxRoom_picture = False
    default searched_MaxRoom_bed = False
    default searched_MaxRoom_plant = False

    default searched_JobHouse_table = False
    default searched_JobHouse_pile = False
    default searched_JobHouse_beam = False
    default searched_JobHouse_stairs = False
    default searched_JobHouse_easel = False
    
    #toggles inventory visibility
    $inventory_visible = False

#Investigation Variables
    default in_room = False
    default move_count = 0
    default current_room = "LivingRoom"
    default previous_room = ""
    default inv_current_selected = ""

    default travel_preview = "LOC_PREV_UNHOVERED"
    default item_preview = "NONE"

    default liv_room_current = False
    default din_room_current = True
    default kit_room_current = True
    default max_room_current = True

# The game starts here.

#   Transforms
    

label start:
    
    $ default_mouse = "mouse"
    $ travel_preview = "LOC_PREV_UNHOVERED"
    $ item_preview = "NONE"
    
    
# Event Flags
    # Please indicate events with the following format
    # ev_ch00_sc00_eventname
    
    $liv_room_visited = False
    $din_room_visited = False
    $kit_room_visited = False
    $max_doorroom_visited = False
    $max_room_visited = False
    $jobert_house_visited = False

    $location_maxroom_locked = True

    $inv_current_selected = ""
    $inv_key_get = False
    $inv_ID_get = True
    $inv_luminol_get = False

    $ev_ch01_sc07_chengapproach = 0

    $ev_ch02_sc13_mcdoorgotkey = False
    $ev_ch02_sc14_jobert = False

    $searched_DinRoom_plate = False
    $searched_DinRoom_calendar = False
    $searched_LivRoom_window = False
    $searched_LivRoom_couch = False
    $searched_LivRoom_curtain = False
    $searched_LivRoom_safebox = False
    $searched_KitRoom_pots = False
    $searched_KitRoom_dishes = False
    $searched_KitRoom_fridge = False
    $searched_KitRoom_journal = False
    $searched_MaxRoom_door = False
    $searched_MaxRoom_window = False
    $searched_MaxRoom_picture = False
    $searched_MaxRoom_bed = False
    $searched_MaxRoom_plant = False

    $searched_JobHouse_table = False
    $searched_JobHouse_pile = False
    $searched_JobHouse_beam = False
    $searched_JobHouse_stairs = False
    $searched_JobHouse_easel = False

    $Dy = "Dy"

    stop music fadeout 1.0

    menu:
        "Chapter 1":
            jump story_ch_01
        "Chapter 2: Investigation":
            jump story_ch_02_investigation
        
    

    return
