#! /usr/bin/env python
# coding: utf-8

"""
Hangman game
"""

import argparse

from utils import *


# For python 2/3 compatibility
try:
    input = raw_input
except NameError:
    pass


def parse_arguments():
    
    parser = argparse.ArgumentParser(description="Hangman game", formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument("--words", type=str, default="./english.txt",
                         help="path to the file containing the list of allowed words to play with")
    parser.add_argument("--save", action="store_true", 
                        help="If specified, try to load './scores.json', or create it. Scores are then saved in this same file.")
    parser.add_argument("--scoref", type=str, default="./scores.json",
                        help="path to the file to load/save scores. Default: 'scores.json'")
    return parser.parse_args()


def main():
    
    # parse command line
    args = parse_arguments()
    
    # load existing scores or create new scores if not provided
    scores = {}
    if args.save:
        if os.path.exists(args.scoref):
            scores = load_scores(args.scoref)
        else:
	    print("{} does not exist yet. New scores will be saved in this file.".format(args.scoref))
    
    # Welcoming the player
    player = load_player(scores)
    
    # Draw hangman or not
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
    if args.save:
        save_scores(scores, args.scoref)
        print("Saving the scores in '{}'".format(args.scoref))
     
    return


if __name__ == "__main__":
    main()
