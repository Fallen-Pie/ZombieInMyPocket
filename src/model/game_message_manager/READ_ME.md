# [2] Component for User Story 9 - Status/Notifications/Alerts/Stats
**Description:** This component covers two aspects: (1) warnings/alerts (2) status (3) tips (4) constant game stats 

**Key responsibilities:**
- shows status updates (room changes, welcome, item acquired).
- shows alerts/warnings (low health, time almost up, invalid actions).
- shows instructions/tooltips (special rooms like Graveyard/Evil Temple/Storage).
- shows stats (constant reminders of outcomes like +1 Health).

**Feature**: As a player, I want to see status messages for what’s happening during the game, so I am informed of the outcomes of my actions.
---
## Interfaces provides: [ IGetGameMessage ]
** IGetGameMessage **
- Tips: handle_help_key
- Occurrences: get_state_message
- Alerts: handle_game_warning_event
- Stats: get_current_time
---

## Acceptance Criteria
### 🟢 Scenario 1: Display Welcome Message at the start of the game - Current Room: Foyer
**Given** the game has just started
**When** the game is initialized
**Then** the player should see a welcome message
**And** the current room tile should be displayed as “Foyer “.

### 🟢Scenario 2: Update Room Change Message
**Given** the player is in a room (indoor or outdoor)
**When** the player moves to a different room
**Then** a message should display the updated room name.

### 🟡 Scenario 3: Display Event Trigger Message
**Given** the player enters a room (e.g. Garden OR Kitchen)
**When** the player’s health incremented by 1
**Then** a message “+1 Health" should be displayed

### 🟡 Scenario 4.1: Display Instruction for Graveyard
**Given** the Graveyard tile is drawn
**When** player enters the Graveyard
**Then** display the instruction, “Resolve a new care to bury totem.“

### 🟡 Scenario 4.2: Display Instruction for Evil Temple
**Given** the Evil Temple tile is drawn
**When** player enters the Evil Temple room
**Then** display the instruction, “Resolve a new care to find totem.“

### 🟡Scenario 5: Display Tool Tip on Storage Room to draw another card
**Given** the player is in Storage Room
**When** the player finishes drawing a Dev Card
**Then** display a prompt to inform user that they can opt to draw a second Dev Card: “You may draw a new card for a chance to acquire an item.“

### 🟡 Scenario 6: Display Low Health Warning
**Given** an “Event“ occurred
**When** the player’s health stat decreased to 1*
**Then** display warning message “Warning: Your health is running low “

### 🟡 Scenario 7: Display Time Warning
**Given** a player action is performed (acquiring items, drawing a card, or changing room)
**When** the time reaches 11PM
**Then** display warning message “Hurry! Your time is running out! “

### 🟡 Scenario 8: Display information that play acquired an item
**Given** the player draw a next card
**When** the item is obtained and collected
**Then** a message should be displayed to confirm the item (and what) was acquired

### 🟡 Scenario 10: Display Zombie Doors created when exits are none
**Given** the player has made a minimum of 1 move since the start of the game
**When** the player enters a new room tile that only has one exit (i.e. Bathroom or Storage)
**And** the user gets prompted to choose which side of the room to create a zombie door
**Then** display the informational message: “No more exits. Zombie door is created on [Chosen direction]. Three (3) zombies incoming.“

### 🟠 Scenario 11: Display Warning on invalid move on Zombie Door attack
**Given** the zombie door has been created and three zombies are spawned
**When** the player selects the action to Cower
**Then** display a failure message prompt: “Invalid move. You cannot cower during Zombie Door attack. You must fight them.“

---

## Tasks (X hours)
1. [ ] Basic Flow - Display a welcome message and the current room tile: Foyer at the start of the game. (**X hours**)
2. [ ] Basic Flow - Display message on change of room tile (new/old room).(**X hours**)
3. [ ] Alternate Flow - Display events (e.g. +1 Health) when entering a particular room (**X hours**)
4. [ ] Alternate Flow - Display an instruction for the following actions that can be done on a particular room (e.g. resolve a new card to find totem & resolve a new card to bury totem).(**X hours**)
5. [ ] Alternate Flow - Display optional action tip (e.g. May draw a new card to find an item) when entering a particular room* (**X hours**)
6. [ ] Alternate Flow - Display warning when health stat is low* (**X hours**)
7. [ ] Alternate Flow - Display warning when time is almost over.* (**X hours**)