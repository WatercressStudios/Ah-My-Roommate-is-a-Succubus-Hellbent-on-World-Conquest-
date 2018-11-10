# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:
        add 'gui/textbox/textbox.png' yalign 1.0
        if who:
            add 'gui/textbox/namebox.png' pos (215, 780)

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who" pos (295, 795) font 'clementepdaqultrabold.ttf' size 46
                text what id "what" pos (420, 850) font 'clementepdairegular.ttf' size 32 xsize 1080
            else:
                text what id "what" pos (420, 890) font 'clementepdairegular.ttf' size 32 xsize 1080

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window" xpos 0 ypos 316

                    text who:
                        id "who" ypos 720 size 58

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what" ypos 830

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    add "gui/menu/background.png"

    imagebutton auto "gui/menu/start_%s.png" xpos 161 ypos 301 focus_mask None action Start()
    imagebutton auto "gui/menu/load_%s.png" xpos 161 ypos 431 focus_mask None action ShowMenu('load')
    imagebutton auto "gui/menu/config_%s.png" xpos 161 ypos 561 focus_mask None action ShowMenu('preferences')
    imagebutton auto "gui/menu/exit_%s.png" xpos 161 ypos 821 focus_mask None action Quit(confirm=False)


##############################################################################
#refer to encyclopedia.rpy
##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    imagebutton auto "gui/navigation/return_%s.png" xpos 51 ypos 190 focus_mask None action [Return(), Hide("set1"), Hide("set2")]
    imagebutton auto "gui/navigation/save_%s.png" xpos 51 ypos 320 focus_mask None action [ShowMenu("save"), Hide("set1"), Hide("set2")]
    imagebutton auto "gui/navigation/load_%s.png" xpos 51 ypos 450 focus_mask None action [ShowMenu("load"), Hide("set1"), Hide("set2")]
    imagebutton auto "gui/navigation/config_%s.png" xpos 51 ypos 580 focus_mask None action [ShowMenu("preferences"), Hide("set2"), Hide("set2")]
    imagebutton auto "gui/navigation/menu_%s.png" xpos 51 ypos 710 focus_mask None action [MainMenu(), Hide("set1"), Hide("set2")]
    imagebutton auto "gui/navigation/exit_%s.png" xpos 51 ypos 840 focus_mask None action [Quit(confirm=True), Hide("set1"), Hide("set2")]



##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

#####SAVE SCREEN###############

screen save:
    tag menu
    add "gui/saveload/background.png"
    add "gui/saveload/save_title.png" xpos 1250 ypos 25
    use navigation
    use file_picker

#####LOAD SCREEN###############
screen load:
    tag menu
    add "gui/saveload/background.png"
    add "gui/saveload/load_title.png" xpos 1250 ypos 25
    use navigation
    use file_picker

#####SAVE/LOAD FILE PICKER##############

screen file_picker:

# FILE PAGES:
    imagebutton auto "gui/saveload/quick_%s.png" xpos 800 ypos 450 focus_mask None action FilePage("quick")
    imagebutton auto "gui/saveload/auto_%s.png" xpos 825 ypos 650 focus_mask None action FilePage("auto")

    imagebutton auto "gui/saveload/page1_%s.png" xpos 525 ypos 75 focus_mask None action FilePage(1)
    imagebutton auto "gui/saveload/page2_%s.png" xpos 575 ypos 225 focus_mask None action FilePage(2)
    imagebutton auto "gui/saveload/page3_%s.png" xpos 625 ypos 375 focus_mask None action FilePage(3)
    imagebutton auto "gui/saveload/page4_%s.png" xpos 625 ypos 525 focus_mask None action FilePage(4)
    imagebutton auto "gui/saveload/page5_%s.png" xpos 575 ypos 675 focus_mask None action FilePage(4)
    imagebutton auto "gui/saveload/page6_%s.png" xpos 525 ypos 825 focus_mask None action FilePage(4)

# LAYOUT OF SAVE SLOTS
    #$ number = range(0, 6)
    imagebutton auto "gui/saveload/slot_%s.png" ypos 220 xpos 1100 focus_mask None action FileAction(1)
    use load_save_slot(number=1, x=1100, y=220)
    imagebutton auto "gui/saveload/slot_%s.png" ypos 510 xpos 1100 focus_mask None action FileAction(2)
    use load_save_slot(number=2, x=1100, y=510)
    imagebutton auto "gui/saveload/slot_%s.png" ypos 800 xpos 1100 focus_mask None action FileAction(3)
    use load_save_slot(number=3, x=1100, y=800)


