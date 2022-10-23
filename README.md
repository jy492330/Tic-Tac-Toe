# Tic-Tac-Toe

1. Introduction
This is a classic two player tic-tac-toe game board which can be played in the command-line.
There could be one person playing the game by taking turns or two players at the same computer to play against each other by taking turns at the keyboard.
The objective is to create a robust game in the simplest way with interesting features, efficient programming, and code reuse.
Key features of the game include a user-friendly visual guide of the game board displayed at every step, sound effects, random choice to select an initial player, and defensive programming to address the following conditions:
•	Attempting to play out of turn.
•	Attempting to play in a board location has already been marked.
•	Attempting to play in a board location that doesn’t exist.
•	Attempting to play after the game has ended.

2. Design and Implementation
A Python list is used to hold the game piece/board data, which initializes each element as empty to represent the 9 empty board locations.
String objects are used as delimiters between rows and columns for optimal visual guide at each step of the game.
A function to show the board state and have visual guide displayed on the side explaining the numeric position of the board.
A function to start and play the game, which consists of various function calls within a loop while the game is still going, to handle turn, to flip player, and check if the game is over to either declare a winner or tie.  
A function to handle turn from a player with input and to check for player input validation, and register a move made by each player.
A helper function to check for input validation.
A function to swap players X and O as they play against each other.
A function to check for winner when any of the three rows are marked with the same player.
A function to check for winner when any of the three columns are marked with the same player.
A function to check for winner when any of the two diagonals are marked with the same player.
A function to check for tie.
