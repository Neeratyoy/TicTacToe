import random
import math


'''======================================== PERIPHERAL FUNCTIONS ========================================'''


def playerInput(grid):							# accepts input from user
	i = input("Enter your move : ")
	while grid[int(i)-1]>0:
		print("Oops! The cell is occupied. Move not allowed.")
		i = input("Enter your move : ")
	return int(i)-1
#end of playerInput(grid)


def playerMove(grid):							# computer's random move
	i = random.randint(0,8)
	while grid[i]>0:
		i = random.randint(0,8)
	return i
#end of playerMove(grid)


def makeMove(grid,move,sign):						# writes a move to the grid
	grid[move] = int(sign)
	return grid
#end of makeMove(grid,move,sign)


def nextMove(currState):						# given a current state, finds the next best move allowed
	i = stateGridList.index(currState)
	move = stateList[i].bestMove()
	return move
#end of nextMove(currState)


def horizontal_win(grid):						# checks for rows
	if grid[0] == grid[1] and grid[1]==grid[2] and grid[2]!=0:
		return grid[0]
	if grid[3] == grid[4] and grid[4]==grid[5] and grid[5]!=0:
		return grid[3]
	if grid[6] == grid[7] and grid[7]==grid[8] and grid[8]!=0:
		return grid[6]
	return -1
#end of horizontal_win(grid)


def vertical_win(grid):							# checks for columns
	if grid[0] == grid[3] and grid[3]==grid[6] and grid[6]!=0:
		return grid[0]
	if grid[1] == grid[4] and grid[4]==grid[7] and grid[7]!=0:
		return grid[1]
	if grid[2] == grid[5] and grid[5]==grid[8] and grid[8]!=0:
		return grid[2]
	return -1
#end of vertical_win(grid)


def diagonal_win(grid):							# checks for diagonals
	if grid[0] == grid[4] and grid[4]==grid[8] and grid[8]!=0:
		return grid[0]
	if grid[2] == grid[4] and grid[4]==grid[6] and grid[6]!=0:
		return grid[2]
	return -1
#end of vertical_win(grid)


def isFull(grid):							# checks if the grid is full and no other move is possible
	count = 0
	for i in range(9):
		if grid[i]==0:
			count = count+1
	if count==0:
		return 1
	else:
		return 0
#end of isFull(grid)
	
	
def victory(grid):							# checks all possible combinations for winning
	a = horizontal_win(grid)
	if a>0:
		return(a)
	b = vertical_win(grid)
	if b>0:
		return(b)
	c = diagonal_win(grid)
	if c>0:
		return(c)
	if isFull(grid)==1:
		return 0
	return -1
#end of victory(grid)


def printGrid(grid):							# prints the grid in 3x3 
	print() 
	for i in range(9):
		if grid[i]==1:
			c = 'X'
		elif grid[i]==2:
			c = 'O'
		else:
			c = i+1
		if i%3<2:
			print(c,end = ' ')
		else:
			print(c)
	print()
#end of printGrid(grid)
			

'''======================================== POSSIBLE GAME COMBOS ========================================'''


def game():								# basic Comp vs Comp, random, game template
	grid = [0]*9
	result = -1
	gridStates = []
	gridStates.append(list(grid))
	while result<0:							# continue till outcome of game is not decided
		printGrid(grid)
		move1 = playerMove(grid)				# player one's move	
		grid = makeMove(grid,move1,1)
		gridStates.append(list(grid))				
		printGrid(grid)
		result = victory(grid)					# grid is checked for a possible outcome
		if result>0:
			print("Player "+str(result)+" wins!")
			return ([result]+gridStates)
		if result==0:						
			print("It's a tie!")
			return ([0]+gridStates)
		move2 = playerMove(grid)				# player two's move
		grid = makeMove(grid,move2,2)
		gridStates.append(list(grid))
		printGrid(grid)
		result = victory(grid)					# grid is checked for a possible outcome
		if result>0:
			print("Player "+str(result)+" wins!")
			return ([result]+gridStates)
		if result==0 or isFull(grid)==1:			# if no outcome and grid is full, then it's a tie
			print("It's a tie!")
			return ([0]+gridStates)				 
	return ([0]+gridStates)
