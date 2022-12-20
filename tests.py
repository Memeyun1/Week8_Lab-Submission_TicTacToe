import unittest
import logic


class TestLogic(unittest.TestCase):              #test the functions of class
    def test_Game_get_winner(self):              #test Game class first
        
        game = logic.Game()                      #init a Game class object
        
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        
        board_1 = [
            [None, 'X', 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]

        board_2 = [
            ['O', 'O', 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]

        board_3 = [
            ['X', 'X', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'X'],
        ]
        
        self.assertEqual(game.get_winner(board), 'X')             # test different situation 'X':理论上回传的结果，做判断
        
        self.assertEqual(game.get_winner(board_1), None)           # you can decide any situation and give them an answer
        
        self.assertEqual(game.get_winner(board_2), "O")
        
        self.assertEqual(game.get_winner(board_3), 'X')
        
    def test_Game_other_player(self):
        
        game = logic.Game()                       #init a Game class object
        self.assertEqual(game.other_player("O"),"X")
        self.assertEqual(game.other_player("X"),"O")
        
    #Now, test Player class
    
    def test_player_move(self):          #remember to put 'self' in every define fucntion(def) in class
        board = [                         
            ['X', None, 'O'],             #given a board for test
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        player = logic.Player("O")        #initialize a Player object
        
        row = 0
        col = 1                 #design player input position
        
        board_after = [                   #result after player input
            ['X', 'O', 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
    
        self.assertEqual(player.player_move(row,col,board),board_after)   #unit test and check the result


if __name__ == '__main__':
    unittest.main()
