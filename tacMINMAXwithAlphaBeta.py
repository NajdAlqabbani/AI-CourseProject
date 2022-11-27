import math
import time


class Game:
    def __init__(self):
        self.init_game()

    def init_game(self):
        self.current_state = [[' ',' ',' '],
                              [' ',' ',' '],
                              [' ',' ',' ']]
        self.depth=0
        self.size=0
                              
        # X is start first
        self.player_turn = 'O'
    
   
             

    def make_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ") #inter the position
            print()
        print()

        #_______________________________________________________________

        
    # Check the move is legal 
    def check_valid(self, px, py):#px = position x , py = position y
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != ' ':
            return False
        else:
            return True
        #________________________________________________________________
    def check_winner(self):
    # Check Vertical 
        for i in range(0, 3):#012 (3 not includ)
            if (self.current_state[0][i] != ' ' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):

                return self.current_state[0][i]  # e.g. p1=p4 & p4=p7 - return the sign in this position

    # Check Horizontal 
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                
                return 'O'  

    # Check first diagonal 
        if (self.current_state[0][0] != ' ' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            
            return self.current_state[0][0] # e.g.p1=p5 & p5=p9 - return the sign in this position

    # Check second diagonal 
        if (self.current_state[0][2] != ' ' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            
            return self.current_state[0][2]  # e.g.p3=p5 & p5=p7 - return the sign in this position

    # Full or not
        for i in range(0, 3):
            for j in range(0, 3):
            # There's an empty position, the game will continue 
               if (self.current_state[i][j] == ' '):
                   return None 

    # If a tie!
        
        return ' '

    #__________________________________________________________
    # Player 'X' is max
    def max_alpha_beta(self, alpha, beta):

    # We're initially setting it to -infinty as the worst case:
       maxv = -math.inf  #max vlaue
       px = None
       py = None
       score = self.check_winner()

    # the evaluation function:
    # -1 - loss
    # 0  - a tie
    # 1  - win
       if score == 'X':  
           return (-11, 0, 0)
       elif score == 'O': 
           return (1, 0, 0)
       elif score == ' ':
           return (0, 0, 0)

       self.size +=1 #size of tree
       for i in range(0, 3):
           for j in range(0, 3):

                # On the empty position player 'X' makes a move and calls Min
                # That's one branch of the game tree.
               if self.current_state[i][j] == ' ':
                  self.current_state[i][j] = 'X'
                  
                  (m, min_i, min_j) = self.min_alpha_beta( alpha, beta) #Call the min
                  
                # Change the maxv value if needed
                  if m > maxv:
                      maxv = m
                      px = i
                      py = j
                    
                # Setting back the position to empty
                  self.current_state[i][j] = ' ' 

                  if maxv >= beta: #alpha >= beta
                        return (maxv, px, py) #pruning

                  if maxv > alpha:
                        alpha = maxv
                  
                            
       return (maxv, px, py)

#___________________________
# Player 'O' is min, in this case AI
    def min_alpha_beta(self, alpha, beta):

    # We're initially setting it to Infinty as the worst case:
       minv = math.inf # min value
       qx = None
       qy = None
       score = self.check_winner()

    # the evaluation function:
    # -1 - win
    # 0  - a tie
    # 1  - loss
       if score == 'X':
           return (-1, 0, 0)
       elif score == 'O':
           return (1, 0, 0)
       elif score == ' ':
           return (0, 0, 0)

       self.size +=1 #size of tree
       for i in range(0, 3):
           for j in range(0, 3):
               # On the empty position player 'O' makes a move and calls Max
                # That's one branch of the game tree.
               if self.current_state[i][j] == ' ':
                   self.current_state[i][j] = 'O'
                   (m, max_i, max_j) = self.max_alpha_beta( alpha, beta) #Calls the max
                   # Change the minv value if needed
                   if m < minv:
                       minv = m
                       qx = i
                       qy = j
                   # Setting back the position to empty   
                   self.current_state[i][j] = ' '

                   if minv <= alpha: #beta <=alpha
                        return (minv, qx, qy)

                   if minv < beta:
                        beta = minv
                   
       return (minv, qx, qy)

    #______________________________________________
    #Start the game
    def play_alpha_beta(self):
        # always true until the end of the game
        while True:
            self.make_board()
            self.score = self.check_winner()

        # Printing the right message if the game has ended

            if self.score != None: #the game is end
                if self.score == 'X':
                    print('The winner is X!')
                    print('Depth:',self.depth)
                    print('Size:',self.size)
                    
                elif self.score == 'O':
                    print('The winner is O!')
                    print('Depth:',self.depth)
                    print('Size:',self.size)
                    
                elif self.score == ' ':
                    print("It's a tie!")
                    print('Depth:',self.depth)
                    print('Size:',self.size)
                   

                self.init_game()
                return

        # If X player turn
            if self.player_turn == 'O':
                self.depth +=1
                while True:
                    self.depth +=1

                    start = time.time()
                    (m, px, py) = self.max_alpha_beta(-math.inf,math.inf)#max
                    end = time.time()

                    print('Evaluation time for AI: {}s'.format(round(end - start, 5))) #num - digit0

                    self.current_state[px][py] = 'O'
                    self.player_turn = 'X'
                    
                   


        # If it's O player turn
            else:

                start = time.time() 
                (m, qx, qy) =self.min_alpha_beta(-math.inf,math.inf) 
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 5))) #num - digit
                print('Recommended move: X = {}, Y = {}'.format(qx, qy)) 

                px = int(input('Enter the X position: '))
                py = int(input('Enter the Y position: '))

                (qx, qy) = (px, py)

                if self.check_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                else:
                        print('The move is not valid! Try again.')
            #_________________________________________________


#main         
if __name__ == "__main__":
           
            print("select position (XY):")
            print("00| 01| 02|")
            print("10| 11| 12|")
            print("20| 21| 22|")
            print()
            g = Game()
            g.play_alpha_beta() 
