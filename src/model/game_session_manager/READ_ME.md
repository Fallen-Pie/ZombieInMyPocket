# [1] Component for User Story 12 - Game set-up start thing
**Description:** This component is closely related to Game over as it also states what the game would do when player wins/lose. In future iterations, this component will also include saving and restoring progress. 

**Key responsibilities:**
- Initializes the game (setup)
- Transitions states (start, end, reset)
- Persists state (save/load)
- Will link tightly with the Game Over component

---

**User Story/ Feature**:
- As a player, I want the game set up and started so that I can play the game
- As a player I want to save my game and comeback to it later
(Requirement created by Josiah)
---
## Interfaces provides: [ IGameStateManager, IEndGameHandler, IGameOver ]
**Setup game**
- Sets up a new game ready for the player to start playing
- Takes None
- Returns Bool (True if successful else False)

**Start game**
- starts the game
- Takes None
- Returns Bool (True if the player won else False)

**End game: win**
- Stops the game at any point during the game
- Takes None (?)
- Returns Bool (True if the game was has been successfully stopped else False)

**End game: loss**
- Stops the game after player lose
- Takes None (?)
- Returns Bool (True if the game was has been successfully stopped else False)

**End game: Reset**
- Resets an existing game to a default state
- Takes None (?)
- Returns Bool (True if the game has been reset else False)

**Save**
- Saves the current state of the game in a way it can be loaded later
- Takes None
- Returns The current state of the game

**Load**
- loads a saved game ready for the player to continue 
- Takes a game state
- Returns Bool (True if the game has been loaded successfully else False)

---

## Acceptance Criteria

### Setup
**Given** The player wants to start a new game
**When** The player has pressed the new game button
**Then** A new game is setup

### Set up the game
**Given** the player has pressed "New Game"
**When** the game is being set up
**Then** the first tile is placed at position (0, 0) on the game board
**And** the cards are shuffled

### Start Game
**Given** a new game has been set up
**When** the player pressed the start button
**Then** The game starts

### End games:
#### Player manually ends the game
**Given** The game is active
**When** The player pressed the end game button
**Then** The game ends

#### Player Wins the game
**Given** The game is active
**When** The player wins
**Then** The game ends with the win screen

#### Player Lost the game
**Given** The game is active
**When** the player has loss
**Then** The game ends with the loss screen

---
## Tasks (4.5 hours)
1. [ ] Set up a game, place the first tile, shuffle cards, Set/Reset start time to 9pm (**1.5 hours**)
2. [ ] Start first turn and subsequent turns (**0.5 hours**)
3. [ ] Save and load any game state (**2 hours**)
4. [ ] Reset a game to default state (**0.5 hours**)

---

# Component for User Story 8 - Game Over
**User Story/ Feature**: As a user I want the game to stop after a win or loss event so that I can finish the game and restart.

---
## Interfaces provides:
** [ TODO ] **
- x
- x
- x

## Acceptance Criteria
### **🟡 Scenario (Alternate Flow): Winning-Player managed to bury the zombie totem before midnight**
**Given** the player has the zombie totem, current time is earlier than 12:00, and is in the Graveyard grass tile
**When** the player draws a Dev Card to resolve a card to bury the totem
**Then** the game should apply a game finished state to stop all other player actions.
**And** calls a winning handler to inform the player that they won the game.

### **🟡 [WIP] Scenario (Alternate Flow): Losing-Player got eaten alive by the zombies by not having items**
**Given** the player does not have enough AP scores to combat zombies or enough HP to run away.
**When** there are zombies present on the Dev Card drawn by the player
**Then** the player's health points will decrease to 0 (or less) -> the player will die.
**And** the game should apply a game finished state to stop all other player actions.
**And** calls a losing handler to inform the player that they lose the game.

### **🟡 Scenario (Alternate Flow): Losing-Player loses its last health during COMBAT**
**Given** the player is on their _HP_ level of health (e.g. 2) and _AP_ level of Attack Score (e.g. 2)
**When** the player combats _N_ number of zombies (e.g. 4)
**Then** the player loses 2 _HP_, reducing their _HP_ from 2 to 0.
**And** the game should apply a game finished state to stop all other player actions.
**And** calls a losing handler to inform the player that they lose the game.

### **🟡 Scenario (Alternate Flow): Losing-Player loses its last health after RUNNING AWAY**
**Given** the player is on their last health point
**When** the player moves through a door or grassy edge into a previously explored tile (NOT a new tile),
**Then** the player's health point decreases to 0
**And** the game should apply a game finished state to stop all other player actions.
**And** calls a losing handler to inform the player that they lose the game.

### **🟡 Scenario (Alternate Flow): Losing-Player DOES NOT have the totem, but ran out of time before being able to bury the zombie totem**
**Given** player does not have the zombie totem
**When** the player draws a Dev card at 11:00 but none are left
**Then** the current time updates to 12:00/midnight
**And** the game should apply a game finished state to stop all other player actions.
**And** calls a losing handler to inform the player that they lose the game.

### **🟡 Scenario (Alternate Flow): Losing-Player DOES have the totem, but ran out of time before being able to bury the zombie totem**
**Given** the current time is 11 PM
**And** no Dev card is lef
**When** the player draws a Dev card
**Then** the current time updates to 12:00/midnight
**And** the game should apply a game finished state to stop all other player actions.
**And** calls a losing handler to inform the player that they lose the game.

### 🟢 Scenario (Basic Flow): Winning/Losing-Play Again option after game finishes
**Given** the Play Again button is enabled, and the game is in a finished state
**When** a click event from the Play Button is received,
**Then** the game will return to the starting state