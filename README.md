# Hangman Game

A command line [Hangman Game](https://en.wikipedia.org/wiki/Hangman_(game)). 

![Hangman Gif](hangman.gif)

[Installation](#installation) • [How to play?](#how-to-play) • [List of words](#list-of-words) • [Save players and scores](#save-players-and-scores)


## Installation 

`git clone https://github.com/bloodymosquito/hangman`

## How to play?

```bash
cd hangman
python main.py
```

## List of words
### Available lists
- 100k English words (default): `python main.py --words english.txt`
- 138k French words: `python main.py --words french.txt`

### Custom list
Create a custom list of words and save it in a text file, **one word per line**. Then: `python main.py --words <your_file>`

## Save players and scores

Add `--save` to your command: 
```bash
python main.py --save
```
Player *names* and *scores* will be saved (and loaded if a save file already exists). 

By default, this information is saved in (and loaded from) `scores.json`. You can change this file with the `--scoref` option, for instance: `python main.py --save --scoref another_score_file.json` 
