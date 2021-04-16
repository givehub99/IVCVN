# we use default to make a variable have a default value. 
# this is useful so we can use saves from previous versions of the game without it crashing because a variable isn't initialized!
default players_name = "Jane Doe"

define chris = Character("Christian", color="#fff")

define huntyr = Character("Huntyr", color="#fff")

define boy = Character("Boy", color="#fff")

define boy2 = Character("Boy #2", color="#fff")

# labels are kind of like functions. they can be called. in ren'py they can 
# also be jumped to, which means it won't return to the point where it was called.

label start:
    # comments start with the pound sign

    # This makes the narrator say Welcome to the game. By default no name is displayed in the name box.

    "VARSITY GOLF CHRISTIAN 2020"

    chris "i love golf. it's just so amazing, like Lauren."

    scene bg doggo1
    

    "Welcome to the game."

    # call the label. it's like calling a function.
    call set_players_name

    "Your name is [players_name]."


    

    #the real story begins lmao
    
    "The lights are dim. There’s so much noise around me, but I’m so nervous I’m practically deaf - and that music? I guess they’re so drunk they don’t even notice this music is from 2002."

    "Oh God, there’s a couple making out on the couch. That’s uncomfortable to look at. I’ll look the other way. "
    
    "Wait, that’s Huntyr over there. Look at her, she’s completely drunk."

    scene bg drunk doggo
    with fade

    "I can’t believe I let her talk me into this"

    "Wait, I just got a text from her, while she’s literally making out with someone. Talk about a multi-tasker."

    huntyr "***stop staring you perv***"

    menu:
        "Text you want to leave":
            players_name "***I want to go home***"
            huntyr "***fuk of go play w ur magic or wutever***" 

        "Walk away":
            "She’s too drunk. I can bother her about leaving later. Should’ve listened to Mom and Dad. "


    "I miss being close to Huntyr. "
    "When I was a kid, Huntyr used to always stick up for me."
    "Mom always told Huntyr it was her job as an older sibling to take care of me."

    #flasback image of angry middle school boy standing over player

    "I was bullied at our community pool by a middle schooler."
    "He didn’t like that I accidentally splashed water in his mouth."
    "Huntyr quickly dealt with him."

    #image huntyr shooting a fireball at boy

    #young angry huntyr
    huntyr "Stay back!"

    #scared boy
    boy "Jesus Christ! You almost killed me!"

    huntyr "The next one won't miss. Leave her alone."

    "Mom was pissed. “Magic’s our a secret,” she scolded us."
    "It didn’t matter to me. Huntyr was my hero."

    #INT. PARTY (PRESENT) (PLAYER IS ALONE, DRINKING)
    "Great, now I’m drunk too. How long has it been? Who the hell is that?"

    boy2 "Hey, cutie. I’m heading out cuz this party’s fucked."
    #wink?
    boy2 "Here’s my number."

    "Thank god he’s gone."

    #IMAGE - PLAYER HOLDING PAPER WITH PHONE NUMBER, HOLDING BEER IN OTHER HAND
    
    "This is the end of the example for now."

    # end of the label. return is technically not needed, but better for organization in my opinion.
    return

label set_players_name:
    # https://www.renpy.org/doc/html/input.html?highlight=renpy%20input#renpy.input
    # python code in ren'py can start with the $ symbol.
    # we are calling the renpy.input function to allow the player to enter a string and then store the result of that in the variable players_name
    # the first argument is the prompt for the input. the default parameter sets what is in the input by default. 
    # in this example I'm setting it to what the value of the players name is currently.
    # its default value is above (Jane Doe)
    $ players_name = renpy.input("What's your name?", default = players_name)

    menu:
        # you can put a sentence at the beginning of a menu to display a message alongside the choices.
        # using brackets allows you to put the value of a variable in a message.
        "Your name is [players_name]?"
        "Yes":
            # pass doesn't do anything - it's used so there isn't an empty block
            pass
        "No":
            # call the same label so we can change the name.R

            call set_players_name 

    return