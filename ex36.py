from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard")


def bear_room():
    print("There is a bed here.")
    print("There is a laptop also")
    print("The laptop is on the table with gtypist on")
    print("what do you want?")

    while True:
        choice = input("> ")

        if choice == "take laptop":
            dead("you are not sleeping.")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("Tge bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")


def cthulhu_room():
    print("Here you see great evil Cthulhu")
    print("He, it , whatever stares at you and go insane ")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job")
    exit(0)

def start():
    print("You have reached home ")
    print("There is a door to your right and left")
    print("which one do you take?")

    choice = input("> ")

    if choice == "left":
        bed_room()
    elif choice == "right":
        dine_room()
    else:
        dead("you are not allowed inside house")


start()
        
