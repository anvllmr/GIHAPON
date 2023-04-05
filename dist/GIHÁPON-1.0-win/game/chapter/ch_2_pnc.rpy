#####################################################
#                                                   #
#         GIHAPON: POINT N' CLICK SEGMENT           #
#                                                   #
#####################################################

#This contains the codes for our Point n' Click portion.
#Enjoy!

init python:
    def update_gamestate():
        global move_count
        newcount = move_count + 1
        SetVariable("move_count", newcount)()
        return

    def check_intro_reactions(room):
        if room == "LivingRoom":
            renpy.call("EnterLivingRoom")
        elif room == "DiningRoom":
            renpy.call("EnterDiningRoom")
        elif room == "Kitchen":
            renpy.call("EnterKitchen")
        elif room == "MaxRoom":
            renpy.call("EnterMaxRoom")
        elif room == "JobertHouse":
            renpy.call("EnterJobertHouse")
        return

    def travel_location_toggle(room):
        if room == "LivingRoom":
            SetVariable("liv_room_current", False)()
        else:
            SetVariable("liv_room_current", True)()
        if room == "DiningRoom":
            SetVariable("din_room_current", False)()
        else:
            SetVariable("din_room_current", True)()
        if room == "Kitchen":
            SetVariable("kit_room_current", False)()
        else:
            SetVariable("kit_room_current", True)()
        if room == "MaxRoom":
            SetVariable("max_room_current", False)()
        else:
            SetVariable("max_room_current", True)()
        return

label story_ch_02_investigation:
    #Update values behind the scenes
    $ update_gamestate()
    window hide
    
    #Enter the scene
    $ in_room = False
    $ inventory_visible = True

    #React to entrance
    if current_room != previous_room:
        $ check_intro_reactions(current_room)
    $ previous_room = current_room

    #Travel Menu Check
    #Disables a location in the travel menu if the Location Button is same as the Current Location
    $ travel_location_toggle(current_room)
    
    #Enable scene interactivity
    $ in_room = True

    play sound "audio/SFX_actionmenu_show.wav"
    $ renpy.transition(wipedown)
    $ renpy.call_screen(current_room + "Screen") 
 
    return

screen Travel_Menu:
    $ travel_preview = "LOC_PREV_UNHOVERED"
    frame:
        pos (128,256)
        background "images/UI/UI_Action_2_BG.png"
        text "Travel to where?":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            pos (55,150)
            spacing -4
            textbutton "Living Room":
                action [SensitiveIf(liv_room_current), SetVariable("current_room", "LivingRoom"), Jump("story_ch_02_investigation")]
                hovered [SetVariable("travel_preview", "LOC_PREV_LIVINGROOM")]
                text_style "action_button"
                hover_sound "audio/SFX_actionmenu_hover_2.wav"
                activate_sound "audio/SFX_MMClick.wav"
            textbutton "Dining Room":
                action [SensitiveIf(din_room_current), SetVariable("current_room", "DiningRoom"), Jump("story_ch_02_investigation")]
                hovered [SetVariable("travel_preview", "LOC_PREV_DININGROOM")]
                text_style "action_button"
                hover_sound "audio/SFX_actionmenu_hover_2.wav"
                activate_sound "audio/SFX_MMClick.wav"
            textbutton "Kitchen":
                action [SensitiveIf(kit_room_current), SetVariable("current_room", "Kitchen"), Jump("story_ch_02_investigation")]
                hovered [SetVariable("travel_preview", "LOC_PREV_KITCHEN")]
                text_style "action_button"
                hover_sound "audio/SFX_actionmenu_hover_2.wav"
                activate_sound "audio/SFX_MMClick.wav"
            textbutton "Max's Bedroom":
                action [SensitiveIf(max_room_current), SetVariable("current_room", "MaxRoom"), Jump("story_ch_02_investigation")]
                hovered [SetVariable("travel_preview", "LOC_PREV_MAXROOM")]
                text_style "action_button"
                hover_sound "audio/SFX_actionmenu_hover_2.wav"
                activate_sound "audio/SFX_MMClick.wav"
    imagebutton:
        auto "/images/button/btn_return_%s.png"
        pos (105,665)
        focus_mask "images/button/btn_actionmenu_mask.png"
        action [SensitiveIf(in_room), Hide("Travel_Menu"), Show(current_room + "Screen", wipeleft)]
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover.wav"
        activate_sound "audio/SFX_actionmenu_back.wav"
    frame:
        pos(460,160)
        background "images/BG/[travel_preview].png"
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"
    frame:
        pos (750,160)
        background "images/UI/UI_Pin.png"
    frame:
        pos (175,260)
        background "images/UI/UI_String.png"

screen Inventory_Menu:
    $ item_preview = "NONE"
    #Inventory
    frame:
        pos (128,256)
        background "images/UI/UI_Action_2_BG.png"
        text "Inventory":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            pos (45,150)
            spacing -4
            if inv_ID_get == True:
                textbutton "Student I.D.":
                    action [SensitiveIf(in_room), SetVariable("inv_current_selected", "student_id"), SetVariable("item_preview", "ID"),  SetVariable("in_room", False), Show("Inventory_Menu_dropdown", wipedown)]
                    hovered [SetVariable("item_preview", "ID")]
                    text_style "action_button"
                    hover_sound "audio/SFX_actionmenu_hover_2.wav"
                    activate_sound "audio/SFX_actionmenu_show_2.wav"
            if inv_key_get == True:
                textbutton "Spare Bedroom Key":
                    action [SensitiveIf(in_room), SetVariable("inv_current_selected", "spare_key"), SetVariable("item_preview", "KEY"),  SetVariable("in_room", False), Show("Inventory_Menu_dropdown", wipedown)]
                    hovered [SetVariable("item_preview", "KEY")]
                    text_style "action_button"
                    hover_sound "audio/SFX_actionmenu_hover_2.wav"
                    activate_sound "audio/SFX_actionmenu_show_2.wav"
            if inv_luminol_get == True:
                textbutton "Luminol Testing Fluid":
                    action [SensitiveIf(in_room), SetVariable("inv_current_selected", "luminol"), SetVariable("item_preview", "LUMINOL"), SetVariable("in_room", False), Show("Inventory_Menu_dropdown", wipedown)]
                    hovered [SetVariable("item_preview", "LUMINOL")]
                    text_style "action_button"
                    hover_sound "audio/SFX_actionmenu_hover_2.wav"
                    activate_sound "audio/SFX_actionmenu_back_2.wav"
    #Return Button
    imagebutton:
        auto "/images/button/btn_return_%s.png"
        pos (105,665)
        focus_mask "images/button/btn_actionmenu_mask.png"
        action [SetVariable("inv_current_selected", ""), SetVariable("in_room", True), Hide("Inventory_Menu"), Hide( "Inventory_Menu_dropdown", irisout), Show(current_room + "Screen", wipeleft)]
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover.wav"
        activate_sound "audio/SFX_actionmenu_back.wav"
    #Item Preview Display
    frame:
        pos(480,180)
        background "images/UI/UI_Action_3_BG.png"
        frame:
            pos (64,83)
            background "images/props/ITEM_PREVIEW_[item_preview].png"
    #Item Name Display
    frame:
        pos(445,160)
        background "images/UI/UI_Action_5_BG.png"
        if inv_current_selected == "student_id":
            text "Student I.D.":
                color "#646457"
                pos (20,37)
                kerning -2
                bold True
                size 22
        elif inv_current_selected == "spare_key":
            text "Spare Key":
                color "#646457"
                pos (20,37)
                kerning -2
                bold True
                size 22
        elif inv_current_selected == "luminol":
            text "Luminol Testing Fluid":
                color "#646457"
                pos (20,37)
                kerning -2
                bold True
                size 20
        else:
            text "No Item Selected":
                color "#646457"
                pos (20,37)
                kerning -2
                bold True
                size 22
    #Burloloy
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"
    frame:
        pos (750,160)
        background "images/UI/UI_Pin.png"
    frame:
        pos (175,260)
        background "images/UI/UI_String.png"

screen Inventory_Menu_dropdown:
    frame:
        pos (480, 680)
        background "images/UI/UI_Action_4_BG.png"
        text "What would you like to do?":
            pos (35,25)
            color "#8D1B1A"
            size 30
        hbox:
            pos (24,65)
            spacing -10
            imagebutton:
                auto "/images/button/btn_examine_%s.png"
                focus_mask "images/button/btn_inventorydropdown_mask.png"
                action [Hide("Inventory_Menu"), Hide( "Inventory_Menu_dropdown", irisout), Call(inv_current_selected + "_examine")]
                hover_sound "audio/SFX_actionmenu_hover_3.wav"
                activate_sound "audio/SFX_MMClick.wav"
            imagebutton:
                auto "/images/button/btn_use_%s.png"
                focus_mask "images/button/btn_inventorydropdown_mask.png"
                action [Hide("Inventory_Menu"), Hide( "Inventory_Menu_dropdown", irisout), Call(inv_current_selected + "_use")]
                hover_sound "audio/SFX_actionmenu_hover_3.wav"
                activate_sound "audio/SFX_MMClick.wav"
            imagebutton:
                auto "/images/button/btn_back_%s.png"
                focus_mask "images/button/btn_inventorydropdown_mask.png"
                action [SetVariable("inv_current_selected", ""),  SetVariable("in_room", True), Hide("Inventory_Menu_dropdown", irisout)]
                hover_sound "audio/SFX_actionmenu_hover_3.wav"
                activate_sound "audio/SFX_actionmenu_back_2.wav"
    frame:
        pos (890,620)
        background "images/UI/UI_Pin.png"
    frame:
        pos (772,265)
        background "images/UI/UI_String_2.png"

label Inventory_Menu_callback:
    $in_room = True

    play sound "audio/SFX_actionmenu_back_2.wav"
    call screen Inventory_Menu with wipedown

    return

label SearchMode:

    $ default_mouse = "mode_search_def"
    $ in_room = True
    $ renpy.transition(dissolve)
    $ renpy.call_screen(current_room + "Search")

    return

#Location Search Screens

screen LivingRoomSearch:
    frame:
        pos (35,35)
        background "images/UI/UI_SearchMode_Overlay.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 120
        ypos 1030
        auto "/images/button/btn_back_%s.png"
        action [SensitiveIf(in_room), Hide(current_room + "Search", dissolve), SetVariable("default_mouse", "mouse"), Show(current_room + "Screen", wipedown)]
        hovered  SetVariable ("default_mouse", "mouse")
        unhovered SetVariable ("default_mouse", "mode_search_def")
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover_3.wav"
        activate_sound "audio/SFX_actionmenu_back_2.wav"
    
    #Inspect Window
    if searched_LivRoom_window == False:
        imagebutton:
            anchor(0.5,0.5)
            padding(0,75)
            pos (1222,340)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_window")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding(0,75)
            pos (1222,340)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_window")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
        
    #Inspect Couch
    if searched_LivRoom_couch == False:
        imagebutton:
            anchor(0.5,0.5)
            padding(250,100)
            pos (1555,893)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_couch")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else: 
        imagebutton:
            anchor(0.5,0.5)
            padding(250,100)
            pos (1555,893)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_couch")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
        
    #Inspect Curtain
    if searched_LivRoom_curtain == False:
        imagebutton:
            anchor(0.5,0.5)
            padding(0,150)
            pos (869,450)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_curtain")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding(0,150)
            pos (869,450)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_curtain")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
        
    #Inspect Safebox
    if searched_LivRoom_safebox == False:
        imagebutton:
            anchor(0.5,0.5)
            pos (1050,550)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_safebox")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            pos (1050,550)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_living_safebox")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

screen DiningRoomSearch:
    frame:
        pos (35,35)
        background "images/UI/UI_SearchMode_Overlay.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 120
        ypos 1020
        auto "/images/button/btn_back_%s.png"
        action [SensitiveIf(in_room), Hide(current_room + "Search", dissolve), SetVariable("default_mouse", "mouse"), Show(current_room + "Screen", wipedown)]
        hovered  SetVariable ("default_mouse", "mouse")
        unhovered SetVariable ("default_mouse", "mode_search_def")
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover_3.wav"
        activate_sound "audio/SFX_actionmenu_back_2.wav"
    
    #Inspect Plates
    if searched_DinRoom_plate == False:
        imagebutton:
            anchor(0.5,0.5)
            padding(100,0)
            pos (907,512)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_dining_plates")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding(100,0)
            pos (907,512)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_dining_plates")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    
    #Inspect Calendar
    if searched_DinRoom_calendar == False:    
        imagebutton:
            anchor(0.5,0.5)
            pos (810,190)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_dining_calendar")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            pos (810,190)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_dining_calendar")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

screen KitchenSearch:
    frame:
        pos (35,35)
        background "images/UI/UI_SearchMode_Overlay.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 120
        ypos 1020
        auto "/images/button/btn_back_%s.png"
        action [SensitiveIf(in_room), Hide(current_room + "Search", dissolve), SetVariable("default_mouse", "mouse"), Show(current_room + "Screen", wipedown)]
        hovered  SetVariable ("default_mouse", "mouse")
        unhovered SetVariable ("default_mouse", "mode_search_def")
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover_3.wav"
        activate_sound "audio/SFX_actionmenu_back_2.wav"
    
    #Inspect Pots
    if searched_KitRoom_pots == False:
        imagebutton:
            anchor(0.5,0.5)
            padding(50,0)
            pos (1535,450)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_pots")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding(50,0)
            pos (1535,450)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_pots")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
            
    #Inspect Dishes
    if searched_KitRoom_dishes == False:
        imagebutton:
            anchor(0.5,0.5)
            pos (1823,574)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_dishes")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            pos (1823,574)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_dishes")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
        
    #Inspect Fridge
    if searched_KitRoom_fridge == False:
        imagebutton:
            anchor(0.5,0.5)
            padding(100,230)
            pos (170,521)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_fridge")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding(100,230)
            pos (170,521)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_fridge")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
            
    #Inspect Journal
    if searched_KitRoom_journal == False:
        imagebutton:
            anchor(0.5,0.5)
            pos (381,922)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_journal")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            pos (381,922)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_kitchen_journal")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