#end of game()


def gameExplore():							# Comp vs Comp, Exploration			
	grid = [0]*9
	result = -1
	gridStates = []
	gridStates.append(list(grid))
	while result<0:
		move1 = playerMove(grid)
		grid = makeMove(grid,move1,1)
		gridStates.append(list(grid))
		result = victory(grid)
		if result>0:
			return ([result]+gridStates)
		if result==0:
			return ([0]+gridStates)
		move2 = playerMove(grid)
		grid = makeMove(grid,move2,2)
		gridStates.append(list(grid))
		result = victory(grid)
		if result>0:
			return ([result]+gridStates)
		if result==0 or isFull(grid)==1:
			return ([0]+gridStates)
	return ([0]+gridStates)
#end of game()


def gameExploit():							# Comp vs Comp, Exploitation
	grid = [0]*9
	result = -1
	gridStates = []
	gridStates.append(list(grid))
	move1 = playerMove(grid)
	grid = makeMove(grid,move1,1)
	gridStates.append(list(grid))
	move2 = nextMove(grid)
	grid = makeMove(grid,move2,2)
	gridStates.append(list(grid))
	while result<0:
		move1 = nextMove(grid)
		grid = makeMove(grid,move1,1)
		gridStates.append(list(grid))
		result = victory(grid)
		if result>0:
			return ([result]+gridStates)
		if result==0:
			return ([0]+gridStates)
		move2 = nextMove(grid)
		grid = makeMove(grid,move2,2)
		gridStates.append(list(grid))
		result = victory(grid)
		if result>0:
			return ([result]+gridStates)
		if result==0 or isFull(grid)==1:
			return ([0]+gridStates)
	return ([0]+gridStates)
#end of game()


def gameExploreExploit():						# Comp vs Comp, Comp1 explores and Comp2 exploits
	grid = [0]*9
	result = -1
	gridStates = []
	gridStates.append(list(grid))
	while result<0:
		move1 = playerMove(grid)
		grid = makeMove(grid,move1,1)
		gridStates.append(list(grid))
		result = victory(grid)
		if result>0:
			return ([result]+gridStates)
		if result==0:
			return ([0]+gridStates)
		move2 = nextMove(grid)
		grid = makeMove(grid,move2,2)
		gridStates.append(list(grid))
		result = victory(grid)
		if result>0:
			return ([result]+gridStates)
		if result==0 or isFull(grid)==1:
			return ([0]+gridStates)
	return ([0]+gridStates)
#end of game()


def gamePlayerComp(start):						# Player vs Comp, alternating starts
	grid = [0]*9
	result = -1
	gridStates = []
	gridStates.append(list(grid))
	printGrid(grid)
	while result<0:
		if start==0:
			move1 = playerInput(grid)
		else:
			move1 = nextMove(grid)
		grid = makeMove(grid,move1,1)
		gridStates.append(list(grid))
		printGrid(grid)
		result = victory(grid)
		if result>0:
			print("Player "+str(result)+" wins!")
			return ([result]+gridStates)
		if result==0:
			print("It's a tie!")
			return ([0]+gridStates)
		if start==0:
			move2 = nextMove(grid)
		else:
			move2 = playerInput(grid)
		grid = makeMove(grid,move2,2)
		gridStates.append(list(grid))
		printGrid(grid)
		result = victory(grid)
		if result>0:
			print("Player "+str(result)+" wins!")
			return ([result]+gridStates)
		if result==0 or isFull(grid)==1:
			print("It's a tie!")
			return ([0]+gridStates)
	return ([0]+gridStates)
#end of gamePlayerComp(start)


'''======================================== CLASS DEFINITION ========================================'''


