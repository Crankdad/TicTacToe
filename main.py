class TicTacTo:
    # dic type {'No': 0, 'Name': '', 'Symbol': ''}
    
    def __init__(self,  player1Name: str = 'X', player2Name: str = 'O'):
        self.players = ({'Name': '', 'Symbol': 'X'}, {'Name': '', 'Symbol': 'O'})
        self.players[0]['Name'] = player1Name
        self.players[1]['Name'] = player2Name
        self.gameboard = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
        
    def show(self) -> str:
        return f'''
                   _______________________
                  |       |       |       |
                  |   {self.gameboard[1]}   |   {self.gameboard[2]}   |   {self.gameboard[3]}   |
                  |_______|_______|_______|
                  |       |       |       |
                  |   {self.gameboard[4]}   |   {self.gameboard[5]}   |   {self.gameboard[6]}   |
                  |_______|_______|_______|
                  |       |       |       |
                  |   {self.gameboard[7]}   |   {self.gameboard[8]}   |   {self.gameboard[9]}   |
                  |_______|_______|_______|
                  '''        
    
    def setPosition(self, player: int, position: int) -> str:
        try:
            if self.gameboard[position] == str(position):
                self.gameboard[position] = self.players[player]['Symbol']
                return f'{self.players[player]['Name']} write {self.players[player]['Symbol']} at position {position}'
            else:
                return 'Position is occupied!'
        except KeyError:
            return 'Position is not availible!'
    
    def checkForVictory(self) -> str:
        # check horizontal lines
        for i in range(1,10,3):
            if self.gameboard[i] == self.gameboard[i+1] == self.gameboard[i+2]:
                winnerSymbol = self.gameboard[i]        
        # check vertikal lines
        for i in range(1,4):
            if self.gameboard[i] == self.gameboard[i+3] == self.gameboard[i+6]:
                winnerSymbol = self.gameboard[i]              
        # check diagonal lines
        if self.gameboard[1] == self.gameboard[5] == self.gameboard[9]:
            winnerSymbol = self.gameboard[1]
        elif self.gameboard[3] == self.gameboard[5] == self.gameboard[7]:
            winnerSymbol = self.gameboard[3]
        
        if winnerSymbol != None:
            for index in self.players:
                if index['Symbol'] == winnerSymbol:
                    return index['Name']
        else:
            return None
                 
            
            
            
#test
if __name__ == '__main__':
    game = TicTacTo('David', 'Cilia')
    print(game.setPosition(0,3))
    print(game.setPosition(0,5))
    print(game.setPosition(0,7))

    print(game.show())
    print(game.checkForVictory())