screen MaxRoomSearch:
    frame:
        pos (35,35)
        background "images/UI/UI_SearchMode_Overlay.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 120
        ypos 1020
        auto "/images/button/btn_back_%s.png"
        action [SensitiveIf(in_room), Hide(current_room + "Search", dissolve), SetVariable("default_mouse", "mouse"), Show(current_room + "Screen", wipedown)]
        hovered  SetVariable ("default_mouse", "mouse")
        unhovered SetVariable ("default_mouse", "mode_search_def")
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover_3.wav"
        activate_sound "audio/SFX_actionmenu_back_2.wav"
    
    #Inspect Window
    if location_maxroom_locked == False:
        if searched_MaxRoom_window == False:
            imagebutton:
                anchor(0.5,0.5)
                padding(0,80)
                pos (1066,465)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_window")]
                hovered  SetVariable ("default_mouse", "mode_search_not")
                unhovered SetVariable ("default_mouse", "mode_search_def")
        else:
            imagebutton:
                anchor(0.5,0.5)
                padding(0,80)
                pos (1066,465)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_window")]
                hovered  SetVariable ("default_mouse", "mode_search_done")
                unhovered SetVariable ("default_mouse", "mode_search_def")
                
        #Inspect picture
        if searched_MaxRoom_picture == False:
            imagebutton:
                anchor(0.5,0.5)
                pos (1660,623)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_picture")]
                hovered  SetVariable ("default_mouse", "mode_search_not")
                unhovered SetVariable ("default_mouse", "mode_search_def")
        else:
            imagebutton:
                anchor(0.5,0.5)
                pos (1660,623)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_picture")]
                hovered  SetVariable ("default_mouse", "mode_search_done")
                unhovered SetVariable ("default_mouse", "mode_search_def")
            

        #Inspect Bed
        if searched_MaxRoom_bed == False:
            imagebutton:
                anchor(0.5,0.5)
                padding(100,0,250,0)
                pos (940,880)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_bed")]
                hovered  SetVariable ("default_mouse", "mode_search_not")
                unhovered SetVariable ("default_mouse", "mode_search_def")
        else:
            imagebutton:
                anchor(0.5,0.5)
                padding(100,0,250,0)
                pos (940,880)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_bed")]
                hovered  SetVariable ("default_mouse", "mode_search_done")
                unhovered SetVariable ("default_mouse", "mode_search_def")
                
        #Inspect Plant
        if searched_MaxRoom_plant == False:
            imagebutton:
                anchor(0.5,0.5)
                padding(0,0,0,80)
                pos (382,581)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_plant")]
                hovered  SetVariable ("default_mouse", "mode_search_not")
                unhovered SetVariable ("default_mouse", "mode_search_def")
        else:
            imagebutton:
                anchor(0.5,0.5)
                padding(0,0,0,80)
                pos (382,581)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_plant")]
                hovered  SetVariable ("default_mouse", "mode_search_done")
                unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        if searched_MaxRoom_door == False:
            imagebutton:
                anchor(0.5,0.5)
                padding(200,350)
                pos (960,540)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_door")]
                hovered  SetVariable ("default_mouse", "mode_search_not")
                unhovered SetVariable ("default_mouse", "mode_search_def")
        else:
            imagebutton:
                anchor(0.5,0.5)
                padding(200,350)
                pos (960,540)
                idle "images/area_search.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_maxroom_door")]
                hovered  SetVariable ("default_mouse", "mode_search_done")
                unhovered SetVariable ("default_mouse", "mode_search_def")

screen JobertHouseSearch:
    frame:
        pos (35,35)
        background "images/UI/UI_SearchMode_Overlay.png"
    
    if searched_JobHouse_table == False:
        imagebutton:
            anchor(0.5,0.5)
            padding (120,120)
            pos (715,535)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_table")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding (120,120)
            pos (715,535)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_table")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    
    if searched_JobHouse_pile == False:
        imagebutton:
            anchor(0.5,0.5)
            padding (100,10,120,100)
            pos (250,850)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_pile")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding (100,10,120,100)
            pos (250,850)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_pile")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

    if searched_JobHouse_beam == False:
        imagebutton:
            anchor(0.5,0.5)
            padding (300,20)
            pos (1580,80)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_beam")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding (300,20)
            pos (1580,80)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_beam")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

    if searched_JobHouse_stairs == False:
        imagebutton:
            anchor(0.5,0.5)
            padding (150,150)
            pos (1310,580)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_stairs")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            padding (150,150)
            pos (1310,580)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_stairs")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

    if searched_JobHouse_easel == False:
        imagebutton:
            anchor(0.5,0.5)
            pos (1675,1000)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_easel")]
            hovered  SetVariable ("default_mouse", "mode_search_not")
            unhovered SetVariable ("default_mouse", "mode_search_def")
    else:
        imagebutton:
            anchor(0.5,0.5)
            pos (1675,1000)
            idle "images/area_search.png"
            action [SensitiveIf(in_room), SetVariable("default_mouse", "mouse"), Hide(current_room + "Search", dissolve), Call ("inspect_jobhouse_easel")]
            hovered  SetVariable ("default_mouse", "mode_search_done")
            unhovered SetVariable ("default_mouse", "mode_search_def")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 120
        ypos 1020
        auto "/images/button/btn_back_%s.png"
        action [SensitiveIf(in_room), Hide(current_room + "Search", dissolve), SetVariable("default_mouse", "mouse"), Show(current_room + "Screen", wipedown)]
        hovered  SetVariable ("default_mouse", "mouse")
        unhovered SetVariable ("default_mouse", "mode_search_def")
        keysym "K_ESCAPE"
        hover_sound "audio/SFX_actionmenu_hover_3.wav"
        activate_sound "audio/SFX_actionmenu_back_2.wav"

#Location Main Screens

screen LivingRoomScreen():
    
    
    frame:
        pos (128,256)
        background "images/UI/UI_Action_BG.png"
        text "Living Room":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            ypos 130
            spacing -5
            imagebutton:
                xpos 40
                auto "/images/button/btn_travel_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("in_room", "True"), Hide(current_room + "Screen",), ShowTransient("Travel_Menu", wiperight)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            imagebutton:
                xpos 25
                auto "/images/button/btn_inspect_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mode_search_def"), Hide(current_room + "Screen"), Show(current_room + "Search", wipedown)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            if inventory_visible == True:
                imagebutton:
                    xpos 40
                    auto "/images/button/btn_bag_%s.png"
                    focus_mask "images/button/btn_actionmenu_mask.png"
                    action [SensitiveIf(in_room), Hide(current_room + "Screen"), Show("Inventory_Menu", wiperight)]
                    hover_sound "audio/SFX_actionmenu_hover.wav"
                    activate_sound "audio/SFX_actionmenu_show.wav"
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"

screen DiningRoomScreen():
    frame:
        pos (128,256)
        background "images/UI/UI_Action_BG.png"
        text "Dining Room":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            ypos 130
            spacing -5
            imagebutton:
                xpos 40
                auto "/images/button/btn_travel_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("in_room", "True"), Hide(current_room + "Screen",), ShowTransient("Travel_Menu", wiperight)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            imagebutton:
                xpos 25
                auto "/images/button/btn_inspect_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mode_search_def"), Hide(current_room + "Screen"), Show(current_room + "Search", wipedown)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            if inventory_visible == True:
                imagebutton:
                    xpos 40
                    auto "/images/button/btn_bag_%s.png"
                    focus_mask "images/button/btn_actionmenu_mask.png"
                    action [SensitiveIf(in_room), Hide(current_room + "Screen"), Show("Inventory_Menu", wiperight)]
                    hover_sound "audio/SFX_actionmenu_hover.wav"
                    activate_sound "audio/SFX_actionmenu_show.wav"
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"

screen KitchenScreen():
    frame:
        pos (128,256)
        background "images/UI/UI_Action_BG.png"
        text "Kitchen":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            ypos 130
            spacing -5
            imagebutton:
                xpos 40
                auto "/images/button/btn_travel_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("in_room", "True"), Hide(current_room + "Screen",), ShowTransient("Travel_Menu", wiperight)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            imagebutton:
                xpos 25
                auto "/images/button/btn_inspect_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mode_search_def"), Hide(current_room + "Screen"), Show(current_room + "Search", wipedown)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            if inventory_visible == True:
                imagebutton:
                    xpos 40
                    auto "/images/button/btn_bag_%s.png"
                    focus_mask "images/button/btn_actionmenu_mask.png"
                    action [SensitiveIf(in_room), Hide(current_room + "Screen"), Show("Inventory_Menu", wiperight)]
                    hover_sound "audio/SFX_actionmenu_hover.wav"
                    activate_sound "audio/SFX_actionmenu_show.wav"
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"

screen MaxRoomScreen():
    frame:
        pos (128,256)
        background "images/UI/UI_Action_BG.png"
        text "Max's Room":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            ypos 130
            spacing -5
            imagebutton:
                xpos 40
                auto "/images/button/btn_travel_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("in_room", "True"), Hide(current_room + "Screen",), ShowTransient("Travel_Menu", wiperight)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            imagebutton:
                xpos 25
                auto "/images/button/btn_inspect_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mode_search_def"), Hide(current_room + "Screen"), Show(current_room + "Search", wipedown)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            if inventory_visible == True:
                imagebutton:
                    xpos 40
                    auto "/images/button/btn_bag_%s.png"
                    focus_mask "images/button/btn_actionmenu_mask.png"
                    action [SensitiveIf(in_room), Hide(current_room + "Screen"), Show("Inventory_Menu", wiperight)]
                    hover_sound "audio/SFX_actionmenu_hover.wav"
                    activate_sound "audio/SFX_actionmenu_show.wav"
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"

screen JobertHouseScreen():
    frame:
        pos (128,256)
        background "images/UI/UI_Action_BG.png"
        text "Jobert's House":
            pos (45,85)
            color "#8D1B1A"
            size 30
        vbox:
            ypos 130
            spacing -5
            imagebutton:
                xpos 40
                auto "/images/button/btn_inspect_%s.png"
                focus_mask "images/button/btn_actionmenu_mask.png"
                action [SensitiveIf(in_room), SetVariable("default_mouse", "mode_search_def"), Hide(current_room + "Screen"), Show(current_room + "Search", wipedown)]
                hover_sound "audio/SFX_actionmenu_hover.wav"
                activate_sound "audio/SFX_actionmenu_show.wav"
            if inventory_visible == True:
                imagebutton:
                    xpos 25
                    auto "/images/button/btn_bag_%s.png"
                    focus_mask "images/button/btn_actionmenu_mask.png"
                    action [SensitiveIf(in_room), Hide(current_room + "Screen"), Show("Inventory_Menu", wiperight)]
                    hover_sound "audio/SFX_actionmenu_hover.wav"
                    activate_sound "audio/SFX_actionmenu_show.wav"
    frame:
        pos (155,235)
        background "images/UI/UI_Pin.png"

label EndGame:
    MC "Let's finish the game!"

    return

#Inspect Mode Dialogue Events

#Living Room

label inspect_living_window:
    if searched_LivRoom_window == False:
        #First Interaction
        window show
        pause 0.5

        show azzi - confused
        with dissolve
        show dy - thinking at offscreenleft

        pause 0.5 
        azzi "Inspector.
        {w=0.5}There’s something {=hl}weird{/=hl} here."
        window hide

        pause 0.5

        show azzi at offscreenright
        show dy at center
        with decay10inleft

        pause 0.5
        show item_phone at halfleft
        with irisin

        window show
        d "Yes,
        {w=0.5}I told you the{nw}"
        play sound SFX_Mystery
        extend " {=hl}files are on top of my desk{/=hl}." with sshake
        window hide

        pause 0.5
        hide item_phone
        with irisout
        show azzi at center
        show dy at offscreenleft
        with decay10inleft
        pause 0.5

        window show
        MC "Yeah it looks like it’s been{nw}"
        play sound SFX_Foreshadow
        extend" {=hl}wiped{/=hl}?
        {w=0.5}It’s awfully clean here compared to the others." with sflash
        
        MC "Hey Inspector you should check this out."
        window hide

        pause 0.5

        show azzi at offscreenright
        show dy - angry at center
        with decay10inleft

        pause 0.5
        show item_phone at halfleft
        with irisin

        window show
        play sound SFX_Idea
        d "It’s not on the desk?{w=0.5}{nw}" with sflash
        play sound SFX_Smack
        extend " Well did you try looking below the desk?" with sshake
        window hide

        pause 0.5
        hide item_phone
        with irisout
        show azzi at center
        show dy at offscreenleft
        with decay10inleft
        pause 0.5

        window show
        azzi "He’s {=hl}engrossed with that phone call{/=hl} of his.
        {w=0.5}Wonder what’s the problem?"

        show azzi - neutral
        with dissolve

        azzi "We should {=hl}take note of this window{/=hl} for later"

        MC "On it."
        window hide
        
        pause 0.5
        
        hide azzi
        with dissolve

        pause 0.5
        $searched_LivRoom_window = True
    else:
        #Subsequent Interaction
        pause 0.5
        show azzi - confused
        with dissolve
        window show
        MC "It looks like it’s been {=hl}wiped{/=hl}?
        {w=0.5} It’s awfully clean here compared to the others."
        
        show azzi - neutral
        with dissolve
        
        azzi "We should {=hl}take note of this window{/=hl} for later"
        window hide
        
        pause 0.5
        
        hide azzi
        with dissolve

    jump SearchMode

