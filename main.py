#! /usr/bin/env python
# coding: utf-8

"""
Hangman game
"""

import argparse

from utils import *


def parse_arguments():
    
    parser = argparse.ArgumentParser(description="Hangman game", formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument("--words", type=str, default="./english.txt",
                         help="path to the file containing the list of allowed words to play with")
    
    return parser.parse_args()


def main():
    
    # parse command line
    args = parse_arguments()
    
    # load existing scores or create new scores if not provided
    score_file = input("Enter the name of the score file (or press ENTER if there isn't any): ").lower()
    if score_file == "":
        scores = {}
    else:
        scores = load_scores(score_file)

    # Welcoming the player
    player = load_player(scores)
    draw = input("Draw the hangman? (y/N) ").lower() == "y"
    print("\n\n")
        
    # Load words
    words = load_words(args.words)
    
    # start the game
    while True:
        print("\nNOTE: to stop the game, enter 'stop' instead of your guess\n")
        score, end = game(words, draw=draw)
        if end:
            update_player_score(scores, player, score)
        if input("Do you want to continue? [Y/n] \n").lower() == "n":
            break
    
    # save scores
    if score_file == "":
        score_file = input("Enter a file name to store the scores (or press ENTER to not save the scores): ")
    if score_file == "":
        print("Not saving the scores.")
    else:
        print("Saving the scores in '{}'".format(score_file))
        save_scores(scores, score_file)
    
    return


if __name__ == "__main__":
    main()
