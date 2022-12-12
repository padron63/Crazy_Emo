import random
import sys
import os
import subprocess


class Card:

    start = True
    deck = ["Defuse", "Defuse"]
    while start:

        cards = ['EXPLODING DOGGO', 'Defuse', 'Rainbow Doggo', 'Rainbow Doggo', 'Rainbow Doggo']
        explosm = 'EXPLODING DOGGO'
        cute = 'Rainbow Doggo'
        defuse = "Defuse"
        choice = random.choice(cards)
        yessir = "yes" or "yep" or "yessir" or "yass" or "yup"

        draw = input
        print(choice)

        if choice == explosm:
            explode_ans = input(f"Do you want to Defuse?\n(Tip: YOU SHOULD!)\n")
            print(explode_ans)
            if explode_ans == "yes":
                print("You Lucky...")
                deck.remove(defuse)
                print(deck)

            else:
                print("You Have Exploded!!! (Sry)")
                again = lower().input("Wanna play again?")

                if not again == yessir:
                    start = False

        if choice == cute:
            deck.append(cute)
            print(deck)

        if choice == defuse:
            deck.append(defuse)
            print(deck)


Card()