label inspect_living_couch:
    if searched_LivRoom_couch == False:
        #First Interaction
        pause 0.5
        
        show azzi - neutral
        with dissolve

        window show
        MC "The sofa is still as {=hl}soft{/=hl} as the time we bought it when I was a little kid."

        show azzi - confused
        with dissolve

        azzi "You still remember how soft the couch is?
        {w=0.5}What a memory you got there."
        window hide

        hide azzi
        with dissolve

        pause 0.5
        $searched_LivRoom_couch = True
    else:
        #Subsequent Interaction
        pause 0.5
        window show
        MC "The sofa is still as {=hl}soft{/=hl} as the time we bought it when I was a little kid."
        window hide
        pause 0.5

    jump SearchMode
    
label inspect_living_curtain:
    if searched_LivRoom_curtain == False:
        #First Interaction
        pause 0.5

        show dy - thinking at center
        show azzi - neutral at offscreenleft
        with dissolve

        pause 0.5

        window show
        show dy - surprised
        play sound SFX_Idea
        MC "Hey Inspector!
        {w=0.5}Look here.
        {w=0.5}The curtain is {=hl}slightly torn apart{/=hl}." with sflash

        show dy - neutral
        with dissolve

        d "Azzi,
        {w=0.5}come here take a photo of this curtain this will be useful."

        show azzi at left
        show dy at right
        with decay10inleft
        pause 0.25
        show azzi - happy
        with dissolve

        azzi "Right on it,
        {w=0.5}Sir!"

        MC "{=hl}Signs of distress{/=hl}.
        {w=0.5}This was probably torn when {=hl}Auntie Cheng{/=hl} was fighting for her life."
        window hide

        hide dy
        hide azzi
        with dissolve

        pause 0.5

        $searched_LivRoom_curtain = True
    else:
        #Subsequent Interaction
        pause 0.5

        window show 
        MC "{=hl}Signs of distress{/=hl}.
        {w=0.5}This was probably torn when {=hl}Auntie Cheng{/=hl} was fighting for her life."
        window hide 

        pause 0.5
    jump SearchMode

label inspect_living_safebox:
    if searched_LivRoom_safebox == False:
        #First Interaction
        $Auntie = "Auntie"
        $LivRoom_safebox_code = "0000"
        pause 0.5

        show azzi - smug
        with dissolve

        pause 1.0
        window show

        azzi "Hey Max!{w=0.5} Is this the {=hl}safebox{/=hl} you were talking about?"
        window hide
        pause 0.5
        show item_safelocked  at truecenter
        with irisin

        pause 1.0
        window show
        MC "Yeah this is it
        {w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}Wait a second there’s a {=hl}passcode{/=hl} for this?"
        window hide
        
        pause 0.5
        play sound SFX_Sweep
        pause 1
        show bg-intmaxbedroomnightpast
        show chengpast - confused
        with sflash
        
        hide item_safelocked
        pause 0.5

        window show

        side_cheng "I have to apologize however. Remember me being not good with {=hl}locking{/=hl}?"
        
        side_cheng "Well I {=hl}forgot the code to the safebox{/=hl}. I’ve {=hl}written it somewhere{/=hl} but forgetful auntie strikes again I guess."

        show chengpast - happy
        with dissolve

        side_cheng "Future problem for the both of us, am I right?"
        window hide

        pause 0.5
        play sound SFX_Sweep
        pause 1
        hide bg-intmaxbedroomnightpast
        hide chengpast
        show azzi - sad
        with sflash

        pause 1.0

        window show
        MC "Geez,
        {w=0.5}it needs a code!"

        show azzi at left
        with decay10inleft

        show dy - thinking at right
        with dissolve

        d "Try putting my {=hl}birthday{/=hl} on it?"
        window hide
        
        pause 0.5

        window show
        MC "{cps=*0.15}...{/cps}{w=0.5}{nw}"
        show dy - surprised
        show azzi - confused
        play sound SFX_Idea
        extend " Why would something from my house have your birthday as a passcode?" with sflash

        show dy - smug
        with dissolve

        d "I’m {=hl}very popular{/=hl} as you can see.
        {w=0.5}Surely people have my birthdate as their code somehow."
        
        pause 1.0

        show dy - annoyed
        show azzi - happy
        play sound SFX_Smack
        MC "That’s as real as Santa Claus gets!" with sshake

        show azzi - confused
        with dissolve

        azzi "When’s your birthday anyway,
        {w=0.5} I believe I haven’t even asked you that?"

        show dy - smug

        d "Finally!
        {w=0.5}someone asks.
        {w=0.5}It’s Nov-" with sshake

        play sound SFX_Idea
        MC "Inspector the code’s not your birthday!
        {w=0.5} trust me on this." with sflash
        
        show dy - annoyed
        with dissolve

        d "Sigh{cps=*0.15}...{/cps}"

        MC "Hmmm{cps=*0.15}...{/cps}
        {w=0.5} let me try something out"
        window hide

        pause 0.5

        hide dy
        hide azzi
        with dissolve

        pause 0.5
        show item_safelocked  at truecenter
        with irisin

        pause 0.5
        window show
        #INPUT PROMPT
        $LivRoom_safebox_code = renpy.input("I think I know the code for this safebox!{p}(Press Enter to continue.)", default="0000", allow="0123456789", length=4)
        window hide

        if LivRoom_safebox_code == "0704":
            $LivRoom_safebox_locked = False
            $inv_key_get = True
            call inspect_living_safebox_success from _call_inspect_living_safebox_success
        else:
            call inspect_living_safebox_fail from _call_inspect_living_safebox_fail
        
        $LivRoom_safebox_code = "0000"
        $searched_LivRoom_safebox = True
    elif searched_LivRoom_safebox == True and LivRoom_safebox_locked == True:
        #Subsequent Interaction
        pause 0.5
        window show
        MC "The safebox needs a code.
        {w=0.5} Hmmm…
        {w=0.5} let me try something out"
        window hide
        pause 0.5

        pause 0.5
        show item_safelocked at truecenter
        with irisin
        
        pause 0.5
        window show
        #INPUT PROMPT
        $LivRoom_safebox_code = renpy.input("I think I know the code for this safebox! (Press Enter to continue.)", default="0000", allow="0123456789", length=4)
        window hide

        if LivRoom_safebox_code == "0704":
            $LivRoom_safebox_locked = False
            $inv_key_get = True
            call inspect_living_safebox_success from _call_inspect_living_safebox_success_1
        else:
            call inspect_living_safebox_fail from _call_inspect_living_safebox_fail_1
        $LivRoom_safebox_code = "0000"
    elif searched_LivRoom_safebox == True and LivRoom_safebox_locked == False:
        #SUBSEQUENT INTERACTION IF SAFEBOX IS UNLOCKED
        pause 0.5
        window show
        MC "{=txt_vo}(I’ve already unlocked the safebox and got the spare key for my bedroom.)"

        MC "{=txt_vo}(I should go and use it so we can investigate my room.)"
        window hide
        pause 0.5
    jump SearchMode

label inspect_living_safebox_success: 
    stop music fadeout 1.0

    pause 1.5
    
    play sound SFX_safeboxunlocked
    show item_safeunlocked  at truecenter
    with sshake

    pause 1.5
    window show
    play sound SFX_Idea
    MC "I got it!
    {w=0.5}So it was {=hl}Auntie Cheng’s birthday{/=hl} after all.
    {w=0.5}I have to tell her to make a new passcode for this one later on." with sflash
    
    MC"Sorry Dy,
    {w=0.5}the passcode wasn’t your birthday."

    play sound SFX_Mystery
    show dy - annoyed at right
    show azzi - happy at left
    with dissolve

    pause 0.5
    d "I am honestly saddened."

    show azzi - neutral
    with dissolve
    azzi "Great,
    {w=0.5}so are your {=hl}keys{/=hl} in there?"


    MC "Let me check."
    window hide
    pause 0.5
    window show
    play sound SFX_Idea
    MC "They are!
    {w=0.5}That’s Great!" with sflash
    window hide

    pause 1.0

    play sound SFX_Fanfare_Item

    hide item_safelocked
    hide item_safeunlocked
    with irisout

    show item_key at truecenter
    with irisin

    pause 1.0

    window show
    sys_nar "You’ve obtained {=hl}Max’s Spare Bedroom Key{/=hl}
    {w=0.5}Use it to open Max’s locked door."
    window hide

    pause 0.5

    hide item_key
    with irisout
    play music BGM_casual fadein 1.0

    pause 0.5
    window show

    MC "{=txt_vo}(Okay I'll put the key in my {=hl}bag{/=hl})"

    d "Let’s use it and inspect your room.
    {w=0.5}We might find something there of importance."

    window hide
    
    hide dy
    hide azzi
    with dissolve

    pause 0.5
    $searched_LivRoom_safebox = True
    jump story_ch_02_investigation

label inspect_living_safebox_fail:
    pause 0.5

    show item_safelocked at truecenter
    play sound SFX_wrong
    with sshake

    pause 1.0

    hide item_safelocked
    with irisout
    show azzi - confused
    with dissolve
    #SFX Fail Sound
    window show
    azzi"No dice? Too bad."

    MC "I think I have to {=hl}check around{/=hl} first."
    window hide
    hide azzi
    with dissolve
    
    pause 0.5
    return

#Dining Room

label inspect_dining_plates:
    if searched_DinRoom_plate == False:
        #First Interaction
        pause 0.5
        
        window show
        MC "{=txt_vo}(The food we ate for breakfast yesterday was left here on the table)"
        window hide
        pause 0.5
        show azzi - confused at left
        show dy - neutral at right
        with dissolve
        pause 0.5
        window show
        azzi "You guys love leaving your food on the table after eating? 
        {w=0.5}You don’t clean it up and put it inside the fridge?"

        show dy - confused
        with dissolve

        d "Yeah, 
        {w=0.5}would be a waste to throw leftovers if they go bad."

        MC "I think you guys are missing a teensy weensy detail that{cps=*0.15}...{/cps}{w=0.5}{nw}"
        play sound SFX_Idea
        extend " We literally got {=hl}broken in{/=hl} and Auntie Cheng had to go to the {=hl}hospital{/=hl} for a {=hl}concussion{/=hl},{w=0.5}{nw}" with sflash
        play sound SFX_Smack
        show dy - surprised
        show azzi - angry
        extend " right!?" with sshake

        show dy - thinking
        with dissolve

        d "Totally flew by my mind, 
        {w=0.5}sorry Max."

        show azzi - happy
        with dissolve

        azzi "Now that you’ve mentioned. 
        {w=0.5}Well, 
        {w=0.5}my bad!"

        MC "{=txt_vo}(These two are infuriating)"
        window hide

        hide azzi
        hide dy
        with dissolve
        
        pause 0.5
        
        $searched_DinRoom_plate = True
    else:
        #Subsequent Interaction
        pause 0.5
        
        window show
        MC "{=txt_vo}(The food we ate for breakfast yesterday was left here on the table)"
        window hide

        pause 0.5

    jump SearchMode

label inspect_dining_calendar:
    if searched_DinRoom_calendar == False:
        #First Interaction
        pause 0.5

        #SHOW CG of CALENDAR @ Truecenter
        show item_calendar at truecenter
        with dissolve
        pause 1.5

        window show
        azzi "It’s {=hl}June{/=hl} right now,
        {w=0.5}but why is your calendar set to{nw}"
        play sound SFX_Mystery
        extend " {=hl}July{/=hl}?"

        MC "I have no idea.{w=0.5}{nw}"
        play sound SFX_Idea
        extend " Wait a minute!" with sflash

        MC "The {=hl}4th date on the calendar is encircled{/=hl}. 
        {w=0.5}There’s also a{nw}"
        play sound SFX_Foreshadow
        extend " {=hl}very poorly drawn cake{/=hl} on it" with sflash

        azzi "{cps=*0.15}...{/cps}What could it mean?"
        window hide
        #HIDE CG of Calendar
        hide item_calendar
        with dissolve

        pause 0.5

        $searched_DinRoom_calendar = True
    else:
        #Subsequent Interaction
        pause 0.5

        show item_calendar at truecenter
        with dissolve
        pause 1.5

        window show
        MC "The {=hl}4th date on the calendar is encircled{/=hl}. 
        {w=0.5}There’s also a{nw}"
        play sound SFX_Foreshadow
        extend " {=hl}very poorly drawn cake{/=hl} on it" with sflash

        azzi "{cps=*0.15}...{/cps}What could it mean?"
        window hide

        hide item_calendar
        with dissolve

        pause 0.5

    jump SearchMode

#Kitchen

