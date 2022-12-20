import random    

class Game():
    def __init__(self):
        
        self.board = []
        self.result_O = '0'
        self.result_x = 'x'
        
    
    def make_empty_board(self):
        
        self.board =[
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]   
        return self.board

    
    def get_winner(self,board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        for i in range(3):
            flag = ""
            flagg = "" 
            for j in range(3):
                if board[i][j] == "O":
                    flag = flag + "O"
                if board[i][j] == "X":
                    flag = flag + "X"
                if board[j][i] == "O":
                    flagg = flagg + "O"
                if board[j][i] == "X":
                    flagg = flagg + "X"
            if flag == "OOO" or flagg =="OOO":
                return "O"
            if flag == "XXX" or flagg =="XXX":
                return "X"
        
        aflag = ""
        aaflag = ""
        for i in range(3):
            if board[i][i] == "O":
                aflag = aflag + "O"
            if board[2-i][i] == "X":
                aaflag = aaflag + "X"
            if board[i][i] == "X":
                aflag = aflag + "X"
            if board[2-i][i] == "O":
                aaflag = aaflag + "O"

        if aflag == "OOO" or aaflag =="OOO":
            return "O"
        if aflag == "XXX" or aaflag =="XXX":
            return "X"      
        return None 
        
    
    def other_player(self,player):
        """Given the character for a player, returns the other player."""
        if player == "O":
            return "X"

        if player == "X":
            return "O"
        

class Player(Game): # Game：Class father, Player inherit them from Game
    def __init__(self,role):                 #init with role, player is "O" or "X"
        super().__init__()                   #inherent Game class's init function, "what's inside init function?"
        self.player_role = role  #self.own varible， role: input specific variable
        
    def player_move(self,row,col,board):   #get the position where player want to put thier chess
        # position: (row,col) 
                                             #for example, player input "(rows,cols)"        
        board[row][col] = self.player_role
        
        return board
  
class Robot(Game):
    def __init__(self,role):                 #init with role, player is "O" or "X"
        super().__init__()                   #inherent Game class's init function, "what's inside init function?"
        self.robot_role = role
    
    def robot_move(self,board):
        
        x = random.randint(0,2)               #random pick a number between 0-2 for x
        y = random.randint(0,2)               #random pick a number between 0-2 for y
       # robot_placement = (x,y)
        
        while board[x][y]!= None:             #check whether the location have been place
            x = random.randint(0,2)               
            y = random.randint(0,2)   

        board[x][y] = self.robot_role
        
        return board

 

