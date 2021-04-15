init python:
    config.label_overrides = { "start": "act2" }

default mom = Character("Mom", color="#fff")

image black = "#000"

label act2:
    "The morning after the party."
    "As I was in bed, Mom shook me awake."
    mom "Wake up!"

    players_name "What is it?"

    mom "Can you explain why there are police officers at the door? What happened at the party?"

    mom "Really? Was it Huntyr's fault?"
    players_name "No... Not really."
    mom "You guys better have a good explanation for those officers."
    mom "I'll cover for you, but if they find out we're lying..."
    players_name "They won't."
    "As long as Huntyr keeps her story straight."
    #INT. HOME (FRONT DOOR)
    #Two police officers are present, along with Huntyr, who is
    #looking very tired. In Huntyr's arms is a cat. Player and Mom
    #arrive.
    "Jesus, Huntyr looks rough. Might be a bit harder to convince these guys than I thought."

    "Oh my god, she brought Mimi. Stupid cat."
    "Officer #1" "Good morning, miss. We won't take much of your time."

    menu:
        #(Choice A): Lie
        "Lie":
            players_name "Nope. We spent the entire night here, in the living room, watching TV."
            mom "I can vouch for them, officers."

        #(Choice B): 
        "Tell the truth":
            players_name "Yeah. We went to a party. So, what?"

    #Either choice leads to here.
    "Officer #1" "There were reports that a certain magic user attended as well. That user was said to be someone with a description similar to Huntyr here."
    players_name "We had nothing to do with that."
    mom "If there's nothing else, officers, I think you should leave. We need to get to breakfast."
    #One of the officers moves closer to Mom and I while the other watches Huntyr.
    "Officer #2" "If you have anything to tell us..."

    #IMAGE - OFFICER WITH A HAND ON MOM AND PLAYER'S SHOULDERS
    #On the floor, Mimi is next to Huntyr, looking angry.

    "Officer #2" "Now is the time. There are magic users trying to destroy this country."
    #(Smile)
    #(MORE)

    "Officer #2" "We're just trying to keep you all safe. So please, help us."
    #offscreen
    huntyr "Get your hands off of them."
    players_name "Huntyr!"
    #Huntyr has her fire fist again, threatening to punch and burn
    #the officer. The officer backs off, hands in the air.
    "She shouldn't have done that."
    #(Radio in hand)#
    "Officer #1" "This is the place."
    #The officer gives a brief description of Huntyr's appearance. Since we haven't finalized her appearance yet, I'm adding this note here.
    #IMAGE - MEN IN BLACK STORM THE HOUSE
    #One of the men is holding a special device, pointing it at Huntyr.
    huntyr "Huh? What did you do to me?"
    #Mimi is frightened.
    "That device... Huntyr can't make her ice anymore!"
    "Agent #1" "Are you Huntyr? You're coming with us."
    "Huntyr is handcuffed and blindfolded. Mimi is angry."
    huntyr "What the fuck!"
    mom "Wait! You can't just to this!"
    #Huntyr, Agent #1, and whoever was holding the device disappears. Mimi begins attacking one of the officers.
    "Get him, Mimi."
    "Officer #1" "Sorry, miss. Your daughter is under arrest for suspicion of arcane terrorism. We'll need you two to stay put."
    #I clench my fist, it glistens with embers, considering scorching them alive on the spot. Luckily, neither officer notices, one of them too occupied with Mimi.
    #Officer #2 shakes Mimi off. The two officers leave, leaving
    #Mom, Player, and Mimi alone. Mimi is very distraught.
    #Mimi looks like she's trying to go after them.
    #(Worried)
    mom "[players_name], this is bad. Who knows what they could do to Huntyr! They're treating her like a terrorist!"
    players_name "I... I'm not sure what to do. I'm scared."
    mom "Help. There has to be someone willing to help us."
    "Mimi! She ran out after the officers."
    "Should I go after her? Will Huntyr want me to put myself at risk for her?"

    menu:
        #(Choice C): Go with Mimi
        "Go with Mimi":
            #The following scene will take place if Player chooses C.
            "I run outside, after Mimi, leaving Mom there alone."
            "I hate this cat, but she's got the right idea."
            #EXT. OUTSIDE
            "Huntyr! She's there, she's being pushed into one of the vans."
            "Officer #1" "Stop or we will use force!"
            "Mimi lunges after one of the officers. They swat her away."
            players_name "Mimi!"
            "Never thought I'd be so worried about that cat."
            "The device! They're using it on me, just in case. I'm useless."
            "I continue running. I have to."
            #IMAGE - OFFICER SPRAYING GAS INTO FACE
            #CUT TO: BLACK
            #Go to where "Choice C meets here."

        #(Choice D): 
        "Stay with Mom":
            players_name "Mom! The cat-"
            #A faint gas enters the scene.
            "This smell... What is this..."
            #Both Mom and Player get progressively sleepier.

    #Choice C meets here.
    "Is this..."
    "No... Huntyr..."
    #CUT TO:
    show black
    with Dissolve(0.5)

    "end of act 2"
        

    return