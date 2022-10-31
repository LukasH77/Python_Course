print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to treasure Island.\nCan you survive to find the treasure?")
print("You arrive at the beach, the sun overhead and head into the jungle along a faint trail. "
      "After a short hike you arrive at a T-junction.")
choice1 = input("Do you go left or right? ").lower()

if choice1 == "left":
    print("You delve further into the jungle, following a light trail in the underbrush.\n"
          "By what you estimate to be early evening you break out of the dense jungle "
          "and arrive at a small clearing bordering a lake.\n"
          "On the other side you see the entrance to a cave.\n"
          "The opposite shore is not too far away..you could try swimming across.\n"
          "You could also try to go around the lake, a long trek along a shore mostly covered in"
          " a dense mix of thorny vines and buzzing insects.")
    choice2 = input("Do you swim or walk? ").lower()
    if choice2 == "swim":
        print("You undress and wade into the water, slowly starting to swim, desperately trying to minimize "
              "the amount of water soaking into your bundled up clothes.\nAs you cross the halfway point you notice a "
              "previously unnoticed detail: now not far from you a pair of eyes hovers barely above the surface,\n"
              "slowly creeping towards you before disappearing. Trying not to panic you start to accelerate, "
              "hoping that whatever that was didn't notice you.\n"
              "Just as you think you have made it you are severely disappointed. "
              "Something snatches your leg, almost crushes it.\nYou are jerked around "
              "before being pulled into the abyss.\nYou will never know what manner of creature devoured you that day.")
    elif choice2 == "walk":
        print("You start walking, fighting your way through the vegetation.\n"
              "It's not long until you give up swatting away the mosquitoes biting at your flesh, "
              "and stop counting the stitches various plants left across your body.\n"
              "Exhausted you wander until late in the night, before finally breaking out of that hellish environment.\n"
              "Aching and probably infected with some unknown jungle disease you fall down at the entrance of the cave "
              "and sleep through the last hours of darkness.\nAs you awake you feel terrible..but alive. "
              "You enter the cave, determined to finish what you started.\n"
              "After following the looping paths of the mysterious cave you arrive at three unmarked doors.")
        choice3 = input("Which door do you open? Right, left or center. ").lower()
        if choice3 == "right":
            print("You open the door and are greeted by the miraculous glitter of a mountain of treasure.\n"
                  "Chests overflowing with heavenly jewels and glittering coins support an avalanche of "
                  "various precious trinkets and curiosities.\nYou have made it..for now.")
            print('''
                Congratulations!
                    _______
                  .'_/_|_\_'.
                  \`\  |  /`/
                   `\\ | //'
                     `\|/`
                       `
            ''')
        elif choice3 == "center":
            print("You open the door, staring into darkness. As you make a first cautious step, you immediately slip "
                  "on the incredibly slick floor.\n"
                  "You start sliding down some sort of ramp, unable to discern any detail "
                  "in the utter blackness surrounding you.\nClawing for purchase you barely notice "
                  "the wooden poles impaling you before the darkness takes your mind as well.")
        elif choice3 == "left":
            print("As you grab the knob to push open the door you are immediately incinerated "
                  "as the door bursts outward in a gust of flame.")
        else:
            print("Undecided, you try inducing clues as to which door best to open.\n"
                  "After spending the better part of the day you suddenly hear a thumping, "
                  "rapidly closing in on your location.\n"
                  "Before you can discern its origin you are pummeled over the head and falling to the ground.\n"
                  "The last thing you see is a massive figure looming above you.\n"
                  "You never wake again.")
    else:
        print("You are unsure and decide to rest through the night. You are slaughtered by predators in your sleep.")
elif choice1 == "right":
    print("As you turn right you stumble over a low branch and fall into a hole in the ground.\n"
          "You die instantly as you hit the bottom of the pit.")
else:
    print("You are undecided and just walk straight into unmarked territory.\n"
          "You don't come far before being snatched up and restrained by a massive carnivorous plant.\n"
          "You spend weeks slowly dissolving in its burning digestive fluids.")
