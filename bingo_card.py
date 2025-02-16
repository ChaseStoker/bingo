from random import sample

class BingoCard:
    """Object to represent a bingo card"""

    def __init__(self, bingo_balls):
        """create a blank bingo card"""
        self.bingo_balls = bingo_balls
        self.card = {'B': [], 'I': [],'N': [],'G': [],'O': [],}
        self.fill_card()

    def fill_card(self):
        balls = self.bingo_balls.balls_left

        #fill B column
        nums = sample(range(0,15), 5)
        B_cells = self.card['B']
        for num in nums:
            B_cells.append(balls[num])

        #fill I column
        nums = sample(range(15,30), 5)
        I_cells = self.card['I']
        for num in nums:
            I_cells.append(balls[num])

        #fill N column
        nums = sample(range(30,45), 4)
        I_cells = self.card['N']
        for num in nums:
            I_cells.append(balls[num])
        #add in free space
        I_cells.insert(2, self.bingo_balls.free_ball)

        #fill G column
        nums = sample(range(45,60), 5)
        G_cells = self.card['G']
        for num in nums:
            G_cells.append(balls[num])

        #fill O column
        nums = sample(range(60,75), 5)
        O_cells = self.card['O']
        for num in nums:
            O_cells.append(balls[num])


    def __str__(self):
        message = ''
        header = "|---B---|---I---|---N---|---G---|---O---|\n"
        message += header

        for row in range(5):
            row_message = '| '
            row_message+=f"{self.card['B'][row]}| "
            row_message+=f"{self.card['I'][row]}| "
            row_message+=f"{self.card['N'][row]}| "
            row_message+=f"{self.card['G'][row]}| "
            row_message+=f"{self.card['O'][row]}|\n"
            message+=row_message
        
        return(message)


