# Rock, Scissor, Paper Game

A simple Python-based **Rock, Scissor, Paper** game where the user plays against the computer for 5 rounds.

## Features

- Start or exit the game.
- User can select Rock, Scissor, or Paper.
- Computer makes a random choice.
- Each round displays:
  - Computer's choice
  - User's choice
  - Round result
- Keeps track of user and computer scores.
- Displays the final result after 5 rounds.
- Allows the user to start another game.

## Game Rules

| User Choice | Computer Choice | Winner |
|---|---|---|
| Rock | Scissor | User |
| Scissor | Paper | User |
| Paper | Rock | User |
| Same choice | Same choice | Draw |

Otherwise, the computer wins the round.

## Requirements

- Python 3.x
- Any Python editor or IDE such as VS Code

No external packages are required because the program uses Python's built-in `random` module.

## How to Run

1. Make sure Python 3 is installed.
2. Save the program as `main-3.py`.
3. Open the file in VS Code or another Python editor.
4. Run the program using:

```bash
python3 main-3.py
```

On some systems, the command may be:

```bash
python main-3.py
```

## How the Program Works

### 1. Import random

The program imports Python's `random` module so that the computer can randomly select Rock, Scissor, or Paper.

```python
import random
```

### 2. Store the choices

The three possible computer choices are stored in a list:

```python
l = ["rock", "scissor", "paper"]
```

### 3. Start or exit

The program asks the user whether they want to start the game.

- `1` = Start
- `2` = Exit

### 4. Five rounds

When the user starts the game, a `for` loop runs 5 times:

```python
for a in range(1,6):
```

Therefore, the game contains 5 rounds.

### 5. User choice

The user enters:

- `1` for Rock
- `2` for Scissor
- `3` for Paper

The program converts the number into the corresponding choice.

### 6. Computer choice

The computer selects one option randomly:

```python
Cchoice = random.choice(l)
```

### 7. Decide the round winner

The program first checks whether both choices are the same. If they are, the round is a draw.

It then checks the winning combinations for the user:

- Rock vs Scissor
- Paper vs Rock
- Scissor vs Paper

If none of these conditions is true, the computer wins.

### 8. Score calculation

The program uses:

```python
ucount
```

for the user score and:

```python
ccount
```

for the computer score.

The scores are updated after every round.

**Note:** In the attached program, a draw increases both scores by 1. This README documents the program as it is currently written.

### 9. Final result

After 5 rounds:

- If `ucount == ccount`, the final game is a draw.
- If `ucount > ccount`, the user wins.
- Otherwise, the computer wins.

The final scores are displayed as well.

## Program Structure

```text
Start
  |
  v
Initialize scores
  |
  v
Ask: Start game?
  |
  +---- No ----> Exit
  |
 Yes
  |
  v
Play 5 rounds
  |
  v
Take user choice
  |
  v
Generate computer choice
  |
  v
Compare choices
  |
  v
Update scores
  |
  v
Display round result
  |
  v
After 5 rounds
  |
  v
Compare final scores
  |
  v
Display final result
  |
  v
Ask to start again
```

## Files

```text
.
├── main-3.py
├── statement.md
└── README.md
```

## Notes

The project uses only Python's built-in `random` module and does not require any third-party library.