label inspect_kitchen_pots:
    if searched_KitRoom_pots == False:
        #First Interaction
        pause 0.5

        window show
        MC "{=txt_vo}(This smells good. 
        {w=0.5}Auntie Cheng is really a good cook.)"

        show dy - happy
        with dissolve

        d "MMMhmmm, 
        {w=0.5}That smells {=hl}delicious{/=hl}."

        show dy - smug
        with dissolve

        d "Hey Max. 
        {w=0.5}How about I set the table up and let's eat this for lunch?"

        MC "Sure- 
        {w=0.5}I mean{nw}"
        play sound SFX_Smack
        extend " no!{w=0.5}{nw}" with sshake
        extend" This was left here yesterday. 
        {w=0.5}Auntie Cheng must’ve been {=hl}preparing food{/=hl}."

        MC "This may smell good but you wouldn’t know if it went bad."

        show dy - annoyed
        with dissolve

        d "Awwww... 
        {w=0.5}Let’s try it anyway."

        play sound SFX_Idea
        show dy - surprised
        MC "Inspector! 
        {w=0.5}I think we should focus on our investigation." with sflash
        window hide

        hide dy
        with dissolve

        pause 0.5
        $searched_KitRoom_pots = True
    else:
        #Subsequent Interaction
        pause 0.5

        window show
        MC "{=txt_vo}(This smells good. 
        {w=0.5}Auntie Cheng is really a good cook.)"
        window hide

        pause 0.5

    jump SearchMode

label inspect_kitchen_dishes:
    if searched_KitRoom_dishes == False:
        #First Interaction
        pause 0.5

        show azzi - confused
        with dissolve

        pause 0.5

        window show
        azzi "Wasn’t Mrs. Malano cleaning this up when she heard that {=hl}noise{/=hl} upstairs?"

        MC "Yeah, 
        {w=0.5}she left it in the midst of the incident. 
        {w=0.5}Poor Auntie"

        MC "{=txt_vo}(Auntie Cheng really has a lot of work to do around the house.)"
        window hide

        hide azzi
        with dissolve

        pause 0.5

        $searched_KitRoom_dishes = True
    else:
        #Subsequent Interaction
        pause 0.5

        window show
        MC "{=txt_vo}(Auntie Cheng really has a lot of work to do around the house.)"
        window hide
        
        pause 0.5

    jump SearchMode

label inspect_kitchen_fridge:
    if searched_KitRoom_fridge == False:
        #First Interaction
        pause 0.5

        show azzi - happy
        with dissolve

        window show
        play sound SFX_Idea
        azzi "Let’s see if your fridge is stocked up!" with sflash

        MC "Hey{nw}"
        play sound SFX_Smack
        extend" wait! 
        {w=0.5}You can’t just rummage into other people’s fridge like that!" with sshake

        show azzi - smug
        with dissolve

        azzi "I already did. 
        {w=0.5}You’ve got a lot of stuff here. 
        {w=0.5}We should cook something up."

        MC "Uhhh nope."

        MC "{=txt_vo}(The groceries Wynona brought remained untouched.)"
        window hide

        hide azzi
        with dissolve

        pause 0.5
        $searched_KitRoom_fridge = True
    else:
        #Subsequent Interaction
        pause 0.5

        window show
        MC "{=txt_vo}(The groceries Wynona brought remained untouched.)"
        window hide

        pause 0.5

    jump SearchMode

label inspect_kitchen_journal:
    if searched_KitRoom_journal == False:
        #First Interaction
        pause 0.5

        show dy - thinking at right
        show azzi - neutral at left
        with dissolve
        window show
        d "Hey look, 
        {w=0.5}there’s a {=hl}journal{/=hl} here"
        window hide

        pause 0.5
        #SHOW CG OF JOURNAL
        show item_journal at truecenter
        with dissolve
        pause 1.5
        hide item_journal
        with dissolve
        pause 0.5

        show azzi - confused
        with dissolve
        window show
        azzi "”{=hl}Auntie Cheng’s Journal of Wild Experiences{/=hl}”
        {w=0.5}Wow{w=0.5}{nw}"
        show azzi - happy
        show dy - confused
        play sound SFX_Idea
        extend " what a {=hl}title{/=hl}!" with sflash

        MC "I think we shouldn’t try to read that."

        show azzi - neutral
        with dissolve
        azzi "Entry: no. 37 Date: March 25, 1991. 
        {w=0.5}So today was a hot day in the {=hl}Boracay Islands{/=hl}! 
        {w=0.5}I had to wear my most exotic clothing at the beach to fight the heat."

        show dy - surprised
        with dissolve

        azzi "There was this guy, 
        {w=0.5}I’d say my age.{w=0.5}{nw}"
        play sound SFX_Mystery 
        extend " He was looking at me with those {=hl}piercing eyes{/=hl}-" with sflash

        show azzi - confused
        show dy - annoyed
        play sound SFX_Smack
        MC "OKAY OKAY! 
        {w=0.5}I think that’s enough story time for the day! 
        {w=0.5}Let’s put it back where it came from okay Azzi?" with sshake

        show azzi - angry
        play sound SFX_Idea
        azzi "Aww it was getting to the good part Max!" with sflash
        window hide

        pause 0.5

        window show
        show azzi - confused
        show dy - thinking
        with dissolve
        azzi "..."

        azzi "Wait, 
        {w=0.5}there’s a {nw}"
        play sound SFX_Foreshadow
        extend "{=hl}folded page{/=hl} here at the end. 
        {w=0.5}Let me check it" with sshake

        play sound SFX_Smack
        MC "Wait no you’ll probably see another-" with sshake

        play sound SFX_Idea
        azzi "Look at this Max! 
        {w=0.5}Look at what’s {=hl}written{/=hl}." with sflash
        window hide
        hide azzi
        hide dy
        with dissolve

        #SHOW IMAGE OF PAGE
        show item_journalpage at truecenter
        with dissolve
        pause 0.5
        window show
        "”I’m writing this down so I won’t forget. The code to the safebox for the spare keys is my {=hl}birth month{/=hl} then {=hl}birth date{/=hl}."
        
        "It’s the most obvious thing but it’s what’s in my head at the moment. I’ll think of something neat later on”"
        window hide
        
        pause 0.5
        
        window show
        MC "What?{w=0.5}{nw}"
        play sound SFX_Foreshadow
        extend" What could this {=hl}mean{/=hl}?" with sflash


        d "Could be a {=hl}hint{/=hl} or something."

        hide item_journalpage
        with dissolve
        #HIDE IMAGE OF PAGE

        pause 0.5
        window hide
        pause 0.5

        $searched_KitRoom_journal = True
    else:
        #Subsequent Interaction
        pause 0.5
        show item_journalpage at truecenter
        with dissolve
        pause 0.5
        window show
        "”I’m writing this down so I won’t forget. The code to the safebox for the spare keys is my {=hl}birth month{/=hl} then {=hl}birth date{/=hl}."
        
        "It’s the most obvious thing but it’s what’s in my head at the moment. I’ll think of something neat later on”"
        window hide
        
        pause 0.5
        
        window show
        MC "What?{w=0.5}{nw}"
        play sound SFX_Foreshadow
        extend" What could this {=hl}mean{/=hl}?" with sflash


        d "Could be a {=hl}hint{/=hl} or something."
        window hide

        #HIDE IMAGE OF PAGE
        hide item_journalpage
        with dissolve
        pause 0.5
        
        pause 0.5

    jump SearchMode

#Max Room

label inspect_maxroom_door:
    if searched_MaxRoom_door == False:
        #First Interaction
        pause 0.5
        window show
        MC "{=txt_vo}(It’s still weird how my door just up and {=hl}got itself locked{/=hl}.)"

        MC "{=txt_vo}(I’m pretty sure I left it {=hl}unlocked{/=hl} after I left to go eat lunch with Wynona and her mom.)"

        play sound SFX_Mystery
        show azzi - confused
        with dissolve
        azzi "Hey Max, what are we standing here for?
        {w=0.5}Have you gotten an idea to open this door?" with sshake

        MC "{=txt_vo}(Azzi’s right.
        {w=0.5}I have to find a way to unlock my bedroom door.)"
        window hide
        hide azzi
        with dissolve
        pause 0.5
    
        $searched_MaxRoom_door = True
    else:
        #Subsequent Interaction
        pause 0.5
        window show
        MC "{=txt_vo}(My door’s locked.
        {w=0.5}I have to find a way to unlock it.)"
        window hide
        hide azzi
        with dissolve
        pause 0.5
    jump SearchMode

label inspect_maxroom_window:
    if searched_MaxRoom_window == False:
        #First Interaction
        pause 0.5
        window show
        MC "{=txt_vo}(I can see a run down house from. I bet you could go there if you follow the trail by the long grass behind my house.)"
        window hide
        pause 0.5

        $searched_MaxRoom_window = True
    else:
        #Subsequent Interaction
        pause 0.5
        window show
        MC "{=txt_vo}(I can see a run down house from. I bet you could go there if you follow the trail by the long grass behind my house.)"
        window hide
        pause 0.5

    call event_MaxRoom_Luminol from _call_event_MaxRoom_Luminol

    jump SearchMode

label inspect_maxroom_picture:
    if searched_MaxRoom_picture == False:
        #First Interaction
        pause 0.5

        play sound SFX_Mystery
        show item_photoframe at truecenter
        with irisin

        pause 1.0

        window show
        MC "{=txt_vo}({cps=*0.15}...{/cps}{w=0.5}It’s a picture of {=hl}Lheona and I{/=hl})"
        window hide
        pause 1.0

        window show
        MC "{cps=*0.15}...{/cps}"
        window hide
        pause 0.5
        
        show dy - sad
        with dissolve
        pause 0.5

        window show
        d "{cps=*0.15}...{/cps}"
        window hide
        
        pause 0.5
        hide dy
        with dissolve
        pause 1.0

        show item_photoframe at halfleft
        with decay10inleft
        show azzi - confused
        play sound SFX_Mystery
        with dissolve

        window show
        azzi "Why’s everyone {=hl}quiet{/=hl} all of the sudden?"

        play sound SFX_Idea
        azzi "Wait,
        {w=0.5}who's that." with sflash

        MC "Ah!
        {w=0.5}It’s a picture of an old {=hl}friend and I{/=hl}."

        azzi "She definitely looks{nw}"
        play sound SFX_Foreshadow
        extend "{=hl} familiar{/=hl}."

        MC "Must be your{nw}"
        play sound SFX_Mystery
        extend "{=hl} imagination{/=hl}." with sshake

        azzi "Hmmm{cps=*0.15}...{/cps}
        {w=0.5}Maybe."
        window hide

        hide item_photoframe
        with irisout

        hide azzi
        with dissolve

        pause 0.5

        $searched_MaxRoom_picture = True
    else:
        #Subsequent Interaction
        pause 0.5
        window show
        MC "{=txt_vo}({cps=*0.15}...{/cps}{w=0.5}It’s a picture of {=hl}Lheona and I{/=hl})"
        window hide
        pause 0.5

    call event_MaxRoom_Luminol from _call_event_MaxRoom_Luminol_1

    jump SearchMode

label inspect_maxroom_plant:
    if searched_MaxRoom_plant == False:
        #First Interaction
        pause 0.5

        show dy - neutral at offscreenright
        show azzi - neutral
        with dissolve
        window show
        play sound SFX_Idea
        MC "Oh,
        {w=0.5}it’s my plant,
        {w=0.5}{=hl}Jeremy{/=hl}.
        {w=0.5}Good thing it wasn’t harmed." with sflash

        show azzi - confused
        with dissolve

        azzi "You named your plant {=hl}Jeremy{/=hl}?"

        MC "Yeah,
        {w=0.5}is something the matter?"

        azzi "No not really,
        {w=0.5}but you could’ve called it something more creative."

        MC "Like what?"

        show azzi - smug
        with dissolve

        azzi "I don’t know.
        {w=0.5}Maybe,{w=1.0}{nw}"
        play sound SFX_Mystery
        extend " {=hl}Jhemerlyn{/=hl}." with sflash
        window hide

        show azzi at left
        with decay10inleft
        show dy - smug at right
        with dissolve

        pause 0.5
        window show
        d "Or you could call it{w=1.0}{nw}"
        play sound SFX_Mystery
        extend " {=hl}Jebediah{/=hl}." with sflash

        MC "errr{cps=*0.15}...{/cps}
        {w=0.5}I think I’ll just stick with calling it {=hl}Jeremy{/=hl}."
        window hide

        hide azzi
        hide dy
        with dissolve

        pause 0.5

        $searched_MaxRoom_plant = True
    else:
        #Subsequent Interaction
        MC "Oh, it’s my plant, Jeremy. Good thing it wasn’t harmed"

    call event_MaxRoom_Luminol from _call_event_MaxRoom_Luminol_2

    jump SearchMode

