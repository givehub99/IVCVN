# we use default to make a variable have a default value. 
# this is useful so we can use saves from previous versions of the game without it crashing because a variable isn't initialized!
default players_name = "Jane Doe"

define chris = Character("Christian", color="#fff")

define huntyr = Character("Huntyr", color="#fff")

define boy = Character("Boy", color="#fff")

define boy2 = Character("Boy #2", color="#fff")

define thom = Character("Thomas", color="#fff")

define nico = Character("Nicolette", color="#fff")

default letterman = False
default classes = False
default drink = False

define audio.partybgm = "music/party bgm.mp3"
image black = "#000"
# labels are kind of like functions. they can be called. in ren'py they can 
# also be jumped to, which means it won't return to the point where it was called.

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

label start:
    # comments start with the pound sign

    # This makes the narrator say Welcome to the game. By default no name is displayed in the name box.

    # "VARSITY GOLF CHRISTIAN 2020"

    # chris "i love golf. it's just so amazing, like Lauren."

    scene bg doggo1
    

    "Welcome to the game."

    # call the label. it's like calling a function.
    call set_players_name

    "Your name is [players_name]."


    

    #the real story begins lmao

    play music partybgm fadein 1.0 fadeout 1.0
    
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


    stop music fadeout 1.0
    show black
    with fade
    "I miss being close to Huntyr. "
    "When I was a kid, Huntyr used to always stick up for me."
    "Mom always told Huntyr it was her job as an older sibling to take care of me."

    #flashback image of angry middle school boy standing over player
    scene bg angry doggo
    with fade

    "I was bullied at our community pool by a middle schooler. He didn’t like that I accidentally splashed water in his mouth."
    "Huntyr quickly dealt with him."

    #image huntyr shooting a fireball at boy

    #young angry huntyr
    huntyr "Stay back!"

    #scared boy
    boy "Jesus Christ! You almost killed me!"

    huntyr "The next one won't miss. Leave her alone."

    "Mom was pissed. “Magic’s our a secret,” she scolded us."
    "It didn’t matter to me. Huntyr was my hero."

    play music partybgm fadein 1.0 fadeout 1.0
    #INT. PARTY (PRESENT) (PLAYER IS ALONE, DRINKING)
    scene bg drunk doggo
    with fade
    "Great, now I’m drunk too. How long has it been? Who the hell is that?"

    boy2 "Hey, cutie. I’m heading out cuz this party’s fucked."
    #wink?
    boy2 "Here’s my number."

    "Thank god he’s gone."

    #IMAGE - PLAYER HOLDING PAPER WITH PHONE NUMBER, HOLDING BEER IN OTHER HAND

    "What a douche, thinking I’ll call him."

    #IMAGE - PLAYER FROSTING PAPER IN HAND

    "Take that, loser."

    huntyr "Hey!"

    #INT. PARTY

    "Holy fuck, she scared the shit out of me."

    players_name "Where did you come from? I thought you were off making out with that guy."

    huntyr "Who cares? What do you think you’re doing? You just burned that paper, where anybody could’ve seen."

    players_name "Not like you were here to stop me."
    #angry
    huntyr "Fine, don’t listen to me. Why would I try and help the person who gave me this scar?"
    #Flashing scar

    players_name "Do you really have to bring that up now? We were kids."

    huntyr "And now neither of us get to use our powers at home. It’ll get much worse if we get caught using it at a party."

    "Boy #3" "Using what?"

    huntyr "Oh shit."
    #(fake smile)
    huntyr "Hey! Tooo..."

    thom "Thomas. We were just making out, how did you forget my name?"

    huntyr "Hehe. Who cares. This is just my sister."
    #(flirty)
    huntyr "Why don’t you and I go somewhere more private..."

    #(smiling)
    thom "Fine, but you better not ditch me again."

    huntyr "Go on ahead, I’m almost done here"

    "Thomas leaves and Huntyr turns back to me, still angry."

    huntyr "Anyways, look. There’s a cute guy over there with Nicolette from Statistics." 
    
    huntyr "I talked to her earlier, she knows you’re coming, and is setting you up. Just do some normal people stuff."

    "Now she decides to get all “older sibling savior” on me?" 
    "So annoying, wish she would just keep one mask on instead of switching back and forth."
    "..."
    "Guess that guy IS cute. Fine. One more cup of liquid courage."

    #Cut to:
    nico "There you are! Let me introduce you to Christian."

    menu:
        "Flirty opening":
            jump flirty

        '"Normal" opening':
            jump normal

    #IMAGE - PLAYER HOLDING PAPER WITH PHONE NUMBER, HOLDING BEER IN OTHER HAND

    "What a douche, thinking I’ll call him."

    #IMAGE - PLAYER FROSTING PAPER IN HAND

    "Take that, loser."

    huntyr "Hey!"

    #INT. PARTY

    "Holy fuck, she scared the shit out of me."

    players_name "Where did you come from? I thought you were off making out with that guy."

    huntyr "Who cares? What do you think you’re doing? You just burned that paper, where anybody could’ve seen."

    players_name "Not like you were here to stop me."
    #angry
    huntyr "Fine, don’t listen to me. Why would I try and help the person who gave me this scar?"
    #Flashing scar

    players_name "Do you really have to bring that up now? We were kids."

    huntyr "And now neither of us get to use our powers at home. It’ll get much worse if we get caught using it at a party."

    "Boy #3" "Using what?"

    huntyr "Oh shit."
    #(fake smile)
    huntyr "Hey! Tooo..."

    thom "Thomas. We were just making out, how did you forget my name?"

    huntyr "Hehe. Who cares. This is just my sister."
    #(flirty)
    huntyr "Why don’t you and I go somewhere more private..."

    #(smiling)
    thom "Fine, but you better not ditch me again."

    huntyr "Go on ahead, I’m almost done her"

    "Thomas leaves and Huntyr turns back to me, still angry."

    huntyr "Anyways, look. There’s a cute guy over there with Nicolette from Statistics. I talked to her earlier, she knows you’re coming, and is setting you up. Just do some normal people stuff."

    "Now she decides to get all “older sibling savior” on me? So annoying, wish she would just keep one mask on instead of switching back and forth."
    "..."
    "Guess that guy IS cute. Fine. One more cup of liquid courage."

    #Cut to:
    nico "There you are! Let me introduce you to Christian."

    menu:
        "Flirty opening":
            jump flirty

        "Normal opening":
            jump normal

    
    # end of the label. return is technically not needed, but better for organization in my opinion.
    return

