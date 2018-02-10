#first thing in the program is to set up the global constants
#global constant
X = "X"
O = "O"
EMPTY = " " #means an empty square on the board
TIE = "TIE" #means a tie in the game
NUM_SQ = 9 #means the number of squares on the board
#showing the instructions
def display_instruct():
	#define a function or function definition
	#this line tells the computer that the block of code that follows is to be used together as the function instructions()
	#whenever call instructions(), the following will run

	"""Display game instructions."""
	#functions have a special mechanism that allows you to document them with a docstring.
	#whatever in that triple quote is the docstring for instructions(),to describe what instruction() does

	print(
		"""
		Welcome to the greatest intellectual challeng of all time:
		Tic-Tac-Toe.
		
		This will be a showdown between your human brain 
		and my silicon processor.

		You will make your move known by entering a number, 0-8. 
		The number will correspond to the board position as shown:
					0 | 1 | 2
					---------
					3 | 4 | 5 
					---------
					6 | 7 | 8
		Prepare yourself, human. The ultimate battle is about to begin. \n
		"""
		)

#yes or no function
#this function asks a yes or no question. It receives a question and return an answer.either yes or no
def ask_yes_no(question):
	"""ask a yes or no question."""
	response = None
	while response not in ("y","n"):
		response = input(question).lower()
	return response

#ask for a number function
#this function will ask for a number within a range. It receives a question, a low number and a high number. It returns a number within the range specified
def ask_number(question, low, high):
	"""ask for a number within a range"""
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

#the piece function
#this function will ask the player if one wqants to go first and return the computer's piece and human's piece
def pieces():
	"""determine if the player or computer goes first"""
	go_first = ask_yes_no("Do you require the first to move?(y/n): ")
	#the function calls another function created before
	if go_first == "y":
		print("\nThen take the first move. You will need it.")
		human = X
		computer = O
	else:
		print("\nYour bravery will be your undoing...I will go first.")
		compter = X
		human = O
	return computer, human
#new board function
#this function creates a new board(a list) with all nine elements set to EMPTY and returns it:
def new_board():
	"""create new game board"""
	board = []
	for square in range(NUM_SQ): #square is the number in each square
		board.append(EMPTY)
	return board
#display board function
#this function displays the board passed to it
def display_board(board):
	"""display game board on screen"""
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t","---------")
	print("\n\t", board[3], "|", board[4], "|", board[5])
	print("\t","---------")
	print("\n\t", board[6], "|", board[7], "|", board[8])

#legal moves function
#a legal move is represented by the number of an empty square
#eg. if the center square were open, then 4 would be a legal move
#this function just loops over the list representing the board
#each time it finds an emoty square, it adds that square number to the list of legal moves
#then it returns the legal moves
def legal_moves(board):
	"""create list of legal moves"""
	moves = []
	for square in range(NUM_SQ):
		if board[square] == EMPTY:
			moves.append(square)
	return moves
#the winner function
#this function receives a board and return the winner.
#there are 4 possible values for a winner
#the funtion will return either X or O if anyone wins
#or return TIE when nobody wins and square fills all
#or return None when nobody wins and at least one empty square
def winner(board):
	"""determin the game winner"""
	WAYS_TO_WIN = ((0,1,2), #3 number in a row, all possible
				   (3,4,5),
				   (6,7,8),
				   (0,3,6),
				   (1,4,7),
				   (2,5,8),
				   (0,4,8),
				   (2,4,6))
	#use a for loop to go thru each possible way a player can win, to see if either player has three in a row
	#the if statement is to check to see if the three squares in question all contain the same value and are not empty
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
		return None
#human move function
#this function receives a board and the human's piece
#it returns a square number where the player wants to move
#first the function gets a list of all the legal moves for this board
#then it continues to ask the user for the square number to which he or she wants to move until that response is in theis list of legal moves
#once that happens, the function returns the move
def human_move(board,human):
	"""Get the human move"""
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Where will you move?(0-8):", O, NUM_SQ)
		if move not in legal:
			print("\nThat square us already occupied,foolish human.Choose another.\n")
	print("Fine...")
	return move

#computer move function
#the function receives the board, the computer's piece and the human's piece. It returns the computer's move
def computer_move(board,computer,human):
	"""make computer move"""
	#make a copy to work with since function will be changing list
	board = board[:]
	#the best positions to have,in order,define a tuple
	BEST_MOVES = (4,0,2,6,8,1,3,5,7)
	print("I shall take square number",end = " ")

	#if the computer can win,take that move
	for move in legal_moves(board):
		board[move] = computer
		if winnder(board) == computer:
			print(move)
			return move
		#done checking this move,undo it
		board[move] = EMPTY
	#if the player can win, block that move
	for move in legal_moves(board):
		board[moves] = human
		if winner(board) == human:
			print(move)
			return(move)
		#done checking this move,undo it
		board[move] = EMPTY
	#since no one can win on next move, pick best open square
	for move in BEST_MOVES:
		if move in legal_move(board):
			print(move)
			return move
#next turn function
#this function receives the current turn and returns the next run
#a turn represents whose turn it is and is either X or O
def next_turn(turn):
	"""switch turns"""
	if turn == X:
		return O
	else:
		return X
#the congrat winner function
#this function receives the winner of the game,the couter's piece and the human's piece
#the function is only called only when the fame is over
def congrat_winner(the_winner, computer,human):
	"""congrat the winner"""
	if the_winner != TIE:
		print(the_winner, "won!\n")
	else:
		print("It is a tie!\n")
	if the_winner == computer:
		print("As I predicted, human, I am triumphant once more.\n"\
			  "Proof that computers are superior to humans in all regards.")

	elif the_winner == human:
		print("No,no! I cannot be! Somehow you tricked me,human.\n"\
			  "But never agian! I, the computer, so swear it!")
	elif the_winner == TIE:
		print("You were most lucky,human, and somehow managed to tie me. \n"\
			  "Cekebrate today...for this is the best you will ever achieve.")
#main function
def main():
	display_instruct()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)
	while not winner(board):
		if turn == human:
			move = human_move(board,human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		turn = next_turn(turn)
	the_winner = winner(board)
	congrat_winner(the_winner,computer,human)
#start the program

main()
input("\n\nPress the enter key to exit.")