label inspect_maxroom_bed:
    if searched_MaxRoom_bed == False:
        #First Interaction
        pause 0.5

        show dy - thinking
        with dissolve

        window show
        d "Honestly Max,
        {w=0.5}There doesn't seem to be {=hl}anything out of the ordinary{/=hl} in your room."

        d "I’m not really sure what we can find here{w=0.5}{cps=*0.15}...{/cps}"

        show dy - annoyed
        play sound SFX_Idea
        d "Max?
        {w=0.5}Are you listening?" with sflash
        window hide

        pause 0.5
        stop music fadeout 1.0

        window show
        d "{cps=*0.15}...{/cps}"
        window hide
        
        pause 0.5

        window show
        show dy - confused
        play sound SFX_Smack
        d "Max!?" with sshake

        MC "{=txt_vo}(Something’s{w=0.5}{nw}"
        play sound SFX_Mystery
        extend " {=hl}off{/=hl}{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}Wait a second.)" with sshake

        MC "{cps=*0.15}...{/cps}{w=0.5}{nw}"
        play sound SFX_Idea
        extend "!" with sflash

        MC "{=hl}Under the bed{/=hl}{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}Is that my{nw}"
        play sound SFX_Mystery
        extend " {=hl}bag{/=hl}?" with sshake

        MC "{=txt_vo}(I could’ve sworn my bag was at the end side of my bed.
        {w=0.5}Why’s it on the {=hl}floor{/=hl}?)"

        MC "{=txt_vo}(I should check it out.)"
        window hide
        
        pause 0.5
        play sound SFX_Foreshadow
        show item_maxbag_empty at truecenter
        with irisin
        #SHOW CG OF BAG WITH MISSING LETTER
        pause 2.5

        window show
        play sound SFX_Idea
        MC "{=txt_vo}(!{w=0.5}{nw}" with sflash
        extend " The {=hl}letter{/=hl}!
        {w=0.5}It’s{nw}"
        play sound SFX_Smack
        extend" {=hl}missing{/=hl}!)" with sshake
        window hide

        pause 1.0
        play music BGM_forbode fadein 1.0

        hide item_maxbag_empty
        with irisout
        #HIDE CG BAG
        pause 1.0

        show dy at right
        with decay10inleft
        show azzi - confused at left
        with dissolve

        pause 0.5

        window show
        azzi "Is something the matter,
        {w=0.5}Max?"

        MC "Something’s {=hl}missing{/=hl} from the bag I left here yesterday."

        show dy - surprised
        play sound SFX_Smack
        d "Wait what,
        {w=0.5}well what is it?" with sshake

        MC "It’s a{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}a {=hl}letter{/=hl}."

        show dy - angry
        d "A {=hl}letter{/=hl}!?
        {w=0.5}No wait,
        {w=0.5}so you’re telling me,
        {w=0.5}our {=hl}culprit{/=hl} was out here to steal a letter?" with sshake

        d "Are you sure that’s the only thing they took from here?"

        MC "{=hl}Nothing else was taken from our house{/=hl} as far as I can tell."

        show dy - annoyed
        with dissolve

        d "For heaven’s sake.
        {w=0.5}Mrs. Malano suffered a {=hl}concussion{/=hl} for a mere letter?
        {w=0.5}What even is that letter about if it’s really that important for one to steal?"

        MC "{=txt_vo}(Whoever stole my letter knows about its {=hl}content{/=hl}.
        {w=0.5}Does that mean{nw}"
        play sound SFX_Foreshadow
        extend" {=hl}someone knows{/=hl} I’m here to learn about the truth {=hl}5 years ago{/=hl}?)"with sshake

        MC "{=txt_vo}(This is bad,
        {w=0.5}if someone went out of their way to break in my house and hurt those who’re close to me,
        {w=0.5}then I should stay {=hl}cautious{/=hl})"

        show dy - confused
        play sound SFX_Idea
        d "Max?" with sflash

        MC "uhhh{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}I can’t say for now but that letter is {=hl}important{/=hl} to me.
        {w=0.5}I don’t know why someone would do this but I’m gonna make sure that I’d find out the truth."
        window hide
        pause 0.5

        show dy - neutral
        with dissolve

        pause 0.5
        window show
        d "Well,
        {w=0.5}if that’s so.
        {w=0.5}I won’t pry into it for now.
        {w=0.5}At Least we know now what the culprit’s goal was.
        {w=0.5}However you might need to divulge with us why this letter is so important in the future."

        MC "I understand Inspector."

        MC "{=txt_vo}(Who even wanted that letter?)"
        window hide

        stop music fadeout 1.0

        pause 1.5

        hide dy
        hide azzi
        with dissolve
        play music BGM_cool

        pause 0.5

        $searched_MaxRoom_bed = True
    else:
        #Subsequent Interaction
        pause 0.5

        window show
        MC "{=txt_vo}(The {=hl}letter{/=hl} from my bag went {=hl}missing{/=hl}.
        {w=0.5}I don’t know why someone would want to steal it.
        {w=0.5}What I do know is that {=hl}someone out there knows why I’m here{/=hl}.)"
        
        play sound SFX_Foreshadow
        MC "{=txt_vo}(I have to be {=hl}careful{/=hl} from here on out.)"
        window hide
        
        pause 0.5
    call event_MaxRoom_Luminol from _call_event_MaxRoom_Luminol_3
    
    jump SearchMode

#Jobert's House

label inspect_jobhouse_table:
    if searched_JobHouse_table == False:
        #Initial Dialogue
        pause 0.5
        show azzi - confused
        with dissolve
        window show
        azzi "Look at these{nw}"
        play sound SFX_Mystery
        extend " {=hl}religious figures{=hl}." with sflash

        show azzi at left
        with decay10inleft
        show dy - thinking at right
        with dissolve

        d "Looks like our owner’s a person of faith."

        MC "Honestly,
        {w=0.5}those figurines kind of creep me out."

        show azzi - neutral
        with dissolve

        azzi "There’s some {=hl}photos{/=hl} here as well,
        {w=0.5}must be the owners?"

        MC "Looks like a {=hl}man{/=hl} and his {=hl}wife{/=hl}.
        {w=0.5}They look happy {=hl}here{/=hl}."
        window hide

        show azzi - confused
        show dy - confused
        with dissolve
        stop music fadeout 1.0
        pause 2.0

        window show
        MC "{cps=*0.15}...{/cps}{w=0.5}{nw}"
        play sound SFX_Idea
        extend "!" with sflash

        MC "{=txt_vo}(Hmmm.
        {w=0.5}The {=hl}man{/=hl} in this picture.
        {w=0.5}I can’t help but feel like I’ve{nw}"
        play sound SFX_Mystery
        extend " {=hl}met{/=hl} him before.)" with sshake

        MC "{=txt_vo}(And for some reason it’s really making my blood {=hl}boil{/=hl})"

        show azzi - confused
        with dissolve

        azzi "Hey,
        {w=0.5}you okay Max?
        {w=0.5}You’ve been making weird faces."

        MC "No,
        {w=0.5}I’m fine.
        {w=0.5}It’s nothing really{w=0.5}{cps=*0.15}...{/cps}"

        azzi "Okay then."
        window hide

        hide azzi
        hide dy
        with dissolve

        play music BGM_mystery

        pause 0.5

        $searched_JobHouse_table = True
    else:
        #Subsequent Dialogue
        pause 0.5
        window show
        MC "{=txt_vo}(Hmmm.
        {w=0.5}The {=hl}man{/=hl} in this picture.
        {w=0.5}I can’t help but feel like I’ve {=hl}met{/=hl} him before.)"

        MC "(And for some reason it’s really making my blood {=hl}boil{/=hl})"
        window hide
        pause 0.5
    call event_JobertHouse_inspect from _call_event_JobertHouse_inspect

    jump SearchMode

label inspect_jobhouse_pile:
    if searched_JobHouse_pile == False:
        #Initial Dialogue
        pause 0.5
        window show
        MC "Hey look at this!"
        window hide

        pause 0.5
        play sound SFX_Mystery
        show dy - neutral
        with dissolve
        pause 0.5

        window show
        d "What’s up?
        {w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}It’s-
        {w=0.5}It’s a pile of {=hl}papers{/=hl}?"

        MC "Yeah,
        {w=0.5}but look at what’s on them.
        {w=0.5}Looks like a bunch of sketches.
        {w=0.5}It’s pretty neat"

        show dy - thinking
        with dissolve

        d "An artist huh?"

        d "There’s also other stuff here.
        {w=0.5}“Electricity Bill overdue”,
        {w=0.5}“Water Bill Overdue”,
        {w=0.5}and “Television Cable Bill Overdue”."

        show dy - annoyed
        with dissolve

        d "Well poor fella.
        {w=0.5}Somebody’s having bill problems.
        {w=0.5}Talk about relatable."

        MC "Err{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}That’s unfortunate."
        window hide

        hide dy
        with dissolve

        pause 0.5

        $searched_JobHouse_pile = True
        
    else:
        #Subsequent Dialogue
        pause 0.5
        window show
        MC "{=txt_vo}(There’s a bunch of {=hl}papers{/=hl} piled up here.
        {w=0.5}It’s a mix of beautifully drawn sketches and overdue bill notices.)"
        window hide
        pause 0.5
    call event_JobertHouse_inspect from _call_event_JobertHouse_inspect_1

    jump SearchMode

label inspect_jobhouse_beam:
    if searched_JobHouse_beam == False:
        #Initial Dialogue
        pause 0.5
        window show
        MC "What a weird design for that wooden beam."

        show azzi - confused
        with dissolve

        azzi "What?
        {w=0.5}Oh,
        {w=0.5}you mean that{nw}" 
        play sound SFX_Idea
        extend " support beam?" with sflash

        show azzi at left
        with decay10inleft
        show dy - thinking at right
        with dissolve

        d "I don’t think that’s a design choice for the house."

        show dy - confused
        with dissolve

        d "The support beam’s being held up with{nw}"
        play sound SFX_Mystery
        extend" {=hl}shoddy ropes{/=hl}." with sflash

        azzi "Do you think if that snaps,
        {w=0.5}would it make this house {=hl}collapse{/=hl} on us?"

        show dy - annoyed
        with dissolve

        d "I wouldn’t want to stick around to find out."
        window hide

        hide azzi
        hide dy
        with dissolve

        pause 0.5

        $searched_JobHouse_beam = True
    else:
        #Subsequent Dialogue
        pause 0.5
        window show
        MC "{=txt_vo}(The beam looks like it’s gonna collapse.
        {w=0.5}It’s only held up by {=hl}shoddy ropes{/=hl}.
        {w=0.5}I wouldn’t wanna be here if it snapped.)"
        window hide
        pause 0.5
    call event_JobertHouse_inspect from _call_event_JobertHouse_inspect_2

    jump SearchMode

label inspect_jobhouse_stairs:
    if searched_JobHouse_stairs == False:
        #Initial Dialogue
        pause 0.5

        show azzi - neutral
        with dissolve

        window show
        azzi "You think the owner’s upstairs?"

        show azzi - confused at left
        show dy - angry at right
        play sound SFX_Smack

        d "Hey you shouldn’t go up there!" with sshake

        show azzi - angry
        with dissolve

        azzi "Why?"

        show dy - confused
        with dissolve

        d "Look at the steps,
        {w=0.5}It’s rickety and isn’t even lined up properly.
        {w=0.5}Unless you want to have splinters if the planks snap and collapse,
        {w=0.5}then be my guest." with sshake

        show azzi - happy
        with dissolve

        azzi "On second thought,
        {w=0.5}I’ll just stay down here."
        window hide

        hide azzi
        hide dy
        with dissolve

        pause 0.5

        $searched_JobHouse_stairs = True
    else:
        #Subsequent Dialogue
        pause 0.5
        window show
        MC "{=txt_vo}(The stairs are unaligned.
        {w=0.5}I wouldn’t want to test if the steps are stable enough to carry my weight.)"
        window hide
        pause 0.5
    call event_JobertHouse_inspect from _call_event_JobertHouse_inspect_3

    jump SearchMode

label inspect_jobhouse_easel:
    if searched_JobHouse_easel == False:
        #Initial Dialogue
        pause 0.5
        window show
        MC "There’s a small easel in the corner here.
        {w=0.5}Do you think the owner has a kid?"

        show azzi - confused
        with dissolve

        azzi "Maybe.
        {w=0.5}But you know, the owners could also be{nw}"
        play sound SFX_Mystery
        extend " small?" with sflash

        MC "that's also a possibility."
        window hide

        pause 0.5

        window show
        show azzi at left
        show dy - angry at right
        play sound SFX_Smack
        d "Would you guys be kind enough and  focus on looking for the owner?
        {w=0.5}We don’t got all day here and I'm starving." with sshake

        MC "Okay,
        {w=0.5}okay{w=0.5}{cps=*0.15}...{/cps}"
        window hide

        hide azzi
        hide dy
        with dissolve

        pause 0.5

        $searched_JobHouse_easel = True

    else:
        #Subsequent Dialogue
        pause 0.5
        window show
        MC "{=txt_vo}(There’s a small easel in the corner here.
        {w=0.5}Seems the owners love to paint)"
        window hide
        pause 0.5
    call event_JobertHouse_inspect from _call_event_JobertHouse_inspect_4

    jump SearchMode

#Initial Dialogue Events