class states:								# class forming the template for each state object
	def __init__(self,grid):
		self.currentState = list(grid)				# the state representation the object represents
		self.nextState = []					# the states it can transit to  
		self.nextStateValues = []				# the weight of the transition to a state
		self.nextStateTransition = []				# the next move to be made to transit to the next state
	#end of init()

	def bestMove(self):						# decides on the best available move based on the transition weights 
		temp = []
		for i in range(9):
			if self.currentState[i]==0:
				temp.append(i)
		temp2 = []
		for i in range(len(self.nextState)):
			if self.nextStateTransition[i] in temp:			
				temp2.append(i)
		t = temp2[0]
		m = self.nextStateValues[0]
		for i in temp2:
			if self.nextStateValues[i]>m:
				m = self.nextStateValues[i]
				t = i
		return self.nextStateTransition[t]
	#end of bestMove()

#end of class states


'''======================================== REWARDING ========================================'''
	

def diff(a,b):								# returns the position on the grid by which two states a and b differ
	for i in range(len(a)):
		if a[i]!= b[i]:
			return i
	return -1
#end of diff(a,b)


def rewarding(gameSequence):						# function that reads the sequence of states the completed game has  
	result = gameSequence[0]					# gone through to reward the respective state transitions accordingly
	gameSequence = gameSequence[1:]
	for i in range(len(gameSequence)):
		currState = gameSequence[i]
		if currState not in stateGridList:			# finding if the current state has been encountered
			stateGridList.append(currState)
			stateList.append(states(currState))
		if i==len(gameSequence)-1:
			return
		j = stateGridList.index(currState)			
		if gameSequence[i+1] not in stateList[j].nextState:	# finding if the current next state has been encountered 
			stateList[j].nextState.append(gameSequence[i+1])
			stateList[j].nextStateValues.append(0)
			stateList[j].nextStateTransition.append(diff(gameSequence[i],gameSequence[i+1]))
		k = stateList[j].nextState.index(gameSequence[i+1])
		if result>0:
			if result-1 == i%2:
				stateList[j].nextStateValues[k] = stateList[j].nextStateValues[k] + (math.exp(-(i+1))*lr)   #win:add reward
			else:
				stateList[j].nextStateValues[k] = stateList[j].nextStateValues[k] - (math.exp(-(i+1))*lr/2) #lose:minus reward
		else:
			stateList[j].nextStateValues[k] = stateList[j].nextStateValues[k] + (math.exp(-(i+1))*lr/10)     #tie:add lower reward
	return
#end of rewarding(gameSequence)


'''======================================== MAIN ========================================'''


def gameLoop():								# main function that plays out the game
	count1 = 0							# counts the Player's victories
	count2 = 0							# counts the Computer's victories	
	start = 0
	rounds = 1	
	while int(rounds)==1:
		temp = gamePlayerComp(start)
		if (start==0 and temp[0] == 1) or (start==1 and temp[0]==2):
			count1 = count1 + 1
		elif (start==0 and temp[0] == 2) or (start==1 and temp[0]==1):
			count2 = count2 + 1
		rewarding(temp)
		start = (start+1)%2					# toggling for alternating starts
		rounds = input("Continue? 1.Yes 2.No 	")
	print ("\n\nScores -: Player : "+str(count1)+" ; Computer : "+str(count2)+"\n\n")
	return
#end of gameLoop()


stateList = []
stateGridList = [] 
lr = 0.1								# learning rate


'''======================================== TRAINING PHASE ========================================'''

print("The computer is learning to play Tic-Tac-Toe...")

iterations1 = 250000
iterations2 = 150000							# iteration counts empirically decided
iterations3 = 100000

for i in range(iterations1):
	rewarding(gameExplore())

print("Are you practicing as well ? Be very scared...Computer is invincible")

for i in range(iterations2):
	rewarding(gameExploit())

print("Almost done with the training. Get ready...")

for i in range(iterations3):
	rewarding(gameExploreExploit())

print("Done! Now begin!")


'''======================================== EXECUTION ========================================'''

gameLoop()

