class TicTacTo:
    
    def __init__(self,  player1Name: str = 'X', player2Name: str = 'O'):
        self.players = ({'Name': '', 'Symbol': 'X'}, {'Name': '', 'Symbol': 'O'})
        self.players[0]['Name'] = player1Name
        self.players[1]['Name'] = player2Name
        self.gameboard = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    
    def getPlayer(self, player: int):
        return(self.players[player])

    def showGameboard(self) -> str:
        
        x = ['0']
        for position in self.gameboard:
            if self.gameboard[position] == self.players[0]['Symbol']:
                x.append(f'\x1B[32m{self.gameboard[position]}\x1B[0m')
            elif self.gameboard[position] == self.players[1]['Symbol']:
                x.append(f'\x1B[33m{self.gameboard[position]}\x1B[0m')
            else:
                x.append(self.gameboard[position])       
        
        return f'''
                   _______________________
                  |       |       |       |
                  |   {x[1]}   |   {x[2]}   |   {x[3]}   |
                  |_______|_______|_______|
                  |       |       |       |
                  |   {x[4]}   |   {x[5]}   |   {x[6]}   |
                  |_______|_______|_______|
                  |       |       |       |
                  |   {x[7]}   |   {x[8]}   |   {x[9]}   |
                  |_______|_______|_______|
                  '''        
    
    def setPosition(self, player: int, position: int) -> str:
        if self.gameboard[position] == str(position):
            self.gameboard[position] = self.players[player]['Symbol']
            return f'{self.players[player]['Name']} write {self.players[player]['Symbol']} at position {position}'
        else:
            raise KeyError
        
    def getNamebySymbol(self, symbol: str) -> str:
        for index in self.players:
            if index['Symbol'] == symbol:
                return index['Name']
        
    def checkForVictory(self) -> str:          
        winnerSymbol = ''   
        # check horizontal lines (rows)
        for i in range(1,10,3):
            if self.gameboard[i] == self.gameboard[i+1] == self.gameboard[i+2]:
                winnerSymbol = self.gameboard[i]
                return(self.getNamebySymbol(winnerSymbol))     
        # check vertikal lines (columns)
        for i in range(1,4):
            if self.gameboard[i] == self.gameboard[i+3] == self.gameboard[i+6]:
                winnerSymbol = self.gameboard[i]      
                return(self.getNamebySymbol(winnerSymbol))             
        # check diagonal lines
        if self.gameboard[1] == self.gameboard[5] == self.gameboard[9]:
            winnerSymbol = self.gameboard[1]
            return(self.getNamebySymbol(winnerSymbol))   
        elif self.gameboard[3] == self.gameboard[5] == self.gameboard[7]:
            winnerSymbol = self.gameboard[3]
            return(self.getNamebySymbol(winnerSymbol))   
        
        # check if game is over without winner
        for i in range(1,10):
            if self.gameboard[i] == f'{i}':
                break
            elif i == 9:
                return 'nobody'     
        return ''
          
#test
if __name__ == '__main__':
    
    from random import randint
    
    ################ SETUP ################
    # init users
    name1, name2 = '', ''
    # query the names
    try:
        while name1 == '':
            name1 = input('Please set name of player 1:\t')

        while name2 == '':
            name2 = input('Please set name of player 2:\t')  
    except KeyboardInterrupt:
        print('Programm canceled by user!')
        exit()
    #######################################
    # instance: game -> TicTacTo class    
    game = TicTacTo(name1, name2)
    
    ################ START GAME ################
    print()
    print(name1, ' get symbol ', f'\x1B[32m{game.getPlayer(0)['Symbol']}\x1B[0m')  
    print(name2, ' get symbol ', f'\x1B[33m{game.getPlayer(1)['Symbol']}\x1B[0m')      
    print()
    
    # choose random starter
    actPlayer = randint(0,1)
    print(game.getPlayer(actPlayer)['Name'], ', please start!')
    print()
    while True:
        try:
            pos = int(input(f'{game.getPlayer(actPlayer)['Name']} please choose a Position to set your {game.getPlayer(actPlayer)['Symbol']}: \t'))
            print(game.setPosition(actPlayer, pos))
        except ValueError:
            print('Incorrect Input')
            continue
        except KeyError: # because positionnumber is not in gameboard list or error is raised by setPosition method
            print('Position is not availible!')
            continue
        except KeyboardInterrupt:
            print('Programm canceled by user!')
            exit()
        print(game.showGameboard()) # show gameboard
        winner = game.checkForVictory() # check for winner
        if winner != '':
            #someone or nobody win -> stop while, end script
            print(f'Congratulations, the winner is: {winner}')
            break
        else:
            # next player
            if actPlayer > 0:
                actPlayer -= 1
            else: actPlayer += 1
    exit()