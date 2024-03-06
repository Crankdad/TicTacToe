# TIC TAC TOE
<<<<<<< HEAD

*A TicTacToe who can played in every terminal.<br>Very simple in functionality.*

*Programmed as a "TicTacToe-Class", so you can program your own gamemode.*

## Methods:

### ```__init__``` 

- player1Name -> *str* = **X**
- player2Name -> *str* = **O**

When instantiating the class, the parameters player 1 and player 2 could be set for naming the output. <br>
If you don´t to this, your terminal call the players X 
and O.<br>
Set the Dictionary gameboard to positions 1 - 9

<br>

### ```getPlayer```

- player -> *int*

Return the players dictionary with the elements "Name" and "Symbol".

<br>

### ```showGameboard```

Return the gameboard refurbished for terminal.<br>
Empty positions are numerated by number 1 - 9.

Player 1 get color <span style="color:lightgreen">green</span><br>
Player 2 get color <span style="color:yellow">yellow</span><br>

<br>

### ```setPosition```

- player -> *int*
- position -> *int*

Sets the players "Symbol" in transfered position.
Return a feedback-*str*ing for terminal output.

If position is occupied the method raises an keyerror like an position out of range was transfered.

<br>

### ```getNamebySymbol```

- symbol -> *str*

Return the transfered players symbol.

<br>

### ```checkForVictory```

Check the gameboard-dic, horizontal, vertikal and diagonal whether there are three identical symbols in a row.

In case of an hit the metode return the name of the winner.

If no winner is found and all positions are occupied the function returns "nobody" otherwise the function return an empty string.

## Run the script

#### Standart-Gamemode

1. You have to set two names for the two players.
2. Random pick of the beginnig player.
3. Write the number in terminal where you want to place your symobol.
4. Play until one winns or all position are occupied.