label EnterLivingRoom:
    if liv_room_visited == False:

        scene bg-intmaxhousebrokelr
        with fade
        $ Azzi = "Azzi"
        $LivRoom_safebox_locked = True
        $location_maxroom_locked = True
        $ev_ch02_sc13_mcdoorgotkey = False
        pause 1.5

        window show
        sys_nar "{cps=30}INT. MONTERO HOUSE - LIVING ROOM - JUNE 15, 1992. 11:40 A.M.{/cps}"
        window hide

        pause 1.0
        play music BGM_casual
        pause 1.0

        window show

        show azzi - neutral
        with dissolve

        MC "Wait,
        {w=0.5}so you're telling me you're{nw}" 
        play sound SFX_Mystery
        extend "{=hl} 20 yrs old{/=hl}???" with sflash

        show azzi - confused
        with dissolve

        azzi "Yeah,
        {w=0.5} what did you think?"

        MC "I thought you were the Detective's son or something…"

        show azzi - angry
        with dissolve

        play sound SFX_Smack
        azzi "Hey!{nw}" with sshake
        extend "{w=0.5} I’m not that old fart’s offspring.
        {w=0.5}I’m a {=hl}4th year Forensic Science student{/=hl} training under Tektiv Dy."

        show azzi - confused at left
        show dy - angry at right
        play sound SFX_Smack
        

        d "Who’re you calling old fart!" with sshake

        show dy - annoyed
        with dissolve

        MC "You’re a 4th year student?!
        {w=0.5}Why are you so{cps=*0.15}...{/cps}"
        
        show azzi - confused
        with dissolve

        play sound SFX_Smack
        azzi "Why am I so what!?" with sshake
        
        show azzi - angry
        with dissolve

        play sound SFX_Smack
        azzi "Are you seriously making fun of my height!?" with sshake

        MC "N-{w=0.5}{nw}"
        play sound SFX_Smack
        extend" No!
        {w=0.5}I wasn’t." with sshake

        MC "{=txt_vo}(I was gonna say why were you so
        {w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}errr{cps=*0.15}...{/cps}{w=0.5}{nw}"
        show dy - confused
        show azzi - confused
        play sound SFX_Idea
        extend " cute?)" with sflash

        azzi "{cps=*0.15}Ughhhhh{/cps}
        {w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}That’s even worse Max.
        {w=0.5}Why are you even thinking that?"

        d "Yeah.
        {w=0.5}Not that there’s anything wrong with that."

        play sound SFX_Smack
        MC "Hey!
        {w=0.5}Stop reading my mind!" with sshake

        azzi "Whatever{w=0.5}{cps=*0.15}...{/cps}"

        show dy - annoyed
        play sound SFX_Smack
        d "Alright alright!
        {w=0.5}We’re losing daylight here.
        {w=0.5}We’ve still got a job to do here!" with sshake
        window hide
        
        pause 0.5

        hide dy
        with dissolve

        pause 0.5

        show azzi at center
        with decay10inleft

        pause 0.5

        hide azzi
        with dissolve

        pause 1.0

        play sound SFX_Mystery
        show ex_police
        with dissolve

        pause 0.5
        
        window show
        MC "{=txt_vo}(Hey is that a {=hl}police officer{/=hl}?
        {w=0.5}I’d better ask him for anything new)"

        MC "Excuse me,
        {w=0.5}Sir!
        {w=0.5}Any updates about the incident?
        {w=0.5}Have you found anything that could lead to the culprit?"

        ex_police "Good morning,
        {w=0.5}Sir!
        {w=0.5}Are you the owner of this house?"

        MC "Yes,
        {w=0.5}Sir."

        ex_police "We couldn’t investigate your room since it was {=hl}locked{/=hl}.
        {w=0.5}It would be great if you could lend your assistance in letting us in."

        MC "Uhhh{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}Sure."

        ex_police "Our team is working carefully in the investigation.
        {w=0.5}We will keep you updated if we find {=hl}something{/=hl}.
        {w=0.5}For the meantime we will work on with {=hl}Detective Dy{/=hl} in this case."

        MC "Thank you,
        {w=0.5}Sir!"
        window hide

        pause 0.5

        hide ex_police
        with dissolve
 
        pause 1.0
        
        $liv_room_visited = True
    else:
        play sound SFX_walk

        scene bg-intmaxhousebrokelr
        with fade

    $ renpy.show_screen(current_room + "Screen")

    return
 
label EnterDiningRoom:
    play sound SFX_walk

    
    scene bg-intmaxhousedining
    with fade

    if din_room_visited == False:
        pause 1.0

        play sound SFX_Mystery
        show dy - smug
        with dissolve

        pause 1

        window show
        d "It’s pretty cozy in here."

        MC "You think?"

        show dy - happy
        with dissolve

        d "Yeah.
        {w=0.5}Makes me want to sit down and have a meal."

        MC "This is a dining room if you haven’t realized yet."

        show dy - thinking
        with dissolve

        d "You don’t say?"

        MC "{=txt_vo}(What a weirdo)"
        window hide
        
        pause 0.5

        hide dy 
        with dissolve
        $din_room_visited = True

    $ renpy.show_screen(current_room + "Screen")

    return

label EnterKitchen:
    play sound SFX_walk

    scene bg-intmaxhousekitchen
    with fade

    if kit_room_visited == False:
        pause 1.5
        window show
        play sound SFX_Idea
        show azzi - happy
        azzi "Wow you’ve got everything here, 
        {w=0.5}a fridge, 
        {w=0.5}washing machine, 
        {w=0.5}stove, 
        {w=0.5}pots and pans, 
        {w=0.5}and even little spice jars." with sflash

        show azzi - neutral
        with dissolve

        azzi "Weren’t you staying out of town. 
        {w=0.5}How’s your house still stacked even now?"

        MC "Auntie Cheng takes care of the house for us. 
        {w=0.5}{=txt_vo}(To be specific twice or thrice a month actually...)"

        show azzi - confused
        with dissolve

        azzi "No wonder, 
        {w=0.5}if it weren’t her this place would’ve probably caved in."

        MC "Yeah... 
        {w=0.5}Maybe I haven’t really shown her how I truly appreciate what she’s done for us to this day."

        show azzi - neutral
        with dissolve

        azzi "It’s never too late,
        {w=0.5}you know. 
        {w=0.5}You could throw her a fancy welcoming back party when she gets out of the hospital."

        MC "That doesn’t sound too bad actually"

        MC "{=txt_vo}(Maybe I could bring her to that fancy restaurant that Wynona brought me to.)"
        window hide
        
        pause 0.5

        hide azzi
        with dissolve
        $kit_room_visited = True

    return

label EnterMaxRoom:
    if max_doorroom_visited == False and location_maxroom_locked == True and inv_key_get == False:
        #Initial Dialogue (Room is Locked and Max doesn't have key)
        play sound SFX_walk
    
        scene bg-intmaxroomdoor
        with fade

        pause 0.5

        show dy - thinking at right
        show azzi - neutral at left
        with dissolve
        window show
        d "When my team investigated here yesterday, 
        {w=0.5}they found that your door was{nw}"
        play sound SFX_Mystery 
        extend" {=hl}locked{/=hl}." with sshake

        MC "Yeah.
        {w=0.5}But before I went out, 
        {w=0.5}I’m pretty sure I left it {=hl}unlocked{/=hl}."

        d "That is pretty weird. 
        {w=0.5}Doors just {=hl}don’t lock by themselves{/=hl}."

        show azzi - confused
        with dissolve
        azzi "Faulty doors do."
        window hide

        show dy - annoyed
        with dissolve
        
        pause 0.5

        show dy - sad
        with dissolve
        
        window show 
        d "{cps=*0.15}...{/cps}
        {w=0.5}As I recall, 
        {w=0.5}Mrs. Malano mentioned she heard a {=hl}click sound{/=hl} before she went up and investigated."

        show azzi - smug
        with dissolve

        azzi "Maybe the culprit {=hl}locked the door by themselves{/=hl} to halt the investigation."

        show dy - thinking
        with dissolve

        d "That could be the case. 
        {w=0.5}Anyhow, 
        {w=0.5}let's continue looking for a way to open this door."

        MC "Yeah!"
        window hide

        hide dy
        hide azzi
        with dissolve

        pause 0.5

        $max_doorroom_visited = True
    elif ev_ch02_sc13_mcdoorgotkey == False and max_doorroom_visited == False and location_maxroom_locked == True and inv_key_get == True:
        #Initial Dialogue (Room is Locked and Max has key)
        play sound SFX_walk
    
        scene bg-intmaxroomdoor
        with fade

        pause 0.5

        show dy - thinking at right
        show azzi - neutral at left
        with dissolve
        window show
        d "When my team investigated here yesterday, 
        {w=0.5}they found that your door was{nw}"
        play sound SFX_Mystery 
        extend" {=hl}locked{/=hl}." with sshake

        MC "Yeah.
        {w=0.5}But before I went out, 
        {w=0.5}I’m pretty sure I left it {=hl}unlocked{/=hl}."

        d "That is pretty weird. 
        {w=0.5}Doors just {=hl}don’t lock by themselves{/=hl}."

        show azzi - confused
        with dissolve
        azzi "Faulty doors do."
        window hide

        show dy - annoyed
        with dissolve
        
        pause 0.5

        show dy - sad
        with dissolve
        
        window show 
        d "{cps=*0.15}...{/cps}
        {w=0.5}As I recall, 
        {w=0.5}Mrs. Malano mentioned she heard a {=hl}click sound{/=hl} before she went up and investigated."

        show azzi - smug
        with dissolve

        azzi "Maybe the culprit {=hl}locked the door by themselves{/=hl} to halt the investigation."

        show dy - thinking
        with dissolve

        d "That could be the case. 
        {w=0.5}Anyhow, 
        {w=0.5}We have the {=hl}key{/=hl} already,
        {w=0.5}right?"

        show dy - smug
        with dissolve

        d "Let's go ahead and use it!"

        MC "Yeah!"
        window hide

        hide azzi
        hide dy
        with dissolve

        pause 0.5

        $max_doorroom_visited = True
    elif ev_ch02_sc13_mcdoorgotkey == False and max_doorroom_visited == True and location_maxroom_locked == True and inv_key_get == True:
        #Subsequent Dialogue (Room is Locked and Max has key)
        play sound SFX_walk
    
        scene bg-intmaxroomdoor
        with fade

        pause 0.5

        window show
        MC "{=txt_vo}(I’ve finally got the {=hl}key{/=hl} to my room. It’s time to {=hl}use{/=hl} it)"

        show azzi - angry
        play sound SFX_Idea
        azzi "Hey, 
        {w=0.5}what are you waiting for?{w=0.5}{nw}" with sflash
        play sound SFX_Smack
        extend " {=hl}Open the door{/=hl}!" with sshake

        MC "Yeah yeah, 
        {w=0.5}I’m on it."
        window hide

        hide azzi
        with dissolve

        pause 0.5
        $ev_ch02_sc13_mcdoorgotkey = True
    elif max_doorroom_visited == True and location_maxroom_locked == True:
        play sound SFX_walk
    
        scene bg-intmaxroomdoor
        with fade
    elif max_room_visited == True and location_maxroom_locked == False:
        play sound SFX_walk

        scene bg-intmaxbedroom
        with fade

    return

label EnterJobertHouse:
    scene bg-intjoberthouse
    with fade

    if jobert_house_visited == False:
        pause 1.5

        window show
        sys_nar "{cps=30}INT. UNKNOWN HOUSE - LIVING ROOM - JUNE 15, 1992. 2:20 P.M.{/cps}"
        window hide

        pause 1.0

        show azzi - confused at offscreenright
        show dy - neutral at offscreenright
        pause 0.1
        show azzi at center
        with decay10inleft

        play music BGM_mystery

        window show
        azzi "Hello!"
        window hide

        show azzi at left
        show dy - angry at right
        with decay10inleft

        window show
        d "Hey,{w=0.5}"
        play sound SFX_Smack
        extend " Azzi!
        {w=0.5}You can’t just come in here without the owners letting us in!" with sshake

        show azzi - angry
        with dissolve

        azzi "Well,
        {w=0.5}they left the door{nw}"
        play sound SFX_Mystery
        extend " {=hl}wide open{/=hl}.
        {w=0.5}And another thing,
        {w=0.5}you also went inside here,
        {w=0.5}so{cps=*0.15}...{/cps}" with sflash

        play sound SFX_Smack
        d "Well I had to run after you!
        {w=0.5}Arghh!{w=0.5}{cps=*0.15}...{/cps}
        {w=0.5}{p}Touché." with sshake

        show dy - annoyed
        with dissolve

        d "Well whatever since we’re here let’s see if the owners are in."

        show dy - confused
        with dissolve

        d "Hello?
        {w=0.5}Anyone home?
        {w=0.5}This is Iliganon City Police Department.
        {w=0.5}We’re here to ask a few questions"

        MC "(What a {=hl}run down{/=hl} house.
        {w=0.5}Touching anything could probably make the house {=hl}collapse{/=hl} in dust.)"
        window hide

        show azzi at offscreenleft
        show dy at center
        with decay10inleft

        window show
        azzi "This place is dank."
        window hide
        
        pause 0.5
        #SFX BUMP
        play sound SFX_clothruffle
        with sshake
        pause 0.5

        show azzi - happy at left
        show dy at right
        with decay10inleft

        window show
        azzi "Whoops I didn't mean to-{w=0.5}{nw}"
        play sound SFX_Smack
        show azzi - confused
        extend " Achooo!{w=0.5}{nw}" with sshake
        play sound SFX_Smack
        extend " Achooo!" with sshake

        azzi "Geez this place is so dusty"

        show dy - angry
        show azzi - angry
        play sound SFX_Smack
        d "Be careful not to disturb anything Azzi.
        {w=0.5}We’ve already {=hl}trespassed{/=hl},
        {w=0.5}we don’t want a complaint coming our way." with sshake

        MC "This house looks haunted."

        azzi "Yeah,
        {w=0.5}it seems deserted for a long time now.
        {w=0.5}The dust was piling up."

        MC "(I guess I’ll go look around and {=hl}inspect{/=hl} the area.)"

        hide azzi
        hide dy
        with dissolve

        window hide

        pause 0.5

        $jobert_house_visited = True

    return

#Other Events

label event_MaxRoom_Unlocked:
    $max_room_visited = True
    $location_maxroom_locked = False
    
    hide screen Inventory_Menu
    hide screen Inventory_Menu_dropdown
    with irisout

    pause 0.5

    stop music fadeout 1.0

    scene black
    with fade

    pause 1.0

    play sound SFX_safeboxunlocked

    pause 1.0

    play sound SFX_door1

    pause 2.5

    play sound SFX_Sweep
    pause 1.0

    scene bg-intmaxbedroom
    with wwipe

    pause 1.0

    window show
    sys_nar "{cps=30}INT. MONTERO HOUSE - MAX'S BEDROOM - JUNE 15, 1992. 1:20 P.M.{/cps}"
    window hide

    pause 1.0
    
    show dy - confused at right
    show azzi - confused at left
    with dissolve

    pause 0.5

    window show
    play sound SFX_Idea
    MC "Finally! It’s open." with sflash
    window hide

    pause 0.5
    play music BGM_cool
    
    window show
    MC "So this is it, 
    {w=0.5}my room."

    show dy - thinking
    with dissolve

    d "Hmmm{w=0.5}{cps=*0.15}...{/cps}{w=0.5}{nw}" 
    play sound SFX_Mystery
    extend "{=hl} Nothing out of the regular{/=hl},
    {w=0.5}if I’m being honest."

    show azzi - angry
    with dissolve

    azzi "Doesn’t seem to be disturbed that much."

    show dy - confused
    with dissolve

    d "Seems like it."

    MC "Yeah, 
    {w=0.5}but still, 
    {w=0.5}we must look around. 
    {w=0.5}Maybe there’s something we can find."
    window hide
    
    hide dy
    hide azzi
    with dissolve

    pause 0.5

    jump story_ch_02_investigation

