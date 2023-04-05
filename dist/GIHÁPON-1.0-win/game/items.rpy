label use_message_error:
    window show
    MC "{=txt_vo}(This item is not applicable here.)"
    window hide
    jump Inventory_Menu_callback
    
label student_id_use:
    call use_message_error from _call_use_message_error

    jump Inventory_Menu_callback

label student_id_examine:
    show item_id at truecenter
    with irisin
    window show
    MC "{=txt_vo}(This is my {=hl}student I.D.{/=hl}.
    {w=0.5}Even though I graduated from college a {=hl}year ago{/=hl},
    {w=0.5}I still keep this with me in case.)"

    window hide
    hide item_id
    with irisout
    jump Inventory_Menu_callback

label spare_key_use:
    if current_room == "MaxRoom" and location_maxroom_locked == True and inv_key_get == True:
        jump event_MaxRoom_Unlocked
    else:
        call use_message_error from _call_use_message_error_1

    jump Inventory_Menu_callback

label spare_key_examine:
    show item_key at truecenter
    with irisin
    window show
    MC "{=txt_vo}(The {=hl}spare key{/=hl} for my bedroom.
    {w=0.5}For some reason my bedroom got {=hl}locked{/=hl} during all the commotion.)"

    MC "{=txt_vo}(Good thing Auntie Cheng kept a spare key.
    {w=0.5}Not good that she {=hl}forgot{/=hl} the password for the safebox.
    {w=0.5}Would've helped if she told me about it much earlier)"

    MC "{=txt_vo}(But, oh well{cps=*0.15}...{/cps})"
    window hide
    hide item_key
    with irisout
    jump Inventory_Menu_callback

label luminol_use:
    if current_room == "LivingRoom":
        jump event_LuminolTest_Success
    elif current_room == "JobertHouse":
        jump event_LuminolTestJobert_Fail
    else:
        jump event_LuminolTest_Fail
    jump Inventory_Menu_callback

label luminol_examine:
    show item_luminol at truecenter
    with irisin
    window show
    MC "{=txt_vo}(It's a bottle of {=hl}luminol fluid{/=hl}.
    {w=0.5}According to Azzi,
    {w=0.5}we can use this to {=hl}reveal{/=hl} areas that has {=hl}traces of blood{/=hl}.
    {w=0.5}It can even work where places have been {=hl}cleaned{/=hl}.)"

    MC "{=txt_vo}(Apparently when you spray it on the surface,
    {w=0.5}anything with traces of blood will {=hl}glow blue{/=hl}.
    {w=0.5}It's almost something out of a sci-fi movie.
    {w=0.5}I gotta see this for myself.)"

    MC "{=txt_vo}(I should {=hl}use{/=hl} it where Auntie Cheng got attacked.)"
    window hide
    hide item_luminol
    with irisout
    jump Inventory_Menu_callback