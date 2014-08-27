TicTacToe
=========

On executing the ttt.py file, the computer learns to play Tic-Tac-Toe to win, by simulating about a half a million games, and is ready to play a human opponent.

This is a classic use of Reinforcement Learning for Artificial Intelligence.

Since its a Markov Decision Process, the next move decided by the computer just depends on the present configuration of the board/grid and is independent of the number of moves, who started, etc.

The computer, based on a victory or defeat keeps updating its 'strategies'. Even when playing a human, it continues to learn.

ps : the printGrid() function will not run in Python2.7 or below
