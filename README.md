# ZombieInMyPocket
BCDE321 Advance Programming - Assignment 2 (Group)

# About
This is the source code for the python version of Zombie In My Pocket game

# Game Info

## Imagine you're trapped in a spooky house full of zombies, and you need to save the world before midnight!

## The Goal
Find an evil zombie totem hidden in the house, then bury it in the graveyard before midnight - or you become zombie food!

## How to Play:

Explore the House: You start at the front door and flip over room tiles as you move through the house, discovering new rooms like kitchens, bedrooms, and basements.

Fight Zombies: Each room might have zombies in it. You can find weapons like "a machete, golf club, chain saw, or even your former uncle's grisly femur" to bash them.

Race Against Time: You must complete your mission before midnight - the game has a built-in time limit that makes every decision count.

Find the Temple: Look for the evil temple room where the cursed totem is hidden.

Bury the Totem: Once you have the totem, get to the backyard graveyard and bury it to win!

## Key Features:

It's a solo game that takes 5-20 minutes

Quick to play, easy to learn

It's a free print-and-play game you can download and make at home

Think of it like a mini horror movie where you're the hero trying to save the day - but you only have until midnight to do it!


---
# How to set up a python virtual environment
## In Command Prompt or PowerShell change to the directory of the project then type:

```
python -m venv venv\
```


## How to activate the environment
From the same directory type:

```
venv\scripts\activate
```

Your prompt should look something like:
```
(venv) C:\wherever\you\are
```

You can now install packages to this virtual environment as you would normally install a global package.
```
pip install package-name
```

## How to create requirements.txt
Once you have installed all the packages required you can create requirements.txt with the following command:
```
pip freeze > requirements.txt
```
## How to install packages from requirements.txt
From the project directory (assuming that’s where requirements.txt is and make sure you have activated the venv)
```
pip install -r requirements.txt
```

## How to deactivate the environment

Type:
```
deactivate
```
