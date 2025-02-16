from bingo_balls import BingoBalls
from bingo_card import BingoCard

class BingoGame:
    """Object to simulate a bingo game"""
    def __init__(self):
        self.balls = BingoBalls()
        self.card = BingoCard(self.balls)

    def __str__(self):
        message = str(self.card)
        message += self.balls.selected_balls()
        return message

    def select_ball(self):
        message = f"Selected Ball: {self.balls.select_ball()}"
        print(message)


bingo_game = BingoGame()
while True:
    # Print card & selected balls
    print(bingo_game)

    # Ask user what to do: grab ball or quit
    message = input('Press (y) to select a new ball; (q) to quit. ')
    if message == 'q':
        break
    
    bingo_game.select_ball()