label flirty:
    #(flirty)
    players_name "Heyyy. You’re pretty cute in that Letterman."

    #(flirty)
    chris "Thanks. You’re pretty cute yourself."

    "Christian liked that. Nice job, me."

    jump followup
    return

label normal:
    #(chill)
    players_name "Heyyyy, bro. What’s up? How’s it hangin?"
    "I punch him in the arm. He didn’t like that."
    "How could I forget I was drunk? I’m already awkward. No way I could do a normal opening."

    #(Confused)
    chris "Uh... Hey?"

    #(Awkward)
    nico "Haha... Anyway..."

    jump followup
    return

label followup:
    nico "I’ll leave you two lovebirds alone now, I’m sure you guys have a lot to talk about."

    "Nicolette disappears into the sea of people."

    chris "So... What do you wanna talk about?"

    jump talk
    return

label talk_menu:
    menu: 
        "Letterman" if not letterman:
            $ letterman = True
            "He looks good in that Letterman. Hope it’s for something cool."
            players_name "So, what team are you on?"

            chris "Oh this? I’m the top member of the school’s golf team."

            "Golf? Seriously? You’re lucky you’re cute."
            players_name "That’s so cool!"
            "No, it isn’t. Think of a new topic. Now."

        "Classes" if not classes:
            $ classes = True
            players_name "So, what classes are you taking? Anything interesting?"

            chris "Well, I’m in this one class, World Mythology. It’s cool, but the teacher, Mr. Kennedy, he’s a bit annoying."

            players_name "How so?"

            chris "I swear, the man never blinks. He sits at his desk, watches everyone like a hawk, and catches anything you do. On top of that he keeps you after school for no reason."

            players_name "To do what?"

            chris "Not much, he just asks about “powers” or whether we hear anything strange around school."
            #(confused)
            chris "Sometimes, he’s like “everybody’s got this power in them, but there’s someone out there with a special power and I’m here to find them.”"
            #(smiling)
            chris "Pretty weird, huh!"

            "Mr. Kennedy, eh? Maybe I should pay him a visit sometime. But I should shift the conversation. Don’t want Christian here lingering on this too long or he might actually start to use his brain."

        "Drink" if not drink:
            $ drink = True
            players_name "So, what’re you drinking?"

            chris "Oh this? It’s a beer-suicide."

            players_name "A beer-suicide?"

            chris "Y’know, like when you go to a fountain drink machine and get a cup, mix it with all the soda in the machine? You gotta try it sometime."

            "Gross."
            players_name "Yeah, maybe!"
            "I'm gonna barf."

            chris "It’s that, but it’s all the beer and alcohol I could find in this house. Wine, beer, vodka, you name it, it’s in this cup right here."

            "I’m gagging. Change the topic now."

    if not drink or not classes or not letterman:
        call talk_menu
    return

label talk:
    call talk_menu

    "Fuck. I can’t think of any more topics."

    chris "You know, you’re pretty cute."

    "Thank god."
    "I laugh politely and pretend to blush, turning away slightly."

    menu:
        "Don't comment on compliment":
            "I say nothing back"
            jump end

        "Compliment him back":
            "Better say something back, just to make it not awkward."
            players_name "You're cute too."
            "He laughs and takes another drink from his cup."
            jump end

        "Flirt":
            "I turn and touch his shoulder, getting closer to him with my cutest smile."
            players_name "Thanks. You’re cute yourself."
            jump end

    return

label end:
    "I hear some crashes and screams from the bedroom where Huntyr is."

    thom "What the fuck!"

    "Shit. sounds serious."
    "Thomas stumbles out of the bedroom, cowering after hitting the floor. Above him, Huntyr has a flame fist, threatening Thomas."
    players_name "Huntyr! What happened to not showing your powers?"

    huntyr "Went out the window the second this perv tried touching me where he knows he shouldn’t."

    thom "I’m sorry! Please don’t stab me with your fire-hand-thing!"

    "We need to get out of here before the police shows up."
    players_name "Huntyr! We’re leaving."

    huntyr "Not a chance!"

    "I put my hand on her shoulder and look her in the eyes."
    players_name "Now."

    #CUT TO:
    #BLACK

    show black
    with fade

    "Huntyr scoffs, putting her fist away. She grabs my hand and we leave the party together."
    "What a night."

    "End of Act 1"

    return