label event_MaxRoom_Luminol:
    if searched_MaxRoom_bed == True and searched_MaxRoom_picture == True and searched_MaxRoom_plant == True and searched_MaxRoom_window == True and ev_ch02_sc13_luminol == False:
        stop music fadeout 1.0

        pause 1.0

        scene bg-intmaxbedroom
        with fade

        pause 1.0   
        
        play sound SFX_Mystery
        show dy - neutral at offscreenleft
        show ex_police
        with dissolve

        pause 0.5
        window show
        ex_police "Excuse me, 
        {w=0.5}Sir."

        show ex_police at left
        show azzi - happy at right
        play sound SFX_Idea
        azzi "The {=hl}police officers{/=hl} are here!" with sflash

        show dy - neutral at left
        show ex_police at right
        show azzi at offscreenright
        with decay10inleft

        show azzi - neutral
        d "Good day, 
        {w=0.5}Sir!
        {w=0.5}Have you brought the{nw}"
        play sound SFX_Mystery
        extend" {=hl}stuff{/=hl} I requested?"

        play sound SFX_Smack
        ex_police "Yes,
        {w=0.5}We brought the {=hl}luminol testing kits{/=hl} so we can start testing the evidence we collected if we could find clues that will lead us to the culprit." with sshake

        show dy - neutral at offscreenleft
        show ex_police at left
        show azzi at right
        with decay10inleft

        show azzi - happy
        play sound SFX_Idea        
        azzi "Alright! 
        {w=0.5}Let’s go!" with sflash
        window hide

        pause 1.0

        play sound SFX_Fanfare_Item

        show item_luminol at truecenter
        with irisin

        pause 1.0

        window show
        sys_nar "You’ve obtained {=hl}Luminol Testing Fluid{/=hl}.
        {w=0.5}Use it for your investigation!"

        $inv_luminol_get = True

        window hide

        pause 0.5

        hide item_luminol
        with irisout
        

        pause 0.5

        hide ex_police
        with dissolve
        show dy at left
        with decay10inleft

        pause 1.0
        window show
        MC "Chief, 
        {w=0.5}what’s {=hl}luminol testing fluid{/=hl}?"

        show azzi - smug
        with dissolve

        azzi "Ehem, 
        {w=0.5}Let me explain it to you."
        window hide

        pause 0.5
        play music BGM_thinking
        pause 0.5

        window show
        azzi "In comparison to other methods of {=hl}blood testing{/=hl},
        {w=0.5}Luminol is easy to use,
        {w=0.5}very sensitive to {=hl}blood{/=hl},
        {w=0.5}and {=hl}nondestructive{/=hl}."

        show azzi - neutral
        with dissolve

        azzi "Luminol can scan big areas at crime scenes {=hl}without harming the blood{/=hl}.
        {w=0.5}The easy enhancement of blood stains by Luminol makes it possible to interpret the patterns of blood stains."

        azzi "You simply {=hl}spray the mixture{/=hl} where you’d suspect blood might be to conduct a luminol test."

        show azzi - smug
        with dissolve

        azzi "The iron in hemoglobin speeds up a reaction between the hydrogen peroxide and luminol if it comes into contact with the luminol combination causing it to {=hl}give off a blue light{/=hl}."
        
        show azzi - happy
        play sound SFX_Idea
        MC "Oh,
        {w=0.5}that’s pretty interesting!" with sflash

        MC "{=txt_vo}(It’s kinda surprising Azzi knows this much)"

        show azzi - confused
        play sound SFX_Mystery
        azzi "There you go again thinking things Max!
        {w=0.5}You know that’s rude" with sshake

        play sound SFX_Idea
        MC "Wha!?
        {w=0.5}{=txt_vo}(Did he just read my mind again?)" with sflash

        show azzi - smug
        with dissolve

        azzi "Anyways,
        {w=0.5}did you know that luminol testing was invented back in 19-"

        show dy - annoyed
        play sound SFX_Smack
        d "Azzi!
        {w=0.5}I think we can skip the history lesson for today.
        {w=0.5}Let's focus on the investigation." with sshake

        azzi "Alright
        {w=0.5}alright.
        {w=0.5}Let’s first test it where Auntie Cheng was attacked!"
        window hide

        pause 0.5
        hide dy
        with dissolve
        show azzi at center
        with decay10inleft
        pause 0.5

        window show
        azzi "Here, take{nw}"
        play sound SFX_Mystery
        extend " {=hl}this{/=hl} Max." with sshake
        window hide

        pause 0.5
        #SHOW SHADES
        show item_shades at truecenter
        with irisin

        pause 1.0

        show item_shades
        with irisin
        pause 0.5
        window show
        MC "Uhmmm{cps=*0.15}...{/cps}{w=0.5}{nw}"
        play sound SFX_Idea
        extend" {=hl}Shades{/=hl}?
        {w=0.5}Am I gonna use this?
        {w=0.5}But we’re indoors{cps=*0.15}...{/cps}?" with sflash

        azzi "Yes,
        {w=0.5}they’re shades.
        {w=0.5}Why don’t you try them on?"
        window hide
        
        hide item_shades
        with irisout

        show luminoloverlay at offscreentop
        with dissolve
        pause 0.5
        show luminoloverlay at center
        with decay10inleft

        #CHANGE BG TO BLUE VERSION
        pause 0.5

        window show
        play sound SFX_Idea
        MC "{=hl}Blue{/=hl}!{w=1.0}{cps=*0.15}...{/cps}
        {w=1.0}This is great and all Azzi,
        {w=0.5}but I don’t get it." with sflash

        show azzi - angry
        play sound SFX_Smack
        azzi "Oh come on, stop groaning!
        {w=0.5}They’re {=hl}special shades{/=hl} to help see the {=hl}luminol glowing spots{/=hl} better for later!" with sshake

        play sound SFX_Idea
        MC "Oh,
        {w=0.5}that’s useful." with sflash

        show azzi - smug
        with dissolve

        azzi "You’re welcome.
        {w=0.5}Make sure not to break it, that cost me a fortune.
        {w=0.5}Now,
        {w=0.5}we get to use it in an actual investigation."

        MC "{=txt_vo}(Alright,
        {w=0.5}better {=hl}use{/=hl} this alongside the {=hl}luminol testing fluid{/=hl} and look for {=hl}blood traces{/=hl}.)"
        window hide

        stop music fadeout 1.0
        scene bg-intmaxbedroom
        with fade

        pause 0.5

        play music BGM_cool

        $ev_ch02_sc13_luminol = True

        jump story_ch_02_investigation
    
    return

label event_LuminolTest_Success:
    hide screen Inventory_Menu
    hide screen Inventory_Menu_dropdown
    with irisout
    
    pause 0.5

    show item_luminol at halfleft
    with irisin

    pause 0.25

    show item_shades at halfright
    with irisin

    pause 1.0
    
    window show
    MC "Okay.
    {w=0.5}I’ll test this out in this room."
    window hide
    
    hide item_luminol
    hide item_shades
    with irisout

    pause 0.5

    show luminoloverlay at offscreentop
    with dissolve
    pause 0.5
    show luminoloverlay at center
    with decay10inleft

    window show 
    MC "Just gotta {=hl}spray{/=hl} this on the surfaces."

    show dy - neutral behind luminoloverlay at offscreenright
    with dissolve

    show dy at right
    with decay10inleft

    d "Make sure not to use all of it."
    window hide

    show dy at offscreenright
    with decay10inleft

    hide dy

    pause 0.5
    stop music fadeout 1.0

    show black
    with dissolve

    pause 1.0

    play sound SFX_spray
    pause 0.3
    play sound SFX_spray
    pause 0.75
    play sound SFX_spray
    pause 0.3
    play sound SFX_spray


    show bg-intmaxhouselrluminol behind black
    hide luminoloverlay
    pause 1.0

    hide black
    with dissolve

    pause 1.0

    play sound SFX_Idea
    with sflash

    pause 1.0

    window show
    MC "Wow,
    {w=0.5}it really {=hl}glows{/=hl}!"

    MC "Inspector Dy!
    {w=0.5}Azzi!
    {w=0.5}Come look at {=hl}this{/=hl}!"
    window hide
    pause 0.5

    show dy - neutral at right
    show azzi - neutral at left
    with dissolve

    pause 0.5

    show dy - thinking
    with dissolve

    window show
    d "Well that’s surely a {=hl}glowing spot{/=hl}.
    {w=0.5}Let me have a closer look."
    window hide
    
    play music BGM_thinking

    pause 0.5

    hide bg-intmaxhouselrluminol
    with irisout
    show luminol_closeup at truecenter
    with irisin
    #SHOW LUMINOL CLOSEUP

    pause 0.5
    window show
    show dy - confused
    with dissolve
    d "What do we have here?
    {w=0.5}it seems that there’s a{nw}"
    play sound SFX_Mystery
    extend " {=hl}wiped area{/=hl} here." with sflash

    d "There may not be any {=hl}visible amounts of blood{/=hl} but there’s definitely {=hl}traces{/=hl} here."

    show azzi - confused
    with dissolve

    azzi "The culprit mustn't have known that even just wiping the surface wouldn’t be enough to {=hl}completely be rid{/=hl} of it."

    MC "Maybe they were in a hurry to leave the scene that the thought hadn’t crossed their mind?"

    show dy - thinking
    with dissolve

    d "Probably,
    {w=0.5}but one thing’s for sure this blood’s {=hl}not{/=hl} of Mrs. Malano.
    {w=0.5}Therefore our culprit out there must still have a {=hl}wound{/=hl} somehow."

    azzi "{cps=*0.15}...{/cps}{w=0.5}{nw}"
    play sound SFX_Idea
    show azzi - angry
    extend "!{w=0.5}
    {w=0.5}Hey,
    {w=0.5}Detective!
    {w=0.5}Look here the blood is trailing out towards the {=hl}window{/=hl}." with sflash

    show dy - neutral

    d "Is it now?
    {w=0.5}Hmmm{w=0.5}{cps=*0.15}...{/cps}
    {w=0.5}let’s check {=hl}outside{/=hl}.
    {w=0.5}This trail may perhaps lead us to something substantial"

    window hide
    stop music fadeout 1.0
    pause 0.5

    jump event_ExtMaxHouse_Luminol
 
label event_LuminolTest_Fail:
    hide screen Inventory_Menu
    hide screen Inventory_Menu_dropdown
    with irisout
    
    pause 0.5

    show item_luminol at halfleft
    with irisin

    pause 0.25

    show item_shades at halfright
    with irisin

    pause 1.0
    
    window show
    MC "Okay.
    {w=0.5}I’ll test this out in this room."
    window hide
    
    hide item_luminol
    hide item_shades
    with irisout

    pause 0.5

    show luminoloverlay at offscreentop
    with dissolve
    pause 0.5
    show luminoloverlay at center
    with decay10inleft

    window show 
    MC "Just gotta {=hl}spray{/=hl} this on the surfaces."

    show dy - neutral behind luminoloverlay at offscreenright
    with dissolve

    show dy at right
    with decay10inleft

    d "Make sure not to use all of it."
    window hide

    show dy at offscreenright
    with decay10inleft

    hide dy

    pause 0.5
    stop music fadeout 1.0

    show black
    with dissolve

    pause 1.0

    play sound SFX_spray
    pause 0.3
    play sound SFX_spray
    pause 0.75
    play sound SFX_spray
    pause 0.3
    play sound SFX_spray

    pause 1.0

    hide black
    with dissolve

    pause 1.0

    play sound SFX_Mystery
    with sflash

    pause 1.0

    window show
    MC "{cps=*0.15}...{/cps}{w=0.5}Darn there {=hl}isn’t any traces of blood{/=hl} here"

    MC "(Maybe I should try the {=hl}other areas{/=hl}.)"
    window hide

    show luminoloverlay at offscreentop
    with decay10inleft

    hide luminoloverlay

    play music BGM_cool

    pause 0.5

    jump story_ch_02_investigation

label event_LuminolTestJobert_Fail:
    hide screen Inventory_Menu
    hide screen Inventory_Menu_dropdown
    with irisout
    
    pause 0.5

    show item_luminol at halfleft
    with irisin

    pause 0.25

    show item_shades at halfright
    with irisin

    pause 1.0
    
    window show
    MC "Okay.
    {w=0.5}I’ll test this out in this room."
    window hide
    
    hide item_luminol
    hide item_shades
    with irisout

    pause 0.5

    show luminoloverlay at offscreentop
    with dissolve
    pause 0.5
    show luminoloverlay at center
    with decay10inleft

    window show 
    MC "Just gotta {=hl}spray{/=hl} this on the surfaces."

    show dy - neutral behind luminoloverlay at offscreenright
    with dissolve

    show dy at right
    with decay10inleft

    d "Make sure not to use all of it."
    window hide

    show dy at offscreenright
    with decay10inleft

    hide dy

    pause 0.5
    stop music fadeout 1.0

    show black
    with dissolve

    pause 1.0

    play sound SFX_spray
    pause 0.3
    play sound SFX_spray
    pause 0.75
    play sound SFX_spray
    pause 0.3
    play sound SFX_spray

    pause 1.0

    hide black
    with dissolve

    pause 1.0

    play sound SFX_Mystery
    with sflash

    pause 1.0

    window show
    MC "{cps=*0.15}...{/cps}{w=0.5}Darn there {=hl}isn’t any traces of blood{/=hl} here"

    MC "(Maybe I should try the {=hl}other areas{/=hl}.)"
    window hide

    show luminoloverlay at offscreentop
    with decay10inleft

    hide luminoloverlay

    play music BGM_mystery

    pause 0.5

    jump story_ch_02_investigation

