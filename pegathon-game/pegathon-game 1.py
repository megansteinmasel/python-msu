# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Megan Steinmasel                      |
# Last Modified: April 13, 2021         |
# ---------------------------------------
# Simulates a game of Pegathon (Cracker Barrel game)
# ---------------------------------------

import numpy as np
import string

# ---------------------------------------
# Start of Pegathon Class               

class Pegathon:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer


# legal_move makes sure the move can be legally played 
# Parameters: row_start = row number of peg to move
#             col_start = column number of peg to move
#             row_end = row number that peg lands
#             col_end = column number that peg lands
    
    def legal_move(self, row_start, col_start, row_end, col_end):
        game = self.board
        
        #Vertical and Horizontal
        if (row_start,col_start) == (row_end + 2, col_end):
            return True
        elif (row_start,col_start) == (row_end -2,col_end):
            return True
        elif (row_start,col_start) == (row_end,col_end - 2):
            return True
        elif (row_start,col_start) == (row_end - 2,col_end - 2):
            return True
        elif (row_start,col_start) == (row_end, col_end + 2):
            return True

        #Diagonals
        elif (row_start,col_start) == (row_end + 2, col_end + 2):
            return True
        elif (row_start,col_start) == (row_end - 2, col_end - 2):
            return True
        elif (row_start,col_start) == (row_end - 2, col_end + 2):
            return True
        elif (row_start,col_start) == (row_end + 2, col_end - 2):
            return True
        
        elif (row_start, col_start) == (row_end + 1, col_end):
            return False
        elif (row_start, col_start) == (row_end - 1, col_end):
            return False
        elif (row_start, col_start) == (row_end, col_end + 1):
            return False
        elif (row_start, col_start) == (row_end, col_end - 1):
            return False
        else:
            return False





# make_move moves the peg in empty spaces 
# Parameters: row_start = row number of peg to move
#             col_start = column number of peg to move
#             row_end = row number that peg lands
#             col_end = column number that peg lands

    def make_move(self, row_start, col_start, row_end, col_end):
        
        self.board[row_end][col_end] = True
        self.board[row_start][col_start] = False


        if row_start == row_end or col_start == col_end:
            if col_start == col_end and row_start < row_end:
                self.board[row_end-1][col_end] = False

            if col_start == col_end and row_start > row_end:
                self.board[row_end+1][col_end] = False

            if row_start == row_end and col_start < col_end:
                self.board[row_end][col_end-1] = False

            if row_start == row_end and col_start > col_end:
                self.board[row_end][col_end+1] = False


        #Diagonals
        if row_start != row_end and col_start != col_end:
            
            if row_start + 2 == row_end and col_start + 2 == col_end:
                self.board[row_end-1][col_end-1] = False

            if row_start - 2 == row_end and col_start + 2 == col_end:
                self.board[row_end+1][col_end-1] = False

            if row_start - 2 == row_end and col_start - 2 == col_end:
                self.board[row_end+1][col_end+1] = False
                
            if row_start + 2 == row_end and col_start - 2 == col_end:
                self.board[row_end-1][col_end+1] = False
        
        return(self.board)

# game_over checks if there are any moves left on the board and returns False if there is and True if there is not

    def game_over(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j]:
                    
                    if i+1 < len(self.board) and self.board[i+1][j] == True:
                        if i+2 < len(self.board) and self.board[i+2][j] == False:
                            return False
                        
                    elif i+1 < len(self.board) and j-1 >= 0 and self.board[i+1][j-1] == True:
                        if i+2 < len(self.board) and j-2 >= 0 and self.board[i+2][j-2] == False:
                            return False
                        
                    elif j-1 >= 0 and self.board[i][j-1] == True:
                        if j-2 >= 0 and self.board[i][j-2] == False:
                            return False

                    elif i-1 >= 0 and j-1 >= 0 and self.board[i-1][j-1] == True:
                        if i-2 >= 0 and j-2 >= 0 and self.board[i-2][j-2] == False:
                            return False
                        
                    elif i-1 >= 0 and self.board[i-1][j] == True:
                        if i-2 >= 0 and self.board[i-2][j] == False:
                            return False

                    elif i-1 >= 0 and j+1 < len(self.board) and self.board[i-1][j+1] == True:
                        if i-2 >= 0 and j+2 < len(self.board) and self.board[i-2][j+2] == False:
                            return False
        
                    elif j+1 < len(self.board) and self.board[i][j+1] == True:
                        if j+2 < len(self.board) and self.board[i][j+2] == False:
                            return False
            
                    elif i+1 < len(self.board) and j+1 < len(self.board) and self.board[i+1][j+1] == True:
                        if i+2 < len(self.board) and j+2 < len(self.board) and self.board[i+2][j+2] == False:
                            return False
        
                    else:
                        return True
                    
# final_message prints out a message that relates to the number of pegs left when game is over 

    def final_message(self):
        end = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == True:
                    end += 1
                

        print("Number of pegs left:", end)
        
        if 2 >= end:
            print("You're a Pegenius!")

        if end == 3 or end == 4:
            print("I've worked with better. But no many.")

        if end == 5 or end == 6:
            print(end,"left? Really? You're gonna have to do better than that.")

        if end == 7 or end > 7:
            print("Peg-naramous! Rack'em up and redeem yourself.")
            



# ---------------------------------------
# End of Pegathon Class                 |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Pegathon!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = Pegathon(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
