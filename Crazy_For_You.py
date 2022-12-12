import random
import sys
import os
import subprocess


class Card:

    def __init__(self):

        cards = ['EXPLODING DOGGO', 'Defuse', 'Rainbow Doggo', 'Rainbow Doggo', 'Rainbow Doggo']
        deck = ["Defuse", "Defuse"]
        explosm = 'EXPLODING DOGGO'
        cute = 'Rainbow Doggo'
        defuse = "Defuse"
        choice = random.choice(cards)

        print(choice)

        self.deck = deck
        if choice == explosm:
            explode_ans = input(f"Do you want to Defuse?\n(Tip: YOU SHOULD!)\n")
            print(explode_ans)
            if explode_ans == "yes":
                print("You Lucky...")
                deck.remove(defuse)
                print(deck)
                
            else:
                print("You Have Exploded!!! (Sry)")
                subprocess.call([sys.executable, os.path.realpath(__file__)] +
                                sys.argv[1:])

        if choice == cute:
            deck.append(cute)
            print(deck)

        if choice == defuse:
            deck.append(defuse)
            print(deck)


Card()