label event_ExtMaxHouse_Luminol:
    show black
    with dissolve

    pause 0.5

    play sound SFX_Run

    pause 1.0

    scene bg-extmaxhouse
    with fade

    pause 1.0

    window show
    sys_nar "{cps=30}EXT. MONTERO HOUSE - JUNE 15, 1992. 1:40 P.M.{/cps}"
    window hide

    pause 1.0

    play music AMB_nature fadein 1.0
    show azzi - neutral
    with dissolve

    window show
    azzi "Okay.
    {w=0.5}How about we test the luminol here outside this time?
    {w=0.5}Are you ready Max?"

    MC "Yes!
    {w=0.5}Let me just{cps=*0.15}...{/cps}"
    window hide

    pause 0.5

    show luminoloverlay at offscreentop
    pause 0.1
    show luminoloverlay at center
    with decay10inleft
    pause 0.5

    window show 
    MC "Alright I just gotta spray and-"
    window hide

    stop music fadeout 1.0

    show black
    with dissolve

    pause 1.0

    play sound SFX_spray
    pause 0.3
    play sound SFX_spray
    pause 0.75
    play sound SFX_spray
    pause 0.3
    play sound SFX_spray

    hide azzi
    hide luminoloverlay
    show bg-extmaxhouseluminol behind black 
    pause 1.0

    hide black
    with dissolve

    pause 1.0

    play sound SFX_Idea
    with sflash

    pause 2.0

    play music AMB_nature fadein 1.0

    window show
    MC "!" with sshake
    show dy - angry at right
    show azzi - neutral at left
    with dissolve
    d "As suspected,
    {w=0.5}there’s a {=hl}trail{/=hl}."

    show azzi - confused
    with dissolve

    azzi "It’s leading towards the {=hl}side of the house{/=hl}."

    MC "{=txt_vo}(This luminol testing fluid is{nw}"
    play sound SFX_Idea
    extend " amazing!
    {w=0.5}Just with a few sprays we’ve uncovered a substantial lead to this case)" with sflash

    show dy - neutral
    with dissolve

    d "I suggest we follow this {=hl}trail{/=hl}.
    {w=0.5}Are you boys ready to embark?"

    show azzi - smug
    with dissolve

    play sound SFX_Smack
    azzi "Ready as you are Inspector!" with sshake

    play sound SFX_Idea
    MC "Same here!" with sflash
    window hide
    
    hide azzi
    hide dy
    with dissolve
    stop music fadeout 1.0

    pause 0.5

    jump event_ExtJobertHouse_luminol

label event_ExtJobertHouse_luminol:
    scene bg-extjoberthouse
    with fade

    pause 1.0

    window show
    sys_nar "{cps=30}UNKNOWN HOUSE - JUNE 15, 1992. 2:12 P.M.{/cps}"
    window hide

    pause 1.0

    play music AMB_nature fadein 1.0

    window show
    MC "{=txt_vo}(We followed the {=hl}trail{/=hl} using the luminol testing fluid for a few minutes.
    {w=0.5}I’m kind of tired)"

    MC "{=txt_vo}(Being stuck in the blue shades duty to find any glowing spots is starting to make my eyes hurt.)"

    show azzi - confused
    with dissolve

    azzi "Wait,
    {w=0.5}what’s that {=hl}dark spot{/=hl}?"
    window hide

    pause 0.5
    hide azzi
    with dissolve

    pause 1.0

    show azzi - confused
    with dissolve

    pause 0.5

    window show
    MC "I’m not sure,
    {w=0.5}It kinda looks like mud."
    
    stop music fadeout 1.0
    show azzi - angry
    with dissolve
    
    azzi "Though it has a weird scent to it{w=0.5}{cps=*0.15}...{/cps}
    {w=0.5}is that,{nw}"
    
    play sound SFX_Foreshadow
    extend " {=hl}Blood{/=hl}!?" with sflash

    play music BGM_mystery

    pause 0.5

    MC "!
    {w=0.5}{=hl}B{w=0.5}{nw}"
    play sound SFX_Smack
    extend"-Blood{/=hl}?
    {w=0.5}But that looks like a lot of it." with sshake

    MC "{=txt_vo}(Staring at it is starting to make me squeamish)"

    show azzi at left
    with decay10inleft

    show dy - angry at right
    with dissolve
    play sound SFX_Idea

    d "Stop,
    {w=0.5}let’s check it with the luminol fluid{cps=*0.15}...{/cps}" with sflash

    MC "*gulp*{w=0.5}{cps=*0.15}...{/cps}
    {w=0.5}Here goes I guess."
    window hide

    pause 0.5

    show luminoloverlay at offscreentop
    pause 0.1
    show luminoloverlay at center
    with decay10inleft
    pause 1.0

    stop music fadeout 1.0

    show black
    with dissolve

    pause 1.0

    play sound SFX_spray
    pause 0.3
    play sound SFX_spray
    pause 0.75
    play sound SFX_spray
    pause 0.3
    play sound SFX_spray

    hide dy
    hide azzi
    hide luminoloverlay
    show bg-extjoberthouseluminol behind black 
    pause 1.0

    hide black
    with dissolve

    pause 1.0

    play sound SFX_Idea
    with sflash

    pause 1.5

    play music BGM_mystery

    window show
    MC "Geez,
    {w=0.5}look at that."

    show dy - confused at right
    show azzi - confused at left
    with dissolve

    azzi "Wow this area is really{w=0.5}{nw}"
    play sound SFX_Idea
    extend " {=hl}GLOWING{/=hl}!" with sflash

    show dy - thinking
    with dissolve

    d "it’s blood alright.
    {w=0.5}It’s just {=hl}dried{/=hl}.
    {w=0.5}Azzi! Take a photo of it."

    show azzi - happy
    with dissolve

    azzi "On it!"
    window hide

    show azzi at offscreenleft
    show dy at center
    with decay10inleft
    pause 1.0

    play sound SFX_camera
    with sflash
    pause 0.25
    play sound SFX_camera
    with sflash
    pause 0.5

    play sound SFX_camera
    with sflash
    pause 0.1
    play sound SFX_camera
    with sflash
    pause 0.3
    play sound SFX_camera
    with sflash

    pause 0.5

    window show
    d "{cps=*0.15}...{/cps}"
    show dy - neutral
    with dissolve
    d "Hey there,
    {w=0.5}you look as if you’ve seen a ghost.
    {w=0.5}You’re color’s {=hl}drained{/=hl} from your face.
    {w=0.5}You okay?"

    MC "Y-Yeah,
    {w=0.5}it’s just that it’s the first time I’m seeing a lot of blood.
    {w=0.5} It’s making me a bit woozy."

    show dy - confused
    with dissolve

    d "Well,
    {w=0.5}we’ll try to be here quick.
    {w=0.5}Don’t wanna be carrying you when you lose consciousness."

    MC "I’ll be alright Inspector."

    show azzi at left
    show dy at right
    with decay10inleft

    azzi "Alright Detective,
    {w=0.5}I’ve got the photos!"

    show dy - smug
    with dissolve

    d "Great.
    {w=0.5}It seems that the blood stains lead to this {=hl}house{/=hl} here. let’s check if anyone’s home."

    MC "{=txt_vo}(Now that I think about it.
    {w=0.5}I think I’ve seen this house before.
    {w=0.5}You could see it from my bedroom window)"

    MC "{=txt_vo}(To think that the culprit was just living nearby.)"
    window hide

    pause 0.5

    $current_room = "JobertHouse"

    stop music fadeout 1.0

    jump story_ch_02_investigation

label event_JobertHouse_inspect:
    if searched_JobHouse_beam == True and searched_JobHouse_easel == True and searched_JobHouse_pile and searched_JobHouse_stairs and searched_JobHouse_table and ev_ch02_sc14_jobert == False:
        $ Jobert = "Jobert"
        stop music fadeout 1.0

        scene black
        with fade

        scene bg-intjoberthouse
        with fade
        show dy - annoyed at offscreenright
        pause 0.5

        play sound SFX_glassbreak
        with sshake

        pause 0.5

        window show
        azzi "Darn!"
        window hide

        

        show dy at right
        with decay10inleft

        pause 0.5

        show azzi - happy at offscreenleft

        show azzi at left
        with decay10inleft

        pause 0.5

        window show
        azzi "Uhh{cps=*0.5}...{/cps} 
        {w=0.5}I may have dropped something."

        show dy - angry
        play sound SFX_Smack
        d "AZZI! 
        {w=0.5}I swear- 
        {w=0.5}I told you not to touch anyth-" with sshake

        play sound SFX_Idea
        side_jobert "What the- 
        {w=0.5}who are you?!" with sshake
        window hide
        #SCREEN FLASH
        #SCREEN SHAKE
        pause 0.5

        show jobert - angry
        show dy at offscreenright 
        show azzi at offscreenright 
        play sound SFX_Smack
        play music BGM_uneasy
        side_jobert "Who let you inside my house!?" with sflash

        show azzi - confused at left
        show dy - surprised at right
        show jobert at offscreenleft
        with decay10inleft

        azzi "Uh.. 
        {w=0.5}We are so sorry. 
        {w=0.5}The door was left open and we checked if anybody was home. 
        {w=0.5}Actually were from the police and we’d like to ask you questio-"

        show azzi - confused at offscreenright 
        show dy - surprised at offscreenright 
        show jobert at center
        with decay10inleft

        play sound SFX_Smack
        side_jobert "No! 
        {w=0.5}Get out! 
        {w=0.5}All of you!" with sshake
        window hide
        
        pause 0.5
        play sound SFX_door2
        stop music fadeout 0.2
        pause 0.1
        scene black
        with None

        scene bg-extjoberthouse
        show dy - annoyed at right
        show azzi - sad at left
        
        
        with fade
        #SFX slams door

        window show
        azzi "Well that didn’t go as planned."

        MC "{=txt_vo}(So Jobert lives in this house? 
        {w=0.5}Could he have been the one who broke inside my house)"

        show azzi - confused
        with dissolve

        azzi "Max?"

        MC "{=txt_vo}(Is that why he punched me the other day? 
        {w=0.5}Is it because he knows why I’m here?)"

        azzi "Hey, 
        {w=0.5}earth to Max."

        MC "{=txt_vo}(I have so many questions)"

        show azzi - angry
        play sound SFX_Smack
        azzi "Max!" with sshake

        play sound SFX_Idea
        MC "! 
        {w=0.5}Oh yes Azzi?" with sflash

        show dy - angry
        play sound SFX_Smack
        d "As I was telling you Azzi! 
        {w=0.5}NO, 
        {w=0.5}TOUCHING!" with sshake

        show azzi - sad
        with dissolve

        azzi "*Sigh*{cps=*0.5}...{/cps}
        {w=0.5}I get it, 
        {w=0.5}I get it. 
        {w=0.5}I’m so sorry."

        show dy - confused
        with dissolve

        d "Also Max, 
        {w=0.5}you seem to be zoning out. 
        {w=0.5}Is there something bothering you?"

        MC "Oh it’s nothing. 
        {w=0.5}I was just surprised to find out that he was the one living in that house."

        d "He? 
        {w=0.5}You mean the guy who threw us out? 
        {w=0.5}Do you know him?"

        MC "I guess he gave me this gift that you see on my eye. 
        {w=0.5}He punched me just before I arrived the other day."

        show dy - thinking
        with dissolve

        d "Hmmmm{cps=*0.5}...{/cps} 
        {w=0.5}I do know that he’s garnered himself the title “Local Drunkard”. 
        {w=0.5}We’ve received various complaints against him."

        MC "{=txt_vo}(Yes and he even harassed Dodong’s karinderya)"

        show dy - annoyed
        with dissolve

        d "Well I guess now we’re faced with yet another hurdle."
        window hide

        pause 0.5

        show dy - surprised
        show azzi - confused
        play sound SFX_stomach
        with sshake2

        pause 3.25

        window show 

        #STOMACH GROWLING

        MC "Uhhhhh{cps=*0.5}...{/cps} 
        {w=0.5}Was that you Azzi? 
        {w=0.5}Are you hungry"

        azzi "No it wasn’t{cps=*0.5}...{/cps} 
        {w=0.5}Looks like the inspector here is famished."

        show dy - annoyed
        with dissolve
        d "Errrr{cps=*0.5}...{/cps} 
        {w=0.5}What time is it again? 
        {w=0.5}I think we missed lunch"

        MC "We got engrossed with the investigation I guess."

        show azzi - happy
        with dissolve

        azzi "Why don’t we take a break, 
        {w=0.5}let’s go eat at Dikumakain!"

        show dy - happy
        with dissolve

        d "Sounds like a great idea. 
        {w=0.5}Let’s go!"
        window hide

        scene black
        with fade

        $ev_ch02_sc13_luminol = True

        jump story_ch_02_contd
    