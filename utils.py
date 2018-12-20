#! /usr/bin/env python
# coding: utf-8

import os
import json
import random


# For python 2/3 compatibility
try:
    input = raw_input
except NameError:
    pass


def reset_scores(score_file):
    r"""Reset scores
    Arguments:
        score_file: path to the file to store the scores
    """
    print("Warning: resetting scores!")
    with open(score_file, "w") as f:
        json.dump({}, f)


def save_scores(scores, score_file):
    r"""Save the scores
    Arguments:
        scores: dictionary containing the score of each player
        score_file: path to the file to store the scores
    """
    assert isinstance(scores, dict), "'scores' must be a dictionary"
    with open(score_file, "w") as f:
        json.dump(scores, f)


def load_scores(score_file):
    r"""Load scores
    Arguments:
        score_file: path to the file to store the scores
    """
    assert os.path.exists(score_file), "{}: not found".format(score_file)
    with open(score_file, "r") as f:
        scores = json.load(f)
    return scores


def display_player_score(player, scores):
    r"""Display the score of a player
    Arguments:
        player: name of the player
        scores: dictionary of scores
    """
    if player not in scores:
        print("{}: this player does not exist yet.".format(player))
        return
    else:
        score = scores[joueur][0]
        history = scores[joueur][1]
        n_games = len(history)
        avg_score = score / n_games
        print("Player: {} \nAverage score: {} \nBest score: {}".format(player, avg_score, max(history)))


def update_player_score(scores, player, new_score):
    r"""Add a new score to the scores of a player
    Arguments:
        scores: dictionary of scores
        player: name of the player
        new_score: score to add
    """
    if player in scores:
        scores[player][0] += new_score
        scores[player][1].append(new_score)
    else:
        scores[player] = [new_score, [new_score]]


def reveal_letter(word, current_word, letter):
    r"""Reveal a letter
    Arguments:
        word: complete word to guess
        current_word: current guess
        letter: letter to reveal
    """
    assert len(word) == len(current_word)
    revealed_word = ""
    for (l, x) in zip(word, current_word):
        if l != letter:
            revealed_word += x
        else:
            revealed_word += l
    return revealed_word


def init_stars(word):
    r"""Initialize a sequence of stars of the length of the word"""
    return "*" * len(word)


def load_player(scores):
    r"""
    Arguments:
        scores: dictionary of scores
    """
    player = input("Player name: ")
    if player in scores:
        chain = "Welcome back {} ! Your current score is {}".format(player, scores[player][0])
        star = "\n" + "*" * (len(chain) + 8)
        print(star + "\n")
        print("*** " + chain + " ***" + "\n")
        print(star + "\n\n")
    else:
        chain = "NEW PLAYER, Welcome {} !".format(player)
        star = "\n" + "*" * (len(chain) + 8)
        print(star + "\n")
        print("*** " + chain + " ***" + "\n")
        print(star + "\n\n")
    return player


def game(words, n_trials=8, draw=False):
    r"""Hangman game
    Arguments:
        words: list of possible words
        n_trials: number of trials before loosing
        draw: if True, draw the hangman in console
    """
    step = 0
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    word = random.choice(words)
    revealed_word = init_stars(word)
    trial = 1
    used_letters = []
    while trial <= n_trials:
        print("Used letters: {}".format(used_letters))
        print("Word: {}".format(revealed_word))
        if draw:
            draw_hangman(step)
        letter = input(">>> Trial {} on {} : ".format(trial, n_trials)).lower()
        # Enter "stop" to stop the game
        if letter.lower() == "stop":
            return 0, False
        if len(letter) != 1:
            print("You must enter one and only one letter!\n\n")
            continue
        if letter in map(str.lower, used_letters):
            print("You already tried this letter!\n\n")
            continue
        if letter not in alphabet:
            print("This letter is not valid!\n\n")
            continue
        used_letters.append(letter.upper())
        tmp_word = reveal_letter(word, revealed_word, letter)
        # Winning
        if tmp_word == word:
            s = "" if trial == 1 else "s"
            used_letters.sort(key=lambda v: v.upper())
            print("Used letters: {}".format(used_letters))
            print("Word: {}".format(word))
            print("\n\nCONGRATULATIONS! You found '{}' in {} trial{}".format(word, trial, s))
            # compute score
            score = n_trials - trial + 1
            print("Your score: {}".format(score))
            return score, True
        # Good letter
        if tmp_word != revealed_word:
            used_letters.sort(key=lambda v: v.upper())
            print("Well done, this letter is right!")
        # Bad letter
        else:
            used_letters.pop()
            used_letters.append(letter.lower())
            used_letters.sort(key=lambda v: v.upper())
            print("Too bad!")
            trial += 1
            step += 1
        revealed_word = tmp_word
        print("\n\n")

    if draw:
        draw_hangman(step)

    print("Game over! The word to guess was: {}".format(word))
    return 0, True


def draw_hangman(step=0):
    r"""Draw the hangman in console
    Arguments:
        step: integer defining the current state of the hangman
    """
    l1=""
    l2=""
    l3=""
    l4=""
    l5=""
    if step>= 1:
        l1 = "|"
    if step >= 2:
        l2 = "O"
    if step >= 3:
        l3 = "_"
    if step >= 4:
        l3 = "_|"
    if step >= 5:
        l3 = "_|_"
    if step >= 6 :
        l4 = "|"
    if step >= 7:
        l5 = "/"
    if step >= 8:
        l5 = "/ \ "
    print("\n\n_________________")
    print("|  /           |")
    print("| /            |")
    print("|/             {}".format(l1))
    print("|              {}".format(l2))
    print("|             {}".format(l3))
    print("|              {}".format(l4))
    print("|             {} ".format(l5))
    print("|")
    print("|")
    print("|")
    print("|_______\n\n")


def load_words(fname):
    r"""Read a file with one word per line"""
    assert os.path.exists(fname), "{}: not found".format(fname)
    with open(fname, "r") as f:
        words = f.read().split("\n")
    return words

