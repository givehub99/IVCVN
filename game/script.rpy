# we use default to make a variable have a default value. 
# this is useful so we can use saves from previous versions of the game without it crashing because a variable isn't initialized!
default players_name = "Jane Doe"

define chris = Character("Christian", color="#000")

# labels are kind of like functions. they can be called. in ren'py they can 
# also be jumped to, which means it won't return to the point where it was called.

label start:
    # comments start with the pound sign

    # This makes the narrator say Welcome to the game. By default no name is displayed in the name box.
    "Welcome to the game."

    "VARSITY GOLF CHRISTIAN 2020"

    chris "i love golf. it's just so amazing, like Lauren."

    # call the label. it's like calling a function.
    call set_players_name

    "Your name is [players_name]."

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