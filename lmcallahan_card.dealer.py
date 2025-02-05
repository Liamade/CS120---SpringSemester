# -*- coding: utf-8 -*-
"""
Liam Callahan
February 9 2024
Card Dealer
"""

import random

num_cards=52
rank_name=("ace","two","three","four","five",
           "six","seven", "eight", "nine", "ten",
           "jack", "queen", "king")

suit_name=("clubs", "hearts", "spades", "diamonds")
hands=("deck","player","computer")

deck=0
player=1
computer=2

def main():
    cardDB = initcards()
    
    for i in range(5):
        assigncard(cardDB, player)
        assigncard(cardDB, computer)
    showDB(cardDB)
    
    showhand(cardDB, player)
    showhand(cardDB, computer)

def initcards():
    cardDB=[]
    for i in range (num_cards):
        cardDB.append(0)
    return cardDB

def showDB(cardDB):
    for card_num, location in enumerate(cardDB):
        print(f"{card_num}: {getcardname(card_num):25} {hands[location]}")
    print()
    
def getcardname(card_num):
    suit=card_num//13
    rank=card_num%13
    cardname=f"{rank_name[rank]} of {suit_name[suit]}"
    return cardname

def assigncard (cardDB, hand):
    card_num = random.randrang(num_cards)
    cardDB[card_num]=hand
    
def showhand(cardDB, hand):
    print(f"cards in {hands[hand]} hand")
    for card_num, location in enumerate(cardDB):
        if location == hand:
            print(f"    {getcardname(card_num)}")
            
            print()

main()