screen load_save_slot:
    hbox:
        style_group "bant"
        textbutton _("Delete") xpos x+198 ypos y+220 xanchor 0.5 action FileDelete(number)

# Save slot file text
    $ file_text = "% s\n  %s" % (FileTime(number, empty=" "), FileSaveName(number))

# Save slot file text customization
    text file_text xpos x+200 ypos y+75 size 38 xanchor 0.5

# Save slot thumbnail
    add FileScreenshot(number) xpos x+400 ypos y+0

init -2 python:
    config.thumbnail_width = 450
    config.thumbnail_height = 207

init -2:
    style bant_button:
        is default
        background None
    style bant_button_text:
        is default
        size 32
        idle_color "#FFFFFF"
        hover_color "#f191ac"
        insensitive_color "#A6A6A6"
        outlines [(1, "#80263f", 0, 0)]

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen set1:
    add "gui/config/slider.png" xpos 1225 ypos 822
screen set2:
    add "gui/config/slider.png" xpos 1350 ypos 822
screen preferences():

    tag menu
    add "gui/config/background.png"
    add "gui/config/config_title.png" xpos 1250 ypos 25
    add "gui/config/config_labels.png" xpos 0 ypos 25
    use navigation

    if persistent.eng_lang == True:
        use set1

    imagebutton auto "gui/config/fullscreen_%s.png" xpos 1525 ypos 400 focus_mask None action Preference('display','fullscreen')
    imagebutton auto "gui/config/windowed_%s.png" xpos 1525 ypos 325 focus_mask None action Preference('display', 'window')
    imagebutton auto "gui/config/enabled_%s.png" xpos 1175 ypos 325 focus_mask None action Preference('transitions', 'all')
    imagebutton auto "gui/config/disabled_%s.png"xpos 1175 ypos 400 focus_mask None action Preference('transitions', 'none')
    imagebutton auto "gui/config/skipread_%s.png" xpos 1525 ypos 600 focus_mask None action Preference('skip', 'seen')
    imagebutton auto "gui/config/skipall_%s.png" xpos 1525 ypos 675 focus_mask None action Preference('skip', 'all')
    imagebutton auto "gui/config/stopskip_%s.png" xpos 1175 ypos 600 focus_mask None action Preference("after choices", "stop")
    imagebutton auto "gui/config/contskip_%s.png" xpos 1175 ypos 675 focus_mask None action Preference("after choices", "skip")


    frame xpos 600 ypos 160 xanchor 0.0 yanchor 0.0:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 600 ypos 395:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 600 ypos 640 xanchor 0.0 yanchor 0.0:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    frame xpos 600 ypos 875 xanchor 0.0 yanchor 0.0:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
    frame xpos 1300 ypos 865 xanchor 0.0 yanchor 0.0:
        style_group "pref"
        has vbox
        bar value Preference("voice volume")

init -2 python:
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/config/bar_full.png"
    style.pref_slider.right_bar = "gui/config/bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 661
    style.pref_slider.ymaximum = 74



##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    modal True
    add "gui/yesno/background.png"
    imagebutton auto "gui/yesno/yes_%s.png" xpos 678 ypos 572 focus_mask None action yes_action
    imagebutton auto "gui/yesno/no_%s.png" xpos 1129 ypos 581 focus_mask None action no_action

    if message == layout.ARE_YOU_SURE:
        add "gui/yesno/message_quit.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno/message_delete.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno/message_overwrite.png"
    elif message == layout.LOADING:
        add "gui/yesno/message_load.png"
    elif message == layout.QUIT:
        add "gui/yesno/message_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno/message_menu.png"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    imagebutton auto "gui/textbox/log_%s.png" xpos 746 ypos 1009 focus_mask None action ShowMenu("text_history")
    imagebutton auto "gui/textbox/skip_%s.png" xpos 829 ypos 1012 focus_mask None action Skip()
    imagebutton auto "gui/textbox/auto_%s.png" xpos 910 ypos 1012 focus_mask None action Preference("auto-forward", "toggle")
    imagebutton auto "gui/textbox/save_%s.png" xpos 995 ypos 1014 focus_mask None action ShowMenu('save')
    imagebutton auto "gui/textbox/load_%s.png" xpos 1092 ypos 1015 focus_mask None action ShowMenu('load')
    imagebutton auto "gui/textbox/config_%s.png" xpos 1192 ypos 1014 focus_mask None action ShowMenu('preferences')
    imagebutton auto "gui/textbox/menu_%s.png" xpos 1522 ypos 1014 focus_mask None action MainMenu(confirm=True)
