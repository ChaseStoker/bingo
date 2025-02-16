import random

class BingoCell:
    def __init__(self, ball, sel = False):
        self.ball = ball
        self.sel = sel

    def sel_ball(self):
        self.sel = True

    def __str__(self):
        message_ball = f"{self.ball}"
        message_ball_length = len(message_ball)

        if self.sel:
            message_sel = 'y'
        else:
             message_sel = 'x'

        if message_ball_length == 4:
            message = f"{message_ball} {message_sel}"
        elif message_ball_length == 3:
            message = f"{message_ball}  {message_sel}"
        else:
            message = f"{message_ball}   {message_sel}"

        return message

class BingoBalls:
    """Object to represent the games bingo balls"""
    def __init__(self, game=None):
        self.game = game
        self.reset_balls()

    def reset_balls(self):
        self.balls_left = []
        self.balls_sel = []

        # Make B balls
        for num in range(1, 16):
            self.balls_left.append(BingoCell(f"B{num}"))
        
        # Make I Balls
        for num in range(16, 31):
            self.balls_left.append(BingoCell(f"I{num}"))

        # Make N Balls
        for num in range(31, 46):
            self.balls_left.append(BingoCell(f"N{num}"))

        # Make G Balls
        for num in range(46, 61):
            self.balls_left.append(BingoCell(f"G{num}"))

        # Make O Balls
        for num in range(61, 76):
            self.balls_left.append(BingoCell(f"O{num}"))

        # Add free ball
        self.free_ball = BingoCell("FREE", sel=True)
        self.balls_sel.append(self.free_ball)
    

    def __str__(self):
        message = "Balls Remaining:\n"
        for ball in self.balls_left:
            message += f"\t{ball}\n"

        message += "Balls Selected:\n"
        for ball in self.balls_sel:
            message += f"\t{ball}\n"
        return(message)
    
    def select_ball(self):
        num_balls_left = len(self.balls_left)
        if num_balls_left > 0:
            selected_ball = random.choice(self.balls_left)
            self.balls_left.remove(selected_ball)
            #selected_ball = self.balls_left.pop(random.randrange(len(self.balls_left)))
            selected_ball.sel_ball()
            self.balls_sel.append(selected_ball)
            return selected_ball
        else:
            return None
    
    def selected_balls(self):
        message = "Balls Selected:\n"
        for ball in self.balls_sel:
            message += f"{ball}\n"
        return message

    def ramaining_balls(self):
        message = "Balls Remaining:\n"
        for ball in self.balls_left:
            message += f"{ball}\n"
        return


