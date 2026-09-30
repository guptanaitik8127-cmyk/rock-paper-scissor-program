# Statement

## Rock, Scissor, Paper Game

Develop a Python program to implement a **Rock, Scissor, Paper** game between a user and the computer.

### Requirements

1. The program should display an option to start the game or exit.
2. If the user chooses to start, the game should be played for **5 rounds**.
3. In each round, the user should choose one of:
   - Rock
   - Scissor
   - Paper
4. The computer should randomly choose Rock, Scissor, or Paper.
5. The winner of each round should be decided using these rules:
   - Rock beats Scissor.
   - Scissor beats Paper.
   - Paper beats Rock.
   - If both choices are the same, the round is a draw.
6. The program should display the user's choice, computer's choice, and the result of each round.
7. The program should maintain separate scores for the user and the computer.
8. For a draw, both the user and computer scores are increased by 1 in the given program.
9. After 5 rounds, the program should display the final result:
   - Final game draw
   - User wins the game
   - Computer wins the game
10. The final user score and computer score should also be displayed.
11. The program should allow the user to start another game or exit.

### Objective

The objective of this program is to demonstrate the use of:

- `random.choice()`
- `while` loop
- `for` loop
- `if-elif-else` conditions
- User input
- Variables and score counting
